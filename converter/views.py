import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .utils import (
    pdf_to_word, word_to_pdf, pdf_to_excel, excel_to_pdf,
    pdf_to_ppt, ppt_to_pdf, img_to_pdf, img_to_word, pdf_to_image, ocr_for_pdf, ocr_for_image
)

def ensure_media_dir():
    """Ensure media directory exists."""
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)

def index(request):
    if request.method == "POST":
        ensure_media_dir()

        file = request.FILES['file']
        conversion_type = request.POST['conversion_type']

        input_path = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(input_path, 'wb') as f:
            f.write(file.read())

        output_filename = f"converted_{os.path.splitext(file.name)[0]}"
        output_path = os.path.join(settings.MEDIA_ROOT, f"{output_filename}.output")

        if conversion_type == "pdf_to_word":
            output_path += ".docx"
            pdf_to_word(input_path, output_path)
        elif conversion_type == "word_to_pdf":
            output_path += ".pdf"
            word_to_pdf(input_path, output_path)
        elif conversion_type == "pdf_to_excel":
            output_path += ".xlsx"
            pdf_to_excel(input_path, output_path)
        elif conversion_type == "excel_to_pdf":
            output_path += ".pdf"
            excel_to_pdf(input_path, output_path)
        elif conversion_type == "pdf_to_ppt":
            output_path += ".pptx"
            pdf_to_ppt(input_path, output_path)
        elif conversion_type == "ppt_to_pdf":
            output_path += ".pdf"
            ppt_to_pdf(input_path, output_path)
        elif conversion_type == "img_to_pdf":
            output_path += ".pdf"
            img_to_pdf(input_path, output_path)
        elif conversion_type == "img_to_word":
            output_path += ".docx"
            img_to_word(input_path, output_path)
        elif conversion_type == "pdf_to_image":
            output_path += "_page_1.jpg"
            pdf_to_image(input_path, output_path)
        elif conversion_type == "ocr_for_pdf":
            text = ocr_for_pdf(input_path)
            output_path += ".txt"
            with open(output_path, 'w') as f:
                f.write(text)
        elif conversion_type == "ocr_for_image":
            text = ocr_for_image(input_path)
            output_path += ".txt"
            with open(output_path, 'w') as f:
                f.write(text)
        else:
            return HttpResponse("Invalid conversion type!")

        with open(output_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(output_path)}'
            return response

    return render(request, "index.html")
