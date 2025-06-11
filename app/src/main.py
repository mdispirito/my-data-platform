from fastapi import FastAPI

from src.data import fetch_nba_data
# from nba_api.stats.endpoints import leaguegamefinder, playercareerstats, teamgamelog
# from nba_api.stats.static import players, teams

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the beginnings of my general data platform..."}

@app.get("/nba-data")
async def get_nba_data():
    """Endpoint to trigger NBA data fetch manually"""

    # To start off with, I'm fetching some simple NBA data.
    # I'll drop that raw data in S3 and then start working with it from there.
    try:
        fetch_nba_data()
        return {"message": "NBA data fetched successfully, check console output."}
    except Exception as e:
        return {"error": f"Failed to fetch NBA data: {str(e)}"}
