from websites_links.WebsiteLinks import WebsiteLinks
from capture_screenshot.CaptureScreenshot import CaptureScreenshot
from image_comparisons.CompareImage import CompareImage
from pdf.PdfReport import PdfReport

import os
import time
import util
import ReadFile

# #load Links from exel
# web_links = WebsiteLinks()
# links = web_links.get_links_from_xl('baseline')

# #Capture screenshots from links
# cap = CaptureScreenshot()


# imageA = None
# imageB = None

# #Compare images
# com_image = CompareImage()
# compared_images = []

# for link in links:
#     cap.capture_screenshot(link[0],0)
#     # print(imageA)
#     cap.capture_screenshot(link[1],1)
# #     compared_images.append(com_image.get_image_comparison(imageA, imageB))

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