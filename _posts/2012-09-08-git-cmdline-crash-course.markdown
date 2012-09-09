---
title: A Crash Course in Git and the UNIX Command Line
layout: post
---

## Installation

Download and install git. Mac and Windows users should download the 
installer from [http://git-scm.com/](http://git-scm.com/). Linux users should 
install through their distribution's package management system.

## Getting Started

Open up your terminal. 

 * Mac Users: Search for "terminal" in spotlight
 * Windows Users: Look for "git bash" in the start menu
 * Linux Users: Accessories -> Terminal

## Command Line Basics

 * pwd - print your current working directory
 * ls \[dir\] - list contents of directory, default is your current directory
 * ls -l \[dir\] - more detailed ls listing
 * cd \[dir\] - change your current working directory, default is home directory
 * cat \[file\] - print out contents of file
 * less \[file\] - display contents of file in a scrolling window
 * cp *src* *dest* - copy file from one place to another
 * mv *src* *dest* - move file from one place to another 
 * rm *file* - remove a file
 * rm -rf *dir* - recursively remove a directory and all its contents
 * echo \[text\] - prints text supplied by command line arguments
 * grep *pattern* \[file\] - print lines containing the pattern from the file

## Setting up git:
    
    git config --global user.name "Your Name Here"
    git config --global user.email "Your Email Here"

## Git Basics

 * git init \[dir\] - creates a new git repo
 * git clone \[url\] - clone an existing repo
 * git add \[file\] - adds a file to the index
 * git commit -m *message* - commits changes in index 
 * git log - see list of commits
 * git pull \[remote\] \[branch\] - pulls changes from remote repo to your repo
 * git push \[remote\] \[branch\] - pushes your changes to remote repo
 * git remote add *name* *url* - adds a new remote repo

## Branching

 * git branch *name* - create a new branch
 * git checkout *branch* - check out a branch
 * git merge *branch* - merge changes from other branch into current one

## Learning More
 
 * [http://gitref.org/](http://gitref.org/)
 * [http://linuxcommand.org/](http://linuxcommand.org/)
 * [Pro Git](http://git-scm.com/book)
 * [Introduction to the Command Line](http://en.flossmanuals.net/command-line/index/)
