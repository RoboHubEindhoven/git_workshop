# Git/Github workflow

This document will try to explain how we (RoboHub-Eindhoven) want to
 work with Git and Github.

## Git
Git is an open source version-control system. It keeps track of the full 
history of the source code during an software development project. 
The original author of Git is [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)  
Git was designed as a necessity for linus to manage his bigger project 
which was linux. 

## GitHub
GitHub is an company that provides hosting software version control 
using Git. GitHub is a free version for people like us. Companies can pay
for more functionality and privacy. There are more company's that deliver 
a simular kind of service for instance [BitBucket](https://bitbucket.org/product/) 
or [Gitlab](https://about.gitlab.com/). 

## Use of GitHub:
We can use GitHub as a tool that helps us keep track of the code that is
 writen for our project. Everyone in our group should have his own account 
 on which he has certain rights towards the code on our project.
GitHub makes it easy to review and comment code changes. This is important 
to provide good quality of code. This also improves the speed of development
since people have good insight in what is being developed. 

### Starting a project:
First make sure there is an specific repo for the project. Sometimes it is smarter to 
devide projects into smaller repo's. For instance we could keep the RoboCup tools
 seperated from the robot projects. Always discuss the creation of repositories with 
git masters. A repo always only contains one README.md and one License. <br>
* README.md: in the readme you put a basic explination about your repo and
how to install it on your system. View this example!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
* LICENSE: as a license we always make our package under the BSD 3-Clause 
License. Just copy the file into your 
repository when generating the repo.

For the packages in a repo we want an certain buildup of files and 
directories because most of the 
projects are ROS packages we will keep the [ROS package template](http://wiki.ros.org/Packages) as 
our main lead. But before we upload it to git we always want to have 
some files and directory that 
are needed or recommended for Git. 
* docs/ : In the docs directory you put the documentation of your project
normaly written in Markdown because it is easy. Keeping your documentation 
in your git repo is 
important for also having version control over your documentation. You 
want to have the documentation
updated in relation to the growth of your project. 


If you have these files ready in your directory on your computer. Do what
is explained in the following [link](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line)

# Git naming conventions:
To keep our github clean and understandable for everyone it is important 
that there is an convention for naming everything on github.
## Repository naming convention:
For a new repo we use an basic naming scheme:
```
{project}_{subject}_{technique}
```
So for suii 3d vision it might be: `suii_vision_3d` and for the yolo_vision it is `suii_vision_yolo`.
If the repo is not for a certain technique just use the first two like `suii_base` 
This is always in lowercase with underscores(_) as separator.

## Branch name convention:
The naming of the branches is important to not make an mess of your repo.
Normally you want your branch to be as small as possible so you only have 
branches for certain fixes or features. 
The naming of a branch can be what ever you want. But try to make it as short
as possible. 
Always start your branch name with something meaningful. There are a few standards:

| Tag | Description |
|------|-----------------|
| feature/.. | Used for a new feature as an addition on the branch you're branching from.|
| fix/..     | Used when you are fixing an bug on the branch you're branching from.|
| test/..    | Used when you want to test certain features or do a full test of the system but you are adding files. Might be merged back into parrent branch but not needed if no fixes where done.|
| docs/..    | Used when you're working on some big part of the documentation but also are working on features on an other branch. |
|junk/..    | Nobody want to admit that they use junk branches for experiments or simple tests. but since it is going to happen this might be easy to seperate them from the rest.|


## Commit message convention:
Commit message are really important to give an fast overview of what happend in the 
branch and might describe the reasoning for some changes.
We would really appreciate if everyone would start with a starting word. :

| Tag | Description |
|------|-----------------|
| fix:..|        Speaks for itself |
| doc:..|       When you commit some documentation |
| cleanup:.. |   When you commit only cleanups and no functional changes |
| calib: |  When you change calibration files |
| wip: |        "Work In Progress" when you want to save but still need to test or even just working on it. |
| feat: |       a new feature has been added. |
| refactor: |   when a your change gives the same functional outcome but changes the code significantly |
 
## Pull request description convention:





