import requests
import datetime

def insert_into_notion(title, company, link, notion_token, database_id):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Company": {
                "title": [{
                    "text": {"content": company}
                }]
            },
            "Title": {
                "rich_text": [{
                    "text": {"content": title}
                }]
            },
            "Link": {
                "url": link
            },
            "Status": {
                "select": {
                    "name": "Applied"  # Optional: adjust to your Notion select options
                }
            }
            # Optional: Add "Date Added" if your database schema has it properly configured
            # "Date Added": {
            #     "date": {"start": datetime.datetime.now().isoformat()}
            # }
        }
    }

    res = requests.post(url, headers=headers, json=data)
    if res.status_code == 200:
        return res.json().get("url", "✅ Added to Notion")
    else:
        return f"Error adding to Notion: {res.text}"
