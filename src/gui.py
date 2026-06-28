import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import cv2
import numpy as np

from PIL import Image, ImageTk

from preprocessing import *
from enhancement import *
from filtering import *
from edge_detection import *
from segmentation import *
from face_detection import *

from style import *


class ImageProcessingApp(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Digital Image Processing")
        self.geometry("1280x820")
        self.configure(bg=BG_COLOR)
        self.resizable(True, True)

        set_style()

        self.image_path = None
        self.original_cv = None
        self.result_cv = None
        self.face_count = 0

        self.create_widgets()

    def create_widgets(self):

        header = ttk.Label(
            self,
            text="DIGITAL IMAGE PROCESSING APPLICATION\nCelebrity Face Dataset using Python & OpenCV",
            style="Header.TLabel",
            anchor="center"
        )

        header.pack(fill="x")

        top = tk.Frame(self, bg=BG_COLOR)
        top.pack(pady=10)

        ttk.Button(
            top,
            text="Upload Image",
            command=self.load_image
        ).grid(row=0,column=0,padx=5)

        self.save_btn = ttk.Button(
            top,
            text="Save Result",
            command=self.save_result,
            state="disabled"
        )

        self.save_btn.grid(row=0,column=1,padx=5)

        image_frame = tk.Frame(self,bg=BG_COLOR)
        image_frame.pack()

        left = ttk.LabelFrame(
            image_frame,
            text="Original Image"
        )

        left.grid(row=0,column=0,padx=10)

        right = ttk.LabelFrame(
            image_frame,
            text="Processed Image"
        )

        right.grid(row=0,column=1,padx=10)

        self.canvas_original = tk.Canvas(
            left,
            width=350,
            height=350,
            bg="white"
        )

        self.canvas_original.pack()

        self.canvas_result = tk.Canvas(
            right,
            width=350,
            height=350,
            bg="white"
        )

        self.canvas_result.pack()

        info = ttk.LabelFrame(
            self,
            text="Processing Information"
        )

        info.pack(fill="x",padx=20,pady=10)

        self.info_label = tk.Label(
            info,
            justify="left",
            anchor="w",
            bg="white",
            height=4,
            font=("Segoe UI",9)
        )

        self.info_label.pack(fill="x")

        process = ttk.LabelFrame(
            self,
            text="Image Processing"
        )

        process.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.buttons = {}

        button_data = [

            ("Grayscale","grayscale"),
            ("Binary","binary"),

            ("Histogram","histogram"),
            ("Contrast","contrast"),
            ("Brightness","brightness"),

            ("Mean","mean"),
            ("Median","median"),
            ("Gaussian","gaussian"),

            ("Sobel","sobel"),
            ("Canny","canny"),

            ("Threshold","threshold"),
            ("K-Means","kmeans"),

            ("Face Detection","face")
        ]

        row = 0
        col = 0

        for text, method in button_data:

            btn = ttk.Button(

                process,

                text=text,

                width=14,

                command=lambda m=method:self.process_image(m),

                state="disabled"

            )

            btn.grid(
                row=row,
                column=col,
                padx=3,
                pady=3
            )

            self.buttons[method]=btn

            col +=1

            if col==5:

                col=0
                row+=1

        self.status=tk.Label(

            self,

            text="Status : Ready",

            bg=HEADER,

            fg="white",

            anchor="w"

        )

        self.status.pack(fill="x",side="bottom")
    
    # ==========================================================
    # LOAD IMAGE
    # ==========================================================

    def load_image(self):

        path = filedialog.askopenfilename(
            filetypes=[
                ("Image Files","*.jpg *.jpeg *.png")
            ]
        )

        if not path:
            return

        self.image_path = path

        image = cv2.imread(path)

        image = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        self.original_cv = image
        self.result_cv = image.copy()

        self.display_image(
            self.original_cv,
            self.canvas_original
        )

        self.display_image(
            self.result_cv,
            self.canvas_result
        )

        for btn in self.buttons.values():
            btn.config(state="normal")

        self.save_btn.config(state="normal")

        h, w = image.shape[:2]

        self.update_info(
            "Original Image",
            w,
            h,
            3,
            "-",
            "Ready"
        )

        self.status.config(
            text="Status : Image Loaded"
        )

    # ==========================================================
    # DISPLAY IMAGE
    # ==========================================================

    def display_image(self, image, canvas):

        if len(image.shape) == 2:
            img = Image.fromarray(image)
        else:
            img = Image.fromarray(image.astype(np.uint8))

        img.thumbnail((330,330))

        photo = ImageTk.PhotoImage(img)

        canvas.delete("all")

        canvas.create_image(
            175,
            175,
            image=photo
        )

        canvas.image = photo

    # ==========================================================
    # UPDATE INFORMATION
    # ==========================================================

    def update_info(
            self,
            method,
            width,
            height,
            channel,
            face,
            status
    ):

        self.info_label.config(

            text=
            f"""Method      : {method}

            Resolution : {width} x {height}

            Channels   : {channel}

            Faces      : {face}

            Status     : {status}
            """
                    )

    # ==========================================================
    # SAVE RESULT
    # ==========================================================

    def save_result(self):

        if self.result_cv is None:

            messagebox.showwarning(
                "Warning",
                "No image."
            )

            return

        filename = filedialog.asksaveasfilename(

            defaultextension=".png",

            filetypes=[
                ("PNG","*.png"),
                ("JPEG","*.jpg")
            ]
        )

        if not filename:
            return

        image = self.result_cv

        if len(image.shape)==3:

            image=cv2.cvtColor(
                image,
                cv2.COLOR_RGB2BGR
            )

        cv2.imwrite(
            filename,
            image
        )

        messagebox.showinfo(
            "Success",
            "Image Saved Successfully."
        )
    
    # ==========================================================
    # PROCESS IMAGE
    # ==========================================================

    def process_image(self, method):

        if self.original_cv is None:
            return

        image = self.original_cv.copy()

        face = "-"

        operations = {

            "grayscale": lambda: rgb_to_grayscale(image),

            "binary": lambda: rgb_to_binary(image),

            "histogram": lambda: histogram_equalization(image),

            "contrast": lambda: contrast_stretching(image),

            "brightness": lambda: brightness_adjustment(image),

            "mean": lambda: mean_filter(image),

            "median": lambda: median_filter(image),

            "gaussian": lambda: gaussian_filter(image),

            "sobel": lambda: sobel_edge(image),

            "canny": lambda: canny_edge(image),

            "threshold": lambda: threshold_segmentation(image),

            "kmeans": lambda: kmeans_segmentation(image),

            "face": lambda: detect_face(image)

        }

        result = operations[method]()

        if method == "face":

            image_result, face_count = result

            self.result_cv = image_result

            face = str(face_count)

        else:

            self.result_cv = result

        self.display_image(
            self.result_cv,
            self.canvas_result
        )

        h, w = self.result_cv.shape[:2]

        if len(self.result_cv.shape) == 2:
            channel = 1
        else:
            channel = self.result_cv.shape[2]

        method_name = {

            "grayscale": "Grayscale",

            "binary": "Binary",

            "histogram": "Histogram Equalization",

            "contrast": "Contrast Stretching",

            "brightness": "Brightness Adjustment",

            "mean": "Mean Filter",

            "median": "Median Filter",

            "gaussian": "Gaussian Filter",

            "sobel": "Sobel Edge Detection",

            "canny": "Canny Edge Detection",

            "threshold": "Otsu Threshold",

            "kmeans": "K-Means Segmentation",

            "face": "Face Detection"

        }

        self.update_info(

            method_name[method],

            w,

            h,

            channel,

            face,

            "Success"

        )

        self.status.config(
            text=f"Status : {method_name[method]} Success"
        )