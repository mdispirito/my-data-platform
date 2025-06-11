from nba_api.stats.endpoints import leaguegamefinder, playercareerstats, teamgamelog
from nba_api.stats.static import players, teams
import json

def fetch_nba_data():
    """A placeholder to fetch some test data"""
    print("=" * 50)
    print("FETCHING NBA DATA")
    print("=" * 50)
    
    # Get all teams
    print("\n1. NBA Teams:")
    nba_teams = teams.get_teams()
    for i, team in enumerate(nba_teams[:5]):  # Show first 5 teams
        print(f"   {team['full_name']} ({team['abbreviation']}) - ID: {team['id']}")
    print(f"   ... and {len(nba_teams) - 5} more teams")
    
    # Find some notable players
    print("\n5. Some Notable Players:")
    notable_players = ['Stephen Curry', 'Kevin Durant', 'Giannis Antetokounmpo']
    for player_name in notable_players:
        try:
            player_info = players.find_players_by_full_name(player_name)
            if player_info:
                print(f"   {player_info[0]['full_name']} - ID: {player_info[0]['id']}")
        except Exception as e:
            print(f"   Error finding {player_name}: {e}")
    
    print("\n" + "=" * 50)
    print("NBA DATA FETCH COMPLETE")
    print("=" * 50)
