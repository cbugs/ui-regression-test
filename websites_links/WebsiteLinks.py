import pandas as pd
import os

class WebsiteLinks(object):

    

    def get_links_from_xl(self, sheet):
        excel_path = os.getcwd() + "\\websites_links\\website_links.xlsx"
        xl_sheet = pd.ExcelFile(excel_path)

        links_list = []
        links_list.append([])

        df = xl_sheet.parse(sheet)

        for index, rows in df.iterrows():
            links_list[0].append(rows['baseline_links'])
            links_list[0].append(rows['test_links'])
            # print(index, rows['Links'])
        return links_list











