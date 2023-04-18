from PyPDF2 import PdfReader
import re

class Parse:
    def __init__(self, filename):
        self.filename = filename
        self.SGT = []
        self.SSG = []
        self.dict = {}

    def read_pdf_pages(self, SGT_Pages, SSG_Pages):
        self.reader = PdfReader(self.filename)

        for i in SGT_Pages:
            self.SGT.append(self.reader.pages[i].extract_text())
        for i in SSG_Pages:
            self.SSG.append(self.reader.pages[i].extract_text())

    def regex_extraction(self):
        temp = []
        for page_idx in range(len(self.SGT)):
            self.SGT[page_idx] = self.SGT[page_idx].split('\n')
        
        for page_idx in range(len(self.SGT)):
            for line in self.SGT[page_idx]:
                if re.match(r'^\d{2}[A-Z]{1,3} {1,6}', line.strip()):
                    temp.append(line.strip())
        self.SGT = temp

        temp = []
        for page_idx in range(len(self.SSG)):
            self.SSG[page_idx] = self.SSG[page_idx].split('\n')
        
        for page_idx in range(len(self.SSG)):
            for line in self.SSG[page_idx]:
                if re.match(r'^\d{2}[A-Z]{1,3} {1,6}', line.strip()):
                    temp.append(line.strip())
        self.SSG = temp
        temp = []
        
    def create_mos_dict(self):
        self.regex_extraction()

        for i in range(len(self.SGT)):
            self.SGT[i] = self.SGT[i].split(" ")

            # Declares sub-dictionaries for each MOS where all 4 values will be stored
            self.dict[self.SGT[i][0]] = {}

            # Sets all 4 keys for each MOS... leaves SSG values as None (for now)
            self.dict[self.SGT[i][0]]["SGT PZ"] = self.SGT[i][1]
            self.dict[self.SGT[i][0]]["SGT SZ"] = self.SGT[i][2]
            self.dict[self.SGT[i][0]]["SSG SZ"] = "N/A"
            self.dict[self.SGT[i][0]]["SSG PZ"] = "N/A"


            
            #{"SGT PZ: ":  self.SGT[i][1] , "SGT SZ: ": self.SGT[i][2], "SSG PZ: ": None, "SSG SZ: ": None}

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
        
        """ DEBUG PURPOSES ONLY
        for key in self.dict:
            print(f"{key} : {self.dict[key]}")
        """
        return self.dict







#page = reader.pages[10]
