Title: How to create a blog with Pelican? (Part 2)
Tags: blog, pelican, python, github

This is my tutorial on how I Publish this blog on GitHub Pages.
<!-- PELICAN_END_SUMMARY -->

# Introduction
In the previous article (Part 1) we've seen how to build a website, now it's time to publish it! Let's start!

# The publishing process
The publication process consists of two phases:

1. the first online publication;

2. the second, third, etc.. publication based on updates, new posts and so on.

## The first step

For the first online publication it is useful to follow this procedure.

1. Create a totally empty repository on your GitHub page (without README).

2. Copy the empty repository locally with the command:

    > git clone https:\...

3. For a better usability of GitHub it is advisable at this point to create a branch that we will call "content". In this branch we're going to load the whole structure of the site, the theme, the plug-ins, etc.. . The code to launch is as follows:

    > git checkout -b content

    In this way the empty folder will be inside the "content" branch now created.

4. At this point I copy all files and folders created in the article Part 1, except the output folder. This is because I'm working inside the branch and the output folder will be generated not in the branch but in the "master".

5. I report this operation to GitHub with the following command:

    > git commit - m "message reporting the change".

6. I confirm the operation carried out with:

    > git push origin content

7. At this point I run the Pelican command that allows me to generate the Output folder:

    > pelican ... \content

8. For the final steps you need to install the following library, as suggested in Pelican's documentation:

    > pip install ghp-import

9. With the library installed above I move the Outpur folder from the branch to the master folder:

    > ghp-import -m "son-in-law output" - b master output

10. I confirm with:

    > git push origin master

At this point the folder on GitHub is ready for publication: check the settings of the created folder and the official link will be available at the bottom of the page! As usual, the [Pelican documentation page](https://docs.getpelican.com/en/stable/tips.html#publishing-to-github) is super useful.

To add a custom domain you need to set the GitHub ports on the DNS of the domain (bought for example on Google Domains) so that the link now generated is "nicknamed" with the name of the bought domain. This will be the subject of a future post. 
I used this procedure for [this website](https://www.chiesaevangelicaossola.com/)

## The second step

Created the first time the site, for the following ones there are (obviously) less steps to do!

To modify/update just start again from point 3 of the previous list, then just enter the folder of our site and from the command prompt enter the branch and so on.


# The end

Thank you for your attention, that's all for today! See you at the next post! :) 

For information please do not hesitate to contact me: <daniele.davino@live.it>