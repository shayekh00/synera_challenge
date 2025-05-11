from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Material: Aluminum", ln=True)
pdf.cell(200, 10, txt="Max temperature: 100°C", ln=True)
pdf.cell(200, 10, txt="Density: 2.7 g/cm^3", ln=True)
pdf.output("docs/spec_sheet.pdf")
print("PDF created successfully.")