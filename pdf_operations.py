from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import io
import zipfile
from PIL import Image
from fpdf import FPDF

def merge(request):
    merger = PdfMerger()
    files = request.files.getlist('pdf_files')

    for file in files:
        merger.append(file)

    merged_pdf = io.BytesIO()
    merger.write(merged_pdf)
    merged_pdf.seek(0)
    # return send_file(
    #     merged_pdf,
    #     mimetype='application/pdf',
    #     as_attachment=True,
    #     download_name='merged.pdf'
    # )
    return merged_pdf