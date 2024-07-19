import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from lib.utils import *
root = tk.Tk()
root.title("undefined")
        #setting window size
width=800
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)


def m():
       return root

def chooseimg():
        file=filedialog.askopenfilename(initialdir="C:/")
        print(file)
        from PIL import Image


        
        p=pickle.load('model.pkl')
        


        from googletrans import Translator
        img = Image.open(file)
       

        result = p.image_to_string(img)
        print(result)
        
        T.insert(1.0, result)


def translate():
        TT.delete(1.0,"end")
        k=""
        from googletrans import Translator
        p = Translator()

        inp = T.get(1.0, "end-1c")
        #inp="If we do not specify the source and the destination languages, googletrans tries to detect the language and translates it into English."
        opt=optvalue.get()
        if(opt=="Tamil"):
               k = p.translate(str(inp),src="en",dest='ta')
        elif(opt=="Hindi"):
               k = p.translate(str(inp),src="en",dest='hi')
        elif(opt=="Kannada"):
               k = p.translate(str(inp),src="en",dest='kn')
        elif(opt=="Malayalam"):
               k = p.translate(str(inp),src="en",dest='ml')
        else:
               k = p.translate(str(inp),src="en",dest='te')
        
        

        
        print(k.text)
       
        
        TT.insert(1.0, str(k.text))

def play():
       

        import pyttsx3

        
        engine = pyttsx3.init()

        inp = TT.get(1.0, "end-1c")
        engine.say(inp)
       
        engine.runAndWait()

GLabel_925=tk.Label(root)
ft = tkFont.Font(family='Times',size=22)
GLabel_925["font"] = ft
GLabel_925["fg"] = "#333333"
GLabel_925["justify"] = "center"
GLabel_925["text"] = "IMAGE TO TEXT AND NATIVE LANGUAGE"
GLabel_925.place(x=200,y=40,width=476,height=30)

GButton_642=tk.Button(root)
GButton_642["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
GButton_642["font"] = ft
GButton_642["fg"] = "#000000"
GButton_642["justify"] = "center"
GButton_642["text"] = "choose Image"
GButton_642.place(x=80,y=130,width=123,height=30)
GButton_642["command"] =chooseimg

GButton_657=tk.Button(root)
GButton_657["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
GButton_657["font"] = ft
GButton_657["fg"] = "#000000"
GButton_657["justify"] = "center"
GButton_657["text"] = "Convert"
GButton_657.place(x=410,y=130,width=110,height=30)
GButton_657["command"] =translate

GButton_482=tk.Button(root)
GButton_482["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times',size=10)
GButton_482["font"] = ft
GButton_482["fg"] = "#000000"
GButton_482["justify"] = "center"
GButton_482["text"] = "Play"
GButton_482.place(x=560,y=130,width=70,height=25)
GButton_482["command"] =play
options=["Tamil","Telugu","Malayalam","Hindi","Kannada"]
optvalue=tk.StringVar(root)
optvalue.set("Selcet Language")
GListBox_618=tk.OptionMenu( root ,optvalue, *options )
        
GListBox_618["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GListBox_618["font"] = ft
GListBox_618["fg"] = "#333333"
GListBox_618["justify"] = "center"
GListBox_618.place(x=260,y=130,width=88,height=30)
print(optvalue.get())
T = tk.Text(root)
T.place(x=80,y=170,width=200,height=250)


TT = tk.Text(root)
TT.place(x=500,y=170,width=200,height=250)






if __name__ == "__main__":

    
    root.mainloop()
