
from flask import Flask, render_template, request, send_file
# from PyPDF2 import PdfFileMerger
from pdf_operations import merge
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdf():
    merged_pdf = merge(request)
    return send_file(
        merged_pdf,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='merged.pdf'
    )
    


@app.route('/split')
def split_pdf():
    return render_template('split_pdf.html')

@app.route('/compress')
def compress_pdf():
    return render_template('compress_pdf.html')

@app.route('/pdf_to_word')
def pdf_to_word():
    return render_template('pdf_to_word.html')

@app.route('/pdf_to_powerpoint')
def pdf_to_powerpoint():
    return render_template('pdf_to_powerpoint.html')

@app.route('/pdf_to_excel')
def pdf_to_excel():
    return render_template('pdf_to_excel.html')

@app.route('/word_to_pdf')
def word_to_pdf():
    return render_template('word_to_pdf.html')

@app.route('/powerpoint_to_pdf')
def powerpoint_to_pdf():
    return render_template('powerpoint_to_pdf.html')

@app.route('/excel_to_pdf')
def excel_to_pdf():
    return render_template('excel_to_pdf.html')

@app.route('/edit_pdf')
def edit_pdf():
    return render_template('edit_pdf.html')

@app.route('/pdf_to_jpg')
def pdf_to_jpg():
    return render_template('pdf_to_jpg.html')

@app.route('/jpg_to_pdf')
def jpg_to_pdf():
    return render_template('jpg_to_pdf.html')

@app.route('/sign_pdf')
def sign_pdf():
    return render_template('sign_pdf.html')

@app.route('/watermark')
def watermark():
    return render_template('watermark.html')

@app.route('/rotate_pdf')
def rotate_pdf():
    return render_template('rotate_pdf.html')

@app.route('/html_to_pdf')
def html_to_pdf():
    return render_template('html_to_pdf.html')

@app.route('/unlock_pdf')
def unlock_pdf():
    return render_template('unlock_pdf.html')

@app.route('/protect_pdf')
def protect_pdf():
    return render_template('protect_pdf.html')

@app.route('/organize_pdf')
def organize_pdf():
    return render_template('organize_pdf.html')

@app.route('/pdf_to_pdfa')
def pdf_to_pdfa():
    return render_template('pdf_to_pdfa.html')

@app.route('/repair_pdf')
def repair_pdf():
    return render_template('repair_pdf.html')

@app.route('/page_numbers')
def page_numbers():
    return render_template('page_numbers.html')

@app.route('/scan_to_pdf')
def scan_to_pdf():
    return render_template('scan_to_pdf.html')

@app.route('/ocr_pdf')
def ocr_pdf():
    return render_template('ocr_pdf.html')

if __name__ == '__main__':
    app.run(debug=True)
