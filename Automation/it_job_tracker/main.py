import requests
import pandas as pd
import time
import os
import calendar

keywords = [
    "AI",
    "Frontend",
    "Backend",
    "Cloud",
    "DevOps",
    "IT-support",
    "Cybersecurity"
]

years = [2026]

months = range(1, 13)

CSV_FILE = "jobs_2026.csv"

# Show all dataframe columns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# =========================================================
# TREND DATA
# =========================================================

trend_data = {
    year: {kw: 0 for kw in keywords}
    for year in years
}

# =========================================================
# RAW API TOTALS
# =========================================================

raw_hits = {}

total_raw_hits = 0

# =========================================================
# STORE ALL JOBS
# =========================================================

all_jobs = []

print("Fetching data from JobTech Historical API...")

# =========================================================
# PART 1 — ACCURATE TREND COUNTS
# =========================================================

for year in years:

    for keyword in keywords:

        yearly_total = 0

        for month in months:

            last_day = calendar.monthrange(
                year,
                month
            )[1]

            url = (
                f"https://historical.api.jobtechdev.se/search"
                f"?q={keyword}"
                f"&published-after={year}-{month:02d}-01"
                f"&published-before={year}-{month:02d}-{last_day}"
                f"&limit=0"
            )

            try:

                response = requests.get(
                    url,
                    timeout=15
                )

                data = response.json()

                count = data.get(
                    "total",
                    {}
                ).get("value", 0)

                yearly_total += count

            except Exception:

                print(
                    f"Skipping "
                    f"{keyword} "
                    f"{year}-{month:02d}"
                )
            time.sleep(0.01)

        trend_data[year][keyword] = yearly_total

        raw_hits.setdefault(keyword, 0)

        raw_hits[keyword] += yearly_total

        total_raw_hits += yearly_total

# =========================================================
# PART 2 — FETCH REAL JOBS
# =========================================================

for year in years:

    for month in months:

        last_day = calendar.monthrange(
            year,
            month
        )[1]


        for keyword in keywords:
            for offset in range(0, 3000, 100):
                url = (
                    f"https://historical.api.jobtechdev.se/search"
                    f"?q={keyword}"
                    f"&published-after={year}-{month:02d}-01"
                    f"&published-before={year}-{month:02d}-{last_day}"
                    f"&limit=100"
                    f"&offset={offset}"
                )

                try:
                    response = requests.get(
                        url,
                        timeout=15
                    )

                    data = response.json()

                    hits = data.get("hits", [])

                    # Stop when no more jobs
                    if not hits:

                        break

                    for job in hits:
                        title = job.get(
                            "headline",
                            "N/A"
                        )

                        employer = job.get(
                            "employer",
                            {}
                        ).get("name", "N/A")

                        municipality = job.get(
                            "workplace_address",
                            {}
                        ).get(
                            "municipality",
                            "N/A"
                        )

                        all_jobs.append({
                            "id": job.get(
                                "id",
                                "N/A"
                            ),
                            "publication_date": job.get("publication_date"),
                            "year": year,
                            "month": month,
                            "keyword": keyword,
                            "title": title,
                            "employer": employer,
                            "municipality": municipality
                        })

                except Exception:
                    print(
                        f"Pagination failed for "
                        f"{keyword} "
                        f"{year}-{month:02d}"
                    )

                    break

                #time.sleep(0.001)

# =========================================================
# SAVE TO CSV
# =========================================================

df_new = pd.DataFrame(all_jobs)

# Remove duplicates
df_new = df_new.drop_duplicates(
    subset=["id", "keyword"]
)

# Merge with existing CSV
if os.path.exists(CSV_FILE):

    df_existing = pd.read_csv(CSV_FILE)

    df_combined = pd.concat(
        [df_existing, df_new]
    )

    df_combined = df_combined.drop_duplicates(
        subset=["id", "keyword"]
    )

else:

    df_combined = df_new

# Keep only 2021+
df_combined = df_combined[
    df_combined["year"] >= 2021
]

df_combined["publication_date"] = pd.to_datetime(
    df_combined["publication_date"],
    errors="coerce"
)

df_combined["publication_date"] = df_combined["publication_date"].dt.date

df_combined = df_combined.sort_values(
    by="publication_date",
    ascending=False
)

# Save CSV
df_combined.to_csv(
    CSV_FILE,
    index=False
)

total_saved = len(df_combined)

# =========================================================
# TREND TABLE AFTER DEDUPLICATION
# =========================================================

dedup_table = (
    df_combined
    .groupby(["year", "keyword"])
    .size()
    .unstack(fill_value=0)
)

# =========================================================
# PRINT RESULTS
# =========================================================

print("\nRaw hits count per keyword:")

for keyword in keywords:

    print(f"{keyword}: {raw_hits[keyword]}")

print(
    f"\nTotal raw hits across all keywords: "
    f"{total_raw_hits}"
)

# =========================================================
# BEFORE DEDUPLICATION
# =========================================================

print("\n=== BEFORE DEDUPLICATION ===\n")

header = f"{'year':<8}"

for keyword in keywords:

    header += f"{keyword:<15}"

print(header)

print("-" * len(header))

for year in years:

    row = f"{year:<8}"

    for keyword in keywords:

        row += (
            f"{trend_data[year][keyword]:<15}"
        )

    print(row)

# =========================================================
# AFTER DEDUPLICATION
# =========================================================

print("\n=== AFTER DEDUPLICATION (2021+) ===\n")

print(dedup_table)

print(
    f"\nTotal unique jobs after deduplication: "
    f"{total_saved}"
)

print(f"\nCSV updated: {CSV_FILE}")