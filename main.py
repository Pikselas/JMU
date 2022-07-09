from ModelSystem import *
from UI import *
from threading import Thread

msys = Modelsystem("D:/CODINGS/HTML,JAVASCRIPT,PHP/pikselas.github.io")

def ModelAdder(name : str, desc : str , links : list , profile_pic : str , Output):
    if not msys.AddNewModel(name , desc , links , profile_pic):
        Output(f'MODEL {name} COULD NOT BE ADDED\n')
    else:
        Output(f'MODEL {name} IS NOW IN THE ADDLIST\n')

def CatagoryAdder(catagory : str , Output):
    if not msys.AddNewCatagory(catagory):
        Output(f'CATAGORY {catagory} COULD NOT BE ADDED\n')
    else:
        Output(f'CATAGORY {catagory} IS NOW IN THE ADDLIST\n')

def CatagoryUpdater(catagory : str , models : list , Output):
    if not msys.UpdateCatagory(catagory , models):
        Output(f'CATAGORY {catagory} CANNOT BE UPDATED\n')
    else:
        Output(f'CATAGORY {catagory} IS NOW IN THE UPDATE LIST\n')

def Applier(Outputer):
    thrd = Thread(target = lambda: msys.Submit(Outputer))
    thrd.start()

ui = UI(ModelAdder , msys.GetModels , CatagoryAdder , msys.GetCatagories , CatagoryUpdater , Applier)