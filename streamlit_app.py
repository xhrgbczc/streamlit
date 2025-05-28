import streamlit as st
# import streamlit.components.v1 as components

# st.title("🎈 My new app")
# st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

# components.iframe("https://www.baidu.com", height=500)
pages = {
    "Page": [
        st.Page("page_1.py", title="Page 1"),
        st.Page("page_2.py", title="Page 2"),
    ],
    "Resources": [
        st.Page("learn.py", title="Learn about us"),
        st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()


