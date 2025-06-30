import requests

def scrape_remoteok_jobs(keyword: str = "data scientist", limit: int = 3):
    print(f"🌐 Scraping RemoteOK API for '{keyword}'")

    try:
        res = requests.get("https://remoteok.com/api", headers={"User-Agent": "Mozilla/5.0"})
        jobs_raw = res.json()

        if not isinstance(jobs_raw, list) or len(jobs_raw) < 2:
            print("⚠️ Unexpected response format")
            return []

        jobs = []
        for job in jobs_raw[1:]:  # Skip first element (API metadata)
            title = job.get("position", "")
            company = job.get("company", "")
            url = job.get("url", "")
            tags = job.get("tags", [])
            if keyword.lower() in title.lower() or any(keyword.lower() in t.lower() for t in tags):
                jobs.append({
                    "title": title,
                    "company": company,
                    "link": url
                })
            if len(jobs) >= limit:
                break

        print(f"✅ Found {len(jobs)} jobs on RemoteOK")
        return jobs

    except Exception as e:
        print(f"❌ Failed to scrape RemoteOK API: {e}")
        return []
