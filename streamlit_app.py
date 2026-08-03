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

st.success("Upload all six CSV files to view their details.")