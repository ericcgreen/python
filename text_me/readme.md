### Our Application
We started working with a blog post, but then discovered the admin features of backend database creation and user authentication and started UI development.

### Why did you choose this subject?
1. Eric - I chose this language and framework because it knowing both and how use them are very in demand skills have.

2. Dom - It's a very popular language in the workforce. It's new and I've always wanted to learn it.

### How were you first made aware of it?
1. Eric - I was introduced to python a couple weeks ago at the French Embassy Hack-a-thon where the DSI instructor Joseph Nelson gave a workshop on web scrapping using python.

2. Dom - Talking to more experienced developers and they recommended I should learn it.

### What problem does it solve?
Readability while being concise and expressive.

### How does it solve the problem (conceptually)?
It's simple and easy to use. Python's syntax uses English versus "{}". Python's structure is also very strict. Whether it was written by a novice or a seasoned professional, it will look very similar and be just as easy to read.

### Why does one use it?
It's quick and easy to use, and novices can easily understand the work of seniors.

### What are the alternatives?
Any other coding language and framework.

### What is it similar to, if anything?
Ruby and Rails.

### What is the history of this technology?
Guido van Rossum wanted to correct some of ABC's problems and keep some of its features. At the time he was working on the Amoeba distributed operating system group and was looking for a scripting language with a syntax like ABC but with the access to the Amoeba system calls, so he decided to create a language that was generally extensible.

### Who built it and why?
Python was conceived in the late 1980s, and its implementation began in December 1989 by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL) capable of exception handling and interfacing with the operating system Amoeba.

### Who is maintaining it?
Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, benevolent dictator for life (BDFL).


### What is your opinion on the technology after having built something with it?
Eric - I thought it was very easy to pick up once I started making the parallels between Ruby on Rails and Python/Django.

### What are the biggest conceptual hurdles (if any) you encountered when researching this?
We came in with our product already in mind. We wanted to build a texting app at fist. An app in which the user can "talk" with their computer. However, the concept was too difficult to execute given our very limited knowledge about the program.

### What resources do you recommend for interested students?
1. https://www.youtube.com/watch?v=7rgph8en0Jc

2. https://www.tutorialspoint.com/django/django_creating_project.htm

3. https://docs.python.org/3/tutorial/index.html

### What article or forum was most helpful to you in learning this?
1. https://scotch.io/tutorials/build-your-first-python-and-django-application

### What are 3 interview questions one might be asked about this technology?
1. What is Python really? You can (and are encouraged) make comparisons to other technologies in your answer

2. Python and multi-threading. Is it a good idea? List some ways to get some Python code to run in a parallel way.

3. What does this stuff mean: (*args), (**kwargs)? And why would we use it?


#### Also, please include the instructions necessary to...

#### Run your example.

Python3 and PIP for virtualenv and for Django both need to be installed on to your computer.
## Do I need to run bower install? Do I need an API key?
No...

#### Use your subject.

### Do I need to include it in my HTML with <script> tags? Do I need to brew install anything? Can I deploy it to Heroku?
Brew install Python.
pip install django.
pip install virtualenv
./manage.py createsuperuser
./manage.py makemigrations text_me
./manage.py migrate text_me
virtualenv -p /usr/local/bin/python3 env
source env/bin/activate
./manage.py shell
