import git
import os
import sh
import shutil
import subprocess

#https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde

filePath = os.getcwd()

def readActiveRepo():
    activeRepoFile = open(filePath +'/activeRepoFile.txt', 'r')
    activeRepo = activeRepoFile.read()
    activeRepoFile.close()
    return activeRepo

def readActiveToken():
    activeTokenFile = open(filePath +'/activeTokenFile.txt', 'r')
    activeToken = activeTokenFile.read()
    activeTokenFile.close()
    return activeToken


def pullActiveRepo():

    shutil.rmtree(filePath + "/activeStage")
    os.mkdir(filePath + "/activeStage")
    os.mkdir(filePath + "/activeStage/test-env")
    os.chdir (filePath + "/activeStage/test-env")

    repoToClone = readActiveRepo()
    repoToClone_clean = repoToClone.replace("\n", "")

    # Clone the repository
    repo = git.Repo.clone_from(repoToClone_clean, filePath + "/activeStage/test-env")

    subprocess.call(["python3", "-m", "venv", "env"])
    subprocess.call(["echo", "'env'", ">", ".gitignore"])

    tokenForEnd = readActiveToken()
    print(tokenForEnd)

def pushActiveRepo():

    commitMessage = input("Please enter commit message >> \n")

    repoToPush = readActiveRepo

    os.chdir(filePath + "/activeStage/test-env")

    subprocess.call(["pip", "freeze", ">", "requirements.txt"])

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
