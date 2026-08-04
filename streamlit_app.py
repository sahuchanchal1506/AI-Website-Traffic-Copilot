import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Website Traffic Copilot", layout="wide")

st.title("🚀 AI Website Traffic Copilot")
st.write("Upload your 6 Website Traffic CSV files")

# File Upload
audience = st.file_uploader("Audience CSV", type=["csv"])
events = st.file_uploader("Events CSV", type=["csv"])
landing = st.file_uploader("Landing Page CSV", type=["csv"])
pages = st.file_uploader("Pages CSV", type=["csv"])
traffic = st.file_uploader("Traffic CSV", type=["csv"])
user = st.file_uploader("User Acquisition CSV", type=["csv"])

if (
    audience is not None
    and events is not None
    and landing is not None
    and pages is not None
    and traffic is not None
    and user is not None
):

    audience_df = pd.read_csv(audience)
    events_df = pd.read_csv(events)
    landing_df = pd.read_csv(landing)
    pages_df = pd.read_csv(pages)
    traffic_df = pd.read_csv(traffic)
    user_df = pd.read_csv(user)

    st.success("✅ All six files uploaded successfully!")

    st.header("📊 Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric("Audience Rows", audience_df.shape[0])
    c2.metric("Traffic Rows", traffic_df.shape[0])
    c3.metric("Events Rows", events_df.shape[0])

    st.divider()

    st.subheader("Audience Data")
    st.dataframe(audience_df.head())

    st.subheader("Traffic Data")
    st.dataframe(traffic_df.head())

    st.subheader("Events Data")
    st.dataframe(events_df.head())

    st.divider()

    st.subheader("Traffic Chart")

    numeric_cols = traffic_df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        st.bar_chart(traffic_df[numeric_cols])
    else:
        st.warning("No numeric columns found in Traffic CSV.")

    st.subheader("User Acquisition Chart")

    numeric_cols = user_df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        st.bar_chart(user_df[numeric_cols])
    else:
        st.warning("No numeric columns found in User Acquisition CSV.")

    st.subheader("Events Chart")

    numeric_cols = events_df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        st.bar_chart(events_df[numeric_cols])
    else:
        st.warning("No numeric columns found in Events CSV.")

    st.divider()

    st.subheader("🤖 AI Insights")

    st.info("""
✅ All files uploaded successfully.

📈 Website traffic data loaded.

📊 Dashboard generated.

🎯 Focus on channels with the highest sessions.

🚀 Improve low-performing traffic sources.
""")

else:
    st.warning("Please upload all six CSV files.")