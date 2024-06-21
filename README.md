# Django

<a href="https://www.djangoproject.com/">Django</a> is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that a lot of code is already written for us that we can take advantage of.

  * To get started, we’ll have to install Django, which means you’ll also have to <a href="https://pip.pypa.io/en/stable/installation/">install pip</a> if you haven’t already done so.
  * Once you have Pip installed, you can run `pip3 install Django` in your terminal to install Django.
After installing Django, we can go through the steps of creating a new Django project:

1. Run `django-admin startproject PROJECT_NAME` to create a number of starter files for our project.
2. Run `cd PROJECT_NAME` to navigate into your new project’s directory.
3. Open the directory in your text editor of choice. You’ll notice that some files have been created for you. We won’t need to look at most of these for now, but there are three that will be very important from the start:
- <kbd>  manage.py</kbd> is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often.
+ <kbd> settings.py</kbd> contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time.
+ <kbd> urls.py</kbd> contains directions for where users should be routed after navigating to a certain URL.
4. Start the project by running `python manage.py runserver`.


