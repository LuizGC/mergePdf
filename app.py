from flask import Flask, render_template, request, send_file
from pdfmerger import PDFMerger
import string
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('upload.html')

@app.route('/merge', methods=['POST'])
def merge_pdf():
    uploaded_pdfs = request.files.getlist("pdfs")
    pdfMerger = PDFMerger()
    for pdf in uploaded_pdfs:
        filepath =  '/tmp/' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) + '.pdf'
        pdf.save(filepath)
        pdfMerger.add(filepath)

    merged_filepath = pdfMerger.merge()
    return send_file(merged_filepath)

if __name__ == "__main__":
    app.run()