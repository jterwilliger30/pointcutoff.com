import re
import eel

from pdfminer.high_level import  extract_text


eel.init('web')


@eel.expose
def parse():
    text = extract_text("./Jan23.pdf")
    matches = []
    text = text.split("\n")
    for line in text:
        if re.match(r'^\d{2}[A-Z]{1,3} {1,6}', line):
            matches.append(line)


    for i in matches:
        print(i)

    return i


eel.start('index.html')