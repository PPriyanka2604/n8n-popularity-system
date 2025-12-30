import requests

FORUM_URL = "https://community.n8n.io/latest.json"

def fetch_forum_workflows(limit=10):
    response = requests.get(FORUM_URL)
    data = response.json()

    topics = data.get("topic_list", {}).get("topics", [])
    workflows = []

    for topic in topics[:limit]:
        workflows.append({
            "workflow": topic["title"],
            "platform": "Forum",
            "popularity_metrics": {
                "replies": topic.get("posts_count", 0),
                "likes": topic.get("like_count", 0),
                "views": topic.get("views", 0)
            },
            "country": "Global"
        })

    return workflows


# 🧪 Test
if __name__ == "__main__":
    print(fetch_forum_workflows())
