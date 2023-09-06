# python_base

# this python base project is based on this tutorial
https://www.youtube.com/watch?v=SqFFCTNyi88

# In this tutorial, we learn about:
## 1. Makefile
## 2. Github Actions / Github CI (Continuous Intergration)
### The setup is inside file python_base/.github/workflows/devops.yml
### Whenever we run git push, it will automatically run this CI
### It will install python 3.8 and run everything we setup in Makefile
### Here's the link so we can check the process of own CI:
[![Python application test with Github Actions](https://github.com/congson95dev/python_base/actions/workflows/devops.yml/badge.svg)](https://github.com/congson95dev/python_base/actions/workflows/devops.yml)

## 3. Requirements.txt
## 4. Black (a library to format code)
## 5. Pylint (a library to check coding convention)
## 6. Pytest and Pytest Coverage
## 7. Dockerfile
## 8. Github pull request template
### Create file pull_request_template.md inside root folder, then push to master branch (other branch won't work)
### Now, whenever you create a new PR, it will automatic filled the body with above template
### To click to the checkbox of PR body, you need to fill the [X] (uppercase) inside the option