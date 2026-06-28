from tkinter import ttk


BG_COLOR = "#F5F7FA"
HEADER = "#1E3A8A"
BUTTON = "#2563EB"
BUTTON_ACTIVE = "#1D4ED8"
FRAME = "#FFFFFF"


def set_style():

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Header.TLabel",
        background=HEADER,
        foreground="white",
        font=("Segoe UI", 20, "bold"),
        padding=15
    )

    style.configure(
        "Section.TLabelframe",
        font=("Segoe UI", 10, "bold")
    )

    style.configure(
        "TButton",
        font=("Segoe UI", 10),
        padding=6
    )