from image_comparisons.CompareImage import CompareImage
from pdf.PdfReport import PdfReport
import unittest
from selenium import webdriver
import os
import time

import util
import ReadFile

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
















 
# class MyScreenshot(unittest.TestCase):
 
#     def setUp(self):
#         self.chrome_driver = os.getcwd() +"\\driver\\chromedriver.exe"
#         # self.load_headless_capture()
#         self.driver = webdriver.Chrome( executable_path=self.chrome_driver)
    
#     def test_takescreenshot(self):
#         driver = self.driver
#         driver.maximize_window()
#         driver.get('https://www.kaufmanbroad.fr/search?geolocation=&type_bien%5B%5D=Appartement&type_bien%5B%5D=Maison&prix_max=')
 
#         # driver.save_screenshot(os.getcwd() + '\\test.png')
#         # path = os.getcwd() + '\\test.png'
#         util.fullpage_screenshot(driver, "path.png")
 
 
#     # def tearDown(self):
#     #     self.driver.quit()
 
 
# if __name__ == '__main__':
#     unittest.main()