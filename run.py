from websites_links.WebsiteLinks import WebsiteLinks
from capture_screenshot.CaptureScreenshot import CaptureScreenshot
from image_comparisons.CompareImage import CompareImage
from pdf.PdfReport import PdfReport

#load Links from exel
web_links = WebsiteLinks()
links = web_links.get_links_from_xl('baseline')

#Capture screenshots from links
cap = CaptureScreenshot()


imageA = None
imageB = None

#Compare images
com_image = CompareImage()
compared_images = []

for link in links:
    imageA = cap.capture_screenshot(link[0])
    imageB = cap.capture_screenshot(link[1])
    compared_images.append(com_image.get_image_comparison(imageA, imageB))


#print to pdf
pdf_report = PdfReport()
pdf_report.generate_report(compared_images)








