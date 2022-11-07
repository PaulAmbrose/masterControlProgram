#Master Control Program
#Paul Ambrose
#03/11/2022

#Python program to allow control of automated and user initiated actions on RPi
#Initial set up controls work flow for managing python project

from git.repo import Repo
import os
import shutil

def userInterface():
    print("Master Control Program\n\n")
    print("1-Pull Current Staged Repo\n\n")
    choice = input("Please select>> ")
    
    if choice == str(1):
        warning1 = input("***WARNING***, the current activeStage will be deleted, do you want to continue? y/n >> ")
        if warning1.upper() == "Y":
            return 1
        else:
            return 0
    else:
        pass

def pullActiveRepo():
    filePath = os.getcwd() 
    
    shutil.rmtree(filePath + "/activeStage")
    activeRepoFile = open('staged repo', 'r')
    activeRepo = activeRepoFile.read()
    activeRepoFile.close()

    Repo.clone_from(activeRepo, filePath + "/activeStage/")

def main():
    userChoice = userInterface()
    if userChoice == 1:
        pullActiveRepo()
    else:
        print("\nAction aborted")
main()