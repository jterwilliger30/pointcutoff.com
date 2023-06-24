from flask import Flask, render_template, Response, request, redirect, url_for

from classes.parse import AC_Parse, AGR_Parse

# Set month to parse data from
pdf_name = "Jul23.pdf"

a = AC_Parse("./pdfs/ac/" + str(pdf_name))
a.read_extract()
ac_dict = a.create_mos_dict()

""" Temporarily removed this for the month of June... AGR parsing seems to be the same as AC this month.
b = AGR_Parse("./pdfs/agr/" + str(pdf_name))
b.read_extract()
agr_dict = b.create_mos_dict()
"""

# Added this temporarily:
b = AC_Parse("./pdfs/agr/" + str(pdf_name))
b.read_extract()
agr_dict = b.create_mos_dict()

for key in agr_dict:
    print(f"{key}:\t {agr_dict}")

app = Flask(__name__, template_folder='./')

@app.route('/mos_list', methods=['GET'])
def get_list():
    mos_list = []

    for key in ac_dict:
        if key not in mos_list:
            mos_list.append(key)
    
    for key in agr_dict:
        if key not in mos_list:
            mos_list.append(key)
    
    mos_list.sort()

    return mos_list

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
