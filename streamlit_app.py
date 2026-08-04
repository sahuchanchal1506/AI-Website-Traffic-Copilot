import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Website Traffic Copilot", layout="wide")

st.title("🚀 AI Website Traffic Copilot")
st.write("Upload your 6 website traffic CSV files")

audience = st.file_uploader("Audience CSV", type="csv")
events = st.file_uploader("Events CSV", type="csv")
landing = st.file_uploader("Landing Page CSV", type="csv")
pages = st.file_uploader("Pages CSV", type="csv")
traffic = st.file_uploader("Traffic CSV", type="csv")
user = st.file_uploader("User Acquisition CSV", type="csv")

files = {
    "Audience": audience,
    "Events": events,
    "Landing Page": landing,
    "Pages": pages,
    "Traffic": traffic,
    "User Acquisition": user
}

for name, file in files.items():
    if file is not None:
        df = pd.read_csv(file)

        st.subheader(name)

        c1, c2, c3 = st.columns(3)
        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Missing Values", int(df.isnull().sum().sum()))

        st.dataframe(df.head())

if all(files.values()):
    st.success("✅ All six files uploaded successfully!")

    traffic_df = pd.read_csv(traffic)
    user_df = pd.read_csv(user)
    events_df = pd.read_csv(events)

    st.divider()
    st.header("📊 Website Traffic Dashboard")

    col1, col2, col3 = st.columns(3)

    total_users = user_df.iloc[:, -1].sum()
    total_events = events_df.iloc[:, -1].sum()
    total_traffic = traffic_df.iloc[:, -1].sum()

    col1.metric("👥 Total Users", f"{total_users:,}")
    col2.metric("📈 Total Traffic", f"{total_traffic:,}")
    col3.metric("🎯 Total Events", f"{total_events:,}")

    st.subheader("Traffic Overview")
    st.bar_chart(traffic_df.iloc[:, [0, -1]].set_index(traffic_df.columns[0]))

    st.subheader("User Acquisition")
    st.bar_chart(user_df.iloc[:, [0, -1]].set_index(user_df.columns[0]))

    st.subheader("Events")
    st.bar_chart(events_df.iloc[:, [0, -1]].set_index(events_df.columns[0]))

    st.subheader("🤖 AI Insights")

    top_channel = user_df.iloc[user_df.iloc[:, -1].idxmax(), 0]

    st.info(f"""
    • Top acquisition channel: **{top_channel}**

    • Uploads completed successfully.

    • Focus on the highest-performing traffic source.

    • Optimize low-performing channels to increase website traffic.
    """)
else:
    st.warning("Please upload all six CSV files.")