## Preload JSON Converter

### Overview

This Python script provides a user-friendly interface using Streamlit, allowing users to convert Excel files or CSV files into JSON format. The tool is particularly useful for survey preloading, enabling the easy transformation of spreadsheet data into a format compatible with various software applications.

### How to Use

1. **Upload File**: Start by uploading a CSV or Excel file using the file uploader provided in the user interface.

2. **Preview Data**: Once the file is uploaded, the tool displays the contents of the file as a DataFrame, allowing users to preview the data before conversion.

3. **Convert to JSON**: Click the "Convert to JSON" button to initiate the conversion process. The tool will transform the data into JSON format and display it in a text area below the button.

4. **Download JSON File**: After the conversion, users can download the generated JSON file by clicking the "Download JSON File" button. The downloaded file will be named based on the uploaded file's name.

### Requirements

- Python 3.x
- Required Python libraries are mentioned in the code (Streamlit and Pandas). You can install them using `pip install streamlit pandas`.

### How to Run

To run the script, execute it using a Python interpreter. Ensure that you have the required libraries installed. The script will launch a local web server and provide a link. Click on the link to open the Streamlit app in your web browser. From there, follow the steps mentioned above to convert your files to JSON.

### Note

This tool assumes that the input CSV or Excel file contains data in a structured tabular format. It is important to verify the integrity of the input data to ensure accurate conversion.

Feel free to use, modify, and distribute this tool according to your project requirements. If you encounter any issues or have suggestions for improvement, please feel free to raise them in the repository's issues section.

---

*Disclaimer: This tool is provided as-is without any warranties. Users are encouraged to review and understand the code before use.*
