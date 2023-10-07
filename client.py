import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 5000
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
clients = {}


def musicWindow():
    window = Tk()
    window.title('Music Window')
    window.geometry('300x300')
    window.configure(bg = "LightSkyBlue")

    selectlabel = Label(window, text = "Select Song", bg = "LightSkyBlue", font = (('Calibri', 8)))
    selectlabel.place(x = 2, y = 1)

    listbox = Listbox(window, width = 15, height = 10, activestyle = 'dotbox', bg = "LightSkyBlue", borderwidth = 2, font = (('Calibri', 8)))
    listbox.place(x = 10, y = 15)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

def setup():
    global SERVER, PORT, IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

setup()