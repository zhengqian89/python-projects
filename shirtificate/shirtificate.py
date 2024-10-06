from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("Arial", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

def shirt(name):
    pdf = PDF()
    pdf.add_page("P", "A4")
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    shirt(name)

if __name__ == "__main__":
    main()