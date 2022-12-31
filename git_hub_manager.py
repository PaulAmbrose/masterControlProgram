import git
import os
import sh
import shutil
import subprocess

def readActiveRepo():
    activeRepoFile = open('activeRepoFile.txt', 'r')
    activeRepo = activeRepoFile.read()
    activeRepoFile.close()
    return activeRepo

def readActiveToken():
    activeTokenFile = open('activeTokenFile.txt', 'r')
    activeToken = activeTokenFile.read()
    activeTokenFile.close()
    return activeToken

def pullActiveRepo():

    filePath = os.getcwd()
    shutil.rmtree(filePath + "/activeStage")
    os.mkdir(filePath + "/activeStage")

    repoToClone = readActiveRepo()
    repoToClone_clean = repoToClone.replace("\n", "")

    # Clone the repository
    repo = git.Repo.clone_from(repoToClone_clean, filePath + "/activeStage")

    tokenForEnd = readActiveToken()
    print(tokenForEnd)

def pushActiveRepo():

    commitMessage = input("Please enter commit message >> \n")

    repoToPush = readActiveRepo

    filePath = os.getcwd()
    os.chdir(filePath + "/activeStage")

    # Add all changes to the staging area
        #sh.git.add(".")
    subprocess.call(["git", "add", "*"])

    # Commit the changes with a message
        #sh.git.commit(m = commitMessage)
    subprocess.call(["git", "commit", "-m" + commitMessage])

    # Push the changes to the remote repository
        #sh.git.push()
    subprocess.call(["git", "push"])

def run_git_manager():
    os.chdir("/home/paul/Desktop/staging/")
    while True:
        choice = input("Do you want to start or end a session? (Enter 'start' or 'end')")

        if choice == 'start':
            pullActiveRepo()
        elif choice == 'end':
            pushActiveRepo()
            break
        else:
            print("Invalid choice. Please enter 'start' or 'end'.")
