import requests
import time

# 🔑 PASTE YOUR YOUTUBE API KEY HERE
API_KEY = "AIzaSyDFRuWz0nCBkTQzx8nZH43wSQ_d5P-2tZU"

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"


def fetch_youtube_workflows(country="US", max_results=10):
    """
    Fetch n8n workflow videos from YouTube
    """
    search_params = {
        "part": "snippet",
        "q": "n8n workflow automation",
        "type": "video",
        "regionCode": country,
        "maxResults": max_results,
        "key": API_KEY
    }

    search_response = requests.get(SEARCH_URL, params=search_params).json()

    video_ids = []
    for item in search_response.get("items", []):
        video_ids.append(item["id"]["videoId"])

    if not video_ids:
        return []

    # Fetch statistics (views, likes, comments)
    stats_params = {
        "part": "statistics",
        "id": ",".join(video_ids),
        "key": API_KEY
    }

    stats_response = requests.get(VIDEO_URL, params=stats_params).json()

    stats_map = {}
    for item in stats_response.get("items", []):
        stats_map[item["id"]] = item["statistics"]

    workflows = []

    for item in search_response.get("items", []):
        vid = item["id"]["videoId"]
        stats = stats_map.get(vid, {})

        views = int(stats.get("viewCount", 0))
        likes = int(stats.get("likeCount", 0))
        comments = int(stats.get("commentCount", 0))

        workflows.append({
            "workflow": item["snippet"]["title"],
            "platform": "YouTube",
            "popularity_metrics": {
                "views": views,
                "likes": likes,
                "comments": comments,
                "like_to_view_ratio": round(likes / views, 4) if views else 0,
                "comment_to_view_ratio": round(comments / views, 4) if views else 0
            },
            "country": country
        })

    time.sleep(1)  # Prevent rate-limit issues
    return workflows


# 🧪 TESTING
if __name__ == "__main__":
    data = fetch_youtube_workflows(country="US")
    print(data)
