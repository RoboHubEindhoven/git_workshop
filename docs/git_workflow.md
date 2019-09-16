# Git/GitHub workflow

This document will try to explain how we (RoboHub-Eindhoven) want to
 work with Git and GitHub.

## Git
Git is an open source version-control system. It keeps track of the full 
history of the source code during a software development project. 
The original author of Git is [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)  
Git was designed as a necessity for Linus to manage his bigger project 
which was Linux. 

## GitHub
GitHub is an company that provides hosting software version-control 
using Git. GitHub is a free version for people like us. Companies can pay
for more functionality and privacy. There are more company's that deliver 
a similar kind of service for instance [BitBucket](https://bitbucket.org/product/) 
or [Gitlab](https://about.gitlab.com/). 

## Use of GitHub:
We can use GitHub as a tool that helps us keep track of the code that is
writen for our project. Everyone in our group should have his own account 
on which he has certain rights towards the code on our project.
GitHub makes it easy to review and comment code changes. This is important 
to provide good quality of code. This also improves the speed of development
since people have good insight in what is being developed. 

### Starting a repository:
First make sure there is a specific repository (repo for short) for the project. Sometimes it is smarter to 
divide projects into smaller repo's. For instance we could keep the RoboCup tools
seperated from the robot projects. Always discuss the creation of repositories with 
git masters. A repo always only contains one README.md and one License. <br>
* README.md: in the readme you put a basic explination about your repo and
how to install it on your system. View this [example](https://github.com/RoboHubEindhoven-User/suii_image_processing)
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
preferably written in Markdown (.md ending) because it is easy and clean. Keeping your documentation 
in your git repo is 
important for also having version control over your documentation. You 
want to have the documentation
updated in relation to the growth of your project. 


If you have these files ready in your directory on your computer. Do what
is explained in the following [link](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line)

# Adding stuff to your repo
If you want to add something to the repo you always want to add an new branch
to work on. This can be named anything but we hold ourselfs to some [name
conventions](#branch-name-convention)
You create a branch by running:
```
git checkout -b feature/your_new_feature
```
    
## Adding a file to your repo:
To add the file to the git index localy on your computer run the command:
```
git add sourcefolder/filename.py
```
To add everything from a git repository, you can use the following:
```
git add *
```
Do a local commit: 
```
git commit -m "doc: the commit message"
```
If you have a certain amount of code that you want to merge, be reviewed 
or just have online, then you can push:
```
git push
```
git push sometimes spits back that you need to make it upstream. If 
it happens please do. Check [Pull Requests](#making-a-github-pull-request)

When in doubt you can check git's status by running `git status` or `git
diff` 

## Making a GitHub Pull Request:
The git push can trigger a pull request, if you work in terminal 
you can just click the link and GitHub will open a new pull request.
If a git push is not done on that branch yet, git will respond with the 
remark that you should use the upstream argument. 
What `git push --set-upstream origin branch/name` spits back.
``` bash
ruben@lenov:~/workspace/git_workshop$     git push --set-upstream origin feature/readme
Username for 'https://github.com': ruben-arts
Password for 'https://ruben-arts@github.com': 
Counting objects: 9, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 136.30 KiB | 11.36 MiB/s, done.
Total 9 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'feature/readme' on GitHub by visiting:
remote:      https://github.com/RoboHubEindhoven/git_workshop/pull/new/feature/readme
remote: 
To https://github.com/RoboHubEindhoven/git_workshop.git
 * [new branch]      feature/readme -> feature/readme
Branch 'feature/readme' set up to track remote branch 'feature/readme' from 'origin'.
```
This can also alway be done manualy on GitHub. By clicking the green "open 
Pull Request" button.
In the pull request always fill in the description with as much useful 
information as possible. 
Put `git masters` as assignee's and put the people you work with as `reviewers`.


# Git naming conventions:
To keep our GitHub clean and understandable for everyone it is important 
that there is an convention for naming everything on GitHub.
## Repository naming convention:
For a new repo we use an basic naming scheme:
```
{project}_{subject}_{technique}
```
So for suii 3D vision it might be: `suii_vision_3d` and for the yolo_vision it is `suii_vision_yolo`.
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
| fix/..     | Used when you are fixing a bug on the branch you're branching from.|
| test/..    | Used when you want to test certain features or do a full test of the system but you are adding files. Might be merged back into parent branch but not needed if no fixes where done.|
| docs/..    | Used when you're working on some big part of the documentation but also are working on features on another branch.|
|   junk/..    | Nobody wants to admit that they use junk branches for experiments or simple tests, but since it is going to happen this might be easy to seperate them from the rest.|

**Examples:**
`feature/get_arm_joint_info`, `fix/no_network_error`, `junk/add_objects_as_stl`


## Commit message convention:
Commit message are really important to give a fast overview **of** what happend in the 
branch and might describe the reasoning for some changes.
We would really appreciate if everyone would start with a starting word:

| Tag | Description |
|------|-----------------|
| fix:..|        Speaks for itself |
| doc:..|       When you commit some documentation |
| cleanup:.. |   When you commit only cleanups and no functional changes |
| calib: |  When you change calibration files |
| wip: |        "Work In Progress" when you want to save but still need to test or even just working on it. |
| feat: |       A new feature has been added. |
| refactor: |   When a your change gives the same functional outcome but changes the code significantly |

**Examples:**
`fix: Changed network settings to a environment depended variable.`,
`doc: Documented code with docstrings`

## Pull request description convention:
Add this to the Pull Request description when you want your code to be 
merged into master. 

```
**Checks:**
* [x] Tested on simulation
* [ ] Tested on hardware
* [ ] Added docstrings to the code
* [ ] Made necessary changes to dependencies
* [ ] Added changes to installation documentation
**New Features:**
```

**Checks:**
* [x] Tested on simulation
* [ ] Tested on hardware
* [ ] Added docstrings to the code
* [ ] Made necessary changes to dependencies
* [ ] Added changes to installation documentation

**New Features:**

## Packaging:
When we make a new repo we are mostly using the ros package convention
which can be found [here](http://wiki.ros.org/Packages). 
Just as a summation:
* src/: is for your source files, normaly you will specify your package 
name again to make it easier for separation in the compiler. 
* scripts/: here you put your scripts that are executable.  

# Handy git tools:
|Tool | Description | Link |
|-----|-------------|------|
|GitCola | An easy to use git user interface. |[GitCola](https://git-cola.github.io/)|
|GitKraken| An easy to use git user interface. Much bigger then GitCola|[GitKraken](https://www.gitkraken.com/git-client)|
|bash-git-prompt| When installing git it is really hard to work with it all the git statuses use a bash prompter. This is a nice one but there are way more flavours| [Bash-Git-Prompt](https://github.com/magicmonty/bash-git-prompt)|
|Git adog| This is just an commandline tool from git itself run `git log --all --decorate --oneline --graph` Make an alias for this like `git-adog`||

# Never:
NEVER DO a `git merge feature/branch` in your local master.
This merges your branch into master without a pull request. Always
do it the other way. If you want to get uptodate with master just run:
```
git checkout master
git pull
git checkout yourbranch
git merge master
```

# FAQ:
* **My code is diffrent from the online code**: do a `git pull` and then a `git push` 
this syncs the repos.
* **I can't checkout :` error: Your local changes to the following files would be overwritten by checkout`**. 
first add and commit your changes to your local repo's than you are allowed to change branches.
* **I don't want to commit my changes yet but i need to change branches**: use `git stash` this saves
but doesn't commit yet. More info [here](https://git-scm.com/book/en/v1/Git-Tools-Stashing)
* **I f*cked up the last commit**: `git reset HEAD~1 --hard` sets you one commit back. After this commit the changes and you are ready to go again.
* **That was not the fix something else is broken**: look on this [page](https://ohshitgit.com/):
 
