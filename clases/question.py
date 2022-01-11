from tkinter import *
from tkinter import ttk

class Question:
    def __init__(self, category: str, question: str, answers: dict, ventana):
        self.category = category
        self.question = question
        self.answers = answers
        self.__seleccionada: int = 0
        self.ventana = ventana

    def showCategory(self):
        return self.category

    def showQuestion(self):
        return self.question
    
    def showAnswers(self):
        #allAnswers: str = ''
        keyList = list(self.answers.keys())
        def answerQuestions():
            self.__seleccionada = selec.get()-1
            
        def puntaje():
            ventanas=Tk()
            ventanas.title("PUNTAJE TOTAL")
            tabla = ttk.Treeview(ventanas, columns=("Puntaje"))
            tabla.grid(row=1,column=0,columnspan=2)
            tabla.heading("#0", text= "JUGADOR",anchor= CENTER)
            tabla.heading("Puntaje", text= "PUNTAJE",anchor= CENTER)

            archivo_read = open("jugadores.txt","r")

            for i in archivo_read.readlines():
                valores = i.split(",")
                tabla.insert("",END, text=str(valores[0]),values=(str(valores[1])))
            
            archivo_read.close()

        selec = IntVar()
        Radiobutton(self.ventana,text=keyList[0],value=1,variable=selec,command=answerQuestions,bg='wheat1').place(x=80,y=70)
        Radiobutton(self.ventana,text=keyList[1],value=2,variable=selec,command=answerQuestions,bg='wheat1').place(x=80,y=100)
        Radiobutton(self.ventana,text=keyList[2],value=3,variable=selec,command=answerQuestions,bg='wheat1').place(x=80,y=130)
        Radiobutton(self.ventana,text=keyList[3],value=4,variable=selec,command=answerQuestions,bg='wheat1').place(x=80,y=160)
        Button(self.ventana,text="Puntajes",font='Helvetica 8 bold', command=puntaje).place(x=400,y=13)
    
    def answerQuestion(self):
        valueList = list(self.answers.values())
        verifica = valueList[self.GetSelecionado()]
        return verifica
        
    def GetSelecionado(self):
        return self.__seleccionada
