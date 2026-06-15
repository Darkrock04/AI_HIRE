import streamlit as st
import requests

API_BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="Basic RAG System", page_icon="📄", layout="wide")

st.title("📄 Basic RAG System")
st.markdown("Upload a document, ask questions about it. Simple as that.")

# ---- Sidebar: Upload + Session ----
with st.sidebar:
    st.header("📚 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["txt", "pdf"])

    if st.button("⬆️ Upload & Embed", use_container_width=True):
        if uploaded_file:
            with st.spinner("Chunking and embedding..."):
                try:
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    resp = requests.post(f"{API_BASE_URL}/upload_doc", files=files)
                    if resp.status_code == 200:
                        data = resp.json()
                        st.success(f"{data['message']} ({data['chunks_added']} chunks)")
                    else:
                        st.error("Upload failed.")
                except Exception as e:
                    st.error(f"Backend error: {e}")
        else:
            st.warning("Select a file first.")

    st.divider()

    if st.button("🗑️ Clear Session", type="primary", use_container_width=True):
        with st.spinner("Clearing..."):
            try:
                resp = requests.post(f"{API_BASE_URL}/clear_session")
                data = resp.json()
                if data.get("status") == "success":
                    st.session_state.messages = []
                    st.success("Session cleared!")
                    st.rerun()
                else:
                    st.error(f"Error: {data.get('message')}")
            except Exception as e:
                st.error(f"Backend error: {e}")

# ---- Chat Interface ----
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask anything about your document..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        try:
            payload = {
                "message": prompt,
                "history": st.session_state.messages[-10:]
            }
            resp = requests.post(f"{API_BASE_URL}/chat", json=payload)
            if resp.status_code == 200:
                bot_response = resp.json()["response"]
            else:
                bot_response = f"Error: {resp.status_code}"
        except Exception as e:
            bot_response = f"Could not connect to backend: {e}"

    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
