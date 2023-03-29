from fpdf import FPDF

#P : portrait (vertical)
#L : landscape (horizontal)

#A4 : 210x297mm


pdf = FPDF(orientation = 'P',unit = 'mm', format = 'A4')

pdf.add_page()

#RECTA
pdf.rect(x = 25,y = 25,w = 165,h = 245)

#LINEA
pdf.line(25,70,190,70)
pdf.line(63,25,63,70)

#TEXTO
pdf.set_font('Arial','',14)
pdf.text(x = 65,y = 35, txt = 'Analisis Probabilistico')
pdf.text(x = 65,y = 40, txt = 'Ing. Manuel Eduardo Alvarez Ruiz')
pdf.text(x = 65,y = 45, txt = 'Proyecto Programa prueba de hipotesis')
pdf.text(x = 65,y = 50, txt = 'Eduardo Rubén Cruz Sánchez      202146471')
pdf.text(x = 65,y = 55, txt = 'Nery                           ---------')
pdf.text(x = 65,y = 60, txt = 'Ramiro André Chaón Castañeda   201940859')
pdf.text(x = 65,y = 65, txt = 'Kenat                          ---------')
#IMAGEN
pdf.image('logotipo-cunori-transparente.png',x = 27,y = 29,w = 33, h = 33)
pdf.image('prueba.jpg',x = 50,y = 175,w = 120, h = 90)



''''


#ELIPSE
pdf.ellipse(x= 10,y = 15, w = 100,h =80)
'''

pdf.output('hoja.pdf')