import os
import json

import boto3
from botocore.exceptions import ClientError

def write_to_s3(s3_client, bucket_name, data, key, content_type='application/json'):
    try:
        if isinstance(data, dict) or isinstance(data, list):
            data = json.dumps(data, indent=2, default=str)
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=data,
            ContentType=content_type
        )
        print(f"Successfully wrote data to S3: {key}")

        return True

    except ClientError as e:
        print(f"Error writing to S3: {e}")
        return False
