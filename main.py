import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from io import open
from clases.question import Question


class Player:
    def __init__(self):
        self.__nickname = ""
        self.__point = 0
    
    def getNickname(self):
        return self.__nickname
    
    def setNickname(self, Nname):
        self.__nickname = Nname

    def getPoint(self):
        return self.__point

    def setPoint(self, points):
        self.__point = points


class Round:
    def __init__(self, roundtime: int):
        self.__roundcounter = 1
        self.__roundtime = roundtime
        self.__ganaste = False

    def getRoundCounter(self):
        return self.__roundcounter
    
    def setRoundCounter(self, roundcounter):
        self.__roundcounter = roundcounter

    def getTimer(self):
        return self.__roundtime

    def setTimer(self, time):
        self.__roundtime = time

    def timer(self):
        if round.getTimer() > 1:
            if player.getPoint() < 55:
                round.setTimer(round.getTimer()-1)
                print(round.getTimer())
                ventana.after(1000, self.timer)
        else:
            if(player.getPoint() > 0):
                persistir()
            messagebox.showinfo("TIEMPO ACABADO", "¡Se ha acabado el tiempo!\nSuerte a la proxima")
            exit()

ventana= Tk()

questions: list = [
    [
        Question("GASTRONOMIA","¿Qué fruta seca sale de las uvas?", 
                 {"Ciruelas": False, "Anacardo": False, "Pasas": True, "Ninguna de las anteriores": False}, ventana),
        Question("MATEMATICAS","¿A cuánto equivale Pi?",
                 {"3.141592": True, "3.1492145": False, "3.144433": False, "3.149412": False}, ventana),
        Question("FISICA","¿Qué es la trayectoria de un móvil?",
                 {"Es la dirección del movimiento": False, "Es el sentido del movimiento": True, "Es la línea que describe en su movimiento": False,
                  "Es la dirección y sentido del movimiento": False}, ventana),
        Question("UNIVERSO","¿El universo se forma por?",
                 {"Espacio y agujeros negros": False, "El sol, la tierra y la luna, como elementos principales": False, "Los planetas, los satélites, los cometas, los asteroides y las estrellas. ": True, "Ninguna de las anteriores": False}, ventana),
        Question("PROPIEDADES DE LA MATERIA","Dos propiedades fundamentales de la materia son:",
                 {"Ninguna de las anteriores": False, "El peso y la estructura molecular": False,
                  "La masa y el sabor": False, "El volumen y la masa": True}, ventana)
    ],
    [
        Question("GASTRONOMIA","¿Qué significa ligar un alimento?",
                 {"Añadir salsa a un alimento": False, "Espesar con la ayuda de huevo, harina, etc": True, "Utilizar especias en los ingredientes": False, "Ninguna de las anteriores": False}, ventana),
        Question("MATEMATICAS","¿Qué es un triángulo isósceles?", 
        {"Un tipo de triangulo que tiene todos sus lados iguales": False, "Un tipo de triangulo que tiene los tres lados desiguales": False, "Un tipo de triangulo que tiene dos lados de igual longitud": True, "Ninguna de las anteriores": False}
                 , ventana),
        Question("FISICA","¿En qué unidad se mide la presión?",
                 {"Newton": True, "Kg": False, "Pascales": False,
                  "m/s": False}, ventana),
        Question("UNIVERSO","¿La vía láctea es?", 
        {"Una parte del universo formada por los planetas": False, "Una vía en la que se encuentra la órbita de los planetas": False, "Es una galaxia de forma espiral que contiene el sistema solar y la tierra": True, "Ninguna de las anteriores": False}, ventana
                 ),
        Question("PROPIEDADES DE LA MATERIA","Las unidades que se emplean para medir la masa son:",
                 {"kg, g, mg, t (toneladas)": True, "Peso": False, "Kg/m3": False, "Ninguna de las anteiores": False}, ventana)
    ],
    [
        Question("GASTRONOMIA","¿Si hablamos de concassé, hablamos de...?",
                 {"Un postre de manzana": False, "Un tipo de corte ": True, "Un tipo de cocción que se hace a ciertas verduras": False, "Ninguna de las anteriores": False}, ventana),
        Question("MATEMATICAS","¿Cuánto es la cuarta parte de la tercera parte?",
                 {"Un séptimo": False, "Un doceavo": True, "3/4 partes": False, "4/6 partes": False}, ventana),
        Question("FISICA","Cuál de estas velocidades corresponde a los movimientos circulares",
                 {"Velocidad de trayectoria": False, "Velocidad lineal": False, "Velocidad media": False, "Velocidad angular": True}, ventana),
        Question("UNIVERSO","De las siguientes afirmaciones, identifica la correcta:",
                 {"La tierra se encuentra en el sistema solar como el planeta de mayor tamaño de la vía láctea": False, "La tierra, tiene movimiento de translocación y rotulación ": False, "Los astros del universo son: asteroide, cometa, estrella, satélite y planeta": True, "Ninguna de las anteriores": False}, ventana),
        Question("PROPIEDADES DE LA MATERIA","¿Cómo se llama el paso de líquido a sólido?",
                 {"Condensación": False, "Solidificación": True, "Sublimación": False, "Ninguna de las anteriores": False}, ventana)
    ],
    [
        Question("GASTRONOMIA","¿Qué es bardar una carne?",
                 {"Envolverla en tocino para que no se seque al cocinarla ": True, "Sellarla antes de asarla": False, "Trocearlo antes de cocinarla": False,
                  "Ninguna de las anteriores": False}, ventana),
        Question("MATEMATICAS","¿Qué formula es esta?",
                 {"Superficie de un circulo": True, "Diametro de un circulo": False, "Volumen de un cilindro": False, "Superficie de paralelogramos": False}, ventana),
        Question("FISICA","En qué unidad se mide la velocidad angular", {"Km/h": False, "Newton": False, "Rad/s": True, "Ninguna de las anteriores": False}, ventana),
        Question("UNIVERSO","La máxima evolución del Universo, lo constituye: ",
                 {"El hombre": True, "La materia": False, "La antimateria": False,
                  "El espacio": False}, ventana),
        Question("PROPIEDADES DE LA MATERIA","Mientras dura el cambio de estado de sólido a líquido o de líquido a gas, la temperatura...",
                 {"Aumenta": False, "Se mantiene constante": True, "Disminuye": False,
                  "Ninguna de las anteriores": False}, ventana)
    ],
    [
        Question("GASTRONOMIA","¿Cuál es la temperatura máxima para freír en aceite de oliva?",
            {"180ºC": True, "200ºC": False, "170ºC": False, "Ninguna de las anteriores": False}, ventana),
        Question("MATEMATICAS","¿Que expresa esta fórmula? E=MC²",
                 {"Circunferencia de un circulo": False, "La teoría de la probabilidad": False, "Volumen de un cubo": False, "Equivalencia entre masa y energía": True}, ventana),
        Question("FISICA","¿Cuál de las siguientes leyes no pertenece a los 3 principios de Newton?",
                 {"Ley fundamental de la dinámica": False, "Ley de la inercia": False, "Ley de atracción": True, "Ley de la acción y reacción": False}, ventana),
        Question("UNIVERSO","Debido a las reacciones termonucleares las estrellas:",
                 {"Se convierten en enanas blancas": False, "Desarrollan una rotación diferencial": False, "Emiten radiaciones electromagnéticas": True, "Adoptan formas esferoidales": False}, ventana),
        Question("PROPIEDADES DE LA MATERIA","Vertemos agua en una probeta hasta la marca de 300 ml (300 centímetros cúbicos). Sumergimos en ella una piedra de forma irregular y observamos que el nivel del agua sube hasta la marca de 350 ml. Si la masa de la piedra es 220 g, ¿cuál es su densidad?",
                 {"0,227 centímetros cúbicos por gramo": False, "4,4 gramos por centímetro cúbico": True, "40 gramos por centímetro cúbico": False, "Ninguna de las anteriores": False}, ventana)
    ]
]


def randonNumber(limit: int):
    return random.randint(0, limit)

def NameJugador():
    N_J= entry.get()
    if N_J.strip() == "":
        messagebox.showerror("Error", "Debe insertar un nombre del jugador valido")
    else:
        for widget in ventana.winfo_children():
            widget.destroy()
        ventana.geometry("470x300+0+0")
        ventana.title("CUESTIONARIO DE PREGUNTAS")
        player.setNickname(N_J)
        mostra()
        round.timer()
        return N_J
    


def persistir():
    try:
        datos = player.getNickname()+","+str(player.getPoint())+"\n"
        archivo_add.write(datos)
        archivo_add.close()
    except:
        print("")


def mostra():
    questionChosen: Question = questions[round.getRoundCounter()-1][randonNumber(4)]
    categoryChosenStr: str = questionChosen.showCategory()
    questionChosenStr: str = questionChosen.showQuestion()
    questionChosen.showAnswers()
    Label(ventana,text=questionChosenStr, font='Helvetica 11 bold', bg='wheat1').place(x=40,y=40)
    Label(ventana,text="CATEGORIA :",font='Helvetica 9 bold',bg='wheat1').place(x=40,y=220)
    Label(ventana,text=categoryChosenStr,font='Arial 9 ',bg='wheat1').place(x=120,y=220)
    Label(ventana,text="RONDA :",font='Helvetica 9 bold',bg='wheat1').place(x=330,y=220)
    Label(ventana,text=round.getRoundCounter(),font='Arial 9',bg='wheat1').place(x=390,y=220)
    def vertificar():
        print(round.getTimer())
        correct = questionChosen.answerQuestion()
        if correct:
            if round.getRoundCounter() < 5:
                player.setPoint(player.getPoint()+(5*round.getRoundCounter()))
                round.setRoundCounter(round.getRoundCounter()+1)
                round.setTimer(30)
                for widget in ventana.winfo_children():
                    widget.destroy()
                mostra()
            else:
                player.setPoint(player.getPoint()+5)
                messagebox.showinfo("¡GANASTE!", "¡Has ganado!\nFelicitaciones")
                persistir()
                exit()
        else:
            messagebox.showinfo("PERDISTE", "¡Has perdido!\nSuerte a la proxima")
            exit()
    def abandonar():
        respuesta = messagebox.askquestion(title="Abanadonar la partida",
                                            message="¿Estas seguro que quieres abandonar la partida?")
        print(respuesta)
        if respuesta == "yes":
            if(player.getPoint() > 0):
                persistir()
            exit()
    Button(ventana,text="Salir", command=abandonar, font='Helvetica 9 bold', background = "red4", foreground = "white").place(x=11,y=264)
    Button(ventana,text="Siguiente", command=vertificar, font='Helvetica 9 bold', background = "green4", foreground = "white").place(x=400,y=264)



round = Round(30)
player = Player()
archivo_add = open("jugadores.txt","a")

ventana.config(width=300, height=200),
ventana.config(bg='wheat1')
ventana.title("Nombre de usuario")
lblAnimo=Label(ventana,text= "Inserte nombre del jugador",font='Helvetica 9 bold',bg='wheat1').place(x=80,y=40)
entry = ttk.Entry(ventana)
entry.place(x=90, y=80)
Button(ventana, text="Aceptar", command=NameJugador, font='Helvetica 9 bold', background = "green4", foreground = "white").place(x=127, y=120)

ventana.mainloop()