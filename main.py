import subprocess
import tkinter

import GitCmd

gcm = GitCmd.GitCmd("D:/data")
gcm.AddNewFile("gk.txt")
gcm.CommitFile("gk.txt" , "added file gk.txt")

print(gcm.Execute())