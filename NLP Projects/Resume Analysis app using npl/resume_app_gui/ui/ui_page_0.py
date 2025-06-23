import pyvisual as pv
import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print("PDF reading error:", e)
    return text

def extract_text_from_txt(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print("Text reading error:", e)
        return ""

def create_page_0_ui(window, ui):
    ui_page = {}

    # Title
    ui_page["Text_0"] = pv.PvText(
        container=window,
        x=100, y=100, width=400, height=46,
        text='Resume Classifier',
        font='assets/fonts/JetBrainsMono/JetBrainsMono.ttf',
        font_size=27,
        font_color=(51, 255, 189, 1),
        idle_color=(81, 17, 116, 0),
        is_visible=True
    )

    # Instruction
    ui_page["Text_2"] = pv.PvText(
        container=window,
        x=99, y=209, width=279, height=52,
        text='Upload your resume',
        font='assets/fonts/JetBrainsMono/JetBrainsMono.ttf',
        font_size=20,
        font_color=(51, 255, 189, 1),
        idle_color=(124, 53, 163, 0),
        is_visible=True
    )

    # Uploaded file name
    ui_page["Resume_File_Name"] = pv.PvText(
        container=window,
        x=99, y=270, width=500, height=40,
        text='No file selected',
        font='assets/fonts/JetBrainsMono/JetBrainsMono.ttf',
        font_size=16,
        font_color=(255, 255, 255, 1),
        idle_color=(0, 0, 0, 0),
        is_visible=True
    )

    # Callback function for file upload
    def on_file_select(path):
        print("File selected:", path)
        if path:
            file_name = os.path.basename(path)
            ui_page["Resume_File_Name"].set_text("")  # clear previous text
            ui_page["Resume_File_Name"].set_text(f"Uploaded: {file_name}")

            # Read resume text from file
            if path.lower().endswith('.pdf'):
                resume_text = extract_text_from_pdf(path)
            else:
                resume_text = extract_text_from_txt(path)

            # Save resume text to use later
            ui['resume_text'] = resume_text
            print("Resume loaded:", resume_text[:100])  # Debug: Show first 100 characters

    # Browse button
    ui_page["File_Dialog_1"] = pv.PvFileDialog(
        container=window,
        x=417, y=206, width=200, height=50,
        text='Browse',
        font='assets/fonts/Lexend/Lexend.ttf',
        font_size=15,
        font_color=(255, 255, 255, 1),
        idle_color=(57, 103, 181, 1),
        border_color=(100, 100, 100, 1),
        corner_radius=12,
        dialog_mode="open",
        files_filter="PDF Files (*.pdf);;Text Files (*.txt);;All Files (*.*)",
        is_visible=True,
        on_release=on_file_select
    )

    return ui_page
