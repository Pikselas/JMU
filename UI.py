from tkinter import DISABLED, END, Tk , Button , Text , Entry , Label , ttk , Toplevel
from tkinter.filedialog import askopenfilename
from tkinter.font import NORMAL

class UI:
    __ModelAdderFunc = None
    __ModelsGetterFunc = None
    __CatagoryAdderFunc = None
    __CatagoryGetterFunc = None
    __CatagoryUpdaterFunc = None
    __Applier = None

    __MainPanel = None
    __Console = None

    def __init__(self , ModelAdderFunc , ModelGetterFunc , CatagoryAdderFunc , CatagoryGetterFunc , CatagoryUpdaterFunc , ApplierFunc):
        
        self.__ModelAdderFunc = ModelAdderFunc 
        self.__ModelsGetterFunc = ModelGetterFunc
        self.__CatagoryAdderFunc = CatagoryAdderFunc 
        self.__CatagoryGetterFunc = CatagoryGetterFunc 
        self.__CatagoryUpdaterFunc = CatagoryUpdaterFunc
        self.__Applier = ApplierFunc
        
        self.__MainPanel = Tk()
        self.__MainPanel.geometry("500x300")
        self.__MainPanel.title("JMU - jellymilk updater")
       
        self.__Console = Text(self.__MainPanel , width= 38, height=16)
        self.__Console.place(x = 180 , y = 20)
       
        Button(self.__MainPanel ,width = 15 , height = 3 , text = "ADD MODEL" , command = self.__ModelAddPanel).place(x = 45 , y = 20)
        Button(self.__MainPanel ,width = 15 , height = 3 , text = "ADD CATAGORY" , command = self.__CatagoryAddPanel).place(x = 45 , y = 90)
        Button(self.__MainPanel ,width = 15 , height = 3 , text = "UPDATE CATAGORY" , command = self.__CatagoryUpdatePanel).place(x = 45 , y = 160)
        Button(self.__MainPanel ,width = 15 , height = 3 , text = "APPLY" , command = lambda : self.__Applier(self.Output)).place(x = 45 , y = 225)
        self.__MainPanel.mainloop()
    
    def __ModelAddPanel(self):
        panel = Toplevel(self.__MainPanel)
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
        Button(panel , text = "ADD" , width = 15 , height = 2 , command = lambda : [self.__ModelAdderFunc(name.get() , desc.get() , links.get("1.0" , "end-1c").split('\n') , askopenfilename(title="Select Profile Pic") , self.Output) , panel.destroy()]).pack()
        panel.mainloop()
    
    def __CatagoryAddPanel(self):
        panel = Toplevel(self.__MainPanel)
        panel.geometry("300x100")
        panel.title("ADD NEW CATAGORY")
        Label( panel , text = "Catagory Name").pack()
        catName = Entry(panel)
        catName.pack()
        Button(panel , text = "ADD" , width = 15, height = 2 ,  command = lambda : [self.__CatagoryAdderFunc(catName.get() , self.Output) , panel.destroy()]).pack()
        panel.mainloop()
    
    def __CatagoryUpdatePanel(self):
        def ModelInserter(event):
            val = event.widget.get()
            if val not in ModelsArr:
                Models.configure(state = NORMAL)
                Models.insert(END ,event.widget.get() + '\n')
                Models.configure(state = DISABLED)
                Models.see(END)
                ModelsArr.append(val)
        ModelsArr = []
        panel = Toplevel(self.__MainPanel)
        panel.geometry("300x200")
        panel.title("Update Catagory")
        Label( panel , text = "Select Catagory Name").pack()
        catagory = ttk.Combobox(panel , width = 15)
        catagory["values"] = self.__CatagoryGetterFunc()
        catagory.pack()
        catagory.current(0)
        Label(panel , text = "Select multiple models to be added").pack()
        Models = Text(panel , width = 15 , height = 4)
        Models.configure(state = DISABLED)
        Models.pack()
        ModelList = ttk.Combobox(panel , width = 15)
        ModelList["values"] = self.__ModelsGetterFunc()
        ModelList.bind("<<ComboboxSelected>>" , ModelInserter)
        ModelList.pack()
        Button(panel , text = "UPDATE" , width = 15 , height = 2 , command = lambda : [self.__CatagoryUpdaterFunc(catagory["values"][catagory.current()] , ModelsArr , self.Output) , panel.destroy()]).pack()
        panel.mainloop()
    
    def Output(self , text : str):
        self.__Console.insert(END , text)
        self.__Console.see(END)