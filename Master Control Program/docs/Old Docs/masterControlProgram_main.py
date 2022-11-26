#Master Control Program
#Paul Ambrose
#03/11/2022

#Python program to allow control of automated and user initiated actions on RPi
#Initial set up controls work flow for managing python project

from git import Repo
import git
import os
import shutil
import subprocess
import GUIinterface


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
 
def main():
    userChoice = userInterface()
    if userChoice == 1:
        pullActiveRepo()
    elif userChoice == 2:
        pushActiveRepo()
    else:
        print("\nAction aborted")
main()