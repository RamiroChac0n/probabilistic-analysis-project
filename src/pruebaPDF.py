from fpdf import FPDF
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb


muT = "\u03BC"

def curvanormal(nocolas, alfa, mp, mm, n, desvest,Zinf,Zsup,zp,pvalor):
    alpha2 = str(alfa*100)
    nT = str(n)

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
    pdf.text(x = 195,y = 15, txt = '1')
    pdf.text(x = 65,y = 35, txt = 'Analisis probabilístico.')
    pdf.text(x = 65,y = 45, txt = 'Prueba de hipótesis: curva normal.')

    #Hoja del problema
    pdf.text(x = 30,y = 80, txt = 'Paso 1: formulación de hipótesis.')
    if(nocolas == 1):
        pdf.text(x = 30,y = 85, txt = "Ho: µ  = "+str(mp))
        pdf.text(x = 30,y = 90, txt = "Ho: µ != "+str(mp))
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 225, txt = "Área de no rechazo: entre los valores de Zcrítico ("+str(Zinf)+", "+str(Zsup)+").")
        pdf.text(x = 30,y = 230, txt = "Área de rechazo: a la izquierda de ZcI = "+str(Zinf)+".")
        pdf.text(x = 30,y = 235, txt = "Área de rechazo: a la derecha de ZcS = "+str(Zsup)+".")
    if(nocolas == 2):
        pdf.text(x = 30,y = 85, txt = "Ho: µ >= "+str(mp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ < "+str(mp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 225, txt = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(Zinf)+".")
    if(nocolas == 3):
        pdf.text(x = 30,y = 85, txt = "Ho: µ <= "+str(mp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ > "+str(mp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 225, txt = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(Zsup)+".")

    pdf.text(x = 30,y = 95, txt = 'Paso 2: nivel de significancia alpha.')
    pdf.text(x = 30,y = 100, txt = "alpha = "+str(alfa)+" = "+alpha2+"%.")

    pdf.text(x = 30,y = 105, txt = 'Paso 3: estadístico de prueba.')
    pdf.image('img/Estadistico_curvanormal.png',x = 30,y = 110,w = 40, h = 20)


    #IMAGEN
    pdf.image('img/logotipo-cunori-transparente.png',x = 27,y = 29,w = 33, h = 33)

    '''#-------------------------------------------------PAGINA 2------------------------------------------------'''
    pdf.add_page()
    #RECTA
    pdf.rect(x = 25,y = 25,w = 165,h = 245)
    pdf.text(x = 195,y = 15, txt = '2')
    pdf.text(x = 30,y = 35, txt = 'Paso 5: prueba del estadístico.')
    pdf.image('img/Estadistico_curvanormal.png',x = 30,y = 40,w = 40, h = 20)
    pdf.text(x = 70,y = 50, txt = " = ("+str(mm)+" - "+str(mp)+")/("+str(desvest)+"/raiz("+nT+")) = "+str(zp)+".")
    if(nocolas == 1):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 2[0.500 - p(Zp)]')
        pdf.text(x = 30,y = 70, txt = "pvalor = 2[0.500 - p("+str(zp)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        pdf.text(x = 30,y = 170, txt = 'Paso 6: respuestas.')
        if(zp>Zinf and zp<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "Zcrítico ("+str(Zinf)+", "+str(Zsup)+"), no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" no se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "Zcrítico ("+str(Zinf)+", "+str(Zsup)+"), se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 2):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 0.500 - p(Zp).')
        pdf.text(x = 30,y = 70, txt = "pvalor = 0.500 - p("+str(zp)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        pdf.text(x = 30,y = 170, txt = 'Paso 6: respuestas.')
        if(zp>Zinf):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 3):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 0.500 - p(Zp)')
        pdf.text(x = 30,y = 70, txt = "pvalor = 0.500 - p("+str(zp)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        pdf.text(x = 30,y = 170, txt = 'Paso 6: Respuesta')
        if(zp<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")

    pdf.image('img/grafica2.jpg',x = 40,y = 80,w = 130, h = 80)
    archivo = filedialog.asksaveasfilename()
    print(archivo)
    pdf.output(archivo+".pdf")
    mb.showinfo("Guardado", "El PDF se guardó correctamente en la ruta designada")
    

def tstudent(nocolas, alfa, mp, mm, n, desvest,Zinf,Zsup,zp,pvalor):
    gl = str(n-1)
    alpha2 = str(alfa*100)

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
    pdf.text(x = 195,y = 15, txt = '1')
    pdf.text(x = 65,y = 35, txt = 'Análisis probabilístico.')
    pdf.text(x = 65,y = 45, txt = 'Prueba de hipótesis: t student.')

    #Hoja del problema
    pdf.text(x = 30,y = 80, txt = 'Paso 1: formulación de hipótesis.')
    pdf.text(x = 30,y = 140, txt = "Grados de libertad g.l = muestra(n) - 1 = "+str(n)+" - 1 = "+gl)
    if(nocolas == 1):
        pdf.text(x = 30,y = 85, txt = "Ho: µ = "+str(mp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ != "+str(mp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
        pdf.image('img/grafica.jpg',x = 40,y = 145,w = 130, h = 80)
        pdf.text(x = 30,y = 230, txt = "Área de no rechazo: entre los valores de tcrítico ("+str(Zinf)+", "+str(Zsup)+").")
        pdf.text(x = 30,y = 235, txt = "Área de rechazo: a la izquierda de tcI = "+str(Zinf))
        pdf.text(x = 30,y = 240, txt = "Área de rechazo: a la derecha de tcS = "+str(Zsup))
    if(nocolas == 2):
        pdf.text(x = 30,y = 85, txt = "Ho: µ >= "+str(mp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ < "+str(mp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
        pdf.image('img/grafica.jpg',x = 40,y = 145,w = 130, h = 80)
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 230, txt = "Área de no rechazo: a la derecha del valor de tcrítico = "+str(Zinf))
    if(nocolas == 3):
        pdf.text(x = 30,y = 85, txt = "Ho: µ <= "+str(mp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ > "+str(mp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decision.')
        pdf.image('img/grafica.jpg',x = 40,y = 145,w = 130, h = 80)
        pdf.text(x = 30,y = 230, txt = "Área de no rechazo: a la izquierda del valor de tcrítico = "+str(Zsup))
    pdf.text(x = 30,y = 95, txt = 'Paso 2: nivel de significancia alpha.')
    pdf.text(x = 30,y = 100, txt = "alpha = "+str(alfa)+" = "+alpha2+"%.")
    pdf.text(x = 30,y = 105, txt = 'Paso 3: estadístico de prueba.')
    pdf.image('img/Estadistico_tstudent.png',x = 30,y = 110,w = 40, h = 20)


    #IMAGEN
    pdf.image('img/logotipo-cunori-transparente.png',x = 27,y = 29,w = 33, h = 33)

    '''#-------------------------------------------------PAGINA 2------------------------------------------------'''
    pdf.add_page()
    #RECTA
    pdf.rect(x = 25,y = 25,w = 165,h = 245)
    pdf.text(x = 195,y = 15, txt = '2')
    pdf.text(x = 30,y = 35, txt = 'Paso 5: prueba del estadístico.')
    pdf.image('img/Estadistico_tstudent.png',x = 30,y = 40,w = 40, h = 20)
    pdf.text(x = 70,y = 50, txt = " = ("+str(mm)+" - "+str(mp)+")/("+str(desvest)+"/raiz("+str(n)+")) = "+str(zp))
    if(nocolas == 1):
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        pdf.text(x = 30,y = 170, txt = 'Paso 6: respuestas.')
        if(zp>Zinf and zp<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que tp = "+str(zp)+" se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "tcrítico ("+str(Zinf)+", "+str(Zsup)+"), no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que tp = "+str(zp)+" no se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "tcrítico ("+str(Zinf)+", "+str(Zsup)+"), se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 2):
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        pdf.text(x = 30,y = 170, txt = 'Paso 6: Respuesta')
        if(zp>Zinf):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que tp = "+str(zp)+" es mayor que tcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que tp = "+str(zp)+" es menor que tcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 3):
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        pdf.text(x = 30,y = 170, txt = 'Paso 6: Respuesta')
        if(zp<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que tp = "+str(zp)+" es menor que tcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que tp = "+str(zp)+" es mayor que tcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")

    pdf.image('img/grafica2.jpg',x = 40,y = 80,w = 130, h = 80)
    archivo = filedialog.asksaveasfilename()
    print(archivo)
    pdf.output(archivo+".pdf")
    mb.showinfo("Guardado", "El PDF se guardó correctamente en la ruta designada")


def propmuestral(nocolas, alfa, pm, pp, n,Zinf,Zsup,q,zp,pvalor):
    alpha2 = str(alfa*100)

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
    pdf.text(x = 195,y = 15, txt = '1')
    pdf.text(x = 65,y = 35, txt = 'Analisis probabilístico.')
    pdf.text(x = 65,y = 45, txt = 'Prueba de hipótesis: proporcion muestral.')

    #Hoja del problema
    pdf.text(x = 30,y = 80, txt = 'Paso 1: formulación de hipótesis.')
    if(nocolas == 1):
        pdf.text(x = 30,y = 85, txt = "Ho: µ = "+str(pp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ != "+str(pp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 225, txt = "Área de no rechazo: entre los valores de Zcrítico ("+str(Zinf)+", "+str(Zsup)+").")
        pdf.text(x = 30,y = 230, txt = "Área de rechazo: a la izquierda de ZcI = "+str(Zinf))
        pdf.text(x = 30,y = 235, txt = "Área de rechazo: a la derecha de ZcS = "+str(Zsup))
    if(nocolas == 2):
        pdf.text(x = 30,y = 85, txt = "Ho: µ >= "+str(pp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ < "+str(pp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: Regla de decision')
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 225, txt = "Área de no rechazo: a la derecha del valor de Zc = "+str(Zinf))
        pdf.text(x = 155,y = 225, txt = str(Zinf))
    if(nocolas == 3):
        pdf.text(x = 30,y = 85, txt = "Ho: µ <= "+str(pp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: µ > "+str(pp)+".")
        pdf.text(x = 30,y = 135, txt = 'Paso 4: Regla de decision')
        pdf.image('img/grafica.jpg',x = 40,y = 140,w = 130, h = 80)
        pdf.text(x = 30,y = 225, txt = "Área de no rechazo: a la izquierda del valor de Zc = "+str(Zsup))
    pdf.text(x = 30,y = 95, txt = 'Paso 2: nivel de significancia alpha.')
    pdf.text(x = 30,y = 100, txt = "alpha = "+str(alfa)+" = "+alpha2+"%")
    pdf.text(x = 30,y = 105, txt = 'Paso 3: estadístico de prueba.')
    pdf.image('img/Estadistico_proporciones.png',x = 30,y = 110,w = 40, h = 20)


    #IMAGEN
    pdf.image('img/logotipo-cunori-transparente.png',x = 27,y = 29,w = 33, h = 33)

    '''#-------------------------------------------------PAGINA 2------------------------------------------------'''
    pdf.add_page()
    #RECTA
    pdf.text(x = 195,y = 15, txt = '2')
    pdf.rect(x = 25,y = 25,w = 165,h = 245)
    pdf.text(x = 30,y = 35, txt = 'Paso 5: prueba del estadístico.')
    pdf.image('img/Estadistico_proporciones.png',x = 30,y = 40,w = 40, h = 20)
    pdf.text(x = 70,y = 50, txt = " = ("+str(pm)+" - "+str(pp)+")/raiz("+str(pp)+" * "+str(q)+"/"+str(n)+") = "+str(zp))
    pdf.text(x = 30,y = 170, txt = 'Paso 6: respuestas.')
    if(nocolas == 1):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 2[0.500 - p(Zp)].')
        pdf.text(x = 30,y = 70, txt = "pvalor = 2[0.500 - p("+str(zp)+")]")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        if(zp>Zinf and zp<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "Zcrítico ("+str(Zinf)+", "+str(Zsup)+"), no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipotesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" no se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "Zcrítico ("+str(Zinf)+", "+str(Zsup)+"), se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 2):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 0.500 - p(Zp)')
        pdf.text(x = 30,y = 70, txt = "pvalor = 0.500 - p("+str(zp)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        if(zp>Zinf):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 3):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 0.500 - p(Zp)')
        pdf.text(x = 30,y = 70, txt = "pvalor = 0.500 - p("+str(zp)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        if(zp<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")

    pdf.image('img/grafica2.jpg',x = 40,y = 80,w = 130, h = 80)
    archivo = filedialog.asksaveasfilename()
    print(archivo)
    pdf.output(archivo+".pdf")
    mb.showinfo("Guardado", "El PDF se guardó correctamente en la ruta designada")

def chicuadrado(nocolas, alfa, varm, n,Zinf,Zsup,varp,x2,pvalor):
    gl = str(n-1)
    alpha2 = str(alfa*100)

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
    pdf.text(x = 195,y = 15, txt = '1')
    pdf.text(x = 65,y = 35, txt = 'Analisis probabilístico.')
    pdf.text(x = 65,y = 45, txt = 'Prueba de hipótesis: chi-cuadrado.')

    #Hoja del problema
    pdf.text(x = 30,y = 80, txt = 'Paso 1: formulación de hipótesis.')
    pdf.text(x = 30,y = 140, txt = "Grados de libertad g.l = muestra(n) - 1 = "+str(n)+" - 1 = "+gl+".")
    pdf.text(x = 30,y = 135, txt = 'Paso 4: regla de decisión.')
    pdf.image('img/grafica.jpg',x = 40,y = 145,w = 130, h = 80)
    if(nocolas == 1):
        pdf.text(x = 30,y = 85, txt = "Ho: x² = "+ str(varp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: x² != "+ str(varp)+".")
        pdf.text(x = 30,y = 230, txt = "Área de no rechazo: entre los valores de x²crítico ("+str(Zinf)+", "+str(Zsup)+")")
        pdf.text(x = 30,y = 235, txt = "Área de rechazo: a la izquierda de x²critico I = "+str(Zinf))
        pdf.text(x = 30,y = 240, txt = "Área de rechazo: a la derecha de x²critico S = "+str(Zsup))
    if(nocolas == 2):
        pdf.text(x = 30,y = 85, txt = "Ho: x² >= "+ str(varp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: x² < "+ str(varp)+".")
        pdf.text(x = 30,y = 230, txt = "Área de no rechazo: a la derecha del valor de x²crítico = "+str(Zinf))
        pdf.text(x = 30,y = 235, txt = "Área de rechazo: a la izquierda de x²critico = "+str(Zinf))
    if(nocolas == 3):
        pdf.text(x = 30,y = 85, txt = "Ho: x² <= "+ str(varp)+".")
        pdf.text(x = 30,y = 90, txt = "Ho: x² > "+ str(varp)+".")
        pdf.text(x = 30,y = 230, txt = "Área de no rechazo: a la izquierda del valor de x²crítico = "+str(Zsup))
        pdf.text(x = 30,y = 240, txt = "Área de rechazo: a la derecha de x²critico = "+str(Zsup))
    pdf.text(x = 30,y = 95, txt = 'Paso 2: Nivel de significancia alpha.')
    pdf.text(x = 30,y = 100, txt = "alpha = "+str(alfa)+" = "+alpha2+"%")
    pdf.text(x = 30,y = 105, txt = 'Paso 3: estadístico de prueba.')
    pdf.image('img/Estadistico_chicuadrado.png',x = 30,y = 110,w = 45, h = 20)


    #IMAGEN
    pdf.image('img/logotipo-cunori-transparente.png',x = 27,y = 29,w = 33, h = 33)

    '''#-------------------------------------------------PAGINA 2------------------------------------------------'''
    pdf.add_page()
    #RECTA
    pdf.rect(x = 25,y = 25,w = 165,h = 245)
    pdf.text(x = 195,y = 15, txt = '2')
    pdf.text(x = 30,y = 35, txt = 'Paso 5: prueba del estadístico.')
    pdf.image('img/Estadistico_chicuadrado.png',x = 30,y = 40,w = 40, h = 20)
    pdf.text(x = 70,y = 50, txt = " = ("+str(n)+" - 1)("+str(varm)+")/("+str(varp)+") = "+str(x2)+".")
    pdf.text(x = 30,y = 170, txt = 'Paso 6: respuestas.')
    if(nocolas == 1):
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        if(x2>Zinf and x2<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que X²p = "+str(x2)+" se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "X²crítico ("+str(Zinf)+", "+str(Zsup)+"), no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que X²p = "+str(x2)+" no se encuentra entre los valores de")
            pdf.text(x = 30,y = 185, txt = "X²crítico ("+str(Zinf)+", "+str(Zsup)+"), se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 2):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 0.500 - p(X²p)')
        pdf.text(x = 30,y = 70, txt = "pvalor = 0.500 - p("+str(x2)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        if(x2>Zinf):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que X²p = "+str(x2)+" es mayor que X²crítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que X²p = "+str(x2)+" es menor que X²crítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
    if(nocolas == 3):
        pdf.text(x = 30,y = 65, txt = 'pvalor = 0.500 - p(X²p)')
        pdf.text(x = 30,y = 70, txt = "pvalor = 0.500 - p("+str(x2)+")")
        pdf.text(x = 30,y = 75, txt = "pvalor = "+str(pvalor))
        if(x2<Zsup):
            pdf.text(x = 30,y = 175, txt = '1. No se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que X²p = "+str(x2)+" es menor que X²crítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "no se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" > alpha = "+str(alfa)+", no se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")
        else:
            pdf.text(x = 30,y = 175, txt = '1. Se rechaza la hipótesis nula Ho.')
            pdf.text(x = 30,y = 180, txt = "2. Debido a que X²p = "+str(x2)+" es mayor que X²crítico = "+str(Zinf))
            pdf.text(x = 30,y = 185, txt = "se rechaza la hipótesis nula Ho.")
            pdf.text(x = 30,y = 190, txt = "3. Ya que el pvalor = "+str(pvalor)+" < alpha = "+str(alfa)+", se rechaza la")
            pdf.text(x = 30,y = 195, txt = "hipótesis nula Ho.")
            pdf.text(x = 30,y = 200, txt = "4. Interprete.")

    pdf.image('img/grafica2.jpg',x = 40,y = 80,w = 130, h = 80)
    archivo = filedialog.asksaveasfilename()
    print(archivo)
    pdf.output(archivo+".pdf")
    mb.showinfo("Guardado", "El PDF se guardó correctamente en la ruta designada")