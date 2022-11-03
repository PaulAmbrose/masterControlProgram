#Master Control Program
#Paul Ambrose
#03/11/2022

#Python program to allow control of automated and user initiated actions on RPi
#Initial set up controls work flow for managing python project

from git.repo import Repo
import os

def userInterface():
    print("Master Control Program\n\n")
    print("1-Pull Current Staged Repo\n\n")
    choice = input("Please select>> ")
    return choice

def pullActiveRepo():
    activeRepoFile = open('staged repo', 'r')
    activeRepo = activeRepoFile.read()
    activeRepoFile.close()
    
    filePath = os.getcwd()

    Repo.clone_from(activeRepo, filePath + "/activeStage/")

def main():
    userChoice = userInterface()
    if userChoice == "1":
        pullActiveRepo()
main()