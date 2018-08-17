from websites_links.WebsiteLinks import WebsiteLinks
from capture_screenshot.CaptureScreenshot import CaptureScreenshot
from image_comparisons.CompareImage import CompareImage
from pdf.PdfReport import PdfReport

import os
import time
import util
import ReadFile
import RemoveFiles

#load Links from exel
web_links = WebsiteLinks()
links = web_links.get_links_from_xl('baseline')

#Capture screenshots from links
cap = CaptureScreenshot()

#Compare images
com_image = CompareImage()
compared_images = []

# loop in links
length = int(len(links[0])/2)

for x in range(0, length, 2):

    cap.capture_screenshot(links[0][x], 0)
    # print(imageA)
    time.sleep(3)
    cap.capture_screenshot(links[0][x+1], 1)

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

