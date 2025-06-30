import requests

def generate_doc(cover_letter: str, google_token: str, job_title: str = "Job Application") -> str:
    # === Step 1: Create a new Google Doc ===
    create_url = "https://docs.googleapis.com/v1/documents"
    headers = {
        "Authorization": f"Bearer {google_token}",
        "Content-Type": "application/json"
    }

    create_payload = {
        "title": f"{job_title} - Cover Letter"
    }

    create_response = requests.post(create_url, headers=headers, json=create_payload)
    if create_response.status_code != 200:
        return f"❌ Failed to create doc: {create_response.text}"

    doc_id = create_response.json().get("documentId")

    # === Step 2: Insert cover letter into the Google Doc ===
    insert_url = f"https://docs.googleapis.com/v1/documents/{doc_id}:batchUpdate"
    content_payload = {
        "requests": [
            {
                "insertText": {
                    "location": {
                        "index": 1
                    },
                    "text": cover_letter
                }
            }
        ]
    }

    update_response = requests.post(insert_url, headers=headers, json=content_payload)

    if update_response.status_code == 200:
        return f"https://docs.google.com/document/d/{doc_id}/edit"
    else:
        return f"❌ Failed to update doc: {update_response.text}"
