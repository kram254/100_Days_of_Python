#extract
# Carrie Liu
# carrihl1@uci.edu
# 64814057

import requests

# API endpoint for football results
FOOTBALL_API_URL = "https://api.football-data.org/v2/"

# API key for football results API
FOOTBALL_API_KEY = "YOUR_API_KEY_HERE"

# team ID for your favorite team
TEAM_ID = 66  # team ID for man United

# headers to be included with API requests
headers = {
    "X-Auth-Token": FOOTBALL_API_KEY,
    "Content-Type": "application/json",
}


def get_latest_football_results():
    """
    Returns the latest results of a team's 3 latest matches for football.
    """
    # get the team's latest matches
    url = f"{FOOTBALL_API_URL}teams/{TEAM_ID}/matches?status=FINISHED&limit=3"
    response = requests.get(url, headers=headers)

    # extract data from response
    if response.status_code == 200:
        team_data = response.json()["matches"]
        results = []

        # extract the results for the team's latest 3 matches
        for match in team_data:
            result = {"date": match["utcDate"], "result": match["score"]["fullTime"]}
            results.append(result)

        return results


def main():
    results = get_latest_football_results()
    if results:
        print(f"Latest results for team ID {TEAM_ID}:")
        for result in results:
            print(f"Date: {result['date']}, Result: {result['result']}")
    else:
        print(f"No results found for team ID {TEAM_ID}.")


if __name__ == "__main__":
    main()
