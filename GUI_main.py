# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:27:05 2021

@author:pc
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video


# This is a page design
global fn
fn = ""
# +=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1920x1080")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Fake Image & Video Detection System")

# 43

# path
path = 'F:\\Project\\20c9414 100% fake_image_video\\20c9414 100% fake_image_video\\fake_image_video\\'

# +++++++++++++++++++++++++++++++++++
# For background Image
image2 = Image.open(path+'toa-heftiba-i0p916iq-ew-unsplash.jpg')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=70)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Fake Image Video Detection System", font=("Poppins", 35, 'bold'),
                    background="sky blue", fg="dark blue", width=53, height=2)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

# $%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


# $%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# $%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def reg():
    from subprocess import call
    call(["python", "registration.py"])


def log():
    from subprocess import call
    call(["python", "login.py"])


def window():
    root.destroy()


button1 = tk.Button(root, text="LOGIN", command=log, width=14, height=1, font=(
    'Poppins', 20, ' bold '), bg="sky blue", fg="dark blue")
button1.place(x=650, y=250)

button2 = tk.Button(root, text="REGISTER", command=reg, width=14, height=1, font=(
    'Poppins', 20, ' bold '), bg="sky blue", fg="dark blue")
button2.place(x=650, y=400)


root.mainloop()
