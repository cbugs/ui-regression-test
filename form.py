# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:27:24 2018

@author: framarok
"""


from tkinter import *
from tkinter import ttk
from websites_links.WebsiteLinks import WebsiteLinks
from capture_screenshot.CaptureScreenshot import CaptureScreenshot
from image_comparisons.CompareImage import CompareImage
from pdf.PdfReport import PdfReport

import os
import time
import util
import ReadFile
import RemoveFiles

def run():
    #load Links from exel
    web_links = WebsiteLinks()
    links = web_links.get_links_from_xl('baseline')

    #Capture screenshots from links
    cap = CaptureScreenshot()

    #Compare images
    com_image = CompareImage()
    compared_images = []

    # loop in links
    i = 0
    j = 1

    length = int(len(links[0])/2)

    for x in range(length):

        cap.capture_screenshot(links[0][i], 0)
        # print(imageA)
        time.sleep(3)
        cap.capture_screenshot(links[0][j], 1)

        i = i + 2
        j = j + 2

        read = ReadFile

        one = read.read_file_name("temp0")
        two = read.read_file_name("temp1")
        # print(len(one))

        if len(one) < len(two):
            count = len(one)
        else:
            count = len(two)

        # print(count)
        compared_images = []
        com_image = CompareImage()

        for num in range(count):
            # print(num)
            time.sleep(1)
            compared_images.append(com_image.get_image_comparison(one[num], two[num]))
            # print(one[num] + "  " + two[num])

        # print(compared_images)

        #print to pdf
        pdf_report = PdfReport()
        pdf_report.generate_report(compared_images)

        # remove captured image
        rem_file = RemoveFiles

        rem_file.remove_files("temp")
        rem_file.remove_files("temp0")
        rem_file.remove_files("temp1")

    
fenetre = Tk()
fenetre.geometry("300x200+300+200")
fenetre.title('Interface Python')

#progressbar = ttk.Progressbar(fenetre, orient=HORIZONTAL, length=200)
#progressbar.pack()
#progressbar.config(mode='determinate', value=80)
#progressbar.step()

bouton1 = Button(fenetre, text='Generate Report', bg='grey', relief=GROOVE, command=run)
bouton1.pack()

fenetre.mainloop()