from tkinter import *
import tkinter.messagebox
import sqlite3

#Test Connection in Database
try:
  conn = sqlite3.connect("C:\\Python310\\File Developement - Testing\\cadastro_carros\\djangoProject\\db.sqlite3")
  cur = conn.cursor()
  cur.execute("SELECT * FROM CadastroClientes")
  tkinter.messagebox.showinfo("Success", "Connection to database established successfully.")
  conn.close()
except:
  tkinter.messagebox.showwarning("Warning", "Error connecting to database")

# Set Window Main
wMain = Tk()
wMain.configure(bg="#CCDBDC")
wMain.geometry("450x100")

# Creating Label and Textbox
labelNome = Label(wMain, text="Nome: ",fg="#263D42", font="Verdana 14", bg="#CCDBDC")
textboxNome = Entry(wMain, width=50)

labelIdade = Label(wMain, text="Idade: ",fg="#263D42", font="Verdana 14", bg="#CCDBDC")
textboxIdade = Entry(wMain, width=10)

button = Button(wMain, text="Click me")

# Set Position Label and textbox
rowLine = 0

labelNome.grid(row=rowLine, column=0)
textboxNome.grid(row=rowLine, column=1)
rowLine += 1

labelIdade.grid(row=rowLine, column=0)
textboxIdade.grid(row=rowLine, column=1, sticky=W)
rowLine += 1

button.grid(row=rowLine, column=2)
rowLine += 1

# Action to Click Button 
def on_click():
    recordNome = textboxNome.get()
    recordIdade = textboxIdade.get()
    values = (recordNome, recordIdade)
    conn = sqlite3.connect("C:\\Python310\\File Developement - Testing\\cadastro_carros\\djangoProject\\db.sqlite3")
    cur = conn.cursor()
    cur.execute("INSERT INTO CadastroClientes (Nome, Idade) VALUES (?,?)", values)
    conn.commit()
    conn.close()
    textboxNome.delete(0, END)
    textboxIdade.delete(0, END)
    tkinter.messagebox.showinfo("Success", "Cadastro Gravado.")
    
button.configure(command=on_click)

wMain.mainloop()

#show a messagebox - this server downloaded



