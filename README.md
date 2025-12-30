🚀 n8n Workflow Popularity System

A production-ready analytics system that identifies the most popular n8n workflows across multiple platforms using real engagement and trend data.
The system is API-first, cron-ready, and includes a visual dashboard for insights.

📌 Problem Statement

n8n users rely on community content (videos, forum posts, search trends) to discover useful workflows.
However, there is no unified system that measures workflow popularity across platforms using trustworthy evidence.

This project solves that by aggregating popularity signals from:

YouTube

n8n Community Forum

Google Search Trends

🎯 Objectives

Identify popular n8n workflows across platforms

Use clear, numeric evidence (views, likes, replies, trends)

Segment data by platform and country

Expose results via a REST API

Enable automated, scheduled updates

Ensure the system is scalable to 20,000+ workflows

🧠 System Architecture
YouTube API        Forum API        Google Trends
     │                 │                  │
     ├──── Fetchers ───┼──── Fetchers ────┤
     │                 │                  │
                 Data Aggregation
                         │
                    data.json
                         │
                 FastAPI REST API
                         │
                  Web Dashboard

📊 Data Sources & Popularity Signals
🔹 YouTube (YouTube Data API v3)

Popularity evidence:

View count

Like count

Comment count

Engagement ratios:

like_to_view_ratio

comment_to_view_ratio

Country segmentation: US, IN

🔹 n8n Community Forum (Discourse)

Popularity evidence:

Number of replies

Number of likes

Thread view count

Unique community engagement

🔹 Google Search (Google Trends)

Popularity evidence:

Relative search interest score

Keyword-based discovery

Trend strength over time

📦 Dataset

Total workflows: 50+ (real, verifiable)

Platforms: YouTube, Forum, Google

Countries: United States (US), India (IN), Global

Storage: data.json

Example Entry
{
  "workflow": "Google Sheets → Slack Automation",
  "platform": "YouTube",
  "popularity_metrics": {
    "views": 12500,
    "likes": 630,
    "comments": 88,
    "like_to_view_ratio": 0.05,
    "comment_to_view_ratio": 0.007
  },
  "country": "US"
}

🔗 REST API
Endpoint
GET /workflows

Response

JSON array of workflow popularity data

Platform and country segmented

Ready for external consumption

🖥️ Web Dashboard (Bonus)

Interactive charts (Views vs Likes)

Platform distribution visualization

Filters by platform and country

Built using Chart.js

Access:

http://127.0.0.1:8000/ui

🔁 Automation (Cron-Ready)
Update Script
python update_data.py

What It Does

Fetches latest data from all platforms

Recalculates engagement metrics

Updates dataset automatically

Logs execution timestamps

Scheduling Examples

Linux (cron):

0 2 * * * python update_data.py


Windows (Task Scheduler):

Trigger: Daily / Weekly

Action: python update_data.py

⚙️ Installation & Running Locally
pip install -r requirements.txt
uvicorn main:app --reload


Open:

API → http://127.0.0.1:8000/workflows

Dashboard → http://127.0.0.1:8000/ui

📈 Scalability Note (IMPORTANT)

While the current dataset contains 50+ verified workflows, the system is designed to scale to 20,000+ workflows using keyword expansion, pagination, batching, and scheduled execution, while respecting API rate limits.

✅ Production Readiness

✔ Modular, clean codebase
✔ API-first architecture
✔ Automated data pipeline
✔ Structured JSON output
✔ Country & platform segmentation
✔ Ready for deployment

🏁 Conclusion

This project delivers a reliable, automated, and scalable system to identify popular n8n workflows using real engagement data.
It can be deployed immediately and extended to handle large-scale datasets.

👤 Author

Priyanka