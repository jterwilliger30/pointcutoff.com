from PyPDF2 import PdfReader
from pdfminer.high_level import  extract_text
import re

class Parse:
    def __init__(self, filename):
        self.filename = filename
        self.SGT_SSG = []
        self.dict = {}

    def read_extract(self):
        text = extract_text(self.filename)
        text = text.split("\n")

        for line in text:
            if re.match(r'^\d{2}[A-Z]{1,3} {1,6}', line.strip()):
                line = line.strip()
                line = " ".join(line.split())
                if "(SEE " in line:
                    line = line.replace("(SEE ", "(SEE")
                if ")(" in line:
                    line = line.replace(")(", ") (")
                
                line = line.split(" ")

                # Once divided into list by spaces, add the space back into (SEE XYZ)
                for i in range(len(line)):
                    if "(SEE" in line[i]:
                        line[i] = line[i].replace("(SEE", "(SEE ")

                self.SGT_SSG.append(line)

    def create_mos_dict(self):
        for i in self.SGT_SSG:
            # Declares sub-dictionaries for each MOS (i[0]) where all 4 values will be stored
            self.dict[i[0]] = {}

            # Sets all 4 keys for each MOS
            self.dict[i[0]]["SGT PZ"] = i[1]    # SGT PZ
            self.dict[i[0]]["SGT SZ"] = i[2]    # SGT SZ
            self.dict[i[0]]["SSG PZ"] = i[3]    # SSG PZ
            self.dict[i[0]]["SSG SZ"] = i[4]    # SSG SZ

        return self.dict
