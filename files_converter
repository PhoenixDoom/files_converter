import tkinter as tk
from tkinter import ttk, Button, filedialog, Radiobutton, W
from PIL import Image
import fitz
from moviepy.editor import VideoFileClip

# Functions
def jpg_convert_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        png_path = file_path[:-4] + ".png"
    else:
        png_path = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png")]) + ".png"
    img.save(png_path, "png", quality=100)
    status_label.config(text=f"File converted to PNG: {png_path}")


def jpg_convert_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        pdf_path = file_path[:-4] + ".pdf"
    else:
        pdf_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")]) + ".pdf"
    img.save(pdf_path, "pdf")
    status_label.config(text=f"File converted to PDF: {pdf_path}")


def jpg_convert_to_webp():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        webp_path = file_path[:-4] + ".webp"
    else:
        webp_path = filedialog.asksaveasfilename(filetypes=[("WEBP files", "*.webp")]) + ".webp"
    img.save(webp_path, "webp")
    status_label.config(text=f"File converted to WEBP: {webp_path}")


def jpg_convert_to_tiff():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        tiff_path = file_path[:-4] + ".tiff"
    else:
        tiff_path = filedialog.asksaveasfilename(filetypes=[("TIFF files", "*.tiff")]) + ".tiff"
    img.save(tiff_path, "tiff")
    status_label.config(text=f"File converted to TIFF: {tiff_path}")


def jpg_convert_to_bmp():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        bmp_path = file_path[:-4] + ".bmp"
    else:
        bmp_path = filedialog.asksaveasfilename(filetypes=[("BMP files", "*.bmp")]) + ".bmp"
    img.save(bmp_path, "bmp")
    status_label.config(text=f"File converted to BMP: {bmp_path}")


def png_convert_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return   
    img = Image.open(file_path)
    if choose_path.get() == 0:
        jpg_path = file_path[:-4] + ".jpg"
    else:
        jpg_path = filedialog.asksaveasfilename(filetypes=[("JPEG files", "*.jpg")]) + ".jpg"
    img.save(jpg_path, "jpeg", quality=100)
    status_label.config(text=f"File converted to JPG: {jpg_path}")


def png_convert_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        pdf_path = file_path[:-4] + ".pdf"
    else:
        pdf_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")]) + ".pdf"
    img.save(pdf_path, "pdf")
    status_label.config(text=f"File converted to PDF: {pdf_path}")


def png_convert_to_webp():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        webp_path = file_path[:-4] + ".webp"
    else:
        webp_path = filedialog.asksaveasfilename(filetypes=[("WEBP files", "*.webp")]) + ".webp"
    img.save(webp_path, "webp")
    status_label.config(text=f"File converted to WEBP: {webp_path}")


def png_convert_to_tiff():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        tiff_path = file_path[:-4] + ".tiff"
    else:
        tiff_path = filedialog.asksaveasfilename(filetypes=[("TIFF files", "*.tiff")]) + ".tiff"
    img.save(tiff_path, "tiff")
    status_label.config(text=f"File converted to TIFF: {tiff_path}")


def png_convert_to_bmp():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        bmp_path = file_path[:-4] + ".bmp"
    else:
        bmp_path = filedialog.asksaveasfilename(filetypes=[("BMP files", "*.bmp")]) + ".bmp"
    img.save(bmp_path, "bmp")
    status_label.config(text=f"File converted to BMP: {bmp_path}")


def pdf_convert_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    pdf_file = fitz.open(file_path)
    for page_num in range(pdf_file.page_count):
        page = pdf_file.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        img_byte_arr = pix.tobytes()
        if choose_path.get() == 0:
            jpg_path = file_path[:-4] + f"_{page_num + 1}.jpg"
        else:
            jpg_path = filedialog.asksaveasfilename(filetypes=[("JPEG files", "*.jpg")]) + f"_{page_num + 1}.jpg"
        with open(jpg_path, 'wb') as img_file:
            img_file.write(img_byte_arr)
    pdf_file.close()
    status_label.config(text=f"File converted to JPG: {jpg_path}")

def pdf_convert_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    pdf_file = fitz.open(file_path)
    for page_num in range(pdf_file.page_count):
        page = pdf_file.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        img_byte_arr = pix.tobytes()
        if choose_path.get() == 0:
            png_path = file_path[:-4] + f"_{page_num + 1}.png"
        else:
            png_path = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png")]) + f"_{page_num + 1}.png"
        with open(png_path, 'wb') as img_file:
            img_file.write(img_byte_arr)
    pdf_file.close()
    status_label.config(text=f"File converted to PNG: {png_path}")


def pdf_convert_to_webp():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    pdf_file = fitz.open(file_path)
    for page_num in range(pdf_file.page_count):
        page = pdf_file.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        img_byte_arr = pix.tobytes()
        if choose_path.get() == 0:
            webp_path = file_path[:-4] + f"_{page_num + 1}.webp"
        else:
            webp_path = filedialog.asksaveasfilename(filetypes=[("WEBP files", "*.webp")]) + f"_{page_num + 1}.webp"
        with open(webp_path, 'wb') as img_file:
            img_file.write(img_byte_arr)
    pdf_file.close()
    status_label.config(text=f"File converted to WEBP: {webp_path}")


def pdf_convert_to_tiff():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    pdf_file = fitz.open(file_path)
    for page_num in range(pdf_file.page_count):
        page = pdf_file.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        img_byte_arr = pix.tobytes()
        if choose_path.get() == 0:
            tiff_path = file_path[:-4] + f"_{page_num + 1}.tiff"
        else:
            tiff_path = filedialog.asksaveasfilename(filetypes=[("TIFF files", "*.tiff")]) + f"_{page_num + 1}.tiff"
        with open(tiff_path, 'wb') as img_file:
            img_file.write(img_byte_arr)
    pdf_file.close()
    status_label.config(text=f"File converted to TIFF: {tiff_path}")


def pdf_convert_to_bmp():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    pdf_file = fitz.open(file_path)
    for page_num in range(pdf_file.page_count):
        page = pdf_file.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(600/72, 600/72))
        img_byte_arr = pix.tobytes()
        if choose_path.get() == 0:
            bmp_path = file_path[:-4] + f"_{page_num + 1}.bmp"
        else:
            bmp_path = filedialog.asksaveasfilename(filetypes=[("BMP files", "*.bmp")]) + f"_{page_num + 1}.bmp"
        with open(bmp_path, 'wb') as img_file:
            img_file.write(img_byte_arr)
    pdf_file.close()
    status_label.config(text=f"File converted to BMP: {bmp_path}")


def webp_convert_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        jpg_path = file_path[:-5] + ".jpg"
    else:
        jpg_path = filedialog.asksaveasfilename(filetypes=[("JPEG files", "*.jpg")]) + ".jpg"
    img.save(jpg_path, "jpeg")
    status_label.config(text=f"File converted to JPG: {jpg_path}")


def webp_convert_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        png_path = file_path[:-5] + ".png"
    else:
        png_path = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png")]) + ".png"
    img.save(png_path, "png")
    status_label.config(text=f"File converted to PNG: {png_path}")


def webp_convert_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        pdf_path = file_path[:-5] + ".pdf"
    else:
        pdf_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")]) + ".pdf"
    img.save(pdf_path, "pdf")
    status_label.config(text=f"File converted to PDF: {pdf_path}")


def webp_convert_to_tiff():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        tiff_path = file_path[:-5] + ".tiff"
    else:
        tiff_path = filedialog.asksaveasfilename(filetypes=[("TIFF files", "*.tiff")]) + ".tiff"
    img.save(tiff_path, "tiff")
    status_label.config(text=f"File converted to TIFF: {tiff_path}")


def webp_convert_to_bmp():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        bmp_path = file_path[:-5] + ".bmp"
    else:
        bmp_path = filedialog.asksaveasfilename(filetypes=[("BMP files", "*.bmp")]) + ".bmp"
    img.save(bmp_path, "bmp")
    status_label.config(text=f"File converted to BMP: {bmp_path}")


def tiff_convert_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tiff")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        jpg_path = file_path[:-5] + ".jpg"
    else:
        jpg_path = filedialog.asksaveasfilename(filetypes=[("JPEG files", "*.jpg")]) + ".jpg"
    img.save(jpg_path, "jpeg")
    status_label.config(text=f"File converted to JPG: {jpg_path}")


def tiff_convert_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tiff")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        png_path = file_path[:-5] + ".png"
    else:
        png_path = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png")]) + ".png"
    img.save(png_path, "png")
    status_label.config(text=f"File converted to PNG: {png_path}")


def tiff_convert_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tiff")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        pdf_path = file_path[:-5] + ".pdf"
    else:
        pdf_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")]) + ".pdf"
    img.save(pdf_path, "pdf")
    status_label.config(text=f"File converted to PDF: {pdf_path}")


def tiff_convert_to_webp():
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tiff")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        webp_path = file_path[:-5] + ".webp"
    else:
        webp_path = filedialog.asksaveasfilename(filetypes=[("WEBP files", "*.webp")]) + ".webp"
    img.save(webp_path, "webp")
    status_label.config(text=f"File converted to WEBP: {webp_path}")


def tiff_convert_to_bmp():
    file_path = filedialog.askopenfilename(filetypes=[("TIFF files", "*.tiff")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        bmp_path = file_path[:-5] + ".bmp"
    else:
        bmp_path = filedialog.asksaveasfilename(filetypes=[("BMP files", "*.bmp")]) + ".bmp"
    img.save(bmp_path, "bmp")
    status_label.config(text=f"File converted to BMP: {bmp_path}")


def bmp_convert_to_jpg():
    file_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        jpg_path = file_path[:-4] + ".jpg"
    else:
        jpg_path = filedialog.asksaveasfilename(filetypes=[("JPEG files", "*.jpg")]) + ".jpg"
    img.save(jpg_path, "jpeg")
    status_label.config(text=f"File converted to JPG: {jpg_path}")


def bmp_convert_to_png():
    file_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        png_path = file_path[:-4] + ".png"
    else:
        png_path = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png")]) + ".png"
    img.save(png_path, "png")
    status_label.config(text=f"File converted to PNG: {png_path}")


def bmp_convert_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        pdf_path = file_path[:-4] + ".pdf"
    else:
        pdf_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")]) + ".pdf"
    img.save(pdf_path, "pdf")
    status_label.config(text=f"File converted to PDF: {pdf_path}")


def bmp_convert_to_webp():
    file_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        webp_path = file_path[:-4] + ".webp"
    else:
        webp_path = filedialog.asksaveasfilename(filetypes=[("WEBP files", "*.webp")]) + ".webp"
    img.save(webp_path, "webp")
    status_label.config(text=f"File converted to WEBP: {webp_path}")


def bmp_convert_to_tiff():
    file_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not file_path:
        return
    img = Image.open(file_path)
    if choose_path.get() == 0:
        tiff_path = file_path[:-4] + ".tiff"
    else:
        tiff_path = filedialog.asksaveasfilename(filetypes=[("TIFF files", "*.tiff")]) + ".tiff"
    img.save(tiff_path, "tiff")
    status_label.config(text=f"File converted to TIFF: {tiff_path}")


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
WIN_HEIGHT = 500

root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
root.config(bg="white")

# Dark mode
switch_value = True

# Creating a button to toggle between light and dark theme
switch_button = tk.Button(root, text="Switch Theme", command=switch_theme)
switch_button.grid(row=0, column=1)


# Padding
PADX = 10
PADY = 10


BUTTON_WIDTH = 20
BUTTON_HEIGHT = 3
BUTTON_COLOR = "#00FFFF"
BUTTON_BORDERWIDTH = 10
BUTTON_FONT = "Arial 10 bold"
BUTTON_CURSOR = "hand2"

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
check_path.config(command=switch_theme)


# Buttons

# JPG
jpg_to_png_button = Button(root, text="Convert JPG to PNG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,                       
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=jpg_convert_to_png)
jpg_to_png_button.grid(row=1, column=0, padx=PADX, pady=PADY)

jpg_to_pdf_button = Button(root, text="Convert JPG to PDF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=jpg_convert_to_pdf)
jpg_to_pdf_button.grid(row=2, column=0, padx=PADX, pady=PADY)

jpg_to_webp_button = Button(root, text="Convert JPG to WEBP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=jpg_convert_to_webp)
jpg_to_webp_button.grid(row=3, column=0, padx=PADX, pady=PADY)

jpg_to_tiff_button = Button(root, text="Convert JPG to TIFF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=jpg_convert_to_tiff)
jpg_to_tiff_button.grid(row=4, column=0, padx=PADX, pady=PADY)

jpg_to_bmp_button = Button(root, text="Convert JPG to BMP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=jpg_convert_to_bmp)
jpg_to_bmp_button.grid(row=5, column=0, padx=PADX, pady=PADY)
                           
# PNG
png_to_jpg_button = Button(root, text="Convert PNG to JPG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=png_convert_to_jpg)
png_to_jpg_button.grid(row=1, column=1, padx=PADX, pady=PADY)

png_to_pdf_button = Button(root, text="Convert PNG to PDF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=png_convert_to_pdf)
png_to_pdf_button.grid(row=2, column=1, padx=PADX, pady=PADY)

png_to_webp_button = Button(root, text="Convert PNG to WEBP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=png_convert_to_webp)
png_to_webp_button.grid(row=3, column=1, padx=PADX, pady=PADY)

png_to_tiff_button = Button(root, text="Convert PNG to TIFF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=png_convert_to_tiff)
png_to_tiff_button.grid(row=4, column=1, padx=PADX, pady=PADY)

png_to_bmp_button = Button(root, text="Convert PNG to BMP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=png_convert_to_bmp)
png_to_bmp_button.grid(row=5, column=1, padx=PADX, pady=PADY)

# PDF
pdf_to_jpg_button = Button(root, text="Convert PDF to JPG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=pdf_convert_to_jpg)
pdf_to_jpg_button.grid(row=1, column=2, padx=PADX, pady=PADY)

pdf_to_png_button = Button(root, text="Convert PDF to PNG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=pdf_convert_to_png)
pdf_to_png_button.grid(row=2, column=2, padx=PADX, pady=PADY)

pdf_to_webp_button = Button(root, text="Convert PDF to WEBP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=pdf_convert_to_webp)
pdf_to_webp_button.grid(row=3, column=2, padx=PADX, pady=PADY)

pdf_to_tiff_button = Button(root, text="Convert PDF to TIFF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=pdf_convert_to_tiff)
pdf_to_tiff_button.grid(row=4, column=2, padx=PADX, pady=PADY)

pdf_to_bmp_button = Button(root, text="Convert PDF to BMP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=pdf_convert_to_bmp)
pdf_to_bmp_button.grid(row=5, column=2, padx=PADX, pady=PADY)

# WEBP
webp_to_jpg_button = Button(root, text="Convert WEBP to JPG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=webp_convert_to_jpg)
webp_to_jpg_button.grid(row=1, column=3, padx=PADX, pady=PADY)

webp_to_png_button = Button(root, text="Convert WEBP to PNG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=webp_convert_to_png)
webp_to_png_button.grid(row=2, column=3, padx=PADX, pady=PADY)

webp_to_pdf_button = Button(root, text="Convert WEBP to PDF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=webp_convert_to_pdf)
webp_to_pdf_button.grid(row=3, column=3, padx=PADX, pady=PADY)

webp_to_tiff_button = Button(root, text="Convert WEBP to TIFF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=webp_convert_to_tiff)
webp_to_tiff_button.grid(row=4, column=3, padx=PADX, pady=PADY)

webp_to_bmp_button = Button(root, text="Convert WEBP to BMP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=webp_convert_to_bmp)
webp_to_bmp_button.grid(row=5, column=3, padx=PADX, pady=PADY)

# TIFF
tiff_to_jpg_button = Button(root, text="Convert TIFF to JPG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=tiff_convert_to_jpg)
tiff_to_jpg_button.grid(row=1, column=4, padx=PADX, pady=PADY)

tiff_to_png_button = Button(root, text="Convert TIFF to PNG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=tiff_convert_to_png)
tiff_to_png_button.grid(row=2, column=4, padx=PADX, pady=PADY)

tiff_to_pdf_button = Button(root, text="Convert TIFF to PDF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=tiff_convert_to_pdf)
tiff_to_pdf_button.grid(row=3, column=4, padx=PADX, pady=PADY)

tiff_to_webp_button = Button(root, text="Convert TIFF to WEBP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                                borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=tiff_convert_to_webp)
tiff_to_webp_button.grid(row=4, column=4, padx=PADX, pady=PADY)

tiff_to_bmp_button = Button(root, text="Convert TIFF to BMP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=tiff_convert_to_bmp)
tiff_to_bmp_button.grid(row=5, column=4, padx=PADX, pady=PADY)

# BMP
bmp_to_jpg_button = Button(root, text="Convert BMP to JPG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=bmp_convert_to_jpg)
bmp_to_jpg_button.grid(row=1, column=5, padx=PADX, pady=PADY)

bmp_to_png_button = Button(root, text="Convert BMP to PNG", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=bmp_convert_to_png)
bmp_to_png_button.grid(row=2, column=5, padx=PADX, pady=PADY)

bmp_to_pdf_button = Button(root, text="Convert BMP to PDF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=bmp_convert_to_pdf)
bmp_to_pdf_button.grid(row=3, column=5, padx=PADX, pady=PADY)

bmp_to_webp_button = Button(root, text="Convert BMP to WEBP", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=bmp_convert_to_webp)
bmp_to_webp_button.grid(row=4, column=5, padx=PADX, pady=PADY)

bmp_to_tiff_button = Button(root, text="Convert BMP to TIFF", width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
                            borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=bmp_convert_to_tiff)
bmp_to_tiff_button.grid(row=5, column=5, padx=PADX, pady=PADY)

# MP4
mp4_to_mp3_button = Button(root, text="Convert MP4 to MP3", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, 
                           borderwidth=BUTTON_BORDERWIDTH, bg=BUTTON_COLOR, font=BUTTON_FONT, cursor=BUTTON_CURSOR, command=mp4_convert_to_mp3)
mp4_to_mp3_button.grid(row=1, column=6, padx=PADX, pady=PADY)

# Status label
status_label = tk.Label(root, text="")

#TODO: PDF TO WORD and WORD TO PDF
#TODO: Add a status bar to show the progress of the conversion


# Main loop
root.mainloop()
