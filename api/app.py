from flask import Flask, render_template, Response, request, redirect, url_for

import classes.army_parse as Army

# Set month to parse data from
pdf_name = "Sep23.pdf"

a = Army.AC_Parse("./pdfs/ac/" + str(pdf_name), False)
a.read_extract()
ac_dict = a.create_mos_dict()

b = Army.AC_Parse("./pdfs/agr/" + str(pdf_name), False)
b.read_extract()
agr_dict = b.create_mos_dict()


app = Flask(__name__, template_folder='./')

@app.route('/mos_list', methods=['GET', 'POST'])
def get_list():

    json = request.get_json()
    choice = json['component_selector']

    mos_list = []

    if choice == 'ac':
        for key in ac_dict:
            if key not in mos_list:
                mos_list.append(key)
    elif choice == 'agr':
        for key in agr_dict:
            if key not in mos_list:
                mos_list.append(key)
    
    mos_list.sort()

    return mos_list


@app.route('/army_handle_data', methods=['GET', 'POST'])
def handle_data():
    json = request.get_json()

    mos = json['mos']
    choice = json['component_selector']

    if choice == "ac":
        try:
            return ac_dict[mos.upper()]
        except:
            return
    elif choice == "agr":
        try:
            return agr_dict[mos.upper()]
        except:
            return
    else:
        return
    
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
