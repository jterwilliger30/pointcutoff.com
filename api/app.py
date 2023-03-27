from flask import Flask, render_template, Response, request, redirect, url_for

import re

from pdfminer.high_level import  extract_text


text = extract_text("./Apr23.pdf")
matches = []


text = text.split("\n")

for line in text:
    if re.match(r'^\d{2}[A-Z]{1,3} {1,6}', line):
        matches.append(line)

for i in range(len(matches)):
    matches[i] = " ".join(matches[i].split())
    if "(SEE " in matches[i]:
        matches[i] = matches[i].replace("(SEE ", "(SEE")
        if ")(" in matches[i]:
            matches[i] = matches[i].replace(")(",") (")
    matches[i] = matches[i].split(" ")

# This probably isn't necessary, and might be useful to omit for debugging purposes
#matches = [x for x in matches if len(x) >= 6]

dict = {}

for i in range(len(matches)):
    if len(matches[i]) == 13:
        dict[matches[i][0]] = {"SGT PZ: ":  matches[i][1] , "SGT SZ: ": matches[i][2], "SSG PZ: ": matches[i][3], "SSG SZ: ": matches[i][4]}
    elif len(matches[i]) == 7:
        dict[matches[i][0]] = {"SGT PZ: ":  matches[i][1] , "SGT SZ: ": matches[i][1], "SSG PZ: ": matches[i][2], "SSG SZ: ": matches[i][2]}



#[print(len(x),x) for x in matches]


#for key in dict:
#    print(key, dict[key])

app = Flask(__name__, template_folder='./')

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    json = request.get_json()
    key = json['data']
    try:
        return dict[key.upper()]
    except:
        return

