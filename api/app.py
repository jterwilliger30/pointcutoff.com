from flask import Flask, render_template, Response, request, redirect, url_for

from classes.parse import Parse

a = Parse("./pdfs/Apr23.pdf")
a.read_pdf_pages([4,5,6], [7,8,9])

dict = a.create_mos_dict()


app = Flask(__name__, template_folder='./')

@app.route('/handle_data', methods=['GET', 'POST'])
def handle_data():
    json = request.get_json()
    key = json['data']
    try:
        return dict[key.upper()]
    except:
        return
