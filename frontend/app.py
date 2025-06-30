import streamlit as st
import requests
import webbrowser

st.set_page_config(page_title="ProjectPulse", page_icon="🧠")
st.title("🚀 ProjectPulse: AI-Powered Job Application Assistant")

API_BASE = "http://127.0.0.1:8000"

# ===============================
# 🔐 Step 0: Authenticate with Notion and Google
# ===============================
st.subheader("🔐 Step 0: Connect Your Tools")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔗 Connect Notion"):
        auth_url = f"{API_BASE}/auth/notion/login"
        webbrowser.open_new_tab(auth_url)

with col2:
    if st.button("🔗 Connect Google Docs"):
        auth_url = f"{API_BASE}/auth/google/login"
        webbrowser.open_new_tab(auth_url)

st.markdown("---")

# ===============================
# 📤 Step 1: Upload Your Resume
# ===============================
st.subheader("📤 Step 1: Upload Your Resume")

with st.form("upload_resume_form"):
    resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    upload_btn = st.form_submit_button("Upload Resume")

    if upload_btn:
        if resume_file is not None:
            try:
                response = requests.post(
                    f"{API_BASE}/job/upload-resume",
                    files={"file": (resume_file.name, resume_file, resume_file.type)}
                )
                if response.status_code == 200:
                    st.success("✅ Resume uploaded successfully.")
                else:
                    st.error(f"❌ Upload failed: {response.text}")
            except Exception as e:
                st.error(f"⚠️ Upload error: {e}")
        else:
            st.warning("⚠️ Please upload a file.")

st.markdown("---")

# ===============================
# 🚀 Step 2: Auto Apply for Jobs
# ===============================
st.subheader("🧠 Step 2: Auto Apply for Jobs")

with st.form("auto_apply_form"):
    keyword = st.text_input("Job Keyword", value="data scientist")
    location = st.text_input("Location (optional)", value="remote")
    run_pipeline = st.form_submit_button("Run Auto Pipeline")

    if run_pipeline:
        with st.spinner("🔍 Running job pipeline and generating cover letters..."):
            try:
                response = requests.post(
                    f"{API_BASE}/job/auto",
                    json={"keyword": keyword, "location": location}
                )
                if response.status_code == 200:
                    jobs = response.json().get("jobs", [])
                    if jobs:
                        st.success(f"✅ {len(jobs)} jobs processed.")
                        for job in jobs:
                            st.markdown(f"### 💼 {job['title']} at {job['company']}")
                            st.markdown(f"🔗 [Job Link]({job['job_link']})")
                            st.markdown(f"📄 [Cover Letter]({job['google_doc']})")
                            st.markdown(f"🧱 Notion Status: `{job['notion_entry']}`")
                            with st.expander("📬 View Generated Cover Letter"):
                                st.write(job["cover_letter"])
                            st.markdown("---")
                    else:
                        st.warning("⚠️ No jobs found for this keyword/location.")
                else:
                    st.error(f"❌ API failed: {response.text}")
            except Exception as e:
                st.error(f"⚠️ Request error: {e}")
