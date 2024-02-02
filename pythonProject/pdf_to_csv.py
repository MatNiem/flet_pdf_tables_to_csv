import subprocess
import sys

import pdf2image
from PIL import Image


def pdf2img_cut(pdf_file_name: str) -> str:
    print(pdf_file_name)
    images = pdf2image.convert_from_path(pdf_file_name, poppler_path=r"C:\Program Files\poppler-23.11.0\Library\bin")
    png_name = pdf_file_name.replace(".pdf", ".png")
    images[0].save(png_name, "PNG")

    im = Image.open(png_name)
    top = 156
    left = 156
    right = 1284
    bottom = 1760

    im = im.crop((left, top, right, bottom))
    im.save(png_name, "PNG")

    return png_name


def img_table2csv(pdf_path: str) -> None:
    image_file_name = pdf2img_cut(pdf_path)

    output = subprocess.getoutput('tesseract ' + image_file_name + ' - -l eng+fin --oem 3 --psm 3')

    result_csv_name = image_file_name.replace(".png", ".csv")

    with open(result_csv_name, "w") as f:
        f.write("numer,nazwa,liczba1,liczba2\n")
        for line in output.splitlines():
            if line[:1].isdigit():
                if not line == '':
                    line = line.split(" ")
                    nr = line[0]
                    text = " "
                    for words in line[1:(len(line) - 2)]:
                        text += words
                        text += " "
                    amount1 = line[len(line) - 2]
                    amount2 = line[len(line) - 1]
                    print(f"{nr} |{text}| {amount1} | {amount2}")
                    f.write(f"{nr},{text.replace(",", "")},{amount1},{amount2}\n")


def main(pdf_path):
    if pdf_path:
        img_table2csv(pdf_path)
    else:
        print("bruh")
