from fpdf import FPDF

name = input("What's your name? ")



class PDF(FPDF):
    def header(self):
        # Rendering shirtificate:
        self.image("shirtificate.png", 0, 65)
        # Setting font: helvetica bold 40
        self.set_font("helvetica", "B", 40)
        # Printing title:
        self.cell(0, 40, "CS50 Shirtificate", align="C")

    def footer(self):
        # Setting font: helvetica bold 25
        self.set_font("helvetica", "B", 25)
        # Setting color white
        self.set_text_color(255, 255, 255)
        # Printing name:
        self.text(50, 140, name + " took CS50")

# output shirtificate with name
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
