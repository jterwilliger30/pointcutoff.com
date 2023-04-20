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

                self.SGT_SSG.append(line.split(" "))

    def create_mos_dict(self):
        for i in self.SGT_SSG:
            # Declares sub-dictionaries for each MOS where all 4 values will be stored
            self.dict[i[0]] = {}

            # Sets all 4 keys for each MOS, assuming order of SGT PZ, SGT SZ, SSG PZ, SSG SZ
            self.dict[i[0]]["SGT PZ"] = i[1]
            self.dict[i[0]]["SGT SZ"] = i[2]
            self.dict[i[0]]["SSG SZ"] = i[3]
            self.dict[i[0]]["SSG PZ"] = i[4]

        return self.dict

        """

        for i in range(len(self.SSG)):
            self.SSG[i] = self.SSG[i].split(" ")

            # If this MOS exists in the SSG list but not the SGT list...
            if self.SSG[i][0] not in self.dict:
                # Create a sub-dictionary for it and...
                self.dict[self.SSG[i][0]] = {}

                # Set the SSG keys to N/A
                self.dict[self.SSG[i][0]]["SGT PZ"] = "N/A"
                self.dict[self.SSG[i][0]]["SGT SZ"] = "N/A"

            # For all MOS's in the SSG list, set the 2 SSG keys
            self.dict[self.SSG[i][0]]["SSG PZ"] = self.SSG[i][1]
            self.dict[self.SSG[i][0]]["SSG SZ"] = self.SSG[i][2]
        """

        
        """ DEBUG PURPOSES ONLY
        for key in self.dict:
            print(f"{key} : {self.dict[key]}")
        """
