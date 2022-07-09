import GitCmd
import json
import os.path as op
from os import listdir
from shutil import copyfile 

class Modelsystem:
    
    __path = None
    __modelsDirectory = "jellymilk/data/models"
    __catagoriesDirectory = "jellymilk/data/catagories"
    __profilePicDirectory = "jellymilk/profile_pics"
    __catagoriesPath = "jellymilk/data/catagories.json"

    def __init__(self , path : str) -> None:
        self.__path = path
        self.GitHandler = GitCmd.GitCmd(path)
    
    def GetModels(self) -> list:
        return [Model.replace(".json" , '') for Model in listdir(self.__path + '/' + self.__modelsDirectory)]

    def GetCatagories(self) -> list:
        return [Catagory.replace(".json" , '') for Catagory in listdir(self.__path + '/' + self.__catagoriesDirectory)]

    def AddNewModel(self , name : str, desc : str , links : list , profile_pic : str) -> bool:
        filePath = self.__modelsDirectory + '/' + name + '.json'
        finalPath = self.__path + '/' + filePath
        if not op.isfile( finalPath) : 
            ModelJson = {"description" : desc , "links" : links}
            modelPicPath = self.__profilePicDirectory + '/' + name + ".png"
            copyfile(profile_pic , self.__path + '/' + modelPicPath)
            self.GitHandler.AddNewFile(modelPicPath)
            with open(finalPath , "w") as model:
                model.write(json.dumps(ModelJson , indent=4))
            self.GitHandler.AddNewFile(filePath)
            return True
        return False

    def AddNewCatagory(self , catagory : str) -> bool:
        catagoryPath = self.__catagoriesDirectory + '/' + catagory + '.json'
        if not op.isfile(self.__path + '/' + catagoryPath) :
            with open(self.__path + '/' + catagoryPath , "w") as cat:
                cat.write('{"models" : []}')
            self.GitHandler.AddNewFile(catagoryPath)
            catJson = {}
            with open(self.__path + '/' + self.__catagoriesPath , "r") as cat:
                catJson = json.loads(cat.read())
                catJson["catagories"].append(catagory)
                catJson["catagories"].sort()
            with open(self.__path + '/' + self.__catagoriesPath , "w") as cat:
                cat.write(json.dumps(catJson , indent=4))
            self.GitHandler.CommitFile(self.__catagoriesPath , "NEW CATAGORY ADDED")
            return True
        return False

    def UpdateCatagory(self , catagory : str , models : list) -> bool:
        catagoryPath = self.__catagoriesDirectory + '/' + catagory + '.json'
        if op.isfile(self.__path + '/' + catagoryPath) : 
            catJson = {}
            with open(self.__path + '/' + catagoryPath , "r") as cat:
                catJson = json.loads(cat.read())
                for model in models:
                    if model not in catJson["models"]:
                        catJson["models"].append(model)
                catJson["models"].sort()
            with open(self.__path + '/' + catagoryPath , "w") as cat:
                cat.write(json.dumps(catJson))
            self.GitHandler.CommitFile(catagoryPath,"UPDATED MODELS")
            return True
        return False
    
    def Submit(self , Outputer) ->None:
        self.GitHandler.Execute(Outputer)