# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import os
import numpy as np
import PIL
from PIL import Image, ImageOps

class CompareImage(object):


	def get_image_comparison(self, imageA, imageB):

		# load the two input images
		imageA = cv2.imread(imageA)
		imageB = cv2.imread(imageB)

		# convert the images to grayscale
		grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
		grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)


		# compute the Structural Similarity Index (SSIM) between the two
		# images, ensuring that the difference image is returned
		(score, diff) = compare_ssim(grayA, grayB, full=True)
		diff = (diff * 255).astype("uint8")
		print("SSIM: {}".format(score))

		# threshold the difference image, followed by finding contours to
		# obtain the regions of the two input images that differ
		thresh = cv2.threshold(diff, 0, 255,
			cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
		cnts = cnts[0] if imutils.is_cv2() else cnts[1]

		# loop over the contours
		for c in cnts:
			# compute the bounding box of the contour and then draw the
			# bounding box on both input images to represent where the two
			# images differ
			(x, y, w, h) = cv2.boundingRect(c)
			cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
			cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)


		image_concat_name = os.getcwd() + '\\temp\\' + 'concat_image.png'

		# border widths; I set them all to 150
		top, bottom, left, right = [5]*4
		color = [101, 52, 152] # 'cause purple!

		#Empty vstack list
		image_vstack = []

		#Add borders
		imageA_with_border = cv2.copyMakeBorder(imageA, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
		imageB_with_border = cv2.copyMakeBorder(imageB, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)


		image_vstack.append(imageA_with_border)
		image_vstack.append(imageB_with_border)
		

		#write concatenated image
		image_concat = cv2.imwrite(image_concat_name, np.vstack(image_vstack))

		return os.getcwd() + '\\temp\\' + 'concat_image.png'