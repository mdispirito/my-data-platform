from nba_api.stats.endpoints import leaguegamefinder, playercareerstats, teamgamelog
from nba_api.stats.static import players, teams
import json

def fetch_nba_teams():
    """A placeholder to fetch some test data"""

    print("Fetching NBA teams...")
    
    nba_teams = teams.get_teams()

    return {
        "total_teams": len(nba_teams),
        "teams": nba_teams
    }
