🚀 n8n Workflow Popularity System

A production-ready analytics platform that identifies and ranks the most popular n8n workflows across multiple public platforms using real popularity evidence.

The system aggregates engagement data from YouTube, n8n Community Forum, and Google Search Trends, exposes it through a REST API, and visualizes insights using a web dashboard with charts.

📌 Motivation

The n8n ecosystem has thousands of workflows shared across videos, forum discussions, and blogs.
However, users currently lack a single, reliable source to answer:

Which workflows are most popular?

Which automations are trending right now?

What workflows are popular in different countries?

Which platform contributes the strongest engagement?

This project solves that problem by collecting, validating, and aggregating popularity signals from multiple trusted sources.

🎯 Project Objectives

Collect workflow popularity data from multiple platforms

Use numeric, verifiable evidence instead of assumptions

Segment popularity by platform and country

Expose data through a clean REST API

Enable automated daily/weekly updates

Design a system that can scale to 20,000+ workflows

Provide a visual dashboard for easy exploration

🧠 System Architecture
External Data Sources
 ├─ YouTube Data API
 ├─ n8n Community Forum (Discourse)
 └─ Google Trends
        │
        ▼
Platform-Specific Fetchers
        │
        ▼
Data Aggregation & Normalization
        │
        ▼
data.json (Unified Dataset)
        │
        ▼
FastAPI REST API
        │
        ├─ JSON Consumers
        └─ Web Dashboard (Charts & Tables)

📊 Data Sources & Popularity Signals
🔹 YouTube (YouTube Data API v3)

Used to capture content popularity and engagement.

Metrics collected:

View count

Like count

Comment count

Engagement ratios:

like_to_view_ratio

comment_to_view_ratio

Country segmentation:

United States (US)

India (IN)

🔹 n8n Community Forum (Discourse)

Used to measure community adoption and discussion depth.

Metrics collected:

Number of replies

Number of likes

Number of views

Indicates real usage and problem-solving activity

🔹 Google Search Trends (pytrends)

Used to measure user intent and demand.

Metrics collected:

Relative search interest score

Keyword-based discovery

Trend strength over time

📦 Dataset Overview

Total workflows: 50+ (real, verifiable)

Platforms: YouTube, Forum, Google

Countries: US, IN, Global

Storage: data.json

Update frequency: Automated (cron-ready)

Example Dataset Entry
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

Description

Returns a JSON array of workflows segmented by:

Platform

Country

Popularity metrics

API Characteristics

Stateless

Production-ready

JSON-only (easy integration with other systems)

🖥️ Web Dashboard (Bonus Feature)

The project includes a lightweight web UI built on top of the API.

Features

Interactive table of workflows

Filters by platform and country

Bar chart: YouTube Views vs Likes

Pie/Doughnut chart: Platform distribution

Real-time data loaded from the API

Access:

http://127.0.0.1:8000/ui

🔁 Automation & Scheduling
Update Script
python update_data.py

What the Script Does

Fetches fresh data from all platforms

Recalculates engagement ratios

Updates the dataset (data.json)

Logs execution timestamps (automation.log)

Handles API timeouts gracefully

Scheduling Examples

Linux (cron):

0 2 * * * python update_data.py


Windows (Task Scheduler):

Trigger: Daily / Weekly

Action: python update_data.py

✅ No manual intervention required.

⚙️ Installation & Running Locally
Prerequisites

Python 3.10+

Git

Setup
pip install -r requirements.txt
uvicorn main:app --reload

Access

API → http://127.0.0.1:8000/workflows

Dashboard → http://127.0.0.1:8000/ui

📈 Scalability & Design Considerations

While the sample dataset contains 50+ verified workflows, the system is intentionally designed to scale to 20,000+ workflows using:

Keyword expansion

Pagination

Batched API requests

Scheduled execution

API quotas and rate limits are respected during data collection.

✅ Production Readiness Checklist

✔ Modular code structure
✔ Clean JSON schema
✔ REST API usable on Day 1
✔ Automated data pipeline
✔ Logging & fault tolerance
✔ GitHub-ready documentation
✔ Extensible design

🔮 Future Enhancements

Composite popularity score

Trend growth analysis

User-defined filters

Export to CSV

Cloud deployment

Authentication & pagination

🏁 Conclusion

This project demonstrates how data engineering, APIs, automation, and visualization can be combined to build a real-world analytics system.
It is suitable for production deployment, academic evaluation, and interview discussion.

👤 Author

Priyanka
GitHub: https://github.com/PPriyanka2604
