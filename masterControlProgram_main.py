#Master Control Program
#Paul Ambrose
#03/11/2022

#Python program to allow control of automated and user initiated actions on RPi
#Initial set up controls work flow for managing python project

import git
import os
import shutil

def userInterface():
    print("Master Control Program\n\n")
    print("1-PULL Current Staged Repo\n")
    print("2-PUSH Current Staged Repo\n\n")
    choice = input("Please select>> ")
    
    if choice == str(1):
        warning1 = input("***WARNING***, the current activeStage will be deleted, do you want to continue? y/n >> ")
        if warning1.upper() == "Y":
            return 1
        else:
            return 0
    elif choice == str(2):
        return 2

def readActiveRepo():
    activeRepoFile = open('staged repo', 'r')
    activeRepo = activeRepoFile.read()
    activeRepoFile.close()
    return activeRepo    

def pullActiveRepo():
    filePath = os.getcwd()
    shutil.rmtree(filePath + "/activeStage")
    os.mkdir(filePath + "/activeStage")
    
    repoToClone = readActiveRepo()
    
    #os.chdir(filePath + "/activeStage")
    git.Repo.clone_from(repoToClone, filePath + "/activeStage")

def pushActiveRepo():
    pass

def main():
    userChoice = userInterface()
    if userChoice == 1:
        pullActiveRepo()
    elif userChoice == 2:
        pushActiveRepo()
    else:
        print("\nAction aborted")
main()