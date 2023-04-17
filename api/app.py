from flask import Flask, render_template, Response, request, redirect, url_for

from parser.parse import Parse

a = Parse("./pdfs/Apr23.pdf")
a.read_pdf_pages([4,5,6], [7,8,9])

dict = a.create_mos_dict()
"""



text = extract_text("./Apr23.pdf")
matches = []


text = text.split("\n")

for i in text:
    print(i)

dict = {}

for i in range(len(matches)):
    if len(matches[i]) == 13:
        dict[matches[i][0]] = {"SGT PZ: ":  matches[i][1] , "SGT SZ: ": matches[i][2], "SSG PZ: ": matches[i][3], "SSG SZ: ": matches[i][4]}
    elif len(matches[i]) == 7:
        dict[matches[i][0]] = {"SGT PZ: ":  matches[i][1] , "SGT SZ: ": matches[i][1], "SSG PZ: ": matches[i][2], "SSG SZ: ": matches[i][2]}
"""
        



app = Flask(__name__, template_folder='./')

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    json = request.get_json()
    key = json['data']
    try:
        return dict[key.upper()]
    except:
        return
