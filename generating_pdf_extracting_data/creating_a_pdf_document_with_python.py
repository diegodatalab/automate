from fpdf import FPDF
from fpdf.enums import XPos, YPos



img = "/home/diego/Desktop/automate/generating_pdf_extracting_data/cv.png"
main_text = """
O curriculum vitæ (do latim "trajetória de vida"), também abreviado para CV ou apenas currículo 
(por vezes utiliza-se o termo curricula, como forma no plural do termo) é um documento de tipo histórico, 
que relata a trajetória educacional e as experiências profissionais de uma pessoa, como forma de demonstrar suas habilidades e 
competências. De modo geral, ele tem como objetivo fornecer o perfil da pessoa para um empregador, 
podendo também ser usado como instrumento de apoio em situações acadêmicas.
"""

pdf = FPDF(orientation='P', unit='pt', format='A4')

pdf.add_page()

pdf.image(img, w=50, h=50)

pdf.set_font(family='Times', style='B', size=20)
pdf.cell(w=0, h=50, txt="curriculum vitae", ln=1, align='C')

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=50, txt='Description', ln=1, align='L') 

pdf.set_font(family='Times', size=12)
pdf.multi_cell(w=0, h=15, txt=main_text)

pdf.output('output.pdf')