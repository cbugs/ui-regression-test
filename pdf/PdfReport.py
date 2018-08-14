from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
import datetime
from fpdf import FPDF

class PdfReport(object):

    now = datetime.datetime.now()

    def generate_report(self, image_paths):
        
        pdf = FPDF()
        
        for image_path in image_paths:

            # image = Image.open(image_path)
            # image_width, image_height = image.size
            # self.c.drawImage(image_path, 0, (792 - image_height))
            # self.c.drawImage(image_path, inch*.25, inch*.25, PAGE_WIDTH-(.5*inch), (.316*inch))
            # self.c.showPage()
            pdf.add_page()
            pdf.image(image_path, 5, 5, 200, 0)
        
        
        date_stamp = str(datetime.datetime.now()).split('.')[0]
        date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")
        file_name = 'UI_Report_' + date_stamp + ".pdf"

        pdf.output(file_name, "F")
        # self.c.save()