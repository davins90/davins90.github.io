Title: How to create a blog with Pelican? (Part 1)
Tags: blog, pelican, python, github

This is my tutorial on how I built this blog with Pelican.
<!-- PELICAN_END_SUMMARY -->

# Introduction
With modern technological tools it is becoming increasingly easy to build your own web identity that is not only linked to the world of social networks. 
In this post we will see how to build a blog using [Pelican](https://blog.getpelican.com/), a way to build static websites based on Python, one of the most popular languages of the moment. 

Building it will be the first step, making it operational will be the second, and for this goal we make use of the possibilities offered by [GitHub](https://github.com/), the most known code-repository that allows to host for each user its own web page. 

The purpose?
From creating an alternative Curriculum Vitae, to telling and spreading examples of work, projects or simple tutorials, like this one. Let's get started with the first step!

# The building process
The entire process can be conveniently performed from the command prompt.

1. We create an empty folder, where (if desired) we create a virtual environment and activate it. 
2. Following the instructions of the useful [Pelican documentation](https://docs.getpelican.com/en/stable/index.html), we install the useful packages for the construction phase:
    > pip install pelican[Markdown]
3. When installation is complete, run the following command:
    > pelican-quickstart

    This will launch Pelican's wizard to create a first "skeleton" of the site, requesting basic information (site name, author, time zone, etc...). For further information the previous documentation is very exhaustive.

### Let's take a break.

At this point a first structure of the site is built. If you are curious to see a first result, here are the steps.
- a. From the prompt run the following command:
    > pelican path to the "content" folder --> pelican C:\Users... \content
- b. Wait a few seconds and the prompt will return the message that the site has been correctly uploaded. At this point, to see it working on your browser (but locally, only on your PC's IP address), run the following command:
    > pelica --listen

    At http://localhost:8000/ you will get the result (very primordial but still a result).

### Do you want to start customizing? 
Let's create a first example article!
- c. Let's enter in the "content" folder and create a folder that we will call "pages" .
- d. Inside this folder we create a "Markdown" file. The documentation details this process well.
- e. We repeat the procedure from point a... and here is also our first published example article!

## Let's resume the construction
1. Pelican offers many customization possibilities, and these two are essentials in my opinion: [themes](https://github.com/getpelican/pelican-themes) and [plug-ins](https://github.com/getpelican/pelican-plugins). For both of them I suggest to create a folder with a proper name in which to copy the respective github repository, using the command:
    > git clone https:\...theme or plug link

    In this way we will have all possible alternatives to try. But how to try?
2. If both themes and plug-ins must be specified in the python file "pelicanconf.py" with their respective paths, trying a theme (more than a plug-in) is possible via the following command:
    > pelican content -s pelicanconf.py -t /path to the theme you want to try...
3. Then launched pelican --listen you can see your site with the new "dress".

After choosing the theme you prefer, the useful plug-ins, writing the first presentation articles... you can say that the site is ready to be published!
For this step I refer you to Part 2 of this post, where will be explained the process of uploading to GitHub the site now built.

I know I've been a bit concise in this tutorial, but for further details I suggest you to read [Pelican's well done documentation](https://docs.getpelican.com/en/stable/index.html), which will explain in detail the steps I might have overlooked!

# The end

Thank you for your attention, that's all for today! See you at the next post! :) 

For information please do not hesitate to contact me: <daniele.davino@live.it>