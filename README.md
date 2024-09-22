# Python Virtual Environment

The purpose of a virtual environment is so that you can ensure everyone's libraries are on the same versions and that there's no cross contamination with other libraries

In order to make a virtual environment in python, you'll have to type `python -m venv name_of_venv`. You can name it whatever you'd like. If this doesn't work, try typing `python -m venv name_of_venv`.
Sometimes, if you don't have your aliases setup correctly, "python3" will work while "python" will not.

## For WINDOWS:
If my venv is named `venv`, I'd type `.\venv\Scripts\activate`
Once activated into the virtual environment, you'd type `pip install -r requirements.txt`. This installs all libraries that are "requirements" for this project.

## For MAC:
If my venv is named `venv`, I'd type `source venv/bin/activate`
Once activated into the virtual environment, you'd type `pip install -r requirements.txt`. This installs all libraries that are "requirements" for this project.

## For Both:

Now that you have everything installed, you'll want to go into main.py and modify the variable `name` to be your name. Once you have completed this, you can go to


## Important topics to know:
Q: What is a gitignore?
Q: What is requirements.txt?
Q: Why use a virtual environment?
Q: What is server side rendering?

