from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

# Translator Functionality Part
def change(text="type", src="english", dest="hindi"):
    try:
        trans = Translator()
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    except Exception as e:
        return f"Error: {str(e)}"

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END).strip()
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

# User Interface Part
root = Tk()
root.title("Translator")
root.geometry("500x500")
root.config(bg="grey")

frame = Frame(root, pady=20)
frame.pack(side=BOTTOM, fill=BOTH, expand=True)

label_txt = Label(root, text="Translator", font=("Times New Roman", 20, "italic"), bg="white")
label_txt.place(x=100, y=20, height=40, width=300)

label_input = Label(root, text="Input Text", font=("Times New Roman", 30, "bold"), bg="grey", fg="White")
label_input.place(x=100, y=80, height=50, width=300)

Sor_txt = Text(root, font=("Times New Roman", 20, "normal"), wrap=WORD)
Sor_txt.place(x=10, y=140, height=90, width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=250, height=40, width=150)
comb_sor.set("english")

button_change = Button(root, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=250, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text)
comb_dest.place(x=330, y=250, height=40, width=150)
comb_dest.set("hindi")

label_output = Label(root, text="Destination Text", font=("Times New Roman", 30, "bold"), bg="grey", fg="White")
label_output.place(x=100, y=300, height=50, width=300)

dest_txt = Text(root, font=("Times New Roman", 20, "normal"), wrap=WORD)
dest_txt.place(x=10, y=360, height=90, width=480)

root.mainloop()
