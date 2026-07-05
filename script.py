import os
import sys
from tkinter import *
from tkinter import filedialog

def get_asset_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
root.geometry("800x600")
root.minsize(475, 300)
root.title("BareTXT")

try:
    png_path = get_asset_path('BareTXTicon.png')
    img = PhotoImage(file=png_path)
    root.iconphoto(False,img)
    root.image = img
except Exception:
    pass

root.configure(background="#212121")

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.columnconfigure(0, weight=1)

def save_file(event=None):
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[
                                                ("Text Files", "*.txt"),
                                                ("Markdown Documents", "*.md"),
                                                ("Python Scripts", "*.py"),
                                                ("HTML Documents", "*.html"),
                                                ("CSS Stylesheets", "*.css"),
                                                ("JavaScript Files", "*.js"),
                                                ("JSON Data", "*.json"),
                                                ("YAML Configurations", "*.yaml *.yml"),
                                                ("All Files", "*.*")
                                            ])
    if filename:
        filetext = str(text_area.get("1.0", "end-1c"))
        with open(filename, "w", encoding="utf-8", errors="surrogateescape") as file:
            file.write(filetext)


def open_file(event=None):
    filename2 = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[
                                               ("Text Files", "*.txt"),
                                               ("Markdown Documents", "*.md"),
                                               ("Python Scripts", "*.py"),
                                               ("HTML Documents", "*.html"),
                                               ("CSS Stylesheets", "*.css"),
                                               ("JavaScript Files", "*.js"),
                                               ("JSON Data", "*.json"),
                                               ("YAML Configurations", "*.yaml *.yml"),
                                               ("All Files", "*.*")
                                           ])
    if filename2:
        with open(filename2, "r", encoding="utf-8", errors="surrogateescape") as file:
            content = file.read()
        text_area.delete(1.0, END)
        text_area.insert(1.0, content)


def exit_app(event=None):
    root.destroy()



def create_undo_checkpoint(event):
    text_area.edit_separator()


def on_hover(event):
    event.widget.config(bg="#2f2f2f")


def on_leave(event):
    event.widget.config(bg="#2b2b2b")


def open_about(event=None):
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("500x500")
    about_window.minsize(500, 500)
    about_window.maxsize(500, 500)
    about_window.config(bg="#212121")
    about_window.resizable(False, False)
    about_window.transient(root)
    about_window.grab_set()

    try:
        png_path = get_asset_path('BareTXTicon.png')
        img = PhotoImage(file=png_path)
        about_window.iconphoto(False, img)
        about_window.image = img
    except Exception:
        pass

    about_window.focus()

    frame = Frame(about_window, bg="#1a1a1a", bd=2, relief="flat")
    frame.pack(padx=25, pady=25, fill="both", expand=True)

    def exit_about(event=None):
        about_window.destroy()

    about_header_text = Label(
        frame,
        text="About BareTXT",
        bg="#1a1a1a",
        fg="white",
        font=("Arial", 25, "underline"),
        relief="flat",
        pady=20
    )
    about_header_text.pack(pady=10)

    about_body = Label(
        frame,
        text="A minimalist text editor built for speed and focus.\n\nVersion 1.0",
        bg="#1a1a1a",
        fg="#dbdbdb",
        font=("Arial", 12),
        justify="center"
    )
    about_body.pack(pady=20)

    about_combo_header = Label(
        frame,
        text="Shortcuts:",
        bg="#1a1a1a",
        fg="#dbdbdb",
        font=("Arial", 20),
        justify="center"
    )

    about_combo_header.pack(pady=0)

    about_combo = Label(
        frame,
        text="CTRL+S: Save file \nCTRL+O: Open file \nCTRL+H: Open About window \nCTRL+Z: Undo last word\nCTRL+Q: Quit BareTXT",
        bg="#1a1a1a",
        fg="#dbdbdb",
        font=("Arial", 12),
        justify="left"
    )
    about_combo.pack(pady=0)

    credits = Label(
        frame,
        text="Made by: McNut",
        bg="#1a1a1a",
        fg="#dbdbdb",
        font=("Arial", 12),
        justify="left"
    )

    credits.pack(pady=25)

    root.bind_all("<Escape>", exit_about)

text_area = Text(
    root,
    undo=True,
    autoseparators=False,
    bg="#1a1a1a",
    fg="#dbdbdb",
    font=("Arial", 12),
    insertbackground="white",
    relief="flat",
    padx=5,
    pady=5
)
text_area.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
text_area.focus_set()

button_frame = Frame(root, bg="#212121")
button_frame.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="nsew")
button_frame.columnconfigure(1, weight=1)



about_button = Button(
    button_frame,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    text="About",
    cursor="hand2",
    command=open_about
)
about_button.grid(row=0, column=0, ipadx=25, ipady=5, sticky="w")

open_button = Button(
    button_frame,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    text="Open",
    cursor="hand2",
    command=open_file
)
open_button.grid(row=0, column=2, ipadx=25, ipady=5, padx=(0, 10), sticky="e")

save_button = Button(
    button_frame,
    bg="#2b2b2b",
    fg="white",
    font=("Arial", 12),
    relief="flat",
    text="Save",
    cursor="hand2",
    command=save_file
)
save_button.grid(row=0, column=3, ipadx=25, ipady=5, sticky="e")

for btn in (about_button, open_button, save_button):
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)

root.bind_all("<Control-s>", save_file)
root.bind_all("<Control-S>", save_file)
root.bind_all("<Control-o>", open_file)
root.bind_all("<Control-O>", open_file)
root.bind_all("<Control-q>", exit_app)
root.bind_all("<Control-Q>", exit_app)
root.bind_all("<Control-H>", open_about)
root.bind_all("<Control-h>", open_about)

root.bind("<space>", create_undo_checkpoint)
root.bind("<Return>", create_undo_checkpoint)

root.mainloop()