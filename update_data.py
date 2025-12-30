import json
from datetime import datetime
from youtube_fetch import fetch_youtube_workflows
from forum_fetch import fetch_forum_workflows
from google_fetch import fetch_google_trends

def update_data():
    print("Fetching YouTube US data...")
    us_data = fetch_youtube_workflows(country="US")

    print("Fetching YouTube India data...")
    in_data = fetch_youtube_workflows(country="IN")

    print("Fetching Forum data...")
    forum_data = fetch_forum_workflows()

    print("Fetching Google Trends data...")
    google_data = fetch_google_trends()

    all_data = us_data + in_data + forum_data + google_data

    with open("data.json", "w") as f:
        json.dump(all_data, f, indent=2)

    print(f"Saved {len(all_data)} workflows to data.json")

    # ✅ Automation proof
    with open("automation.log", "a") as log:
        log.write(f"Update ran successfully at {datetime.now()}\n")


if __name__ == "__main__":
    update_data()
