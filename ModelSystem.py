import GitCmd
import json
import os.path as op
from os import listdir
from shutil import copyfile 

class Modelsystem:
    
    __path = None
    __modelsDirectory = "data/models"
    __categoriesDirectory = "data/categories"
    __profilePicDirectory = "profile_pics"
    __categoriesPath = "data/categories.json"

    def __init__(self , path : str) -> None:
        self.__path = path
        self.GitHandler = GitCmd.GitCmd(path)
    
    def GetModels(self) -> list:
        return [Model.replace(".json" , '') for Model in listdir(self.__path + '/' + self.__modelsDirectory)]

    def GetCatagories(self) -> list:
        return [Category.replace(".json" , '') for Category in listdir(self.__path + '/' + self.__categoriesDirectory)]

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
            self.GitHandler.AddNewFile(filePath,"NEW MODEL ADDED:" + name)
            return True
        return False

    def AddNewCategory(self , category : str) -> bool:
        categoryPath = self.__categoriesDirectory + '/' + category + '.json'
        if not op.isfile(self.__path + '/' + categoryPath) :
            with open(self.__path + '/' + categoryPath , "w") as cat:
                cat.write('{"models" : []}')
            self.GitHandler.AddNewFile(categoryPath)
            catJson = {}
            with open(self.__path + '/' + self.__categoriesPath , "r") as cat:
                catJson = json.loads(cat.read())
                catJson["categories"].append(category)
                catJson["categories"].sort()
            with open(self.__path + '/' + self.__categoriesPath , "w") as cat:
                cat.write(json.dumps(catJson , indent=4))
            self.GitHandler.CommitFile(self.__categoriesPath , "NEW CATEGORY ADDED:" + category)
            return True
        return False

    def UpdateCategory(self , category : str , models : list) -> bool:
        categoryPath = self.__categoriesDirectory + '/' + category + '.json'
        if op.isfile(self.__path + '/' + categoryPath) : 
            catJson = {}
            with open(self.__path + '/' + categoryPath , "r") as cat:
                catJson = json.loads(cat.read())
                for model in models:
                    if model not in catJson["models"]:
                        catJson["models"].append(model)
                catJson["models"].sort()
            with open(self.__path + '/' + categoryPath , "w") as cat:
                cat.write(json.dumps(catJson , indent=4))
            self.GitHandler.CommitFile(categoryPath,"UPDATED CATEGORY:" + category)
            return True
        return False
    
    def Submit(self , Outputer) ->None:
        self.GitHandler.Execute(Outputer)