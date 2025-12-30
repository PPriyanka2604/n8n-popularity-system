from pytrends.request import TrendReq
import time

def fetch_google_trends(country=""):
    try:
        pytrends = TrendReq(
            hl="en-US",
            tz=360,
            timeout=(10, 25)  # increased timeout
        )

        keywords = [
            "n8n automation",
            "n8n workflow",
            "n8n integration",
            "n8n slack",
            "n8n gmail"
        ]

        pytrends.build_payload(
            keywords,
            timeframe="today 12-m",
            geo=country
        )

        interest = pytrends.interest_over_time()

        workflows = []

        if interest.empty:
            return workflows

        for kw in keywords:
            workflows.append({
                "workflow": kw,
                "platform": "Google",
                "popularity_metrics": {
                    "average_trend_score": int(interest[kw].mean())
                },
                "country": country if country else "Global"
            })

        return workflows

    except Exception as e:
        print("⚠️ Google Trends fetch failed, skipping.")
        print("Reason:", e)
        return []


# 🧪 Test
if __name__ == "__main__":
    print(fetch_google_trends())
