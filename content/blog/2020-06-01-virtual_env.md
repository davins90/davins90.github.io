Title: How to create a virtual environment on your PC
Tags: virtualenv, env, python

In this post I try to describe the steps useful to create a virtual environment on your machine.
<!-- PELICAN_END_SUMMARY -->

# Why a virtual environment?
A virtual environment is useful in case you want to try particular libraries and extensions of a particular programming language (eg Python), without having to worry about creating conflicts with previous (or later) versions already installed on your machine. 

For example: the XY library only works with version 3.0 of the Z tool, but you have version 4.0 installed on your PC. To avoid creating conflicts by uninstalling the current version, creating a virtual environment is the ideal solution!

# The procedure
These steps can be performed comfortably via command prompts. Let's get started!

1. First of all you need to install the package that allows the creation of a virtual environment. This is possible by running the following code: 
    > pip install virtualenv

    More information about this package at the following [link](https://pypi.org/project/virtualenv/).
2. Through the command prompt you move to the folder of your interest, where you want to create your "virtual world".
3. At this point we can create our virtual environment, which we will call "env", using the following command (always from prompt):
    > virtualenv env
4. After this operation, an additional folder named "env" will be created in the folder where we are located. Let's go inside:
    > cd env
5. Inside env, we enter the "Scripts" folder.
    > cd Scripts
6. Using the tab key on the keyboard we can scroll from the prompt the contents of the Scripts folder. Among the present files we have to search "**activate**", press enter... and our virtual world is created! Here we don't have to worry about creating conflicts!
7. Once we have finished our work and we want to return to the "real world", outside our virtual environment, just search inside "Scripts" for the "**deactivate**" command and press enter. This will bring us back to the "reality" of our machine.

# The end

Thank you for your attention, that's all for today! See you at the next post! :) 

For information please do not hesitate to contact me: <daniele.davino@live.it>