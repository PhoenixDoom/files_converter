import tkinter as tk
from tkinter import ttk, Button, filedialog
from PIL import Image
import fitz
from moviepy.editor import VideoFileClip
from docx2pdf import convert
import os


# Functions
def convert_image(filetypes, format_name):
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        new_path = file_path[:-4] + "." + format_name
    else:
        new_path = filedialog.asksaveasfilename(filetypes=[(format_name.upper() + " files", "*." + format_name)]) + "." + format_name
    img.save(new_path, format_name)
    status_label.config(text=f"File converted to {format_name.upper()}: {new_path}")

def convert_pdf(extension):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    pdf_file = fitz.open(file_path)
    for page_num in range(pdf_file.page_count):
        page = pdf_file.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        img_byte_arr = pix.tobytes()
        if choose_path.get() == 0:
            image_path = os.path.splitext(file_path)[0] + f"_{page_num + 1}.{extension}"
        else:
            image_path = filedialog.asksaveasfilename(filetypes=[(f"{extension.upper()} files", f"*.{extension.lower()}")]) + f"_{page_num + 1}.{extension}"
        with open(image_path, 'wb') as img_file:
            img_file.write(img_byte_arr)
    pdf_file.close()
    status_label.config(text=f"File converted to {extension.upper()}: {image_path}")


def convert_docx():
    file_path = filedialog.askopenfilename(filetypes=[("DOCX files", "*.docx")])
    if not file_path:
        return
    if choose_path.get() == 0:
        pdf_path = file_path[:-5] + ".pdf"
    else:
        pdf_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")]) + ".pdf"
    # Update the status bar to indicate completion
    convert(file_path, pdf_path)
    status_label.config(text=f"File converted to PDF: {pdf_path}")



def mp4_convert_to_mp3():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if not file_path:
        return
    video = VideoFileClip(file_path)
    if choose_path.get() == 0:
        mp3_path = file_path[:-4] + ".mp3"
    else:
        mp3_path = filedialog.asksaveasfilename(filetypes=[("MP3 files", "*.mp3")]) + ".mp3"
    video.audio.write_audiofile(mp3_path)
    status_label.config(text=f"File converted to MP3: {mp3_path}")


# Defining a function to toggle between light and dark theme
def switch_theme():
    global switch_value
    if switch_value:
        root.config(bg="#262626")
        s.configure('TCheckbutton', background='#262626', foreground='white')
        switch_value = False
    else:
        root.config(bg="white")
        s.configure('TCheckbutton', background='white', foreground='black')
        switch_value = True



# Main window
root = tk.Tk()
root.title("Files Converter")

# Window size
WIN_WIDTH = 1500
WIN_HEIGHT = 600

root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
root.config(bg="white")

# Dark mode
switch_value = True

# Creating a button to toggle between light and dark theme
switch_button = tk.Button(root, text="Switch Theme", command=switch_theme)
switch_button.grid(row=0, column=1)


# Checkbox for choosing path
choose_path = tk.IntVar()
s = ttk.Style()
s.configure('TCheckbutton', background='white', foreground='black')
check_path = ttk.Checkbutton(root,
                text='Choose path to save',
                variable=choose_path,
                onvalue=1,
                offvalue=0,
                style='TCheckbutton')
check_path.grid(row=0, column=0)




# Buttons

# JPG
# Define function to create button
def create_button(row, column, text, command):
    button = Button(root, text=text, width=20, height=3, borderwidth=10, bg="#00FFFF", font="Arial 10 bold", cursor="hand2", command=command)
    button.grid(row=row, column=column, padx=10, pady=10)

# Create buttons

# JPG
extensions_for_jpg_conversions = ["png", "pdf", "webp", "tiff", "bmp"]
for i in range(len(extensions_for_jpg_conversions)):
    create_button(i + 1, 0, f"Convert JPG to {extensions_for_jpg_conversions[i].upper()}", lambda i=i: convert_image([("JPEG files", "*.jpeg")], extensions_for_jpg_conversions[i]))

# PNG
extensions_for_png_conversions = ["jpeg", "pdf", "webp", "tiff", "bmp"]
for i in range(len(extensions_for_png_conversions)):
    create_button(i + 1, 1, f"Convert PNG to {extensions_for_png_conversions[i].upper()}", lambda i=i: convert_image([("PNG files", "*.png")], extensions_for_png_conversions[i]))

# PDF
extensions_for_pdf_conversions = ["jpeg", "png", "webp", "tiff", "bmp"]
for i in range(len(extensions_for_pdf_conversions)):
    create_button(i + 1, 2, f"Convert PDF to {extensions_for_pdf_conversions[i].upper()}", lambda i=i: convert_pdf(extensions_for_pdf_conversions[i]))

# WEBP
extensions_for_webp_conversions = ["jpeg", "png", "pdf", "tiff", "bmp"]
for i in range(len(extensions_for_webp_conversions)):
    create_button(i + 1, 3, f"Convert WEBP to {extensions_for_webp_conversions[i].upper()}", lambda i=i: convert_image([("WEBP files", "*.webp")], extensions_for_webp_conversions[i]))

# TIFF
extensions_for_tiff_conversions = ["jpeg", "png", "pdf", "webp", "bmp"]
for i in range(len(extensions_for_tiff_conversions)):
    create_button(i + 1, 4, f"Convert TIFF to {extensions_for_tiff_conversions[i].upper()}", lambda i=i: convert_image([("TIFF files", "*.tiff")], extensions_for_tiff_conversions[i]))

# BMP
extensions_for_bmp_conversions = ["jpeg", "png", "pdf", "webp", "tiff"]
for i in range(len(extensions_for_bmp_conversions)):
    create_button(i + 1, 5, f"Convert BMP to {extensions_for_bmp_conversions[i].upper()}", lambda i=i: convert_image([("BMP files", "*.bmp")], extensions_for_bmp_conversions[i]))

# DOCX
create_button(1, 6, "Convert DOCX to PDF", convert_docx)

# MP4
create_button(2, 6, "Convert MP4 to MP3", mp4_convert_to_mp3)

# Status label
status_label = tk.Label(root, text="")
status_label.grid(row=7, column=0, columnspan=7, pady=10)

#TODO: PDF TO WORD and WORD TO PDF
#TODO: Add a status bar to show the progress of the conversion
#TODO: Add a button to open the file after conversion
#TODO: Drag image to convert

# Main loop
root.mainloop()