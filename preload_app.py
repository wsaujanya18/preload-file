import streamlit as st
import pandas as pd

st.header("Preload JSON")
st.write("Converts preload excel file to preload json file.")
st.write("")

def main():
  st.title("CSV and Excel file Uploader")

  # File uploader
  uploaded_file = st.file_uploader("Uplaod a CSV or Excel file", type=["csv", "xlsx"])

  if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]
    file_name = uploaded_file.name.split(".")[0]

    if file_extension == "csv":
      df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
      df = pd.read_excel(uploaded_file)

    # Show Dataframe
    st.dataframe(df)

    # Convert to JSON Button
    if st.button("Convert to JSON"):
      json_data = df.to_json(orient='records', force_ascii=False)
      st.text_area("JSON Data", json_data, height=500)

      # Download button for JSON data
      st.download_button("Download JSON File", data=json_data, file_name=file_name, mime="text/json")


if __name__ == "__main__":
  main()
