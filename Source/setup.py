from cx_Freeze import setup, Executable
import requests

build_exe_options = {"packages": ["os", "sys", "multiprocessing", "time"],
                     "excludes": ["tkinter"],
                     "includes": ["request", "time", "idna.idnadata", "os"] } 

setup(name = "FreEnotes" ,
      version = "1.1" ,
      description = "Simple CLI application to grab free enotes applications" ,
      author = "Reecepbcups",
      options = {"build_exe": build_exe_options},
      executables = [Executable("freEnotes.py")])



# ToDo at some time - add "tkinter" to includes list
