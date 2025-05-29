import streamlit as st
import streamlit.components.v1 as components

st.title("Page 1")

st.title("🎈 Google")
# st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

components.iframe("https://www.google.com", height=800)
