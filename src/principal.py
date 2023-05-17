from tkinter import *
from fractions import *
import matplotlib.pyplot as plt
import numpy as np
from math import *
from scipy.stats import norm, t, chi2
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pruebaPDF
from tkinter import messagebox as mb
import webbrowser
from tkinter import ttk

root = Tk()

root.title("Prueba de hipótesis")

root.resizable(0,0)

wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 600
hventana = 680

#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = 15

#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
root.config(bg="gray")
frame = Frame(root)
frame.pack()

frame.config(bg="#2874A6")

#frame.config(cursor="cross")
frame.config(relief="groove")
frame.config(bd=30)

lbl1 = Label(frame, text="Seleccione el estadístico de prueba a utilizar:",
             font=("Bold",18), bg="#2874A6", foreground="white").grid(row=0)

def graphcn(nocolas, alfa, mp, mm, n, desvest, redline):
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
      # calculo del zprueba
      zp = round((mm - mp)/(desvest/sqrt(n)),4)

      if(nocolas == 1):
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha/2),4)
            z_critico_superior = round(norm.ppf(1-alpha/2),4)
            # Sombrar el área izquierda debajo de la curva
            plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zc Inferior = {}".format(z_critico_inferior))
            # Sombrar el área derecha debajo de la curva
            plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zc Superior = {}".format(z_critico_superior))
      if(nocolas == 2):
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha),4)
            # Sombrar el área izquierda debajo de la curva
            plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zcrítico = {}".format(z_critico_inferior))
      if(nocolas == 3):
            # Calculo valores críticos de Z
            z_critico_superior = round(norm.ppf(1-alpha),4)
            # Sombrar el área derecha debajo de la curva
            plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zcrítico = {}".format(z_critico_superior))
    
      # Graficar la línea vertical
      if(redline == 1):
            ax.axvline(x=zp, color='red', label = "Zp = {}".format(zp))
            plt.savefig('img/grafica2.jpg')
      else:
           plt.savefig('img/grafica.jpg')
      
      plt.legend()
      plt.xlabel('Valores Z')
      plt.ylabel('Densidad de probabilidad')
      plt.title('Distribución normal estándar')
     
      return fig
     
def curvanormal(nocolas, alfa, mp, mm, n, desvest):
      vcn = Toplevel()
      vcn.title("Curva normal")
      vcn.resizable(0,0)
      vcn.config(bg="#2E4053")

      hvcn = 860
      wvcn = 1475

      pwidthvcn = round(wtotal/2-wvcn/2)
      pheightvcn = 15

      vcn.geometry(str(wvcn)+"x"+str(hvcn)+"+"+str(pwidthvcn)+"+"+str(pheightvcn))

      alpha = alfa
      zp = round((mm - mp)/(desvest/sqrt(n)),4)
      pvalor = round(norm.sf(abs (zp)),4)
      if(nocolas == 1):
            # Hipotesis
            h0 = "Ho: μ = "+str(mp)+"."
            h1 = "H1: μ ≠ "+str(mp)+"."
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha/2),4)
            z_critico_superior = round(norm.ppf(1-alpha/2),4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: entre los valores de Zcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+")."
            ar = "Área de rechazo: a la izquierda de ZcI = "+str(z_critico_inferior)+" y a la derecha \nde ZcS = "+str(z_critico_superior)+"."
            # formula pvalor
            pval = "pvalor = 2[0.500 - p(Zp)]."
            pval2 = " = 2[0.500 - p("+str(zp)+")]."
            # calculo pvalor
            pvalor = round(pvalor*2,4)
            if(zp>z_critico_inferior and zp<z_critico_superior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" se encuentra entre los valores de \nZcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+"), no se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la Hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" no se encuentra entre los valores de \nZcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+"), se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 2):
            # Hipotesis
            h0 = "Ho: μ >= "+str(mp)+"."
            h1 = "H1: μ < "+str(mp)+"."
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha),4)
            z_critico_superior = 0
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(z_critico_inferior)+"."
            ar = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(z_critico_inferior)+"."
            # formula pvalor
            pval = "pvalor = 0.500 - p(Zp)."
            pval2 = " = 0.500 - p("+str(zp)+")."
            if(zp>z_critico_inferior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(z_critico_inferior)+", \nno se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a ya que Zp = "+str(zp)+" es menor que Zcrítico = "+str(z_critico_inferior)+", \nse rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 3):
            # Hipotesis
            h0 = "Ho: μ <= "+str(mp)+"."
            h1 = "H1: μ > "+str(mp)+"."
            # Calculo valores críticos de Z
            z_critico_inferior = 0
            z_critico_superior = round(norm.ppf(1-alpha),4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(z_critico_superior)+"."
            ar = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(z_critico_superior)+"."
            # formula pvalor
            pval = "pvalor = 0.500 - p(Zp)."
            pval2 = " = 0.500 - p("+str(zp)+")."
            if(zp<z_critico_superior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(z_critico_superior)+", \nno se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(z_critico_superior)+", \nse rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."

      #Diseño de GUI
      Label(vcn, text="Paso 1: formulación de hipótesis.",
                  font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=5)
      Label(vcn, text=h0,
                  font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=40)
      Label(vcn, text=h1,
                  font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=70)
      Label(vcn, text="Paso 2: nivel de significancia α.",
                  font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=105)
      Label(vcn, text="α = "+str(alpha)+" = "+str(round(alpha*100,2))+"%.",
                  font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=140)
      Label(vcn, text="Paso 3: estadístico de prueba.",
                  font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=175)
      #Label(vcn, text= "Z = X̅ - μ / ( σ / raíz(n) )",
      #            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=210)
      global imagen
      imagen = PhotoImage(file="./img/curvanormal_func.png")
      Label(vcn, image=imagen).place(x=275,y=210)
      Label(vcn, text= "Paso 4: regla de decisión.",
                  font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=305)
      fig = graphcn(nocolas, alfa, mp, mm, n, desvest, 0)
      canvas = FigureCanvasTkAgg(fig, master=vcn)
      canvas.draw()
      # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=35,y=340, width=600, height=400)
      Label(vcn, text= anr,
                  font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=750)
      Label(vcn, text= ar,
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=35, y=785)
      # Segunda parte de la GUI
      Label(vcn, text= "Paso 5: prueba del estadístico.",
                  font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=5)
      Label(vcn, text= "Z = X̅ - μ / ( σ / raíz(n) ) = "+str(mm)+" - "+str(mp)+" / ( "+str(desvest)+" / raíz("+str(n)+") ).",
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=40)
      Label(vcn, text= "Zprueba = Zp = "+str(zp)+".",
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=70)
      Label(vcn, text= pval+pval2,
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=100)
      Label(vcn, text= "pvalor = "+str(pvalor)+".",
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=130)
      fig2 = graphcn(nocolas, alfa, mp, mm, n, desvest, 1)
      canvas = FigureCanvasTkAgg(fig2, master=vcn)
      canvas.draw()
            # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=815,y=170, width=600, height=400)
      Label(vcn, text= "Paso 6: respuestas.",
                  font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=575)
      Label(vcn, text= "1. "+r1,
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=605)
      Label(vcn, text= "2. "+r2,
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=635)
      Label(vcn, text= "3. "+r3,
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=690)
      Label(vcn, text= "4. Interprete.",
                  font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=745)
      Button(vcn, text="Guardar PDF",font=("bold", 15), bg="#424949",
            foreground="white", command=lambda:[pruebaPDF.curvanormal(nocolas, alfa, mp, mm, n, desvest,z_critico_inferior,z_critico_superior,zp,pvalor)]).place(x=1075, y=795)
     
def wcn():
      # Crear una ventana secundaria.
      vcn = Toplevel()
      vcn.title("Curva normal")
      vcn.resizable(0,0)
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
      
      def limpiartexto():
            c.set(1)
            alfa.set(0.05)
            medp.set(0.0)
            medm.set(0.0)
            mstra.set(0)
            dep.set(0.0)
      Button(vcn, text="Evaluar",font=("bold", 15), bg="#424949",
                  foreground="white", command= lambda: [curvanormal(c.get(), alfa.get(), medp.get(), medm.get(), mstra.get(), dep.get()), vcn.destroy()]).place(x=350, y=425)
    
btn1 = Button(frame, text="Curva normal estándar - Z", width=38,
            height=4, font=("bold", 18), bg="#76448A",foreground="white", anchor="center", command=wcn).grid(row="1")

def graphtst(nocolas, alfa, mp, mm, n, desvest, redline):
    alpha = alfa
    gl = n-1
    # Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
    x = np.arange(-4, 4, 0.1)
    
    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Graficar la función de densidad de probabilidad
    ax.plot(x, t.pdf(x, gl), 'blue')

    # Graficar la línea vertical
    ax.axvline(x=0, color='black', linewidth = 1)

    #calculo tprueba
    tp = round((mm - mp)/(desvest/sqrt(n)),4)

    if(nocolas == 1):
        # Calculo valores críticos de Z
        t_critico_inferior = round(t.ppf(alpha/2, gl),4)
        t_critico_superior = round(t.ppf(1 - (alpha/2), gl),4)
        # Sombrar el área izquierda debajo de la curva
        plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_critico_inferior, color='blue', alpha=0.3, label = "tc Inferior = {}".format(t_critico_inferior))
        # Sombrar el área derecha debajo de la curva
        plt.fill_between(x, 0, t.pdf(x, gl), where=x>=t_critico_superior, color='blue', alpha=0.3, label = "tc Superior = {}".format(t_critico_superior))
    if(nocolas == 2):
        # Calculo valores críticos de Z
        t_critico_inferior = round(t.ppf(alpha, gl),4)
        # Sombrar el área izquierda debajo de la curva
        plt.fill_between(x, 0, t.pdf(x, gl), where=x<=t_critico_inferior, color='blue', alpha=0.3, label = "tcrítico = {}".format(t_critico_inferior))
    if(nocolas == 3):
        # Calculo valores críticos de Z
        t_critico_superior = round(t.ppf(1 - (alpha), gl),4)
        # Sombrar el área derecha debajo de la curva
        plt.fill_between(x, 0, t.pdf(x, gl), where=x>=t_critico_superior, color='blue', alpha=0.3, label = "tcrítico = {}".format(t_critico_superior))

    # Graficar la línea vertical
    if(redline == 1):
        ax.axvline(x=tp, color='red', label = "tp = {}".format(tp))
        plt.savefig('img/grafica2.jpg')
    else:
        plt.savefig('img/grafica.jpg')
      
    plt.legend()
    plt.xlabel('Valores t')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución t Student')

    return fig

def tstudent(nocolas, alfa, mp, mm, n, desvest):
      vts = Toplevel()
      vts.title("t Student")
      vts.resizable(0,0)
      vts.config(bg="#2E4053")

      hvts = 875
      wvts = 1475

      pwidthvts = round(wtotal/2-wvts/2)
      pheightvts = 15

      vts.geometry(str(wvts)+"x"+str(hvts)+"+"+str(pwidthvts)+"+"+str(pheightvts))

      alpha = alfa
      gl = n-1

      #calculo tprueba
      tp = round((mm - mp)/(desvest/sqrt(n)),4)
      pvalor = round(t.sf(abs (tp), gl),4)

      if(nocolas == 1):
            # Hipotesis
            h0 = "Ho: μ = "+str(mp)+"."
            h1 = "H1: μ ≠ "+str(mp)+"."
            # Calculo valores críticos de t
            t_critico_inferior = round(t.ppf(alpha/2, gl),4)
            t_critico_superior = round(t.ppf(1 - (alpha/2), gl),4)
            # calculo pvalor
            pvalor = round(t.sf(abs (tp), gl)*2 ,4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: entre los valores de tcrítico ("+str(t_critico_inferior)+", "+str(t_critico_superior)+")."
            ar = "Área de rechazo: a la izquierda de tcI = "+str(t_critico_inferior)+" y a la derecha \nde tcS = "+str(t_critico_superior)+"."
            if(tp>t_critico_inferior and tp<t_critico_superior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que tp = "+str(tp)+" se encuentra entre los valores de \ntcrítico ("+str(t_critico_inferior)+", "+str(t_critico_superior)+"), no se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza \nla hipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que tp = "+str(tp)+" no se encuentra entre los valores de \ntcrítico ("+str(t_critico_inferior)+", "+str(t_critico_superior)+"), se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 2):
            # Hipotesis
            h0 = "Ho: μ >= "+str(mp)+"."
            h1 = "H1: μ < "+str(mp)+"."
            # Calculo valores críticos de Z
            t_critico_inferior = round(t.ppf(alpha, gl),4)
            t_critico_superior = 0
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la derecha del valor de tcrítico = "+str(t_critico_inferior)+"."
            ar = "Área de no rechazo: a la izquierda del valor de tcrítico = "+str(t_critico_inferior)+"."
            if(tp>t_critico_inferior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que tp = "+str(tp)+" es mayor que tcrítico = "+str(t_critico_inferior)+", \nno se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que tp = "+str(tp)+" es menor que tcrítico = "+str(t_critico_inferior)+", \nse rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 3):
            # Hipotesis
            h0 = "Ho: μ <= "+str(mp)+"."
            h1 = "H1: μ > "+str(mp)+"."
            # Calculo valores críticos de Z
            t_critico_inferior = 0
            t_critico_superior = round(t.ppf(1 - (alpha), gl),4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la izquierda del valor de tcrítico = "+str(t_critico_superior)+"."
            ar = "Área de no rechazo: a la derecha del valor de tcrítico = "+str(t_critico_superior)+"."
            if(tp<t_critico_superior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que tp = "+str(tp)+" es menor que tcrítico = "+str(t_critico_superior)+", \nno se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que tp = "+str(tp)+" es mayor que tcrítico = "+str(t_critico_superior)+", \nse rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
            
      #Diseño de GUI
      Label(vts, text="Paso 1: formulación de hipótesis.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=5)
      Label(vts, text=h0,
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=40)
      Label(vts, text=h1,
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=70)
      Label(vts, text="Paso 2: nivel de significancia α.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=105)
      Label(vts, text="α = "+str(alpha)+" = "+str(round(alpha*100,2))+"%",
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=140)
      Label(vts, text="Paso 3: estadístico de prueba.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=175)
      #Label(vts, text= "t = X̅ - μ / ( s / raíz(n) )",
      #      font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=210)
      global imagen
      imagen = PhotoImage(file="./img/tstudent_func.png")
      Label(vts, image=imagen).place(x=275,y=210)
      Label(vts, text= "Paso 4: regla de decisión.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=300)
      Label(vts, text="Grados de libertad g.l. = muestra(n) - 1 = "+str(n)+" - 1 = "+str(n-1)+".",
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=330)
      fig = graphtst(nocolas, alfa, mp, mm, n, desvest, 0)
      canvas = FigureCanvasTkAgg(fig, master=vts)
      canvas.draw()
      # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=35,y=365, width=600, height=400)
      Label(vts, text= anr,
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=775)
      Label(vts, text= ar,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=35, y=810)
      # Segunda parte de la GUI
      Label(vts, text= "Paso 5: prueba del estadístico.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=5)
      Label(vts, text= "t = X̅ - μ / ( s / raíz(n) ) = "+str(mm)+" - "+str(mp)+" / ( "+str(desvest)+" / raíz("+str(n)+") ).",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=40)
      Label(vts, text= "tprueba = tp = "+str(tp)+".",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=70)
      Label(vts, text= "pvalor = "+str(pvalor)+".",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=100)
      #Label(vts, text= "",
      #      font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=130)
      fig2 = graphtst(nocolas, alfa, mp, mm, n, desvest, 1)
      canvas = FigureCanvasTkAgg(fig2, master=vts)
      canvas.draw()
            # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=815,y=135, width=600, height=400)
      Label(vts, text= "Paso 6: respuestas.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=545)
      Label(vts, text= "1. "+r1,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=580)
      Label(vts, text= "2. "+r2,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=615)
      Label(vts, text= "3. "+r3,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=670)
      Label(vts, text= "4. Interprete.",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=725)
      Button(vts, text="Guardar PDF",font=("bold", 15), bg="#424949",
            foreground="white", command=lambda:[pruebaPDF.tstudent(nocolas, alfa, mp, mm, n, desvest,t_critico_inferior,t_critico_superior,tp,pvalor)]).place(x=1075, y=775)
    
    
def wts():
    # Crear una ventana secundaria.
    vts = Toplevel()
    vts.title("t student")
    vts.resizable(0,0)
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
    dem = DoubleVar()
    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=dem, 
          width=8).place(x= 325, y=315)
    
    Label(vts, text="Muestra n:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=365)
    mstra = IntVar()
    Entry(vts, font=("bold", 15), bg="#154360", foreground="white", textvariable=mstra, 
          width=8).place(x= 325, y=365)
    
    Button(vts, text="Volver",font=("bold", 15), bg="#424949",
           foreground="white", command=vts.destroy).place(x=175, y=425)
    def limpiartexto():
        c.set(1)
        alfa.set(0.05)
        medp.set(0.0)
        medm.set(0.0)
        mstra.set(0)
        dem.set(0.0)
    Button(vts, text="Evaluar",font=("bold", 15), bg="#424949",
           foreground="white", command=lambda: [tstudent(c.get(), alfa.get(), medp.get(), medm.get(), mstra.get(), dem.get()), vts.destroy()]).place(x=350, y=425)
    

btn2 = Button(frame, text="t student - t", width=38,
              height=4, font=("bold", 18), bg="#F39C12",foreground="white", anchor="center", command=wts).grid(row="2")

def graphpm(nocolas, alfa, pm, pp, n, redline):
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

    # calculo del zprueba
    q = round(1-pp,2) 
    zp = round((pm - pp)/(sqrt((pp*q)/n)),4)

    if(nocolas == 1):
        # Calculo valores críticos de Z
        z_critico_inferior = round(norm.ppf(alpha/2),4)
        z_critico_superior = round(norm.ppf(1-alpha/2),4)
        # Sombrar el área izquierda debajo de la curva
        plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zc Inferior = {}".format(z_critico_inferior))
        # Sombrar el área derecha debajo de la curva
        plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zc Superior = {}".format(z_critico_superior))
    if(nocolas == 2):
        # Calculo valores críticos de Z
        z_critico_inferior = round(norm.ppf(alpha),4)
        # Sombrar el área izquierda debajo de la curva
        plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zcrítico = {}".format(z_critico_inferior))
    
    if(nocolas == 3):
        # Calculo valores críticos de Z
        z_critico_superior = round(norm.ppf(1-alpha),4)
        # Sombrar el área derecha debajo de la curva
        plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zcrítico = {}".format(z_critico_superior))

    # Graficar la línea vertical
    if(redline == 1):
        ax.axvline(x=zp, color='red', label = "Zp = {}".format(zp))
        plt.savefig('img/grafica2.jpg')
    else:
        plt.savefig('img/grafica.jpg')
      
    plt.legend()
    plt.xlabel('Valores Z')
    plt.ylabel('Densidad de probabilidad')
    plt.title('Distribución muestral de una proporción')

    return fig

def propmuestral(nocolas, alfa, pm, pp, n):
      if(pm > 1 or pp>= 1):
         mb.showerror("Error", "El valor de la proporción muestral p y el de la proporción problacional P debe ser menor a 1.")
         return
      
      vpm = Toplevel()
      vpm.title("Proporción muestral")
      vpm.resizable(0,0)
      vpm.config(bg="#2E4053")

      hvpm = 865
      wvpm = 1475

      pwidthvpm = round(wtotal/2-wvpm/2)
      pheightvpm = 12

      vpm.geometry(str(wvpm)+"x"+str(hvpm)+"+"+str(pwidthvpm)+"+"+str(pheightvpm))

      alpha = alfa

      # Calculo del zprueba
      q = round(1-pp,2) 
      zp = round((pm - pp)/(sqrt((pp*q)/n)),4)
      pvalor = round(norm.sf(abs (zp)),4)

      if(nocolas == 1):
            # Hipotesis
            h0 = "Ho: μ = "+str(pp)+"."
            h1 = "H1: μ ≠ "+str(pp)+"."
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha/2),4)
            z_critico_superior = round(norm.ppf(1-alpha/2),4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: entre los valores de Zcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+")."
            ar = "Área de rechazo: a la izquierda de ZcI = "+str(z_critico_inferior)+" y a la derecha \nde ZcS = "+str(z_critico_superior)+"."
            # formula pvalor
            pval = "pvalor = 2[0.500 - p(Zp)]."
            pval2 = " = 2[0.500 - p("+str(zp)+")]."
            # calculo pvalor
            pvalor = round(pvalor*2,4)
            if(zp>z_critico_inferior and zp<z_critico_superior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" se encuentra entre los valores de \nZcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+"), no se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" no se encuentra entre los valores de \nZcrítico ("+str(z_critico_inferior)+", "+str(z_critico_superior)+"), se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 2):
            # Hipotesis
            h0 = "Ho: μ >= "+str(pp)+"."
            h1 = "H1: μ < "+str(pp)+"."
            # Calculo valores críticos de Z
            z_critico_inferior = round(norm.ppf(alpha),4)
            z_critico_superior = 0
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(z_critico_inferior)+"."
            ar = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(z_critico_inferior)+"."
            # formula pvalor
            pval = "pvalor = 0.500 - p(Zp)."
            pval2 = " = 0.500 - p("+str(zp)+")."
            if(zp>z_critico_inferior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(z_critico_inferior)+", \nno se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(z_critico_inferior)+", \nse rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 3):
            # Hipotesis
            h0 = "Ho: μ <= "+str(pp)+"."
            h1 = "H1: μ > "+str(pp)+"."
            # Calculo valores críticos de Z
            z_critico_inferior = 0
            z_critico_superior = round(norm.ppf(1-alpha),4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la izquierda del valor de Zcrítico = "+str(z_critico_superior)+"."
            ar = "Área de no rechazo: a la derecha del valor de Zcrítico = "+str(z_critico_superior)+"."
            # formula pvalor
            pval = "pvalor = 0.500 - p(Zp)."
            pval2 = " = 0.500 - p("+str(zp)+")."
            if(zp<z_critico_superior):
                  r1 = "No se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es menor que Zcrítico = "+str(z_critico_superior)+", \nno se rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                  r1 = "Se rechaza la hipótesis nula Ho."
                  r2 = "Debido a que Zp = "+str(zp)+" es mayor que Zcrítico = "+str(z_critico_superior)+", \nse rechaza la hipótesis nula Ho."
                  r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."

      #Diseño de GUI
      Label(vpm, text="Paso 1: formulación de hipótesis.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=5)
      Label(vpm, text=h0,
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=40)
      Label(vpm, text=h1,
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=70)
      Label(vpm, text="Paso 2: nivel de significancia α.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=105)
      Label(vpm, text="α = "+str(alpha)+" = "+str(round(alpha*100,2))+"%",
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=140)
      Label(vpm, text="Paso 3: estadístico de prueba.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=175)
      #Label(vpm, text= "Z = p - P / raíz((P * Q) / n)",
      #      font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=210)
      global imagen
      imagen = PhotoImage(file="./img/propmuestral_func.png")
      Label(vpm, image=imagen).place(x=75,y=215)
      Label(vpm, text="\"p\" = proporcion muestral = "+str(pm)+" = "+str(pm*100)+"%.",
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=225, y=210)
      Label(vpm, text="\"P\" = proporcion poblacional = "+str(pp)+" = "+str(pp*100)+"%.",
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=225, y=245)
      Label(vpm, text="\"Q\" = 1 - P = "+str(q)+" = "+str(q*100)+"%.",
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=225, y=280)
      Label(vpm, text= "Paso 4: regla de decisión.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=315)
      fig = graphpm(nocolas, alfa, pm, pp, n, 0)
      canvas = FigureCanvasTkAgg(fig, master=vpm)
      canvas.draw() 
            # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=35,y=350, width=600, height=400)
      Label(vpm, text= anr,
            font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=760)
      Label(vpm, text= ar,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=35, y=795)
      # Segunda parte de la GUI
      Label(vpm, text= "Paso 5: prueba del estadístico.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=5)
      Label(vpm, text= "Z = p - P / raíz((P * Q) / n) = "+str(pm)+" - "+str(pp)+" /  raíz(("+str(pp)+" * "+str(q)+") /"+str(n)+").",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=40)
      Label(vpm, text= "Zprueba = Zp = "+str(zp)+".",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=70)
      Label(vpm, text= pval+pval2,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=100)
      Label(vpm, text= "pvalor = "+str(pvalor)+".",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=130)
      fig2 = graphpm(nocolas, alfa, pm, pp, n, 1)
      canvas = FigureCanvasTkAgg(fig2, master=vpm)
      canvas.draw()
            # placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=815,y=170, width=600, height=400)
      Label(vpm, text= "Paso 6: respuestas.",
            font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=580)
      Label(vpm, text= "1. "+r1,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=615)
      Label(vpm, text= "2. "+r2,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=650)
      Label(vpm, text= "3. "+r3,
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=705)
      Label(vpm, text= "4. Interprete.",
            font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=760)
      Button(vpm, text="Guardar PDF",font=("bold", 15), bg="#424949",
            foreground="white", command=lambda:[pruebaPDF.propmuestral(nocolas, alfa, pm, pp, n,z_critico_inferior,z_critico_superior,q,zp,pvalor)]).place(x=1075, y=810)
    
def wpm():
    # Crear una ventana secundaria.
    vpm = Toplevel()
    vpm.title("Proporciones muestrales")
    vpm.resizable(0,0)
    vpm.config(bg="#2E4053")

    hvpm= 450
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
    propp = StringVar()
    propp.set("0.0")
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=propp, 
          width=8).place(x= 325, y=265)
    
    Label(vpm, text="Muestra n:", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=315)
    mstra = IntVar()
    Entry(vpm, font=("bold", 15), bg="#154360", foreground="white", textvariable=mstra, 
          width=8).place(x= 325, y=315)
    
    Button(vpm, text="Volver",font=("bold", 15), bg="#424949",
           foreground="white", command=vpm.destroy).place(x=175, y=375)
    def limpiartexto():
        c.set(1)
        alfa.set(0.05)
        propm.set(0.0)
        propp.set(0.0)
        mstra.set(0)
    Button(vpm, text="Evaluar",font=("bold", 15), bg="#424949",
           foreground="white", 
           command= lambda: [vpm.destroy(), propmuestral(c.get(), alfa.get(), round(float(Fraction(propm.get())),4), 
                                         round(float(Fraction(propp.get())),4), mstra.get())]).place(x=350, y=375)

btn3 = Button(frame, text="Proporciones muestrales - p", width=38,
              height=4, font=("bold", 18), bg="#212F3D", foreground="white",anchor="center", command=wpm).grid(row="3")

def graphchicuadrado(nocolas, alfa, n, varm, varp, redline):
      alpha = alfa
      gl = n-1

      # definimos el rango de valores para la variable aleatoria
      x = np.linspace(0, chi2.ppf(0.999, gl), 1000)
      # definimos la función de densidad de probabilidad de la distribución chi-cuadrado
      pdf = chi2.pdf(x, gl)
      # creamos la figura y los ejes
      fig, ax = plt.subplots()
      # graficamos la función de densidad de probabilidad
      ax.plot(x, pdf)
      # ajustamos los límites de los ejes
      ax.set_xlim([0, chi2.ppf(0.999, gl)])
      ax.set_ylim([0, max(pdf)*1.1])

      # calculo del X²prueba
      x2 = round(((n - 1)*(varm))/varp,4)

      if(nocolas == 1):
            # Calculo valores críticos de X²
            left_critical_value = round(chi2.ppf(alpha/2, gl),4)
            right_critical_value = round(chi2.ppf(1 - alpha/2, gl),4)
            # definimos los límites del área de rechazo
            left_limit = x[x <= left_critical_value]
            right_limit = x[x >= right_critical_value]
            # sombrear el área de rechazo a la derecha del valor crítico
            ax.fill_between(right_limit, 0, chi2.pdf(right_limit, gl), alpha=0.5, label="X²crítico Inferior {}".format(right_critical_value))
            # sombrear el área de rechazo a la izquierda del valor crítico
            ax.fill_between(left_limit, 0, chi2.pdf(left_limit, gl), alpha=0.5, label="X²crítico Superior {}".format(left_critical_value))     
      if(nocolas == 2):
            # Calculo valores críticos de X²
            left_critical_value = round(chi2.ppf(alpha, gl),4)
            # definimos los límites del área de rechazo
            left_limit = x[x <= left_critical_value]
            # sombrear el área de rechazo a la izquierda del valor crítico
            ax.fill_between(left_limit, 0, chi2.pdf(left_limit, gl), alpha=0.5, label="X²crítico {}".format(left_critical_value))
      if(nocolas == 3):
            # Calculo valores críticos de X²
            right_critical_value = round(chi2.ppf(1 - alpha, gl),4)
            # definimos los límites del área de rechazo
            right_limit = x[x >= right_critical_value]
            # sombrear el área de rechazo a la derecha del valor crítico
            ax.fill_between(right_limit, 0, chi2.pdf(right_limit, gl), alpha=0.5, label="X²crítico {}".format(right_critical_value))
      
      # Graficar la línea vertical
      if(redline == 1):
            ax.axvline(x=x2, color='red', label = "X²p = {}".format(x2))
            plt.savefig('img/grafica2.jpg')
      else:
            plt.savefig('img/grafica.jpg')
      
      plt.legend()
      plt.xlabel('Valores X²')
      plt.ylabel('Densidad de probabilidad')
      plt.title('Distribución Chi Cuadrado')

      return fig 

def chicuadrado(nocolas, alfa, n, varm, varp):
      vcc = Toplevel()
      vcc.title("Chi Cuadrado")
      vcc.resizable(0,0)
      vcc.config(bg="#2E4053")

      hvcc = 860
      wvcc = 1475

      pwidthvcc = round(wtotal/2-wvcc/2)
      pheightvcc = 12

      vcc.geometry(str(wvcc)+"x"+str(hvcc)+"+"+str(pwidthvcc)+"+"+str(pheightvcc))

      alpha = alfa
      gl = n-1

      # calculo del X²prueba
      x2 = round(((n - 1)*(varm))/varp,4)
      # calculo pvalor
      pvalor = round(chi2.sf(abs (x2),gl),4)

      if(nocolas == 1):
            # Hipotesis
            h0 = "Ho: σ² = "+str(varp)+"."
            h1 = "H1: σ² ≠ "+str(varp)+"."
            # Calculo valores críticos de X²
            left_critical_value = round(chi2.ppf(alpha/2, gl),4)
            right_critical_value = round(chi2.ppf(1 - alpha/2, gl),4)
           # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: entre los valores de X²crítico ("+str(left_critical_value)+", "+str(right_critical_value)+")."
            ar = "Área de rechazo: a la izquierda de X²cI = "+str(left_critical_value)+" y a la derecha \nde X²cS = "+str(right_critical_value)+"."

            # calculo pvalor
            pvalor = pvalor*2

            if(x2>left_critical_value and x2<right_critical_value):
                r1 = "No se rechaza la hipótesis nula Ho."
                r2 = "Debido a que X²p = "+str(x2)+" se encuentra entre los valores de \nX²crítico ("+str(left_critical_value)+", "+str(right_critical_value)+"), no se rechaza la hipótesis nula Ho."
                r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                r1 = "Se rechaza la hipótesis nula Ho"
                r2 = "Debido a que X²p = "+str(x2)+" no se encuentra entre los valores de \nX²crítico ("+str(left_critical_value)+", "+str(right_critical_value)+"), se rechaza la hipótesis nula Ho."
                r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."

      if(nocolas == 2):
            # Hipotesis
            h0 = "Ho: σ² >= "+str(varp)+"."
            h1 = "H1: σ² < "+str(varp)+"."
            # Calculo valores críticos de X²
            left_critical_value = round(chi2.ppf(alpha, gl),4)
            right_critical_value = 0
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la derecha del valor de X²crítico = "+str(left_critical_value)+"."
            ar = "Área de no rechazo: a la izquierda del valor de X²crítico = "+str(left_critical_value)+"."

            if(x2>left_critical_value):
                r1 = "No se rechaza la hipótesis nula Ho."
                r2 = "Debido a que X²p = "+str(x2)+" es mayor que X²crítico = "+str(left_critical_value)+", \nno se rechaza la hipótesis nula Ho."
                r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                r1 = "Se rechaza la hipótesis nula Ho."
                r2 = "Debido a que X²p = "+str(x2)+" es menor que X²crítico = "+str(left_critical_value)+", \nse rechaza la hipótesis nula Ho."
                r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."
      if(nocolas == 3):
            # Hipotesis
            h0 = "Ho: σ² <= "+str(varp)+"."
            h1 = "H1: σ² > "+str(varp)+"."
            # Calculo valores críticos de X²
            left_critical_value = 0
            right_critical_value = round(chi2.ppf(1 - alpha, gl),4)
            # Diseño area de rechazo y no rechazo
            anr = "Área de no rechazo: a la izquierda del valor de X²crítico = "+str(right_critical_value)+"."
            ar = "Área de no rechazo: a la derecha del valor de X²crítico = "+str(right_critical_value)+"."
                  
            if(x2<right_critical_value):
                r1 = "No se rechaza la hipótesis nula Ho."
                r2 = "Debido a que X²p = "+str(x2)+" es menor que X²crítico = "+str(right_critical_value)+", \nno se rechaza la hipótesis nula Ho."
                r3 = "Ya que el pvalor = "+str(pvalor)+" > α = "+str(alpha)+", no se rechaza la \nhipótesis nula Ho."
            else:
                r1 = "Se rechaza la hipótesis nula Ho."
                r2 = "Debido a que X²p = "+str(x2)+" es mayor que X²crítico = "+str(right_critical_value)+", \nse rechaza la hipótesis nula Ho."
                r3 = "Ya que el pvalor = "+str(pvalor)+" < α = "+str(alpha)+", se rechaza la \nhipótesis nula Ho."

      #Diseño de GUI
      Label(vcc, text="Paso 1: formulación de hipótesis.",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=5)
      Label(vcc, text=h0,
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=40)
      Label(vcc, text=h1,
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=70)
      Label(vcc, text="Paso 2: nivel de significancia α.",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=105)
      Label(vcc, text="α = "+str(alpha)+" = "+str(round(alpha*100,2))+"%.",
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=140)
      Label(vcc, text="Paso 3: estadístico de prueba.",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=175)
      #Label(vcc, text= "X² = (n - 1)(s²) / σ²",
      #           font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=210)
      global imagen
      imagen = PhotoImage(file="./img/chicuadrado_func.png")
      Label(vcc, image=imagen).place(x=240,y=210)
      Label(vcc, text= "Paso 4: regla de decisión.",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=15, y=275)
      Label(vcc, text="Grados de libertad g.l. = muestra(n) - 1 = "+str(n)+" - 1 = "+str(n-1)+".",
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=310)
      fig = graphchicuadrado(nocolas, alpha, n, varm, varp, 0)
      canvas = FigureCanvasTkAgg(fig, master=vcc)
      canvas.draw()
	# placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=35,y=345, width=600, height=400)
      Label(vcc, text= anr,
                 font=("bold", 16), bg="#2E4053",foreground="white").place(x=35, y=755)
      Label(vcc, text= ar,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=35, y=790)
      # Segunda parte de la GUI
      Label(vcc, text= "Paso 5: prueba del estadístico.",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=5)
      Label(vcc, text= "X² = (n - 1)(s²) / σ² = ("+str(n)+" - 1)("+str(varm)+") / "+str(varp)+".",
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=40)
      Label(vcc, text= "X²prueba = X²p = "+str(x2)+".",
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=70)
      Label(vcc, text= "pvalor = "+str(pvalor)+".",
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=100)
      #Label(vcc, text= "",
      #           font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=130)
      fig2 = graphchicuadrado(nocolas, alpha, n, varm, varp, 1)
      canvas = FigureCanvasTkAgg(fig2, master=vcc)
      canvas.draw()
	# placing the canvas on the Tkinter window
      canvas.get_tk_widget().place(x=815,y=140, width=600, height=400)
      Label(vcc, text= "Paso 6: respuestas.",
                 font=("bold", 17), bg="#2E4053",foreground="white").place(x=795, y=550)
      Label(vcc, text= "1. "+r1,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=585)
      Label(vcc, text= "2. "+r2,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=615)
      Label(vcc, text= "3. "+r3,
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=670)
      Label(vcc, text= "4. Interprete.",
                 font=("bold", 16), bg="#2E4053",foreground="white", justify="left").place(x=815, y=725)
      Button(vcc, text="Guardar PDF",font=("bold", 15), bg="#424949",
           foreground="white", command=lambda:[pruebaPDF.chicuadrado(nocolas, alfa, varm, n,left_critical_value,right_critical_value,varp,x2,pvalor)]).place(x=1075, y=775)

def wcc():
      # Crear una ventana secundaria.
      vcc = Toplevel()
      vcc.title("Chi cuadrado")
      vcc.resizable(0,0)
      vcc.config(bg="#2E4053")

      hvcc = 450
      wvcc = 610

      pwidthvcc = round(wtotal/2-wvcc/2)
      pheightvcc = round(htotal/2-hvcc/2)

      vcc.geometry(str(wvcc)+"x"+str(hvcc)+"+"+str(pwidthvcc)+"+"+str(pheightvcc))
      Label(vcc, text="Ingrese la información necesaria para realizar la prueba de hipótesis:",
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
      
      Label(vcc, text="Varianza muestral s²:", font=("bold", 15),
            bg="#2E4053", foreground="white").place(x=0, y=265)
      varm = DoubleVar()
      Entry(vcc, font=("bold", 15), bg="#154360", foreground="white", textvariable=varm, 
            width=8).place(x= 325, y=265)
      
      Label(vcc, text="Varianza poblacional σ²:", font=("bold", 15),
            bg="#2E4053", foreground="white").place(x=0, y=315)
      varp = DoubleVar()
      Entry(vcc, font=("bold", 15), bg="#154360", foreground="white", textvariable=varp, 
            width=8).place(x= 325, y=315)
      
      Button(vcc, text="Volver",font=("bold", 15), bg="#424949",
            foreground="white", command=vcc.destroy).place(x=175, y=375)
      def limpiartexto():
            c.set(1)
            alfa.set(0.05)
            mstra.set(0)
            varm.set(0.0)
            varp.set(0.0)
      Button(vcc, text="Evaluar",font=("bold", 15), bg="#424949",
            foreground="white", 
            command= lambda: [chicuadrado(c.get(), alfa.get(), mstra.get(),varm.get(), varp.get()), vcc.destroy()]).place(x=350, y=375)

btn4 = Button(frame, text="Chi cuadrado - X²", width=38,
              height=4, font=("bold", 18), bg="#27AE60",foreground="white", anchor="center", command=wcc).grid(row="4")

def abrir_url(url):
    webbrowser.open(url)

def informacion():
      # Crear una ventana secundaria.
      info= Toplevel()
      info.title("Información")
      info.resizable(0,0)
      info.config(bg="#2E4053")

      hinfo = 350
      winfo = 600

      pwidthinfo = round(wtotal/2-winfo/2)
      pheightinfo = round(htotal/2-hinfo/2)

      info.geometry(str(winfo)+"x"+str(hinfo)+"+"+str(pwidthinfo)+"+"+str(150))

      texto = "Este proyecto fue creado por estudiantes del curso de Análisis\nProbabilístico en el primer semestre de 2023 de la Carrera de \nIngeniería en Ciencias y Sistemas del Centro Universitario de \nOriente CUNORI en Chiquimula, Guatemala."

      Label(info, text=texto, font=("bold", 15),
            bg="#2E4053", foreground="white", justify="left").place(x= 5, y=5)
      Label(info, text="Estudiantes:", font=("bold", 15),
            bg="#2E4053", foreground="white", justify="left").place(x= 5, y=110)
      Label(info, text="‣ Eduardo Rubén Cruz Sánchez - 202146471", font=("bold", 15),
            bg="#2E4053", foreground="white", justify="left").place(x= 15, y=145)
      Label(info, text="‣ Nery José Galdámez Aristondo - 202140502", font=("bold", 15),
            bg="#2E4053", foreground="white", justify="left").place(x= 15, y=180)
      Label(info, text="‣ Ramiro André Chacón Castañeda - 201940859", font=("bold", 15),
            bg="#2E4053", foreground="white", justify="left").place(x= 15, y=215)
      Label(info, text="‣ Kenat Jesiel Pérez Lucas - 202040366", font=("bold", 15),
            bg="#2E4053", foreground="white", justify="left").place(x= 15, y=250)
      
      style = ttk.Style()
      style.configure("Url.TButton", font=("bold", 15), foreground="blue", background="#3498DB")
      url_button = ttk.Button(info, text="Visita el repositorio en GitHub del proyecto.", style="Url.TButton", cursor="hand2", command=lambda: abrir_url("https://github.com/RamiroChac0n/Prueba_de_Hipotesis"))
      url_button.place(x=15, y=285)

btn5 = Button(frame, text="Acerca de", width=38,
              height=2, font=("bold", 18), bg="#707B7C",foreground="white", anchor="center", command=informacion).grid(row="5")

frame.pack(
    fill="both",
    expand="1"
)
root.quit()
root.mainloop()