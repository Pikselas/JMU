from ModelSystem import *
from UI import *
from threading import Thread

msys = Modelsystem("../jellymilk")

def ModelAdder(name : str, desc : str , links : list , profile_pic : str , Output):
    if not msys.AddNewModel(name , desc , links , profile_pic):
        Output(f'MODEL {name} COULD NOT BE ADDED\n')
    else:
        Output(f'MODEL {name} IS NOW IN THE ADDLIST\n')

def CategoryAdder(category : str , Output):
    if not msys.AddNewCategory(category):
        Output(f'CATAGORY {category} COULD NOT BE ADDED\n')
    else:
        Output(f'CATAGORY {category} IS NOW IN THE ADDLIST\n')

def CategoryUpdater(category : str , models : list , Output):
    if not msys.UpdateCategory(category , models):
        Output(f'CATAGORY {category} CANNOT BE UPDATED\n')
    else:
        Output(f'CATAGORY {category} IS NOW IN THE UPDATE LIST\n')

def Applier(Outputer):
    thrd = Thread(target = lambda: msys.Submit(Outputer))
    thrd.start()

ui = UI(ModelAdder , msys.GetModels , CategoryAdder , msys.GetCatagories , CategoryUpdater , Applier)