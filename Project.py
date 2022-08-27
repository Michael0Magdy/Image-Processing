# -*- coding: utf-8 -*-
"""
Created on Thu May 27 08:42:28 2021

@author: Michael Magdy Noshy
"""
###############################################################################
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog, Label, LabelFrame, Button, Entry, Tk, StringVar
import os
from skimage.util import random_noise
from scipy import ndimage
###############################################################################
#Original Image
img = ""
#Noisy Image
N = ""
###############################################################################
#First package
def browseimg():
    global img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Browse Image File", filetypes=(("JPG Image","*.jpg"), ("PNG Image","*.png"), ("All Files","*.*")))
    t1.set(filename)
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    m.set(img.shape[0])
    n.set(img.shape[1])
    
def display():
    cv2.imshow("Original Image",img)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
###############################################################################
#Third package   
def noise_sp():
    global N
    N = random_noise(img, mode= 's&p', seed= None, clip= True)
    cv2.imshow("S&P Noise Image",N)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def noise_g():
    global N
    N = random_noise(img, mode= 'gaussian', seed= None, clip= True)
    cv2.imshow("Gaussian Noise Image",N)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def noise_p():
    global N
    N = random_noise(img, mode= 'poisson', seed= None, clip= True)
    cv2.imshow("Poisson Noise Image",N)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def noise_s():
    global N
    N = random_noise(img, mode= 'speckle', seed= None, clip= True)
    cv2.imshow("Speckle Noise Image",N)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
###############################################################################
#Fourth package 
def gauss():
    G_blur = cv2.GaussianBlur(N,(3,3),5)
    cv2.imshow("Gaussian filter",G_blur)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def median():
    median = ndimage.median_filter(N,5)
    cv2.imshow("Median filter",median)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def average():
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(N,-1,kernel)
    cv2.imshow("Average filter",dst)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def blur():
    blur = cv2.blur(N,(9,9))
    cv2.imshow("Blurring filter",blur)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
###############################################################################
#Fifth package
def hist():
    plt.hist(img.ravel(),256,[0,256])
    plt.show()
    
def equalized():
    eq = cv2.equalizeHist(img)
    cv2.imshow("Equalized Image",eq)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def eqhist():
    eq = cv2.equalizeHist(img)
    plt.hist(eq.ravel(),256,[0,256])
    plt.show()
    
def dec():
    decreased = cv2.convertScaleAbs(img, alpha=0.5, beta=0)
    cv2.imshow("Decreased Contrast Image",decreased)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def inc():
    increased = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
    cv2.imshow("Increased Contrast Image",increased)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def inverse():
    inversed = cv2.bitwise_not(img)
    cv2.imshow("Inversed Contrast Image",inversed)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
###############################################################################
#Sixth package    
def zoomin():
    scaleX = 3
    scaleY = 3
    scaleUp = cv2.resize(img, None, fx= scaleX, fy= scaleY, interpolation= cv2.INTER_LINEAR)
    cv2.imshow("Zoomed In Image", scaleUp)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def zoomout():
    scaleX = 0.7
    scaleY = 0.7
    scaleDown = cv2.resize(img, None, fx= scaleX, fy= scaleY, interpolation= cv2.INTER_LINEAR)
    cv2.imshow("Zoomed out Image", scaleDown)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def rotate90():
    rotated90 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Rotated by 90 Degrees", rotated90)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def rotate180():
    rotated180 = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imshow("Rotated by 180 Degrees", rotated180)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def rotate270():
    rotated270 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Rotated by 270 Degrees", rotated270)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
###############################################################################
#Seventh package
def edge():
    edges = cv2.Canny(img,100,200) 
    cv2.imshow("Edge Image", edges)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

def segment():
    ret,obj = cv2.threshold(img,160,255,cv2.THRESH_TOZERO)
    cv2.imshow("Object Image1", obj)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def trun():
    ret,obj = cv2.threshold(img,160,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("Object Image2", obj)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
def trim():
    ret,obj = cv2.threshold(img,160,255,cv2.THRESH_TOZERO)
    x = img - obj
    cv2.imshow("Image Without Object",x)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
###############################################################################    
GUI = Tk()
#Image Path
t1 = StringVar()
#Number of rows
m = StringVar()
#Number of columns
n = StringVar()
###############################################################################
#Label0
lbl0 = Label(GUI, text="Name: Michael Magdy Noshy")    
lbl0.pack(padx=50, pady=2)
#Label00
lbl00 = Label(GUI, text="SuperVisor: Dr. Khaled El-Sayed")    
lbl00.pack(padx=50, pady=2)
#Label000
lbl000 = Label(GUI, text="Eng: Sameh El-Sayed")    
lbl000.pack(padx=50, pady=2)
###############################################################################
#First package
wrapper = LabelFrame(GUI, text="Source File")
wrapper.pack(fill="both", padx=40, pady=1)
#Create labels in first package
lbl1 = Label(wrapper, text="Source File")    
lbl1.pack(side=tk.LEFT, padx=50, pady=20)
#Create TextBox in first package
ent= Entry(wrapper, textvariable=t1)
ent.pack(side=tk.LEFT, padx=40, pady=20)
#Create buttons in first package
#Button1
btn1 = Button(wrapper, text="Browse Image", command=browseimg)
btn1.pack(side=tk.LEFT, padx=60, pady=20)
#Button2
btn2 = Button(wrapper, text="Display Image", command=display)
btn2.pack(side=tk.LEFT, padx=60, pady=20)
###############################################################################
#Second package
wrapper2 = LabelFrame(GUI, text="Image Details")
wrapper2.pack(fill="both", padx=40, pady=1)
#Label2
lbl2 = Label(wrapper2, text="Dimension")
lbl2.pack(side=tk.LEFT, padx=50, pady=20)
#TextBox2
ent2= Entry(wrapper2, textvariable=m)
ent2.pack(side=tk.LEFT, padx=40, pady=20)
#Label3
lbl3 = Label(wrapper2, text="X")
lbl3.pack(side=tk.LEFT, padx=50, pady=20)
#TextBox3
ent3= Entry(wrapper2, textvariable=n)
ent3.pack(side=tk.LEFT, padx=40, pady=20)
###############################################################################
#Third package
wrapper3 = LabelFrame(GUI, text="Adding Noise")
wrapper3.pack(fill="both", padx=40, pady=1)
#Button3
btn3 = Button(wrapper3, text="S&P Noise", command=noise_sp)
btn3.pack(side=tk.LEFT, padx=55, pady=20)
#Button4
btn4 = Button(wrapper3, text="Gaussian Noise", command=noise_g)
btn4.pack(side=tk.LEFT, padx=55, pady=20)
#Button5
btn5 = Button(wrapper3, text="Poisson Noise", command=noise_p)
btn5.pack(side=tk.LEFT, padx=55, pady=20)
#Button6
btn6 = Button(wrapper3, text="Speckle Noise", command=noise_s)
btn6.pack(side=tk.LEFT, padx=55, pady=20)
###############################################################################
#Fourth Package
wrapper4 = LabelFrame(GUI, text="Smoothing Filters")
wrapper4.pack(fill="both", padx=40, pady=1)
#Create buttons in second package
#Button7
btn7 = Button(wrapper4, text="Gaussian Filter", command=gauss)
btn7.pack(side=tk.LEFT, padx=55, pady=20)
#Button8
btn8 = Button(wrapper4, text="Median Filter", command=median)
btn8.pack(side=tk.LEFT, padx=55, pady=20)
#Button9
btn9 = Button(wrapper4, text="Average Filter", command=average)
btn9.pack(side=tk.LEFT, padx=55, pady=20)
#Button10
btn10 = Button(wrapper4, text="Blurring Filter", command=blur)
btn10.pack(side=tk.LEFT, padx=55, pady=20)
###############################################################################
#Fifth package
wrapper5 = LabelFrame(GUI, text="Histogram and Contrast")
wrapper5.pack(fill="both", padx=40, pady=1)
#Button11
btn11 = Button(wrapper5, text="Histogram", command=hist)
btn11.pack(side=tk.LEFT, padx=20, pady=20)
#Button12
btn12 = Button(wrapper5, text="Equalized Image", command=equalized)
btn12.pack(side=tk.LEFT, padx=20, pady=20)
#Button13
btn13 = Button(wrapper5, text="Equalized Histogram", command=eqhist)
btn13.pack(side=tk.LEFT, padx=20, pady=20)
#Button22
btn22 = Button(wrapper5, text="Decrease Contrast", command=dec)
btn22.pack(side=tk.LEFT, padx=20, pady=20)
#Button23
btn23 = Button(wrapper5, text="Increase Contrast", command=inc)
btn23.pack(side=tk.LEFT, padx=20, pady=20)
#Button14
btn14 = Button(wrapper5, text="Inverse Image", command=inverse)
btn14.pack(side=tk.LEFT, padx=20, pady=20)
###############################################################################
#Sixth package
wrapper6 = LabelFrame(GUI, text="Zooming and Rotate")
wrapper6.pack(fill="both", padx=40, pady=1)
#Button15
btn15 = Button(wrapper6, text="Zoom In", command=zoomin)
btn15.pack(side=tk.LEFT, padx=50, pady=20)
#Button16
btn16 = Button(wrapper6, text="Zoom Out", command=zoomout)
btn16.pack(side=tk.LEFT, padx=50, pady=20)
#Button17
btn17 = Button(wrapper6, text="Angle 90", command=rotate90)
btn17.pack(side=tk.LEFT, padx=50, pady=20)
#Button18
btn18 = Button(wrapper6, text="Angle 180", command=rotate180)
btn18.pack(side=tk.LEFT, padx=50, pady=20)
#Button19
btn19 = Button(wrapper6, text="Angle 270", command=rotate270)
btn19.pack(side=tk.LEFT, padx=50, pady=20)
###############################################################################
#Seventh package
wrapper7 = LabelFrame(GUI, text="Object Detection")
wrapper7.pack(fill="both", padx=40, pady=1)
#Button20
btn20 = Button(wrapper7, text="Edge Detection", command=edge)
btn20.pack(side=tk.LEFT, padx=50, pady=20)
#Button21
btn21 = Button(wrapper7, text="Object Detection1", command=segment)
btn21.pack(side=tk.LEFT, padx=50, pady=20)
#Button25
btn25 = Button(wrapper7, text="Object Detection1", command=trun)
btn25.pack(side=tk.LEFT, padx=50, pady=20)
#Button24
btn24 = Button(wrapper7, text="Image Without Object", command=trim)
btn24.pack(side=tk.LEFT, padx=40, pady=20)
###############################################################################
#Title to the window
GUI.title("Image Processing Project")
#Resize the window
GUI.geometry("900x800")
#Display the GUI 
GUI.mainloop()