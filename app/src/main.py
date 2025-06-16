from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from src.data import fetch_nba_teams
from src.aws.s3 import write_to_s3
# from nba_api.stats.endpoints import leaguegamefinder, playercareerstats, teamgamelog
# from nba_api.stats.static import players, teams

import os
import json
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

s3_client = boto3.client(
    's3',
    endpoint_url=os.getenv('AWS_ENDPOINT_URL', 'http://localstack:4566'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', 'test'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', 'test'),
    region_name=os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
)

BUCKET_NAME = "data-platform-local-test-bucket"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    print('HERE!')
    print(os.getcwd())
    files = await list_s3_files()

    return templates.TemplateResponse("home.html", {
        "request": request,
        "files": files
    })

@app.get("/nba-data")
async def get_nba_data():
    """Endpoint to trigger NBA data fetch manually"""

    # To start off with, I'm fetching some simple NBA data.
    # I'll drop that raw data in S3 and then start working with it from there.

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        teams_data = fetch_nba_teams()
        write_to_s3(s3_client, BUCKET_NAME, teams_data, f"nba_data/teams/teams_{timestamp}.json")
        return {"message": "NBA data fetched successfully, check console output."}
    except Exception as e:
        return {"error": f"Failed to fetch NBA data: {str(e)}"}


@app.get("/s3-files")
async def list_s3_files():
    """List all files in the S3 bucket"""
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        
        if 'Contents' not in response:
            return {"files": [], "message": "No files in bucket"}
        
        files = []
        for obj in response['Contents']:
            files.append({
                "key": obj['Key'],
                "size": obj['Size'],
                "last_modified": obj['LastModified'].isoformat()
            })
        
        return {
            "bucket": BUCKET_NAME,
            "file_count": len(files),
            "files": sorted(files, key=lambda x: x['last_modified'], reverse=True)
        }
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"S3 error: {str(e)}")

@app.get("/s3-files/{file_key:path}")
async def get_s3_file_content(file_key: str):
    """Get the content of a specific file from S3"""
    try:
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        
        try:
            json_content = json.loads(content)
            return {
                "file_key": file_key,
                "content_type": "application/json",
                "content": json_content
            }
        except json.JSONDecodeError:
            return {
                "file_key": file_key,
                "content_type": "text/plain",
                "content": content
            }
            
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            raise HTTPException(status_code=404, detail="File not found")
        raise HTTPException(status_code=500, detail=f"S3 error: {str(e)}")

@app.get("/health")
async def health_check():
    """Check the health of the service and S3 connection"""
    try:
        s3_client.head_bucket(Bucket=BUCKET_NAME)

        return {
            "status": "healthy", 
            "s3": "connected",
            "bucket": BUCKET_NAME,
            "timestamp": datetime.now().isoformat()
        }

    except ClientError:
        return {
            "status": "unhealthy", 
            "s3": "disconnected",
            "bucket": BUCKET_NAME,
            "timestamp": datetime.now().isoformat()
        }
