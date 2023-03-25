from tkinter import *
from fractions import *
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

def valbt(val):
    a = float(Fraction(5/4))
    print(a)
    print(val)

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
    c.set(0)
    
    Radiobutton(vcn,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=50, y=100)

    Radiobutton(vcn,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9", 
            command=lambda: valbt(c.get())).place(x=190,y=100)
    
    Radiobutton(vcn,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=405, y=100)
    
    Label(vcn, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
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
           foreground="white", command="").place(x=350, y=425)
    
btn1 = Button(frame, text="Curva normal \"Z\"", width=38,
              height=6, font=("bold", 18), bg="#707B7C",foreground="white", anchor="center", command=wcn).grid(row="1")

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
    c.set(0)
    
    Radiobutton(vts,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=50, y=100)

    Radiobutton(vts,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9", 
            command=lambda: valbt(c.get())).place(x=190,y=100)
    
    Radiobutton(vts,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=405, y=100)
    
    Label(vts, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
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
    c.set(0)
    
    Radiobutton(vpm,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=50, y=100)

    Radiobutton(vpm,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9", 
            command=lambda: valbt(c.get())).place(x=190,y=100)
    
    Radiobutton(vpm,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=405, y=100)
    
    Label(vpm, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
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
    c.set(0)
    
    Radiobutton(vcc,
            text="2 colas",
            value=1, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=50, y=100)

    Radiobutton(vcc,
            text="1 cola (izquierda)",
            value=2, variable=c, font=("bold", 15), indicatoron=0, 
            bg="#1A5276", foreground="white",selectcolor="#2980B9", 
            command=lambda: valbt(c.get())).place(x=190,y=100)
    
    Radiobutton(vcc,
            text="1 cola (derecha)",
            value=3, variable=c, font=("bold", 15), indicatoron=0,
            bg="#1A5276", foreground="white",selectcolor="#2980B9",
            command=lambda: valbt(c.get())).place(x=405, y=100)
    
    Label(vcc, text="Nivel de significancia α (decimales):", font=("bold", 15),
          bg="#2E4053", foreground="white").place(x=0, y=165)
    alfa = DoubleVar()
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
root.mainloop()