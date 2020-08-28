Title: How to create a webapp and deploy it
Tags: streamlit, heroku, python, github

This is my tutorial on how to create and publish a webapp written in Python, interfaced with Streamlit and brought online with Heroku.
<!-- PELICAN_END_SUMMARY -->

# Introduction
Creating algorithms and applications has a precise purpose: to use them outside of your PC. Using them "locally" risks being a big limitation. Hence my need to find a way to bring small applications online, so that they can be used by more people, without having to go through me or my PC.

To do this you need 3 ingredients: GitHub, Streamlit and Heroku.

# The process
## GitHub

First you need to create a folder on your GitHub account with only the README file where we describe the application we are going to create. Once created the folder we can copy it locally with the usual command:

> git clone https://... .git

## Streamlit
At this point we have to start filling the folder.

- We create here the python file of our application. In order to use Streamlit you will simply need to import the library and use some of the many features provided by this framework to create an application interface.

    > import streamlit as st

Now you need to create files useful for future development on Heroku's servers. The files you need are the following:

- Procfile . This file (created without extensions) fills it with the following line of code:
    > web: sh setup.sh && streamlit NAME-APP.py

- setup.sh . I create this file with the following lines of code:

    > mkdir -p ~/.streamlit/
    >echo "\
    >[server]\n\
    >headless = true
    >port = $PORT\n\
    >enableCORS = false\n\
    >\n\
    >" > ~/.streamlit/config.toml

- requirements.txt . It is necessary to save all the libraries we use in our application so that heroku can know them and download them to its servers.

## Heroku
Now let's move on to the work phase on Heroku. First you need to install Heroku CLI on your PC and create a free account. 
Once this is done, we can go back to the terminal and complete the necessary steps to bring our application online. Let's get started!

- We enter our account from cmd:

    > Heroku login

- We create our own app (with a name if you want):

    > heroku create NAME-APP

- We upload previously created files and comment on the operation:

    > git add .
    > git commit -m "first upload"

- We confirm the upload on Heroku:

    > git push heroku master

- We confirm the upload on our GitHub

    > git push

At this point in the terminal will appear the link of our application that we can use and share.

## Conclusion

As you have read the process is very simple and immediate and in my opinion it is ideal to bring small applications, demos and whatever else online.
The applications I built with this procedure are the following (you can find their files in my GitHub page):

- [Tool](https://financial-markets-overview.herokuapp.com/) to download the weekly performances of some of the main market indexes.

- [Tool](https://check-ao-ptf.herokuapp.com/) to analyze the performance results of the investment portfolios of the AdviseOnly.com website.


# The end

Thank you for your attention, that's all for today! See you at the next post! :)

For information please do not hesitate to contact me: <daniele.davino@live.it>