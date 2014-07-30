#!/bin/bash
#############################################
# backup_to_bitbucket.sh
# Backup core codes & database to bitbucket
#############################################

g=git
gb=git_bitbucket
gi=gitignore
gio=gitignore_original
gib=gitignore_bitbucket
now=`date`

mv .$g $g
mv .$gi $gio

mv $gib .$gi
mv $gb .$g

"""
git init
git add .

git commit -m "backup $now"

git remote add bitbucket https://carpedm20@bitbucket.org/carpedm20/movietag.git 

git push -f -u bitbucket master
"""

git add .
git commit -m "backup $now"
git push -u bitbucket master


mv .$g $gb
mv .$gi $gib

mv $g .$g
mv $gio .$gi

