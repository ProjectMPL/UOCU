import os
if not os.path.exists("completed.txt"):
    packages=["subprocess","numpy","cpu-load-generator","psutil","mock pytest flake8 tox","multiprocessing","threading","random"]
    for i in range(len(packages)):
        os.system("pip install "+packages[i])  
w=open("completed.txt","w")
w.write("COMPILE_FINISH_SUCCESFUL")
w.close()

import time,datetime,psutil,math
import time
import math 
import sys 
import multiprocessing
import threading
import random
import subprocess
class Point():
    EZUserMode=False
    P1=os.path.expanduser('~')+"/"
    os.system("cd "+P1)

class Col:
    PURPLE = '\033[35m'
    BLUE = '\033[34m'
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class BG_Col:
    PURPLE = '\033[45m'
    BLUE = '\033[44m'
    CYAN = '\033[46m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    RED = '\033[41m'
    DEFAULT = '\033[0m'
Running=True
os.system('cls' if os.name == 'nt' else 'clear') 
def commands(cmd):
    RT=Col.RED+"Command not found"+Col.DEFAULT
    if cmd=="unlock":
        RT=""
        for i in range(len(packages)):
            os.system("pip install "+packages[i])  
        os.system("python3 -m pip install --upgrade pip")

    if cmd=="help":
        RT='unlock - used to update all of the packages used for UOCU\n mode - used to switch between Normal and EZUserMode\nexit - used to exit the program\nclear - used to clear the terminal\nls - lists out everything in current directory\ncd - used to change your directory\nrun - used to run any executable/python file\n?pointer - used to get the path of the pointer (your current directory)\nip - used to get your IPv4 address\nsys * - used to run any system command use:"sys ipconfig" --->runs "ipconfiog"\ncredits - self explanatory'
    if cmd=="mode":
        Point.EZUserMode=not Point.EZUserMode
        RT="EZUserMode: "+str(Point.EZUserMode)+" | Press enter to continue to EZUserMode"
        commands("cd  ")   
    if cmd == "exit":
        RT="exit"
    if cmd=='clear':
        os.system('cls' if os.name == 'nt' else 'clear')   
        return ""   
    if cmd=="time":
        RT=datetime.datetime.now().strftime("%H:%M:%S")
    if cmd=="ls":
        r=""
        osdir=os.listdir(os.path.dirname(Point.P1))
        for i in range(len(osdir)):
            if not cmd.startswith("."):
                if osdir[i].find('.')>1:
                    r+=str(i).ljust(5)+"| 📄 "+Col.GREEN+osdir[i]+" "+Col.DEFAULT+"\n"
                else:
                    r+=str(i).ljust(5)+"| 📁 "+Col.BOLD+Col.BLUE+osdir[i]+" "+Col.DEFAULT+"\n"
        RT=r
    if cmd.startswith("cd "):
        RT=Col.RED+"No matching folder"+Col.DEFAULT
        osdir=os.listdir(os.path.dirname(Point.P1))
        for i in range(len(osdir)):
            if cmd.removeprefix("cd ")==osdir[i] and osdir[i].find('.')<1:
                Point.P1+=osdir[i]+"/ ".removesuffix(" ")
                os.system(cmd.removeprefix("cd "+osdir[i]))
                RT="--> "+Point.P1
        if len(cmd.removeprefix("cd"))<2:
            RT="back to root"
            os.system(cmd.removeprefix("cd"))
            Point.P1=os.path.expanduser('~')+"/"
    if cmd=="cd":
        RT="back to root"
        os.system(cmd.removeprefix("cd"))
        Point.P1=os.path.expanduser('~')+"/"
    if cmd.startswith("run "):
        RT=Col.RED+"No matching file"+Col.DEFAULT
        osdir=os.listdir(os.path.dirname(Point.P1))
        for i in range(len(osdir)):
            if cmd.removeprefix("run ")==osdir[i] and osdir[i].find('.')>=1:
                print("Running: "+Col.BOLD+Col.GREEN+cmd.removeprefix("run ")+Col.DEFAULT)
                if cmd.find(".py")>=1:
                    os.system("Python3 "+Point.P1+osdir[i])
                else:
                    os.startfile(Point.P1+osdir[i])
                RT=Col.PURPLE+"Finished running "+Col.BOLD+Col.BLUE+cmd.removeprefix("run ")+Col.DEFAULT

    if cmd=="?pointer":
        RT=Col.BLUE+"<"+Point.P1+">"+Col.DEFAULT
    if cmd=="ip":
        RT=""
        os.system("hostname -i")
    if cmd=="credits":
        RT="everything was made by UrOpinion on Discord"
    if cmd.startswith("sys"):
        RT=""
        os.system(cmd.removeprefix("sys"))
    return RT
print("| "+Col.UNDERLINE+Col.BOLD+Col.PURPLE+"UOCU v0.2"+Col.DEFAULT+" Custom Utilities |")

if Point.EZUserMode:
    print(commands("ls"))

EZB=Point.EZUserMode
while Running:
    RT=""
    if EZB==Point.EZUserMode:
        Cmd=input("@> ")
    else:
        Cmd=" "
        EZB=Point.EZUserMode
    if Point.EZUserMode==False:
        RT=commands(Cmd)
    else:
        commands("clear")
        try: 
           
            if str(os.listdir(os.path.dirname(Point.P1))[int(Cmd)]).find(".")>=1:
                commands("run "+os.listdir(os.path.dirname(Point.P1))[int(Cmd)])
            else:
                commands("cd "+os.listdir(os.path.dirname(Point.P1))[int(Cmd)])
            RT=commands("ls")
        except:
            RT=commands("ls")
            if Cmd=="back":
                commands("cd")
            if Cmd=="exit":
                RT="exit"
            if Cmd=="mode":
                commands("mode")
    print(RT)
    if RT=="exit":
        Running=False
os.system('cls' if os.name == 'nt' else 'clear') 