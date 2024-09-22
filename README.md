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
your terminal and type `python main.py` or `python3 main.py` if the first command didn't work. After this, you'd open up your browser of choice (I use Google Chrome) and type in `http://127.0.0.1:5000` into where the URL of the website would normally be. If you've done everything, you should see your name on the page.


## Important topics to know:
Q: What is a gitignore?<br>
Q: What is requirements.txt?<br>
Q: Why use a virtual environment?<br>
Q: What is server side rendering?<br>
