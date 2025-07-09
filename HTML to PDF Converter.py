import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

def convert_to_pdf():
    html_path = filedialog.askopenfilename(title="اختر ملف HTML", filetypes=[("HTML files", "*.html")])
    if not html_path:
        return
    output_pdf = simpledialog.askstring("اسم الملف", "اكتب اسم ملف PDF اللي هيطلع:")
    if not output_pdf:
        return
    if not output_pdf.lower().endswith('.pdf'):
        output_pdf += '.pdf'
    try:
        pdfkit.from_file(html_path, output_pdf, configuration=config)
        messagebox.showinfo("تم", f"✅ PDF Created: {output_pdf}")
    except Exception as e:
        messagebox.showerror("خطأ", f"❌ حصل مشكلة: {e}")

root = tk.Tk()
root.title("HTML → PDF Converter")
root.geometry("300x100")

btn = tk.Button(root, text="اختار HTML وحوّله PDF", command=convert_to_pdf, padx=10, pady=10)
btn.pack(pady=20)

root.mainloop()
