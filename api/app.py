from flask import Flask, render_template, Response, request, redirect, url_for

from classes.parse import AC_Parse, AGR_Parse

pdf_name = "Apr23.pdf"

a = AC_Parse("./pdfs/ac/" + str(pdf_name))
a.read_extract()
ac_dict = a.create_mos_dict()

b = AGR_Parse("./pdfs/agr/" + str(pdf_name))
b.read_extract()
agr_dict = b.create_mos_dict()

app = Flask(__name__, template_folder='./')

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    json = request.get_json()

    key = json['data']
    ac_agr = json['selector']

    if ac_agr == "ac":
        try:
            return ac_dict[key.upper()]
        except:
            return
    elif ac_agr == "agr":
        try:
            return agr_dict[key.upper()]
        except:
            return
    else:
        return
