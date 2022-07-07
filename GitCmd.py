import subprocess

class GitCmd:
    GIT_CMD_LIST = []
   
    def __init__(self , path : str) -> None:
        self.path = path

    def CommitFile(self , filename : str , message : str) -> None:
        self.GIT_CMD_LIST.append(["commit" , filename , "-m" , message])
    
    def AddNewFile(self , filename : str) ->None:
        self.GIT_CMD_LIST.append(["add" , filename])
        self.CommitFile(filename , "ADDED FILE :" + filename)

    def Clear(self) -> None:
        self.GIT_CMD_LIST.clear()

    def Execute(self ,Executer) -> None:
        git_path = ["git" , "-C" , self.path]
        self.GIT_CMD_LIST.append(["pull"])
        self.GIT_CMD_LIST.append(["push"])
        for command in self.GIT_CMD_LIST:
            cmd = git_path + command
            result = subprocess.run(cmd ,shell = True , capture_output=True , text = True)
            Executer(result.stdout)
            Executer(result.stderr)
        self.Clear()