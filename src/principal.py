from tkinter import *
from fractions import *
import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.stats import norm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()

root.title("Prueba de hipótesis")

root.resizable(0,0)

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 600
hventana = 820

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
root.config(bg="gray")
frame = Frame(root)
frame.pack()

frame.config(bg="#2874A6")

frame.config(cursor="cross")
frame.config(relief="groove")
frame.config(bd=30)

lbl1 = Label(frame, text="Seleccione el estadístico de prueba a utilizar:",
             font=("Bold",18), bg="#2874A6", foreground="white").grid(row=0)

def curvanormal(nocolas, alfa, mp, mm, n, desvest):
      vcn = Toplevel()
      vcn.title("Curva normal")
      vcn.resizable(1,0)
      vcn.config(bg="#2E4053")

      hvcn = 950
      wvcn = 1475

      pwidthvcn = round(wtotal/2-wvcn/2)
      pheightvcn = 12

      vcn.geometry(str(wvcn)+"x"+str(hvcn)+"+"+str(pwidthvcn)+"+"+str(pheightvcn))

      alpha = alfa
      # Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
      x = np.arange(-4, 4, 0.1)
      # Crear la distribución normal
      y = norm.pdf(x, 0, 1)
      # Graficar la distribución normal
      fig, ax = plt.subplots()
      ax.plot(x, y)
      # Graficar la línea vertical
      ax.axvline(0, color='black', linewidth = 1)

      if(nocolas == 1):
            # Hipotesis
            h0 = "Ho: μ = "+str(mp)
            h1 = "H1: μ ≠ "+str(mp)
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha/2),4)
            z_critico_superior = round(norm.ppf(1-alpha/2),4)
            # Sombrar el área izquierda debajo de la curva
            plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zc Inferior = {}".format(z_critico_inferior))
            # Sombrar el área derecha debajo de la curva
            plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zc Superior = {}".format(z_critico_superior))
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: entre los valores de Zcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+")"
            ar = "Área de rechazo: a la izquierda de Zc1 = "+str(z_critico_inferior)+" y a la derecha \nde Zc2 = "+str(z_critico_superior)
            # formula pvalor
            pval = "pvalor = 2(0.500 - p(Zp))"
      if(nocolas == 2):
            # Hipotesis
            h0 = "Ho: μ >= "+str(mp)
            h1 = "H1: μ < "+str(mp)
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha),4)
            # Sombrar el área izquierda debajo de la curva
            plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zc Inferior = {}".format(z_critico_inferior))
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(z_critico_inferior)
            ar = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(z_critico_inferior)
            # formula pvalor
            pval = "pvalor = 0.500 - p(Zp)"
      if(nocolas == 3):
            # Hipotesis
            h0 = "Ho: μ <= "+str(mp)
            h1 = "H1: μ > "+str(mp)
            # Calculo valores críticos de Z
            z_critico_superior = round(norm.ppf(1-alpha),4)
            # Sombrar el área derecha debajo de la curva
            plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zc Superior = {}".format(z_critico_superior))
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(z_critico_superior)
            ar = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(z_critico_superior)
            # formula pvalor
            pval = "pvalor = 0.500 - p(Zp)"
      # Graficar la línea vertical
      zp = round((mm - mp)/(desvest/sqrt(n)),4)
      ax.axvline(x=zp, color='red', label = "Zp = {}".format(zp))
      
      plt.legend()
      plt.xlabel('Valores x')
      plt.ylabel('Densidad de probabilidad')
      plt.title('Distribución normal estándar')

      #Diseño de GUI
      Label(vcn, text="Paso 1: Formulación de hipótesis",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=5)
      Label(vcn, text=h0,
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=40)
      Label(vcn, text=h1,
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=70)
      Label(vcn, text="Paso 2: Nivel de significancia α",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=105)
      Label(vcn, text="α = "+str(alpha)+" = "+str(alpha*100)+"%",
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=140)
      Label(vcn, text="Paso 3: Estadístico de prueba",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=175)
      Label(vcn, text= "Z = X̅ - μ / ( σ / raíz(n) )",
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=210)
      Label(vcn, text= "Paso 4: regla de decisión",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=245)
      canvas = FigureCanvasTkAgg(fig, master=vcn)
      canvas.draw()
	# placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=15,y=285)
      Label(vcn, text= anr,
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=780)
      Label(vcn, text= ar,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=35, y=815)
      # Segunda parte de la GUI
      Label(vcn, text= "Paso 5: Prueba del estadístico",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=5)
      Label(vcn, text= "Z = X̅ - μ / ( σ / raíz(n) ) = "+str(mm)+" - "+str(mp)+" / ( "+str(desvest)+" / raíz("+str(n)+") )",
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=40)
      Label(vcn, text= "Z = "+str(zp),
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=70)
      Label(vcn, text= pval,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=100)
      Label(vcn, text= "pvalor = ",
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=130)
      canvas = FigureCanvasTkAgg(fig, master=vcn)
      canvas.draw()
	# placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=795,y=170)
      Label(vcn, text= "Paso 6: Respuestas",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=665)
      if(nocolas == 1):
           if(zp>z_critico_inferior and zp<z_critico_superior):
                r1 = "No se rechaza la Hipótesis nula H0"
                r2 = "No se rechaza la Hipótesis nula H0, ya que Zp = "+str(zp)+" se \nencuentra entre los valores de Zcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+")"
                r3 = "No se rechaza la Hipótesis nula H0, ya que el \npvalor = "+" > α = "+str(alpha)
           else:
                r1 = "Se rechaza la Hipótesis nula H0"
                r2 = "Se rechaza la Hipótesis nula H0, ya que Zp = "+str(zp)+" no se \nencuentra entre los valores de Zcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+")"
                r3 = "Se rechaza la Hipótesis nula H0, ya que el \npvalor = "+" < α = "+str(alpha)
      if(nocolas == 2):
           if(zp>z_critico_inferior):
                r1 = "No se rechaza la Hipótesis nula H0"
                r2 = "No se rechaza la Hipótesis nula H0, ya que Zp = "+str(zp)+" es \nmayor que Zcrítico = "+str(z_critico_inferior)
                r3 = "No se rechaza la Hipótesis nula H0, ya que el \npvalor = "+" > α = "+str(alpha)
           else:
                r1 = "Se rechaza la Hipótesis nula H0"
                r2 = "Se rechaza la Hipótesis nula H0, ya que Zp = "+str(zp)+" es \nmenor que Zcrítico = "+str(z_critico_inferior)
                r3 = "Se rechaza la Hipótesis nula H0, ya que el \npvalor = "+" < α = "+str(alpha)
      if(nocolas == 3):
           if(zp<z_critico_superior):
                r1 = "No se rechaza la Hipótesis nula H0"
                r2 = "No se rechaza la Hipótesis nula H0, ya que Zp = "+str(zp)+" es \nmenor que Zcrítico = "+str(z_critico_superior)
                r3 = "No se rechaza la Hipótesis nula H0, ya que el \npvalor = "+" > α = "+str(alpha)
           else:
                r1 = "Se rechaza la Hipótesis nula H0"
                r2 = "Se rechaza la Hipótesis nula H0, ya que Zp = "+str(zp)+" es \nmayor que Zcrítico = "+str(z_critico_superior)
                r3 = "Se rechaza la Hipótesis nula H0, ya que el \npvalor = "+" < α = "+str(alpha)
      Label(vcn, text= "1. "+r1,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=695)
      Label(vcn, text= "2. "+r2,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=725)
      Label(vcn, text= "3. "+r3,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=780)
      Button(vcn, text="Guardar PDF",font=("bold", 15), bg="#424949",
           foreground="white", command="").place(x=1075, y=870)

def wcn():
    
    # Crear una ventana secundaria.
    vcn = Toplevel()
    vcn.title("Curva normal")
    vcn.resizable(1,0)
    vcn.config(bg="#2E4053")

    hvcn = 500
    wvcn = 610

    pwidthvcn = round(wtotal/2-wvcn/2)
    pheightvcn = round(htotal/2-hvcn/2)

    vcn.geometry(str(wvcn)+"x"+str(hvcn)+"+"+str(pwidthvcn)+"+"+str(pheightvcn))
    lbl1 = Label(vcn, text="Ingrese la información necesaria para realizar la prueba de hipótesis:",
                 font=("bold", 15), bg="#2E4053",foreground="white").place(x=0, y=5)
    
    Label(vcn, text="Seleccione el número de colas:",
                 font=("bold", 15), bg="#2E4053", foreground="white").place(x=0, y=45)
    
    c = IntVar()
    c.set(1)
    
    Radiobutton(vcn,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=50, y=100)

    Radiobutton(vcn,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=190,y=100)
    
    Radiobutton(vcn,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=405, y=100)
    
    Label(vcn, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
    alfa.set(0.05)
    Entry(vcn, font=("bold", 15), bg="#154360", foreground="white", textvariable=alfa, 
          width=8).place(x= 325, y=165)
    
    Label(vcn, text="Media muestral X̅:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=215)
    medm = DoubleVar()
    Entry(vcn, font=("bold", 15), bg="#154360", foreground="white", textvariable=medm, 
          width=8).place(x= 325, y=215)
    
    Label(vcn, text="Media poblacional μ:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=265)
    medp = DoubleVar()
    Entry(vcn, font=("bold", 15), bg="#154360", foreground="white", textvariable=medp, 
          width=8).place(x= 325, y=265)
    
    Label(vcn, text="Desviación estándar poblacional σ:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=315)
    dep = DoubleVar()
    Entry(vcn, font=("bold", 15), bg="#154360", foreground="white", textvariable=dep, 
          width=8).place(x= 325, y=315)
    
    Label(vcn, text="Muestra n:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=365)
    mstra = IntVar()
    Entry(vcn, font=("bold", 15), bg="#154360", foreground="white", textvariable=mstra, 
          width=8).place(x= 325, y=365)
    
    Button(vcn, text="Volver",font=("bold", 15), bg="#424949",
           foreground="white", command=vcn.destroy).place(x=175, y=425)
    
    Button(vcn, text="Evaluar",font=("bold", 15), bg="#424949",
           foreground="white", command= lambda: curvanormal(c.get(), alfa.get(), medp.get(), medm.get(), mstra.get(), dep.get())).place(x=350, y=425)
    
btn1 = Button(frame, text="Curva normal \"Z\"", width=38,
              height=6, font=("bold", 18), bg="#707B7C",foreground="white", anchor="center", command=wcn).grid(row="1")
#lambda:curvanormal(1,0.05,5,5,5,5)

def wts():
    # Crear una ventana secundaria.
    vts = Toplevel()
    vts.title("T student")
    vts.resizable(1,0)
    vts.config(bg="#2E4053")

    hvts = 500
    wvts = 610

    pwidthvts = round(wtotal/2-wvts/2)
    pheightvts = round(htotal/2-hvts/2)

    vts.geometry(str(wvts)+"x"+str(hvts)+"+"+str(pwidthvts)+"+"+str(pheightvts))
    lbl1 = Label(vts, text="Ingrese la información necesaria para realizar la prueba de hipótesis:",
                 font=("bold", 15), bg="#2E4053",foreground="white").place(x=0, y=5)
    
    Label(vts, text="Seleccione el número de colas:",
                 font=("bold", 15), bg="#2E4053", foreground="white").place(x=0, y=45)
    
    c = IntVar()
    c.set(1)
    
    Radiobutton(vts,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=50, y=100)

    Radiobutton(vts,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=190,y=100)
    
    Radiobutton(vts,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=405, y=100)
    
    Label(vts, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
    alfa.set(0.05)

    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=alfa, 
          width=8).place(x= 325, y=165)
    
    Label(vts, text="Media muestral X̅:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=215)
    medm = DoubleVar()
    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=medm, 
          width=8).place(x= 325, y=215)
    
    Label(vts, text="Media poblacional μ:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=265)
    medp = DoubleVar()
    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=medp, 
          width=8).place(x= 325, y=265)
    
    Label(vts, text="Desviación estándar muestral s:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=315)
    dep = DoubleVar()
    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=dep, 
          width=8).place(x= 325, y=315)
    
    Label(vts, text="Muestra n:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=365)
    mstra = IntVar()
    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=mstra, 
          width=8).place(x= 325, y=365)
    
    Button(vts, text="Volver",font=("bold", 15), bg="#424949",
           foreground="white", command=vts.destroy).place(x=175, y=425)
    
    Button(vts, text="Evaluar",font=("bold", 15), bg="#424949",
           foreground="white", command="").place(x=350, y=425)
    

btn2 = Button(frame, text="T student \"t\"", width=38,
              height=6, font=("bold", 18), bg="#F39C12",foreground="white", anchor="center", command=wts).grid(row="2")

def prr(val):
    #float(Fraction(prm.get()))  así se deben obtener los datos desde las proporciones en fracción
    #q.set(round(1-prp.get(), 3))  así se debe obtener el Q
    print(val)

def wpm():
    # Crear una ventana secundaria.
    vpm = Toplevel()
    vpm.title("Proporciones muestrales")
    vpm.resizable(1,0)
    vpm.config(bg="#2E4053")

    hvpm= 500
    wvpm = 610

    pwidthvpm = round(wtotal/2-wvpm/2)
    pheightvpm = round(htotal/2-hvpm/2)

    vpm.geometry(str(wvpm)+"x"+str(hvpm)+"+"+str(pwidthvpm)+"+"+str(pheightvpm))
    lbl1 = Label(vpm, text="Ingrese la información necesaria para realizar la prueba de hipótesis:",
                 font=("bold", 15), bg="#2E4053",foreground="white").place(x=0, y=5)
    
    Label(vpm, text="Seleccione el número de colas:",
                 font=("bold", 15), bg="#2E4053", foreground="white").place(x=0, y=45)
    
    c = IntVar()
    c.set(1)
    Radiobutton(vpm,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=50, y=100)

    Radiobutton(vpm,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=190,y=100)
    
    Radiobutton(vpm,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=405, y=100)
    
    Label(vpm, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
    alfa.set(0.05)
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=alfa, 
          width=8).place(x= 325, y=165)
    
    Label(vpm, text="Proporción muestral p:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=215)
    propm = StringVar()
    propm.set("0.0")
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=propm, 
          width=8).place(x= 325, y=215)
    
    Label(vpm, text="Proporción poblacional P:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=265)
    propp = DoubleVar()
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=propp, 
          width=8).place(x= 325, y=265)
    
    Label(vpm, text="Q = 1 - P:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=315)
    q = DoubleVar()
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=q, 
          width=8, state="disabled", disabledbackground="#154360").place(x= 325, y=315)
    
    Label(vpm, text="Muestra n:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=365)
    mstra = IntVar()
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=mstra, 
          width=8).place(x= 325, y=365)
    
    Button(vpm, text="Volver",font=("bold", 15), bg="#424949",
           foreground="white", command=vpm.destroy).place(x=175, y=425)
    
    Button(vpm, text="Evaluar",font=("bold", 15), bg="#424949",
           foreground="white", command="").place(x=350, y=425)

btn3 = Button(frame, text="Proporciones muestrales \"p\"", width=38,
              height=6, font=("bold", 18), bg="#212F3D", foreground="white",anchor="center", command=wpm).grid(row="3")

def wcc():
    # Crear una ventana secundaria.
    vcc = Toplevel()
    vcc.title("Chi cuadrado")
    vcc.resizable(1,0)
    vcc.config(bg="#2E4053")

    hvcc = 450
    wvcc = 610

    pwidthvcc = round(wtotal/2-wvcc/2)
    pheightvcc = round(htotal/2-hvcc/2)

    vcc.geometry(str(wvcc)+"x"+str(hvcc)+"+"+str(pwidthvcc)+"+"+str(pheightvcc))
    lbl1 = Label(vcc, text="Ingrese la información necesaria para realizar la prueba de hipótesis:",
                 font=("bold", 15), bg="#2E4053",foreground="white").place(x=0, y=5)
    
    Label(vcc, text="Seleccione el número de colas:",
                 font=("bold", 15), bg="#2E4053", foreground="white").place(x=0, y=45)
    
    c = IntVar()
    c.set(1)
    Radiobutton(vcc,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=50, y=100)

    Radiobutton(vcc,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=190,y=100)
    
    Radiobutton(vcc,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9").place(x=405, y=100)
    
    Label(vcc, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
    alfa.set(0.05)
    Entry(vcc, font=("bold", 15), bg="#154360", foreground="white", textvariable=alfa, 
          width=8).place(x= 325, y=165)
    
    Label(vcc, text="Muestra n:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=215)
    mstra = IntVar()
    Entry(vcc, font=("bold", 15), bg="#154360", foreground="white", textvariable=mstra, 
          width=8).place(x= 325, y=215)
    
    Label(vcc, text="Desviación estándar muestral s:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=265)
    dep = DoubleVar()
    Entry(vcc, font=("bold", 15), bg="#154360", foreground="white", textvariable=dep, 
          width=8).place(x= 325, y=265)
    
    Label(vcc, text="Desviación estándar poblacional μ:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=315)
    dem = DoubleVar()
    Entry(vcc, font=("bold", 15), bg="#154360", foreground="white", textvariable=dem, 
          width=8).place(x= 325, y=315)
    
    Button(vcc, text="Volver",font=("bold", 15), bg="#424949",
           foreground="white", command=vcc.destroy).place(x=175, y=375)
    
    Button(vcc, text="Evaluar",font=("bold", 15), bg="#424949",
           foreground="white", command="").place(x=350, y=375)

btn4 = Button(frame, text="Chi cuadrado \"X^2\"", width=38,
              height=6, font=("bold", 18), bg="#27AE60",foreground="white", anchor="center", command=wcc).grid(row="4")

frame.pack(
    fill="both",
    expand="1"
)
root.quit()
root.mainloop()