#!/user/bin/env python
"""
Ejemplo basico del uso tkinter
Basado en:https://pythonbasics.org/tkinter/
Autor:
"""

from tkinter import *
import time
import speech_recognition as sr
import pyttsx3
import serial

# Inicializar el objeto de reconocimiento de voz
r = sr.Recognizer()

# Configurar el motor de síntesis de voz
engine = pyttsx3.init()


# Configurar la conexión Bluetooth
bluetooth_port = 'COM13'  # Reemplaza 'COMX' con el puerto COM correcto
bluetooth_baud = 9600


# Iniciar la conexión Bluetooth
bluetooth = serial.Serial(bluetooth_port, bluetooth_baud, timeout=1)


class Window(Frame):

    clock_on = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        #se crea el menú principal
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)

        #se crea el menú secundario
        menu_config = Menu(main_menu, tearoff=0)
        menu_config.add_command(label='modo por voz', command=self.start_listening)
        menu_config.add_command(label='salir', command=self.exit_window)

        #se crea el menú principal
        main_menu.add_cascade(label='Opciones', menu=menu_config)

        #creamos un contenedor para otros widgets
        self.pack(fill=BOTH, expand=1)

        #se agrega boton
        self.exitButton = Button(self, text='Cerrar', command=self.exit_window)
        self.exitButton.place(x=450, y=10)

        #se agrega boton de stop
        self.StopButton = Button(self, text='Stop', command=self.stop_window)
        self.StopButton.config(width=10)
        self.StopButton.place(x=213, y=200)

        #se agreaga un boton de Arriba o hacia delante
        self.AdelanteButton = Button(self, text='Avanzar', command=self.Avan_window)
        self.AdelanteButton.config(width=10)
        self.AdelanteButton.place(x=213, y=150)

        #se agreaga un boton de Izquierda
        self.IzquierdaButton = Button(self, text='Izquierda', command=self.Izq_window)
        self.IzquierdaButton.config(width=10)
        self.IzquierdaButton.place(x=125, y=200)

        #se agreaga un boton de Derecha
        self.DerechaButton = Button(self, text='Derecha', command=self.Der_window)
        self.DerechaButton.config(width=10)
        self.DerechaButton.place(x=300, y=200)

        #se agreaga un boton de Abajo o hacia atrás
        self.AtrasButton = Button(self, text='Atras', command=self.Atras_window)
        self.AtrasButton.config(width=10)
        self.AtrasButton.place(x=213, y=250)

        #se agrega boton
        self.clockButton = Button(self, text='Activa reloj', command=self.clock)
        self.clockButton.place(x=375, y=10)

        #se crea las etiquetas
        self.labell1 = Label(self.master, text='Hora local')
        self.labell1.place(x=220, y=10)
        self.labell2 = Label(self.master, text=self.get_time(), fg='Green', font=('helvetica', 18))
        self.labell2.place(x=200, y=30)


    #método salir
    def exit_window(self):
        exit()

    #método get_time
    def get_time(self):
        now = time.strftime('%H:%M:%S')
        return now
    
    #método update_clock
    def update_clock(self):
        self.labell2.configure(text=self.get_time())
        if self.clock_on:
            self.after(1000, self.update_clock)
    
    #método clock
    def clock(self):
        if self.clock_on == False:
            self.clock_on = True
            self.clockButton.configure(text='desactivar reloj')
            self.update_clock()
        else:
            self.clock_on = False
            self.clockButton.configure(text='Activar reloj')

    listening = False

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()

    
    def listen(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = r.listen(source)
        try:
            print("Reconociendo...")
            text = r.recognize_google(audio, language="es-ES")
            print("Has dicho: " + text)
            return text.lower()
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio.")
            return ""
        except sr.RequestError as e:
            print("Error en la solicitud al servicio de reconocimiento de voz: {0}".format(e))
            return ""

    
    def stop_window(self):
        bluetooth.write(b'S')
    
    def Avan_window(self):
        bluetooth.write(b'A')

    def Izq_window(self):
        bluetooth.write(b'I')

    def Der_window(self):
        bluetooth.write(b'D')

    def Atras_window(self):
        bluetooth.write(b'R')
    def start_listening(self):
        global listening
        listening = True
        while listening == TRUE:
            command = self.listen()
            if "encender" in command:
                self.speak("Auto avanzando.")
                print('Auto avanzando.')
                self.Avan_window()
            elif "atrás" in command:
                self.speak("Auto retrocediendo.")
                print("Auto retrocediendo.")
                self.Atras_window()
            elif "apagar" in command:
                self.speak("Auto deteniendose.")
                print("Auto deteniendose.")
                self.stop_window()
            elif "salir" in command:
                self.speak("Saliendo del programa.")
                listening = False
                break
    def stop_listening():
        global listening
        listening = False
# Analiza una ventana
root = Tk()
app = Window(root)
# agrega titulo
root.wm_title("Ventana principal")
root.geometry('500x400-0-0')
# muestra de ventana
root.mainloop()