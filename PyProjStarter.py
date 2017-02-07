#Python script project starter...

import os;

print "This script generates a directory  with a main script and supporting script file..."

location = raw_input("Enter the project location : ")

if(location == ""):
	print "Choosing default location"
	location = "/home/kiren/bin/"

os.chdir(location)

print "The current working directory is : "+os.getcwd()

authName =  raw_input("Enter author's Name : ")

if(authName == ""): authName = "Unknown"

dirName = raw_input("Enter the name of the Project ... The main script will be named after this...");

if (dirName == ""): dirName = "MyScriptMain"

mainFileName = dirName + ".py"

supportFile = dirName + "Utils.py"

os.mkdir(dirName)

os.chdir(dirName)

wfo = open(supportFile,"w")

wfo.write("#"+supportFile+" -- Created by " + authName)

wfo.close()

wfo = open(mainFileName,"w")

wfo.write("#"+mainFileName+" -- Created by " + authName)
wfo.write("\nimport "+supportFile)

wfo.close()

print "Project folder created ... enjoy!!!"


