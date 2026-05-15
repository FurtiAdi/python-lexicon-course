import requests
import pandas as pd
import time
import os
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv(
    "/Users/furtunaeyob/Library/CloudStorage/OneDrive-StockholmUniversity/Skrivbordet/python_course_lexicon/python-lexicon-course/.env"
)


# =========================
# SAME KEYWORDS AS MAIN
# =========================

keywords = [
    "AI",
    "Frontend",
    "Backend",
    "Cloud",
    "DevOps",
    "IT-support",
    "Cybersecurity"
]

CSV_FILE = "weekly_jobs.csv"

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# =========================
# DATE RANGE (LAST 7 DAYS)
# =========================

today = datetime.today()
last_week = today - timedelta(days=7)

start_date = last_week.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

print(f"Fetching jobs from {start_date} to {end_date}")

# =========================
# STORE JOBS (SAME STRUCTURE)
# =========================

all_jobs = []

# =========================================================
# FETCH REAL JOBS (SAME AS MAIN BUT WEEKLY)
# =========================================================

for keyword in keywords:

    for offset in range(0, 15000, 100):   # same improvement as main

        url = (
            f"https://historical.api.jobtechdev.se/search"
            f"?q={keyword}"
            f"&published-after={start_date}"
            f"&published-before={end_date}"
            f"&limit=100"
            f"&offset={offset}"
        )

        try:
            response = requests.get(url, timeout=15)
            data = response.json()

            hits = data.get("hits", [])

            # stop when no more jobs
            if not hits:
                break

            for job in hits:

                date = job.get("publication_date")
                if not date:
                    continue

                title = job.get("headline", "N/A")

                employer = job.get(
                    "employer", {}
                ).get("name", "N/A")

                municipality = job.get(
                    "workplace_address", {}
                ).get("municipality", "N/A")

                all_jobs.append({
                    "id": job.get("id"),
                    "publication_date": date,
                    "keyword": keyword,
                    "title": title,
                    "employer": employer,
                    "municipality": municipality
                })

        except Exception:
            print(f"Error fetching {keyword}")
            break

# =========================================================
# SAVE TO CSV (SAME LOGIC AS MAIN)
# =========================================================

df_new = pd.DataFrame(all_jobs)

# 🔥 same fix as main
df_new = df_new.drop_duplicates(subset=["id"])

if os.path.exists(CSV_FILE):

    df_existing = pd.read_csv(CSV_FILE)

    df_combined = pd.concat([df_existing, df_new])

    df_combined = df_combined.drop_duplicates(subset=["id"])

else:
    df_combined = df_new

# =========================
# CLEAN DATE 
# =========================

df_combined["publication_date"] = pd.to_datetime(
    df_combined["publication_date"],
    errors="coerce"
)

df_combined = df_combined.dropna(subset=["publication_date"])

df_combined["year"] = df_combined["publication_date"].dt.year
df_combined["month"] = df_combined["publication_date"].dt.month

df_combined["publication_date"] = df_combined["publication_date"].dt.date

df_combined = df_combined.sort_values(
    by="publication_date",
    ascending=False
)

# save
df_combined.to_csv(CSV_FILE, index=False)

# =========================================================
# WEEKLY SUMMARY
# =========================================================

weekly_summary = df_new.groupby("keyword").size()

print("\n=== WEEKLY SUMMARY ===\n")
print(weekly_summary)

print(f"\nNew jobs added this week: {len(df_new)}")

# =========================
# EMAIL
# =========================

summary_text = "Weekly Job Summary:\n\n"
summary_text += weekly_summary.to_string()

def send_email(message):

    msg = MIMEText(message)
    msg["Subject"] = "Weekly Job Report"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)

send_email(summary_text)

print("\nEmail sent successfully!")