#!/bin/bash

staging_path="/home/pablorose34/Desktop/staging/activeStage"
current_git_token="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"

git remote set-url origin https://${current_git_token}@github.com/${pablo_rose34@hotmail.com}/${https://github.com/PaulAmbrose/piSenseHat}.git

cd $staging_path
git add *
git commit -m"update"
git push