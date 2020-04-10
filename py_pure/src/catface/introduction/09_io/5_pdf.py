# -写pdf文件
from reportlab.pdfgen import canvas


def main():
    c = canvas.Canvas('../../introduction_dir/hi.pdf')
    c.drawString(10, 600, '2020.04.09', wordSpace=10)
    c.drawString(100, 100, 'hi')
    c.showPage()
    c.save()


if __name__ == '__main__':
    main()
