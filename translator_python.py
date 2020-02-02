import tkinter as tk 
#pip install googletrans 
from googletrans import Translator

win=tk.Tk() 
win.title("Translator") 
win.geometry("200x70") 

#Function To Translate English to Tamil 
def translation():
    word=entry.get() 
    translator=Translator(service_urls=['translate.google.com']) 
    translated_text=translator.translate(word,dest="ta") #Here ta refers to Tamil.
    label1=tk.Label(win,text=f"Translated In Tamil : {translated_text.text}",bg="blue")  
    label1.grid(row=2,column=0) 


label=tk.Label(win,text="Enter Word :") 
label.grid(row=0,column=0,sticky="w") 

#To get input from user
entry=tk.Entry(win) 
entry.grid(row=1,column=0) 

#Button to Translate 
#Clicking on this will call translation function
button=tk.Button(win,text="Translate",command=translation) 
button.grid(row=1,column=2) 

win.mainloop()