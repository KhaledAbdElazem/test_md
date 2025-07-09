
# HTML to PDF Converter

This is a simple Python application that allows you to convert HTML files to PDF documents using a graphical user interface (GUI).

## Features

* **Easy-to-use GUI:** A straightforward interface for selecting HTML files and specifying output PDF names.

* **HTML to PDF Conversion:** Leverages `pdfkit` and `wkhtmltopdf` to perform the conversion.

* **Error Handling:** Provides feedback on successful conversion or any issues encountered.

## Prerequisites

Before running this application, you need to install the following:

1. **Python 3:** Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

2. **wkhtmltopdf:** This is a command-line tool that renders HTML into PDF and various image formats. The `pdfkit` Python library uses it under the hood.

   * Download the appropriate installer for your operating system from the official [wkhtmltopdf downloads page](https://wkhtmltopdf.org/downloads.html).

   * **Important:** During installation, ensure you install it to the default path or note down the installation path. The provided Python code expects `wkhtmltopdf.exe` to be located at `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe` on Windows. If you install it elsewhere, you will need to update the `config` line in the Python script:

     ```python
     config = pdfkit.configuration(wkhtmltopdf=r'C:\Your\Custom\Path\to\wkhtmltopdf.exe')
     ```

3. **Python Libraries:**

   * `tkinter` (usually comes with Python installation)

   * `pdfkit`

## Installation

1. **Install `pdfkit`:**
   Open your terminal or command prompt and run:

   ```bash
   pip install pdfkit
   ```

2. **Download `wkhtmltopdf`:**
   As mentioned in the Prerequisites, download and install `wkhtmltopdf` from its official website.

## How to Use

1. **Save the Code:**
   Save the provided Python code into a file named `html_to_pdf_converter.py` (or any `.py` extension).

2. **Update wkhtmltopdf Path (if necessary):**
   Open the `html_to_pdf_converter.py` file and verify the `wkhtmltopdf` path in the `config` variable. Adjust it if your `wkhtmltopdf.exe` is installed in a different location.

   ```python
   config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
   # Change the path above if wkhtmltopdf.exe is installed elsewhere
   ```

3. **Run the Application:**
   Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

   ```bash
   python html_to_pdf_converter.py
   ```

4. **Convert HTML:**

   * A small window titled "HTML → PDF Converter" will appear.

   * Click the "اختار HTML وحوّله PDF" (Choose HTML and convert to PDF) button.

   * A file dialog will open. Select the HTML file you wish to convert.

   * A small input box will appear, prompting you to "اكتب اسم ملف PDF اللي هيطلع:" (Type the name of the output PDF file). Enter your desired name (e.g., `my_document.pdf`). The `.pdf` extension will be added automatically if you don't include it.

   * Click "OK".

   * The application will attempt to convert the HTML file.

   * You will receive a message box indicating whether the conversion was successful ("✅ PDF Created") or if an error occurred ("❌ حصل مشكلة").

## Troubleshooting

* **`wkhtmltopdf` not found:** If you get an error related to `wkhtmltopdf` not being found, double-check the path in the `config` variable in your Python script. Ensure it points directly to the `wkhtmltopdf.exe` executable.

* **`pdfkit.exceptions.No._wkhtmltopdf.Error`:** This error usually means `wkhtmltopdf` is not installed or `pdfkit` cannot find it. Re-install `wkhtmltopdf` and verify the path.

* **Other Errors:** The application provides the error message from the underlying `pdfkit` library. If you encounter specific issues, the error message should give you a clue.

