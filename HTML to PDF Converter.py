import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import pdfkit
import os
import json

# --- Configuration Management ---
CONFIG_FILE = "config.json"

def load_config():
    """Loads configuration from a JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config(config):
    """Saves configuration to a JSON file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def get_wkhtmltopdf_path():
    """
    Attempts to get wkhtmltopdf.exe path from config,
    common locations, or by prompting the user.
    """
    config = load_config()
    wkhtmltopdf_path = config.get("wkhtmltopdf_path")

    if wkhtmltopdf_path and os.path.exists(wkhtmltopdf_path):
        return wkhtmltopdf_path

    # Try common default installation paths for Windows
    common_paths = [
        r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'
    ]
    for path in common_paths:
        if os.path.exists(path):
            config["wkhtmltopdf_path"] = path
            save_config(config)
            return path

    # If not found, ask the user to locate it
    messagebox.showinfo(
        "wkhtmltopdf Not Found",
        "wkhtmltopdf.exe was not found. Please locate it manually."
    )
    new_path = filedialog.askopenfilename(
        title="Locate wkhtmltopdf.exe",
        filetypes=[("Executable files", "wkhtmltopdf.exe")]
    )
    if new_path:
        config["wkhtmltopdf_path"] = new_path
        save_config(config)
        return new_path
    return None

# --- PDF Conversion Function ---
def convert_to_pdf():
    """Handles the HTML to PDF conversion process."""
    wkhtmltopdf_exe_path = get_wkhtmltopdf_path()
    if not wkhtmltopdf_exe_path:
        messagebox.showerror("Error", "wkhtmltopdf.exe path not set. Cannot proceed.")
        return

    try:
        # Configure pdfkit with the determined path
        pdf_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_exe_path)
    except Exception as e:
        messagebox.showerror("Configuration Error", f"Failed to configure pdfkit: {e}")
        return

    html_path = filedialog.askopenfilename(title="اختر ملف HTML", filetypes=[("HTML files", "*.html")])
    if not html_path:
        return

    if not os.path.exists(html_path):
        messagebox.showerror("خطأ", "❌ ملف HTML المحدد غير موجود.")
        return

    output_pdf = simpledialog.askstring("اسم الملف", "اكتب اسم ملف PDF اللي هيطلع:")
    if not output_pdf:
        return

    if not output_pdf.lower().endswith('.pdf'):
        output_pdf += '.pdf'

    try:
        # Display a simple "Converting..." message
        status_label.config(text="Converting... Please wait.")
        root.update_idletasks() # Update the GUI immediately

        pdfkit.from_file(html_path, output_pdf, configuration=pdf_config)
        messagebox.showinfo("تم", f"✅ PDF Created: {output_pdf}")
    except Exception as e:
        error_message = str(e)
        if "No wkhtmltopdf executable found" in error_message:
            messagebox.showerror(
                "خطأ",
                "❌ wkhtmltopdf.exe غير موجود أو المسار غير صحيح. يرجى التحقق من التثبيت والمسار."
            )
        else:
            messagebox.showerror("خطأ", f"❌ حصل مشكلة: {error_message}")
    finally:
        status_label.config(text="") # Clear status message

# --- GUI Setup ---
root = tk.Tk()
root.title("HTML → PDF Converter")
root.geometry("400x150") # Slightly larger window

# Center the window
window_width = 400
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

btn = tk.Button(root, text="اختار HTML وحوّله PDF", command=convert_to_pdf, padx=15, pady=10)
btn.pack(pady=20)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

root.mainloop()
