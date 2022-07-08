from tkinter import END, Tk , Button , Text , Entry , Label
from tkinter.filedialog import askopenfilename

class UI:
    ModelAdderFunc = None
    CatagoryAdderFunc = None
    __Console = None

    def __init__(self):
        MainPanel = Tk()
        MainPanel.geometry("500x300")
        MainPanel.title("JMU - jellymilk updater")
       
        self.__Console = Text(MainPanel , width= 38, height=16)
        self.__Console.place(x = 180 , y = 20)
       
        Button(MainPanel ,width = 15 , height = 3 , text = "ADD MODEL" , command = self.__ModelAddPanel).place(x = 45 , y = 20)
        Button(MainPanel ,width = 15 , height = 3 , text = "ADD CATAGORY" , command = self.__CatagoryAddPanel).place(x = 45 , y = 90)
        Button(MainPanel ,width = 15 , height = 3 , text = "UPDATE CATAGORY").place(x = 45 , y = 160)
        Button(MainPanel ,width = 15 , height = 3 , text = "APPLY").place(x = 45 , y = 225)

        MainPanel.mainloop()
    def __ModelAddPanel(self):
        panel = Tk()
        panel.geometry("300x250")
        panel.title("ADD NEW MODEL")
        Label(panel , text = "Model Name").pack()
        name = Entry(panel)
        name.pack()
        Label(panel , text = "Description").pack()
        desc = Entry(panel)
        desc.pack()
        Label(panel , text = "Links (enter to seperate)").pack()
        links = Text(panel , width = 15 , height = 3)
        links.pack()
        Button(panel , text = "ADD" , width = 15 , height = 2 , command = lambda : [self.ModelAdderFunc(name.get() , desc.get() , links.get("1.0" , "end-1c").split('\n') , askopenfilename()) , panel.destroy()]).pack()
        panel.mainloop()
    
    def __CatagoryAddPanel(self):
        panel = Tk()
        panel.geometry("300x100")
        panel.title("ADD NEW CATAGORY")
        Label( panel , text = "Catagory Name").pack()
        catName = Entry(panel)
        catName.pack()
        Button(panel , text = "ADD" , width = 15, height = 2 ,  command = lambda : [self.CatagoryAdderFunc(catName.get()) , panel.destroy()])
        panel.mainloop()
    
UI()