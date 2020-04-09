import PyPDF2
import sys

def convert_watermark(watermark_input, pdf_input, convert_output):
    output = PyPDF2.PdfFileWriter()
    with open(pdf_input, "rb") as input_file:
        pdf = PyPDF2.PdfFileReader(input_file)
        with open(watermark_input, "rb") as input_watermark:
            watermark = PyPDF2.PdfFileReader(input_watermark)
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                page.mergePage(watermark.getPage(0))
                output.addPage(page)
            with open(convert_output, "wb") as new_output:
                output.write(new_output)
                    


def main():
    watermark_input = sys.argv[1]
    pdf_input = sys.argv[2]
    convert_output = sys.argv[3]
    convert_watermark(watermark_input, pdf_input, convert_output)

if __name__ == "__main__":
    main()
