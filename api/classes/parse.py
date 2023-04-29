import PyPDF2 as rd
from pdfminer.high_level import  extract_text
import re

class AC_Parse:
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

                # Once divided into list by spaces, add the space back into (SEEXYZ)
                for i in range(len(line)):
                    if "(SEE" in line[i]:
                        line[i] = line[i].replace("(SEE", "(SEE ")

                self.SGT_SSG.append(line)

    def create_mos_dict(self):
        for i in self.SGT_SSG:
            # Hopefully tosses garbage pulled in by the regex...
            if len(i) > 4:
                # Declares sub-dictionaries for each MOS (i[0]) where all 4 values will be stored
                self.dict[i[0]] = {}

                # Sets all 4 keys for each MOS
                self.dict[i[0]]["SGT PZ"] = i[1]
                self.dict[i[0]]["SGT SZ"] = i[2]
                self.dict[i[0]]["SSG PZ"] = i[3]
                self.dict[i[0]]["SSG SZ"] = i[4]

        return self.dict
    

class AGR_Parse:
    def __init__(self, filename):
        self.filename = filename
        self.SGT = []
        self.SSG = []
        self.dict = {}
    
    def read_extract(self):
        raw_data = rd.PdfReader(self.filename)

        lines = []

        # Extract all relevant lines from the PDF
        for page in raw_data.pages:
            for line in page.extract_text().split("\n"):
                if re.match(r'^\d{2}[A-Z]{1,3} {1,6}', line.strip()):
                    line = line.strip()
                    line = " ".join(line.split())

                    line = line.split(" ")
                    
                    lines.append(line)

                # The "TOTALS" row is the demarcation b/w SGT and SSG sections, which we will use to split the list
                elif line.startswith("TOTALS"):
                    lines.append("LINEBREAK")
        
        is_SSG = False
        for line in lines:
            if line == "LINEBREAK":
                is_SSG = True
                continue
            
            if is_SSG:
                self.SSG.append(line)
            else:
                self.SGT.append(line)

    def create_mos_dict(self):
        for i in self.SGT:
            # Declares sub-dictionaries for each MOS (i[0]) where all 4 values will be stored
            self.dict[i[0]] = {}

            self.dict[i[0]]["SGT PZ"] = i[1]
            self.dict[i[0]]["SGT SZ"] = i[2]
            self.dict[i[0]]["SSG PZ"] = "NA"
            self.dict[i[0]]["SSG SZ"] = "NA"

        for i in self.SSG:
            # If this MOS exists in the SSG list but not the SGT list
            if i[0] not in self.dict:
                self.dict[i[0]] = {}
                
                self.dict[i[0]]["SGT PZ"] = "NA"
                self.dict[i[0]]["SGT SZ"] = "NA"
            
            self.dict[i[0]]["SSG PZ"] = i[1]
            self.dict[i[0]]["SSG SZ"] = i[2]
        
        return self.dict