<h1 align="center">
	<img src="https://github.com/jatolentino/Django-CRM/blob/main/sources/img/logo.svg" width="200" alt="crm-logo">
</h1>

<p align="center">
    A Customer Relationship Management for your clients and deals
</p>

<div align="center">

[![Docs-en](https://shields.io/badge/Docs-English-blue?logo=Read%20The%20Docs)](#comprehensive-guide-to-progressively-implement-this-project)
![Static Badge](https://img.shields.io/badge/downloads-1.3k-red?logo=GitHub)
![GitHub repo size](https://img.shields.io/github/repo-size/jatolentino/Django-CRM)
![GitHub language count](https://img.shields.io/github/languages/count/jatolentino/Django-CRM?color=success&logo=CodersRank&logoColor=%23FFFFFF)
[![version](https://img.shields.io/badge/version-1.9-red.svg)](//npmjs.com/package/Django-CRM)
![GitHub watchers](https://img.shields.io/github/watchers/jatolentino/Django-CRM)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![rating](https://img.shields.io/badge/rating-★★★★★-yellow)
![coverage](https://img.shields.io/badge/coverage-96%25-yellowgreen)
![uptime](https://img.shields.io/badge/uptime-100%25-green)
![Static Badge](https://img.shields.io/badge/forks-342-red?logo=fork)

</div>


## Features 
Project features @ [`ver-1.9`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.9)
<details>
	<ul>
		<li>user login</li>
		<li>user registration</li>
		<li>user password reset by email</li>
		<li>leads & agents creation</li>
		<li>leads & agents management</li>
		<li>agents classification</li>
		<li>category creation & assignement</li>
	</ul>
</details>


https://github.com/jatolentino/Django-CRM/assets/61167951/e1d5a130-3951-4319-b8be-ea264394de4e


<p align="center">
    	<img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step50-test-1.png">
</p>

## Quick Installation
Previous considerations: 
 - Python 3.9 installed
 - Pip installed (comes with Python 3, no worries)
 - Virtualenv installed (comes with Python 3, no worries)
 - Python added to your local variables <br>
	If you have python 3.11 or other versions, it's necessary to configure a new environment because the default environment with which this project runs works under Python 3.9. <br>
	To configure a new environment with your Python version, do this:
	- Delete the `env` folder on the root of this project
	- Create a new env: `python -m venv env`
	> Note: It's known that the package psycopg2-binary==2.9.5 is compatible with python 3.11 version and psycopg2-binary==2.9.3 (used in this project) is compatible with python 3.9
	> If you have python 3.11, be careful to make this change in the requirements.txt (meaning change to psycopg2-binary==2.9.5 as we use Python 3.9 that works with psycopg2 2.9.3)

This project uses PostgreSQL as database (like described in step 52), so you will need to follow that step to download and configure your database if you want to use PostgreSQL. But, if you just want to use the default sqlite3 database that comes with django and run the project as quick as possible. Follow these steps :)

- Clone the repository to your local folder
- Open the folder repo with VS code or git bash
- In VS terminal or git bash, input the following commands
	```bash
	env/Scripts/activate #for vscode  # for git bash: source env/Scripts/activate
	pip install -r requirements.txt # don't forget to change here to psycopg2-binary==2.9.5 if you use python 3.11
	```
- Comment out the postgresql database config under `crm/settings.py`, so that you can switch to sqlite3, and change it to the default sqlite3
	```python
	# DATABASES = {
	    # 'default': {
		# 'ENGINE': 'django.db.backends.postgresql_psycopg2',
		# 'NAME': env("DB_NAME"),
		# 'USER': env("DB_USER"),
		# 'PASSWORD': env("DB_PASSWORD"),
		# 'HOST': env("DB_HOST"),
		# 'PORT': env("DB_PORT"),
	    # }
	# }

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	    }
	}
	```
- Continue the setup in the terminal, we are about to set this thing up :D
	```bash
	python manage.py collectstatic
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser #create a user and assign a password as you like
	python manage.py runserver #add a port if the django default port (8000) is in use by other apps on your machine
	```
- Learn how to use below ...

## How to use

- Navigate to the home page `http://192.168.0.127:8000/` and login with the superuser you created, add leads and agents as you want in `http://192.168.0.127:8000/admin` or create your agent acc in the home page.

<br>

<a id="Begin-Docs"></a>
## Comprehensive guide to progressively implement this project
The pictures portray the results reached on every step and the versions keep track of the project's progress

### 1 Create & activate the virtual enviroment
- In MINGW
	```bash
	python -m venv enviroment
	source env/Scripts/activate
	```
- In VSCODE
	```bash
	python -m venv enviroment
	env/Scripts/activate
	```
	
### 2 Check packages
```bash
pip freeze
```
### 3 Install django
```bash
pip install django==3.1.4
pip freeze > requirements.txt
```
### 4 Create the project
```bash
django-admin startproject crm .
```
### 5 Add the gitignore
- Create the gitignire file and fill with: `https://github.com/github/gitignore/blob/main/Pythongitignore`

### 6 Run the server
```bash
python manage.py runserver # port if necessary
```
### 7 Run migrate
```bash
python manage.py migrate
```
### 8 Create the app  (for users/leads/payments)
```bash
python manage.py startapp leads
```

### 9 Add the new app 'leads' into the settings of the project
- In crm/setting.py, edit
	```python
	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'leads'
	]
	```
	
### 10 Open models, edit & run
- In leads/models.py, create the model Lead as a class
	```python
	class Lead(models.Model):
	    first_name = models.CharField(max_length=20)
	    last_name = models.CharField(max_length=20)
	    age = models.IntegerField(default=0)
	```
	
- In the terminal
	```bash
	python manage.py makemigrations  # create the 001_initial.py, auth_user is created, db.sqlite3 needs to be deleted in custom user
	python manage.py migrate	 # create the database/applying leads.0001_initial
	```
- In VS CODE install SQLite to see the database

### 11 Create a model Agent  (every Lead will have an agent)
- In leads/models.py
	```python
	class Agent(models.Model):
	    user = models.OneToOneField(User, on_delete=models.CASCADE)
	```
### 12 Add a customizable User model
- In leads/models.py
	```python
	from django.contrib.auth.models import AbstractUser
	
	class User(AbstractUser)L
		pass
	```
	
- In crm/settings.py
	```python
	AUTH_USER_MODEL = "leads.User"
	```
- Delete 001_initial.py and db.sqlite3 files
	```bash
	python manage.py makemigrations
	python manage.py migrate
	```
### 13 Models Managers
- Check the leads in the python shell
	```bash
	python manage.py shell
	```
	```bash
	from leads.models import Lead
	Lead.objects.all()
	```
	Output: `<QuerySet []>`
- Creating a superuser
	```bash
	python manage.py createsuperuser
	```
- Check the user, in the terminal `python manage.py shell`
	```bash
	from django.contrib.auth import get_user_model
	User = get_user_model()
	User.objects.all()
	```
	Output: `<QuerySet [<User: jose>]>`
	```bash
	from leads.models import Agent
	admin_user = User.objects.get(username="jose")
	admin_user	
	```
	Output: `<User: jose>`
	```bash
	agent = Agent.objects.create(user=admin_user)
	exit()
	```
### 14 Configure the Agent to show up the email
- Edit leads/models.py
	```python
	class Agent(models.Model):
		user = models.OneToOnefield(User, on_delete=models.CASCADE)

		def __str__(self):
			return self.user.email
	```
	
- In ther terminal `python manage.py shell`
	```bash
	from leads.models import Agent
	Agent.objects.all()
	```
	Output: `<Queryset [<Agent: jose@mail.com>]>`
	```bash
	from leads.models import Lead
	jose_agent = Agent.objects.get(user__email="jose@mail.com")
	jose_agent
	```
	Output: `<Agent: jose@mail.com>`
	```bash
	Lead.objects.create(first_name="Joe", last_name="Soap", age=35, agent=jose_agent)
	```
	Output: `<Lead: LEAD OBJECT (1)>`
- Edit leads/models/py
	```python
	class Lead(models.Model):
		first_name = models.CharField(max_length=20)
	    	last_name = models.CharField(max_length=20)
	    	age = models.IntegerField(default=0)
		
		def __str__(self):
			return f"{self.first_name} {self.last_name}"
    
	class Agent(models.Model):
		user = models.OneToOneField(User, on_delete=models.CASCADE)	
		def __str__(self):
			return self.user.email	
	```
- In the terminal
	```bash
	python manage.py shell
	from lead.models import Lead
	Lead.objects.all()
	```
	Output: `<QuerySet [<Lead: Joe Soap>]>`
### 15 Forms and create view
- Run the server and go to `http://127.0.0.1/admin`
- Login with the superuser: jose
- Add the user to show up in the admin site, go to leads/admin.py
	```python
	from .models import User, Lead, Agent
	
	admin.site.register(User)
	admin.site.register(Lead)
	admin.site.register(Agent)
	```
- Check `http://127.0.0.1/admin`
	output:
	```bash
	Leads
	Agents	+Add  Change
	Leads	+Add  Change
	Users	+Add  Change
	```
- Configure the output of Agent in leads/models.py
	```python
	def __str__(self):
		return self.user.username
	```
- The User/Agents/Leads can be created/modified/deleted in the `http://127.0.0.1/admin`

### 16 Add a home_page to display "hello world"
- In leads/views.py
	```python
	from django.http import HttpResponse
	
	def home_page(request):
		return HttpResponse("Hello World")
	```
- In crm/urls.py
	```python
	from leads.views import home_page
	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', home_page)
	]
	```

### 17 Add a html page
- Inside the app leads create the forlders templates/leads
- Inside leads/templates/leads create & edit the file home_page.html
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset = "UTF-8">
		<meta name = "viewport" content="width=device-width", initial-scale=1.0>
		<title>Document</title>
	</head>
	<body>
		<h1>Hello world</h1>
		<p>Here is our HTML template</p>
	</body>
	</html>
	```
- Go to leads/views.py
	```python
	def home_page(request):
		return render(request,"leads/home_page.html" )
	```
- Create a general 'templates' folder in crm (crm/templates)
- Make the folder searcheable
- Edit crm/settings.py
	```python
	TEMPLATES = [
		{
			'BACKEND': 'django.template.backends.django.Djangotemplates',
			'DIRS': [BASE_DIR / "templates"],
		}
	]
	```
	
- Create the html in crm/templates/second_page.html
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset = "UTF-8">
		<meta name = "viewport" content="width=device-width, initial-scale=1.0>
		<title>Document</title>
	</head>
	<body>
		<h1>Hello world</h1>
		<p>This is the second page</p>
	</body>
	</html>
	```
- Go to leads/views.py
	```python
	def home_page(request):
		return render(request, "second_page.html" )
	```
	
### 18 Context
- Create the context variable in leads/views.py
	```python
	def home_page(request):
		context = {
			"name" : Joe",
			"age" : 35
		}
		return render(request,"second_page.html",context)
	```
- In templates/second_page.html
	```html
	<body>
		<h1>Hello world</h1>
		<p>This is the second page</p>
		{{ name }}
		{{ age }}
	</body>
	```
- Using the database, looping the data
- In leads/views.py
	```python
	from .models import Lead

	def home_page(request):
		leads = Lead.objects.all()
		context = {
			"leads": leads
		}
		return render(request,"secon_page.html",context)
	```
- In templates/second_page.html
	```html
	<body>
		<ul>
			{% for lead in leads %}
			<li>{{ lead }} </li>
			{% endfor %}
		</ul>
	</body>
	```
### 19 Urls in the app, namespaces
- Create & edit leads/urls.py
  ```python
  from django.urls import path
  from .views import home_page

  app_name = "leads"
  urlpatterns = [
    path('all/', home_page)  OR path('', home_page)
  ]
  ```

- Edit crm/urls.py
delete -> from leads.views import home_page
delete -> path('', home_page)
	```python
	from django.urls import path, include

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('leads/', include('leads.urls', namespace="leads"))
	]
	```

Test: navigate to `http://127.0.0.1:8000/leads/all` OR `http://127.0.0.1:8000/leads/` <br>
Compiled in the branch of [`ver-1.0`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.0)

### 20 Lead's list
- Change home_page.html name to lead_list.html (leads/templates/leads/lead_list.html) and edit leads/views.py `def home_page(request)` -> `def lead_list`
	```python
	def lead_list(request):
		leads = Lead.objects.all()
		context = {
			"leads": leads
		}
		return render(request, "leads/lead_list.html", context)
	```
- Edit leads/urls.py
	```python
	from django.urls import path
	from .views import lead_list
	app_name = "leads"
	urlpatterns = [
		path('', lead_list)
	]
	```
- Add style to lead_list.html
	```html
	<title>Document</title>
	<style>
		.lead {
			padding-top: 10px;
			padding-bottom: 10px;
			padding-left: 6px;
			padding-right: 6px;
			margin-top: 10px;
			background-color: #f6f6f6;
			width: 100%;
		}
	</style>
	
	<body>
		<h1> This is all of our leads</h1>
		{% for lead in leads %}
			<div class="lead">
				{{ lead.first_name }} {{ lead.last_name }}. Age: {{ lead.age }}
			</div>
		{% endfor %}
	</body>	
	```
Test in: `http://127.0.0.1:8000/leads/`

- Create another view for the details of the leads in leads/views.py
	```python
	def lead_detail(request, pk):
		print(pk)
		lead = Lead.objects.get(id=pk)
		return HttpResponse("here is the detail view")
	```
- Import lead_detail in lead/urls.py
	```python5
	from .views import lead_list, lead_detail
	
	app_name = "leads"
	
	urlspatterns = [
		path('', lead_list),
		path('<int:pk>', lead_detail)  #this is going to add a path according to the ID (primary key) of the user (pk)
	```
- Add links to the lead in leads/templates/leads/lead_list.html
	```html
	<body>
		<a href="/leads/create">Create a new lead</a>
		<h1> This is all of our lead lead</h1>
		{% for lead in leads %}
			<div class="lead">
				<a href="/leads/{{ lead.pk }}/"> {{ lead.first_name }} {{ lead.last_name }}</a>. Age: {{ lead.age }}
			</div>
		{% endfor %}
	</body>
	```
	Test: `http://127.0.0.1:8000/leads/1/` <br>
	<p align="center">
	<img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step19-test-2.png">
	</p>
- Modify the lead_detail, in leads/views.py
	```python
	def lead_detail(request, pk):
		lead = Lead.objects.get(id=pk)
		context = {
			"lead": lead
		}
		return render(request, "leads/lead_detail.html", context)
	```
- Create & edit the html file templates/leads/lead_detail.html
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Document</title>
		<style>
			.lead {
				padding-top: 10px;
				padding-bottom: 10px;
				padding-left: 6px;
				padding-right: 6px;
				margin-top: 10px;
				background-color: #f6f6f6;
				width: 100%;
			}
		</style>
	</head>
	<body>
		<a href="/leads">Go back to leads</a>
		<hr />
		<h1> This is the details of {{ lead.first_name }}</h1>
		<p> This persons age: {{ lead.age }} </p>
	</body>
	</html>
	```
- Edit the PATH leads/urls.py
	```python
	from .views import lead_list, lead_detail
	
	app_name = "leads"
	urlpatterns = [
		path('', lead_list),
		path('<int:pk>/', lead_detail)
	]
	```
    Test 20-3: `http://127.0.0.1:8000/leads/1/` <br>
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step20-test-3.png">
    </p>
### 21  Create leads with Forms
- Create the lead_create in leads/views.py
	```python
	def lead_create(request):
		return render(request, "leads/lead_create.html")

- Create the html file: templates/leads/lead_create.html
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Document</title>
	</head>
	<body>
		<a href="/leads">Go back to leads</a>
		<hr />
		<h1> Create a new lead </h1>
	</body>
	</html>
	```
- Edit the PATH leads/urls.py
	```python
	from .views import lead_list, lead_detail, lead_create
	
	app_name = "leads"
	urlpatterns = [
		path('', lead_list),
		path('<int:pk>/', lead_detail),
		path('create', lead_create),
	]
	```
    Test 21-1: `http://127.0.0.1/leads/create` <br>
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step21-test-1.png">
    </p>
    
- Create & edit the file forms in crm/leads/forms.py
	```python
	from django import forms
	
	class LeadForm(forms.Form):
		first_name = forms.CharField()
		last_name = forms.CharField()
		age=forms.IntegerField(min_value=0)
	```
- Import Leadform to leads/views.py
	```python
	from .forms import LeadForm
	
	def lead_create(request):
		context = {
			"form": LeadForm()
		}
		return render(request, "leads/lead_create.html", context)
	```
- Configure the form html and add security to the form: leads/lead_create.html
	```html
	<body>
		<a href="/leads"> Go back to leads</a>
		<hr />
		<h1> Create a new lead</h1>
		<form method="post"> <!-- form method="post" action="/leads/another-url/"> -->
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit" >Submit</button>
		</form>
	</body>
	```
- Grab the data from the POST form: leads/views.py
	```python
	from .models import Lead, Agent
	def lead_create(request):
		form = LeadForm()
		if request.method == "POST":
			print('Receiving a post request')
			form = LeadForm(request.POST)
			if form.is_valid():
				print("the form in valid")
				print(form.cleaned_data)
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				age = form.cleaned_data['age']
				agent = Agent.objects.first()
				Lead.objects.create(
					first_name=first_name,
					last_name=last_name,
					age=age,
					agent=agent
				)
				print("The lead has been created")
		
		context = {
			"form": LeadForm()
		}
		return render(request, "leads/lead_create.html", context)
	```
    Test 21-2: Go to `http://127.0.0.1:8000/leads/create/` and create a lead, then SUBMIT <br>
        Verify in `http://127.0.0.1:8000/leads/` <br>
        Verify the prompt in the VS code or check in `http://127.0.0.1:8000/admin/leads/lead/`
        <br>
        <p align="center">
            <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step21-test-2.png">
        </p>
        Compiled in the branch of [`ver-1.1`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.1)
- Redirect to `http://127.0.0.1:8000/leads/` after creating a user
	In leads/view.py
	```python
	from django.shortcuts import render, redirect
	:
	:
	agent = Agent.objects.first()
		Lead.objects.create(
			first_name=first_name,
			last_name=last_name,
			age=age,
			agent=agent
			)
			return redirect("/leads")
	: 
	```
### 22 Using Django ModelsForm
- Edit leads/forms.py
	```python
	from django import forms
	from .models import Lead
	
	class LeadModelForm(forms.ModelForm):
		class Meta:
			model = Lead
			fields = (
				'first_name',
				'last_name',
				'age',
				'agent',
			)
	```
- Simplify using LeadModelForm: edit leads/views.py, change LeadForm -> LeadModelForm
	```python
	from .forms import LeadModelForm
	
	def lead_create(request):
		form = LeadModelForm()
		if request.method == "POST":
			form = LeadModelForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect("/leads")
		context = {
			"form": form
		}
		return render(request, "leads/lead_create.html", context)
	```

- Edit leads/lead_detail.html 
	```html
	<body>
		<a href="/leads">  Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
	</body>
	```
    Test 21-3: Go to `http://127.0.0.1:8000/leads/` <br>
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step21-test-3.png">
    </p>
### 23 Create the lead_update model
- In lead/views.py
	```python
	def lead_update(request, pk):
		lead = Lead.objects.get(id=pk)
		form = LeadForm()
		if reques.method == "POST":
			form = LeadForm(request.POST)
			if form.is_valid():
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				age = form.cleaned_data['age']
				lead.first_name = first_name
				lead.last_name = last_name
				lead.age = age
				lead.save()
				return redirect("/leads")
		context = {
			"form": form,
			"lead": lead
		}
		return render(request, "leads/lead_update.html", context)
		```
- Edit leads/urls.py
	```python
	from .views import lead_list, lead_detail, lead_create, lead_update
	app_name = "leads"
	
	urlpatterns = [
		path('', lead_list),
		path('<int:pk>/', lead_detail),
		path('<int:pk>/update/', lead_update),
		path('create'/, lead_create)
		]
		```
- Create the templates/leads/lead_update.html file
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Document</title>
	</head>
	<body>
		<a href="/lead">Go back to leads</a>
		<hr />
		<h1>Update lead: {{ lead.first_name }} {{ lead.last_name }}</h1>
		<form method="post">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit">Submit</button>
		</form>
	</body>
	</html>
	```
- Simplify the lead_update model with LeadModelform in templates/leads/views.py
	```python
	def lead_update(request, pk):
		lead = Lead.objects.get(id=pk)
		form = LeadModelForm(instance=lead)
		if request.method == "POST":
			form = LeadModelForm(request.POST, instance=lead)
			if form.is_valid():
				form.save()
				return redirect("/leads")
		context = {
			"form": form,
			"lead": lead
		}
		return render(request, "leads/lead_update.html", context)
	```
    Test 23.1 Go to `http://127.0.0.1:8000/leads/1/update/` and update/edit <br>
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step23-test-1.png">
    </p>

### 24 Create the model delete
- In lead/views.py, create the lead_delete model
	```python
    def lead_delete(request, pk):
        lead = Lead.objects.get(id=pk)
        lead.delete()
        return redirect("/leads")
	```
- Edit the leads/urls.py
	```python
	from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete
	app_name = "lead"
	
	urlpatterns = [
		path('', lead_list),
		path('<int:pk>', lead_detail),
		path('<int:pk>/update/', lead_update),
		path('<int:pk>/delete/', lead_delete),
		path('create/', lead_create)
	]
	```
- Add a delete and update button the lead_detail.html page
	```html
	<body>
		<a href="/leads">  Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
		<hr />
		<a href="/leads/{{ lead.pk }}/update/">Update</a>
		<a href="/leads/{{ lead.pk }}/delete/">Delete</a>
	</body>
	```
    Test 24.1 Go to `http://127.0.0.1:8000/leads/`, choose a lead to be deleted <br>
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step24-test-1.png">
    </p>
### 25 Change URLs' names
- Edit the leads/urls.py
	```python
	:
	urlpatterns = [
		path('', lead_list, name='lead-list'),
		path('<int:pk>/', lead_detail, name='lead-detail'),
		path('<int:pk>/update/', lead_update, name='lead-update'),
		path('<int:pk>/delete/', lead_delete, name='lead-delete'),
		path('create/', lead_create, name='lead-create') #i.e. path('create-a-lead/', lead_create, name='lead-create')
	]
- Change to the URL's name in leads/lead_detail.html: from this `<a href="/leads"> Go back..`  -> `<a href="{% url 'leads:lead-list' %"> Go back..`
	```html
	<body>
		<a href="{% url 'leads:lead-list' %}">Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
		<hr />
		<a href="{% url 'leads:lead-update' lead.pk %}">Update</a>
		<a href="{% url 'leads:lead-delete' lead.pk %}">Delete</a>
	</body>
	```
	
- Change to the URL's name in leads/lead_list.html: from this `<a href="/leads/create">Create..`  -> `<a href="{% url 'leads:lead-create' %">Create..`
	```html
	<body>
		<a href="{% url 'leads:lead-create' %}">Create a new lead</a>
		<h1> This is all of our leads</h1>
		{% for lead in leads %}
			<div class="lead">
				<a href="{% url 'leads:lead-detail' lead.pk %}"> {{ lead.first_name }} {{ lead.last_name }}</a>. Age: {{ lead.age }}
			</div>
		{% endfor %}
	</body>
	```
	
- Change to the URL's name in leads/lead_create.html: `<a href="/lead">Go back...` -> `<a href="{% url 'leads:lead-detail' %}">Go back...`
	```html
	<body>
		<a href="{% url 'leads:lead-list' %}"> Go back to leads</a>
		<hr />
		<h1> Create a new lead</h1>
		<form method="post"> <!-- form method="post" action="/leads/another-url/"> -->
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit" >Submit</button>
		</form>
	</body>
	```
- Change to the URL's name in leads/lead_update.html: `<a href="/lead">Go back...` -> `<a href="{% url 'leads:lead-detail' %}">Go back...`
	```html
	<body>
		<a href="{% url 'leads:lead-detail' lead.pk %}">Go back to {{ lead.first_name }} {{ lead.last_name }} </a>
		<hr />
		<h1>Update lead: {{ lead.first_name }} {{ lead.last_name }}</h1>
		<form method="post">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit">Submit</button>
		</form>
	</body>
	```
    Compiled in the branch of [`ver-1.2`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.2)
### 26 Create a template
- Create base.html in crm/templates/
	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>CRM</title>
		<style>
			.lead {
				padding-top: 10px;
				padding-bottom: 10px;
				padding-left: 6px;
				padding-right: 6px;
				margin-top: 10px;
				background-color: #f6f6f6;
				width: 100%;
			}
		</style>
	</head>
	<body>
		{% block content %}
		{% endblock content %}
	</body>
	</html>
	```	
- Update the leads/lead_list.html file
	```html
	{% extends "base.html" %}

	{% block content %}
        <a href="{% url 'leads:lead-create' %}">Create a new lead</a>
        <hr />
	    <h1> This is all of our leads</h1>
	    {% for lead in leads %}
            <div class="lead">
                <a href="{% url 'leads:lead-detail' lead.pk %}"> {{ lead.first_name }} {{ lead.last_name }}</a>. Age: {{ lead.age }}
            </div>
		{% endfor %}
	{% endblock content %}
	```
- Update the leads/lead_detail.html file
	```html
	{% extends "base.html" %}
	{% block content %}
		<a href="{% url 'leads:lead-list' %}">Go back to leads</a>
        <hr />
        <h1>This is the details of {{ lead.first_name }}</h1>
        <p>This persons age: {{ lead.age }} </p>
        <p>The agent responsible for this lead is : {{ lead.agent }}</p>
        <hr />
        <a href="{% url 'leads:lead-update' lead.pk %}">Update</a>
        <a href="{% url 'leads:lead-delete' lead.pk %}">Delete</a>
	{% endblock content %}
	```
- Update the leads/lead_update.html file
	```html
	{% extends "base.html" %}
	{% block content %}
        <a href="{% url 'leads:lead-detail' lead.pk %}">Go back to {{ lead.first_name }} {{ lead.last_name }} </a>
        <hr />
        <h1>Update lead: {{ lead.first_name }} {{ lead.last_name }}</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Submit</button>
        </form>
	{% endblock content %}
	```
- Update the leads/lead_create.html file
	```html
	{% extends "base.html" %}
	{% block content %}
        <a href="{% url 'leads:lead-list' %}"> Go back to leads</a>
        <hr />
        <h1> Create a new lead</h1>
        <form method="post"> <!-- form method="post" action="/leads/another-url/"> -->
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" >Submit</button>
        </form>
	{% endblock content %}
	```
- Update the leads/lead_list.html file
	```html
	{% extends "base.html" %}
	{% block content %}
        <a href="{% url 'leads:lead-create' %}">Create a new lead</a>
        <hr />
        <h1> This is all of our leads</h1>
        {% for lead in leads %}
            <div class="lead">
                <a href="{% url 'leads:lead-detail' lead.pk %}"> {{ lead.first_name }} {{ lead.last_name }}</a>. Age: {{ lead.age }}
            </div>
		{% endfor %}
	{% endblock content %}
	```
- Example to create ah html script file crm/templates/scripts.html and include it on the base.html <br>
Edit the crm/templates/scripts.html
	```javascript
	<script>
	console.log("hello")
	</script>
	```
- Include the scripts in base.html
	```html
	:
	<body>
		{% block content %}
		{% endblock content %}
		{% include "scripts.html" %}
	</body>
	```
    Compiled in the branch of [`ver-1.3`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.3)
### 27 Adding Tailwindcss
- Go to https://v2.tailwindcss.com/docs/installation#using-tailwind-via-cdn and edit templates/base.html
	```html
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>CRM</title>
			<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
		</head>
		<body>
			<div class = "max-w-4xl mx-auto bg-gray-100">
				{% block content %}
				{% endblock content %}
			</div>
		</body>
		</html>
	```	

- Create the file crm/templates/navbar.html and add the navbar header from https://tailblocks.cc/
	```html
	<header class="text-gray-600 body-font">
	  <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
	    <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
	      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
		<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
	      </svg>
	      <span class="ml-3 text-xl"> CRM </span>
	    </a>
	    <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
	      <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gray-900">Leads</a>
	      <a class="mr-5 hover:text-gray-900">Sign up</a>
	    </nav>
	    <a href="{% url 'leads:lead-list' %}" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Login
	      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
		<path d="M5 12h14M12 5l7 7-7 7"></path>
	      </svg>
	    </a>
	  </div>
	</header>
	```
- Update the templates/base.html file, including the navbar.html
	```html
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>CRM</title>
			<link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
		</head>
		<body>
			<div class = "max-w-7xl mx-auto">
				{% include 'navbar.html' %}
				{% block content %}
				{% endblock content %}
			</div>
		</body>
		</html>
	```
    Test 27.1 Go to `http://127.0.0.1:8000/leads/`
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step27-test-1.png">
    </p>
- Create the file templates/landing.html and add the code from HERO 2nd option at https://tailblocks.cc/
	```html
	{% extends 'base.html' %}
	{% block content %}
	<section class="text-gray-600 body-font">
	  <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
	    <img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" alt="hero" src="https://dummyimage.com/720x600">
	    <div class="text-center lg:w-2/3 w-full">
	      <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900"> CRM build with Django </h1>
	      <p class="mb-8 leading-relaxed">
	      	This CRM helps you manage your leads.
	      </p>
	      <div class="flex justify-center">
		<button class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">Button</button>
		<button class="ml-4 inline-flex text-gray-700 bg-gray-100 border-0 py-2 px-6 focus:outline-none hover:bg-gray-200 rounded text-lg">Button</button>
	      </div>
	    </div>
	  </div>
	</section>
	{% endblock content %}
	```
- Define the landing_page in leads/views.py
	```python
	def landing_page(request):
		return render(request, "landing.html")
	```
- Create the paths in crm/urls.py
	```python
	 :
	 from leads.views import landing_page
	 urlpatterns = {
	 :
	 path('', landing_page, name='landing-page'),
	 :
	 ]
	```
    Test 27.2 Go to `http://127.0.0.1:8000`
    <br>
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step27-test-2.png">
    </p>
- Format the leads/lead_list.html from tailwindcss (FEATURE, 4th option) inside the {% block content %}
	```html
	{% extends "base.html" %}
	{% block content %}
		<section class="text-gray-600 body-font">
		  <div class="container px-5 py-24 mx-auto flex flex-wrap">
		  
		    <!-- 1st script Added -->
		    <div class="w-full mb-6 py-6 flex justify-between items-center border-b border-gray-200">
		    	<div>
				<h1 clas="text-4xl text-gray-800">Lead</h1>
			</div>
			<div>
				<a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">Create a new lead</a>
			</div>
		    </div>
		    <!-- End 1st script -->
		    
		    <div class="flex flex-wrap -m-4">
		    
		     {% for lead in leads %}
		      <div class="p-4 lg:w-1/2 md:w-full">
			<div class="flex border-2 rounded-lg border-gray-200 border-opacity-50 p-8 sm:flex-row flex-col">
			  <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
			    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
			      <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
			    </svg>
			  </div>
			  <div class="flex-grow">
			    <h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ lead.first_name }} {{ lead.last_name }}</h2>
			    <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast 
			    vegan taxidermy. Gastropub indxgo juice poutine.</p>
			    <a href="{% url 'leads:lead-detail' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">View this lead
			      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" 
			      stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
				<path d="M5 12h14M12 5l7 7-7 7"></path>
			      </svg>
			    </a>
			  </div>
			</div>
		      </div>
		     {% endfor %}
		     
		    </div>
		  </div>
		</section>
	{% endblock content %}
	```
    Test 27.3 Go to `http://127.0.0.1:8000/leads/`
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step27-test-3.png">
    </p>
    
- Format the leads/lead_detail.html from tailwindcss (ECOMMERCE, 2nd option) inside the {% block content %}	
	```html
	{% extends "base.html" %}
	{% block content %}

		<section class="text-gray-600 body-font overflow-hidden">
		  <div class="container px-5 py-24 mx-auto">
		    <div class="lg:w-4/5 mx-auto flex flex-wrap">
		      <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
			<h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
			<h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
			<div class="flex mb-4">
			  <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
			  <a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		<!-- interchaged -->
			  <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
			</div>
			<p class="leading-relaxed mb-4">Fam locavore kickstarter distillery. Mixtape chillwave tumeric sriracha taximy chia microdosing tilde DIY. 
			XOXO fam inxigo juiceramps cornhole raw denim forage brooklyn. Everyday carry +1 seitan poutine tumeric. 
			Gastropub blue bottle austin listicle pour-over, neutra jean.</p>
			<div class="flex border-t border-gray-200 py-2">
			  <span class="text-gray-500">Age</span>
			  <span class="ml-auto text-gray-900">{{ lead.age }}</span>
			</div>
			<div class="flex border-t border-gray-200 py-2">
			  <span class="text-gray-500">Location</span>
			  <span class="ml-auto text-gray-900">Random location</span>
			</div>
			<div class="flex border-t border-b mb-6 border-gray-200 py-2">
			  <span class="text-gray-500">Cellphone</span>
			  <span class="ml-auto text-gray-900">+351244352432</span>
			</div>
			<div class="flex">
			  <!-- <span class="title-font font-medium text-2xl text-gray-900">$58.00</span> -->
			  <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
			  <button class="rounded-full w-10 h-10 bg-gray-200 p-0 border-0 inline-flex items-center justify-center text-gray-500 ml-4">
			    <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
			      <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 
			      1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"></path>
			    </svg>
			  </button>
			</div>
		      </div>
		      <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
		    </div>
		  </div>
		</section>	
		
		<!--
		<a href="{% url 'leads:lead-list' %">Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
		<hr />
		<a href="{% url 'leads:lead-update' lead.pk %}">Update</a>
		<a href="{% url 'leads:lead-delete' lead.pk %}">Delete</a>
		-->
	{% endblock content %}
	```
- Format the leads/lead_update.html from tailwindcss (ECOMMERCE, 2nd option) inside the {% block content %}	
	```html
	{% extends "base.html" %}
	{% block content %}

		<section class="text-gray-600 body-font overflow-hidden">
		  <div class="container px-5 py-24 mx-auto">
		    <div class="lg:w-4/5 mx-auto flex flex-wrap">
		      <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
			<h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
			<h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
			<div class="flex mb-4">
			  <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
			  <a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		<!-- interchaged -->
			  <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
			</div>
			<form method="post">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit">Submit</button>
			</form>
			<a href="{% url 'leads:lead-delete' lead.pk %}" class="w-1/2 mt-3 flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
		      </div>
		      <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
		    </div>
		  </div>
		</section>	
		
		<!--
		<a href="{% url 'leads:lead-list' %">Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
		<hr />
		<a href="{% url 'leads:lead-update' lead.pk %}">Update</a>
		<a href="{% url 'leads:lead-delete' lead.pk %}">Delete</a>
		
		
		<a href="{% url 'leads:lead-detail' lead.pk %}">Go back to {{ lead.first_name }} {{ lead.last_name }} </a>
		<hr />
		<h1>Update lead: {{ lead.first_name }} {{ lead.last_name }}</h1>
		-->
	{% endblock content %}
	```
    Test 27.4 Go to `http://127.0.0.1:8000/leads/update`
    <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step27-test-4.png">
    </p>

### 28 Using classes & replacing the functions
- Create a templates/leads/lead_delete.html
    ```html
    {% extends "base.html" %}
    {% block content %}
        <a href="{% url 'leads:lead-list' %}"> Go back to leads</a>
        <hr />
        <h1>Are you sure you want to delete this lead?</h1>
        <form method="post"> <!-- form method="post" action="/leads/another-url/"> -->
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" >Submit</button>
        </form>
    {% endblock content %}
    ```
- In leads/views.py, add class LandingPageView using `django.viwes.generic`
    ```python
    from django.shortcuts import render, redirect, reverse
    from django.http import HttpResponse
    from django.views.generic import (TemplateView, ListView, DetailView,
    CreateView, DeleteView, UpdateView)
    from .models import Lead, Agent
    from .forms import LeadModelForm

    class LandingPageView(TemplateView):
        template_name = "landing.html"
    #def landing_page(request):
    #   return render(request, "landing.html")

    class LeadListView(ListView):
        template_name = "leads/lead_list.html"
        queryset = Lead.objects.all()
        context_object_name = "leads"
    #def lead_list(request):
    #   leads = Lead.objects.all()
    #   context = {
    #     "leads": leads
    #    }
    #   return render(request, "leads/lead_list.htnl)

    class LeadDetailView(DetailView):
        template_name = "leads/lead_detail.html"
        queryset = Lead.objects.all()
        context_object_name = "lead"
    #def lead_detail(request, pk):
    #	lead = Lead.objects.get(id=pk)
    #	context = {
    #		"lead": lead
    #	}
    #   return render(request, "leads/lead_detail.html", context)

    class LeadCreateView(CreateView):
        template_name = "leads/lead_create.html"
        form_class = LeadModelForm
        def get_success_url(self):
            return reverse("leads:lead-list")
    #def lead_create(request):
    #	form = LeadModelForm()
    #	if request.method == "POST":
    #		form = LeadModelForm(request.POST)
    #		if form.is_valid():
    #			form.save()
    #			return redirect("/leads")
    #	context = {
    #		"form": form
    #	}
    #	return render(request, "leads/lead_create.html", context)

    class LeadUpdateView(UpdateView):
        template_name = "leads/lead_update.html"
        queryset = Lead.objects.all()
        form_class = LeadModelForm
        def get_success_url(self):
            return reverse("leads:lead-list")    
    #def lead_update(request, pk):
    #	lead = Lead.objects.get(id=pk)
    #	form = LeadModelForm(instance=lead)
    #	if request.method == "POST":
    #		form = LeadModelForm(request.POST, instance=lead)
    #		if form.is_valid():
    #			form.save()
    #			return redirect("/leads")
    #	context = {
    #		"form": form,
    #		"lead": lead
    #	}

    class LeadDeleteView(DeleteView):
        template_name = "leads/lead_delete.html"
        queryset = Lead.objects.all()
        def get_success_url(self):
            return reverse("leads:lead-list")
    #def lead_delete(request, pk):
    #    lead = Lead.objects.get(id=pk)
    #    lead.delete()
    #    return redirect("/leads")
    ```
- Edit the crm/urls.py
    ```python
    from django.contrib import admin
    from django.urls import path, include
    from leads.views import LandingPageView, LeadListView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', LandingPageView.as_view(), name='landing_page'),
        path('leads/', include('leads.urls', namespace="leads"))
    ]
    ```
- Edit the leads/urls.py
    ```python
    from .views import (lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadDeleteView, 
    LeadUpdateView)
       
    app_name = "leads"

    urlpatterns = [
        path('', LeadListView.as_view(), name='lead-list'),
        path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
        path('create/', LeadCreateView.as_view(), name='lead-create'),
        path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
        path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
        #path('', lead_list, name='lead-list'),
        #path('<int:pk>/', lead_detail, name='lead-detail'),
        #path('<int:pk>/update/', lead_update, name='lead-update'),
        #path('<int:pk>/delete/', lead_delete, name='lead-delete'),
        #path('create/', lead_create, name='lead-create')
    ]
    ```
	Compiled in the branch of [`ver-1.4`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.4)

### 29 Set the static files
- Create the folder ./static and add the files main.js (console.log("hi") & style.css
- Configure the crm/settings.py
    ```python
    :
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR/ "static"
    ]
    STATIC_ROOT = "static_root"
    ```
- Edit crm/urls.py and import the settings and static
    ```python
    :
    from django.conf import settings
    from django.conf.urls.static import static
    :
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('leads/', include('leads.urls', namespace="leads"))
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ]

    # access to static only if it's on debug mode
    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```
    Test: Go to `http:127.0.0.1:8000/static/main.js`<br>
    `console.log("hi")`
- Create folders: css, images, js in crm/static and move the files style.css and main.js to those folders
- Add link to style.css in the templates/base.html
    ```html
    {% load static %}
    
    <!DOCTYPE html>
    :
        <link href = "{% static 'css/styles.css' %}" rel="stylesheet" />
    ```
- Call static/js/main.js from the templates/scripts.html file<br>
  Edit(delete content) o templates/scripts.html
  ```html
    {% load static %}
    <script src="{% static 'js/main.js' %}"></script>
  ```
  Test: Go to `http://127.0.0.1:8000` F12 inspect and see the message in the terminal

### 30 Send emails
- Edit the leads/views.py (more info check env/lib/python3.7/site-packages/django/core/__init__.py send_mail section)
    ```python
    from django.core.mail import send_mail
    :
    class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return "/leads"
    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the website to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)  
    ```
- Edit the email backend in crm/settings.py
    ```python
    :
    STATIC ROOT = "static_root'
    :
    AUTH_USER_MODEL = 'leads.User'
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    ```
    Test: Create a lead in `http:127.0.0.1:8000/leads/create` and check on the VS console the email that has been sent alering that a new lead has been created.
### 31 Authentication
- Create the folder `registration` in crm/templates/ and the file login.html & logout.html inside
- Edit the crm/templates/registration/login.html file
    ```html
    {% extends 'base.html' %}
    {% block content %}

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type='submit'>Login</button>
    </form>

    {% endblock content %}
    ```
- Edit the crm/templates/registration/logout.html file
    ```html
    {% extends 'base.html' %}
    {% block content %}

    <h2> Thanks for visiting, you have been logged out </h2>

    {% endblock content %}
    ```

- Import LoginView & LogoutView in crm/urls.py, more info in `env/lib/python3.7/site-packages/django/contrib/auth/views.py`
    ```python
    :
    from django.contrib.auth.views import LoginView, LogoutView
    :
    urlpatterns = [
        path('admin/, admin.site.urls),
        path('', LandingPageView.as_view(), name='landing-page'),
        path('leads/', include('leads.urls', name='leads'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout')
    ]
    ```
- Configure redirect after login, go to crm/settings.py
    ```python
    :
    EMAIL_BACKEND = ...
    LOGIN_REDIRECT_URL = "/leads"
    ```
    Test: Go to `http://127.0.0.1:8000/login/` and test with the superuser or a random user to see the success/error of login

- Configure the navbar after login, in crm/templates/navbar.html
    ```html
	<header class="text-gray-600 body-font">
	  <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
	    <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
	      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
		<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
	      </svg>
	      <span class="ml-3 text-xl"> CRM </span>
	    </a>
	    <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
	      <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gray-900">Leads</a>
          {% if not request.user.is_authenticated %}
	        <a class="mr-5 hover:text-gray-900">Sign up</a>
          {% endif %}
	    </nav>
        {% if request.user.is_authenticated %}
            Logged in as: {{ request.user.username }}
            <a href="#" class="ml-3 inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Logout
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
            </a>
        {% else %}
            <a href="{% url 'leads:lead-list' %}" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Login
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
            </a>
        {% endif %}
	  </div>
	</header>
	```
- Create the signup view in leads/views.py
    ```python
    :
    from django.contrib.auth.forms import UserCreationForm
    :

    class SignupView(CreateView):
        template_name = "registration/signup.html"
        form_calss = UserCreationForm

        def get_success_url(self):
            return reverse("login")
    ```

- Create the templates/registration/signup.html file
    ```html
    {% extends 'base.html' %}
    {% block content %}

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type='submit'>Signup</button>
    </form>

    {% endblock content %}
    ```
- Edit the crm/urls.py
    ```python
    :
    from leads.views import LandingPageView, SignupView
    :
    urlpatterns = [
        path('admin/, admin.site.urls),
        path('', LandingPageView.as_view(), name='landing-page'),
        path('leads/', include('leads.urls', name='leads'),
        path('signup/', SignupView.as_view(), name='signup'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout')
    ]
    ```

- Configure the navbar with the signup templates/navbar.html
    ```html
	<header class="text-gray-600 body-font">
	  <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
	    <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
	      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
		<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
	      </svg>
	      <span class="ml-3 text-xl"> CRM </span>
	    </a>
	    <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
	      <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gray-900">Leads</a>
          {% if not request.user.is_authenticated %}
	        <a href="{% url 'signup' %}" class="mr-5 hover:text-gray-900">Sign up</a>
          {% endif %}
	    </nav>
        {% if request.user.is_authenticated %}
            Logged in as: {{ request.user.username }}
            <a href="{% url 'logout' %}" class="ml-3 inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Logout
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
            </a>
        {% else %}
            <a href="{% url 'login' %}" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Login
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
            </a>
        {% endif %}
	  </div>
	</header>
	```

- Create the own userform: CustomUserCreationForm in leads/forms.py
    ```python
    from django import forms
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UsernameField
    from .models import Lead
    
    User = get_user_model()

    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = User
            fields = ("username",)
            field_classes = {'username': UsernameField}
    ```
- Edit the leads/views.py
    ```python
    #from django.contrib.auth.forms import UserCreationForm
    from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
    
    class SignupView(CreateView):
        template_name = "registration/signup.html"
        form_class = CustomUserCreationForm

        def get_success_url(self):
            return reverse("login")
    ```
    Test: Go to `http://127.0.0.1:8000/signup/` and create a new user, verify the user in `http://127.0.0.1:8000/login/`

### 32 Test django
- The test python files always start with the string "test_name.py"
- Test the landing page, edit leads/templatees/leads/tests.py
    ```python
    from django.test import TestCase
    from django.shortcuts import reverse

    class LandingPageTest(TestCase):
        def test_status_code(self):
            # TODO some sort of test
            response = self.client.get(reverse("landing-page"))
            print(response.content)
            self.asserEqual(response.status_code, 200) #check status
            self.asserTemplateUser(response, "landing.html") #check response of page
        def test_template_name(self):
            response = self.client.get(reverse("landing-page"))
            self.assertTemplateUsed(response, "landing.html")
         def test_get(self):
            # TODO some sort of test
            response = self.client.get(reverse("landing-page"))
            self.asserEqual(response.status_code, 200)
            self.asserTemplateUser(response, "landing.html")
    ```
    Test in console: python manage.py test

- Create a tests folder in crm/leads, to run the tests' files {test_views,test_forms), also add the __init__.py
    ```python
    from django.test import TestCase
    from django.shortcuts import reverse

    class LandingPageTest(TestCase):
         def test_get(self):
            response = self.client.get(reverse("landing-page"))
            self.asserEqual(response.status_code, 200)
            self.asserTemplateUser(response, "landing.html")
    ```
### 33 Authorization restriction
Restrict users to be only the leads they created
- Edit leads/views.py, pass the LoginRequiredMixin to the models that require it
    ```python
    from django.contrib.auth.mixins import LoginRequiredMixin
    
    class LeadListView(LoginRequiredMixin, ListView):
    :
    class LeadDetailView(LoginRequiredMixin, DetailView):
    :
    class LeadCreateView(LoginRequiredMixin, CreateView):
    :
    class LeadUpdateView(LoginRequiredMixin, UpdateView):
    :
    class LeadDeleteView(LoginRequiredMixin, DeleteView):
    :
    ```
    Go to `http://127.0.0.1/leads` and verify the restriction with the error (you must be logged out or in incognito mode)

- Modify the redirection so it ca redirect to the login site, go to crm/settings.py
    ```python
    :
    LOGIN_REDIRECT_URL = "/leads"
    LOGIN_URL = "/login"
    ```
- Create a model for the user so that the agent will inherit the userprofile properties in crm/leads/models.py
    ```python
    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        def __str__(self):
            return self.user.username

    class Agent(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        def __str__(self):
            return self.user.email
    ```
- Add the userprofile tab in the database of the admin website, edit leads/admin.py

    ```python
    from django.contrib import admin
    from .models import User, Lead, Agent, UserProfile

    admin.site.register(User)
    admin.site.register(UserProfile)
    admin.site.register(Lead)
    admin.site.register(Agent)
    ```
- To test, delete the crm/db.sqlite3 database, migrate and create again the superuser
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
        user: jose
        password: 1
    python manage.py makemigrations
    1
    2
    python manage.py migrate
    python manage.py runserver
    ```
> Note: We wouldn't want to create a user profile for the new users because that process ought be automatic, so the triggering of events is handled by **signals** in Django

### 34 Using signals
- Edit leads/models.py
    ```python
    from django.db.models.signals import post_save

    def post_user_created_signal(sender, instance, created, **kwargs):
        print(instance, created) #created boolena T/F if the user was or not created
    
    post_save.connect(post_user_created_signal, sender=User)
    ```
    Test in `http://127.0.0.1:8000/admin/leads/user/`, select a user and then in his profile, click save
    > For instance the above script depicts a process when we push the save buttom of a user through the admin site, after clicking the save command, the **event post_user_created_signal** is triggered and shows the name of the user(instance) in the VS terminal

- Configure the creation of a userprofile after the user was created, in leads/models.py

    ```python
    def post_user_created_signal(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        :
    ```

### 35 Create the Agents app
- Create the new app in crm folder: <br>
    `python manage.py startapp agents`
- Add the agent app in crm/settings.py
    ```python
    INSTALLED_APPS = [
        :
        'leads',
        'agents'
    ]
    ```
- Create crm/agents/urls.py and edit
    ```python
    from django.urls import path
    from .views import AgentListView, AgentCreateView

    app_name = 'agents'
    urlpatterns = [
        path('', AgentListView.as_view(), name='agent-list'),
        path('create/', AgentCreateView.as_view(), name='agent-create')
    ]
    ```
- Add the app in crm/urls.py
    ```python
    :
    urlpatterns = [
        :
        path('agents/', include('agents.urls', namespace='agents')),
        :
    ]
    ```
- Edit the agents/views.py file
    ```python
    from django.views import generic
    from django.contrib.auth.mixins import LoginRequiredMixin
    from leads.models import Agent
    from django.shortcuts import reverse
    from .forms import AgentModelForm

    class AgentListView(LoginRequiredMixin, generic.ListView):
        template_name = "agents/agent_list.html"
        def get_queryset(self):
            return Agent.objects.all()
    
    class AgentCreateView(LoginRequiredMixin, generic.CreateView):
        template_name = "agents/agent_create.html"
        form_class = AgentModelForm

        def get_success_url(self):
            return reverse("agents:agent-list")

        def form_valid(self, form):
            agent = form.save(commit=False)
            agent.organization = self.request.user.userprofile  #agents have a organiz property, Check leads/models.py
            agent.save() #agent is save in the organization
            return super(AgentCreateView, self).form_valid(form)
    ```

- Create the templates folder inside the agents app (crm/agents/templates) and then the folder crm/agents/templates/agents.<br>
Inside agents/templates/agents/ create the agent_list.html file and edit it <br>
    ```html
    {% extends "base.html" %}
        {% block content %}
            <section class="text-gray-600 body-font">
            <div class="container px-5 py-24 mx-auto flex flex-wrap">
                <div class="w-full mb-6 py-6 flex justify-between items-center border-b border-gray-200">
                    <div>
                    <h1 class="text-4xl text-gray-800">Agents</h1>
                </div>
                <div>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'agents:agent-create' %}">Create a new agent</a>
                </div>
                </div>
                <div class="flex flex-wrap -m-4">
                {% for agent in object_list %}
                <div class="p-4 lg:w-1/2 md:w-full">
                <div class="flex border-2 rounded-lg border-gray-200 border-opacity-50 p-8 sm:flex-row flex-col">
                <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                    </svg>
                </div>
                <div class="flex-grow">
                    <h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ agent.user.username }}</h2>
                    <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast 
                    vegan taxidermy. Gastropub indxgo juice poutine.</p>
                    <a href="{% url 'agents:agent-detail' agent.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">View agent
                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" 
                    stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                    <path d="M5 12h14M12 5l7 7-7 7"></path>
                    </svg>
                    </a>
                </div>
                </div>
                </div>
                {% endfor %}
                </div>
            </div>
            </section>
    {% endblock content %}
    ```

- Create crm/agents/forms.py
    ```python
    from django import forms
    from leads.models import Agent
    class AgentModelForm(forms.ModelForm):
            class Meta:
                    model = Agent
                    fields = (
                            'user',
                    )
    ```
- Create the agents/templates/agents/agent_create.html
    ```html
    {% extends "base.html" %}
    {% block content %}
        <a href="{% url 'agents:agent-list' %}"> Go back to agents</a>
        <hr />
        <h1> Create a new agent</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" >Submit</button>
        </form>
    {% endblock content %}
    ```
    Test: Go to `http://127.0.0.1:8000/agents/` and click on Create a new agent

### 36 Create the other agents view
- Create the AgentDetailView in agents/views.py
    ```python
    :
    class AgentDetailView(LoginRequiredMixin, generic.DetailView):
        template_name = "agents/agent_detail.html"
        def get_queryset(self):
            return Agent.objects.all
    ```
- Edit the agents/urls.py
    ```python
    from django.urls import path
    from .views import AgentListView, AgentCreateView, AgentDetailView
    app_name = 'agents'

    urlpatterns=[
        path('', AgentListView.as_view(), name='agent-list'),
        path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
        path('create/', AgentCreateView.as_view(), name='agent-create'),
    ]
    ```
- Create agent_detail.html inside templates/agents
    ```html
    {% extends "base.html" %}
    {% block content %}
        <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
            <div class="lg:w-4/5 mx-auto flex flex-wrap">
            <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
            <h2 class="text-sm title-font text-gray-500 tracking-widest">AGENT</h2>
            <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ agent.user.username }}</h1>
            <div class="flex mb-4">
            <a href="{% url 'agents:agent-detail' agent.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Overview</a>
            <a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>
            <a href="#" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a>
            </div>
            <p class="leading-relaxed mb-4">Fam locavore kickstarter distillery. Mixtape chillwave tumeric sriracha taximy chia microdosing tilde DIY. 
            XOXO fam inxigo juiceramps cornhole raw denim forage brooklyn. Everyday carry +1 seitan poutine tumeric. 
            Gastropub blue bottle austin listicle pour-over, neutra jean.</p>
            <div class="flex border-t border-gray-200 py-2">
            <span class="text-gray-500">Age</span>
            <span class="ml-auto text-gray-900">{{ lead.age }}</span>
            </div>
            <div class="flex border-t border-gray-200 py-2">
            <span class="text-gray-500">Location</span>
            <span class="ml-auto text-gray-900">Random location</span>
            </div>
            <div class="flex border-t border-b mb-6 border-gray-200 py-2">
            <span class="text-gray-500">Cellphone</span>
            <span class="ml-auto text-gray-900">+351244352432</span>
            </div>
            <div class="flex">
            <!-- <span class="title-font font-medium text-2xl text-gray-900">$58.00</span> -->
            <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
            <button class="rounded-full w-10 h-10 bg-gray-200 p-0 border-0 inline-flex items-center justify-center text-gray-500 ml-4">
                <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 
                1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"></path>
                </svg>
            </button>
            </div>
            </div>
            <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
            </div>
        </div>
        </section>
    {% endblock content %}
    ```
- Edit the agents/views.py file to add the agentdetailview class
    ```python
    class AgentDetailView(LoginRequiredMixin, generic.DetailView):
        template_name = "agents/agent_detail.html"
        context_object_name = "agent"
        def get_queryset(self):
            return Agent.objects.all()
            ```
- Update the navbar.html to display the correct path of agents
    ```html
	<header class="text-gray-600 body-font">
	  <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
	    <a class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
	      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-10 h-10 text-white p-2 bg-indigo-500 rounded-full" viewBox="0 0 24 24">
		<path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
	      </svg>
	      <span class="ml-3 text-xl"> CRM </span>
	    </a>
	    <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
            {% if not request.user.is_authenticated %}
	            <a href="{%url 'signup' %}" class="mr-5 hover:text-gray-900">Sign up</a>
            {% else %}
            <a href="{% url 'agents:agent-list' %}" class="mr-5 hover:text-gray-900">Agents</a>
	        <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gray-900">Leads</a>
            {% endif %}
	    </nav>
        {% if request.user.is_authenticated %}
            Logged in as: {{ request.user.username }}
            <a href="{% url 'logout' %}" class="ml-3 inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Logout
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
            </a>
        {% else %}
            <a href="{% url 'login' %}" class="inline-flex items-center bg-gray-100 border-0 py-1 px-3 focus:outline-none hover:bg-gray-200 rounded text-base mt-4 md:mt-0">Login
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-1" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
            </a>
        {% endif %}
	  </div>
	</header>
	```
- Add the updateview & deleteview in agents/views.py
    ```python
    :
    class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
        template_name = "agents/agent_update.html"
        form_class = AgentModelForm

        def get_success_url(self):
            return reverse("agents:agent-list")

        def get_queryset(self):
            return Agent.objects.all()
    
    class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
        template_name = "agents/agent_delete.html"
        context_object_name = "agent"

        def get_success_url(self):
            return reverse("agents:agent-list")

        def get_queryset(self):
            return Agent.objects.all()
    ```
- Update the agents/urls.py and add de updateview & deleteview
    ```python
    from django.urls import path
    from .views import (AgentListView, AgentCreateView, 
    AgentDetailView, AgentUpdateView, AgentDeleteView) 

    app_name = 'agents'

    urlpatterns = [
        path('', AgentListView.as_view(), name='agent-list'),
        path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
        path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
        path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
        path('create/', AgentCreateView.as_view(), name='agent-create').
    ]
    ```
- Create the agents/templates/agents/agent_update.html
	```html
	{% extends "base.html" %}
	{% block content %}

		<section class="text-gray-600 body-font overflow-hidden">
		  <div class="container px-5 py-24 mx-auto">
		    <div class="lg:w-4/5 mx-auto flex flex-wrap">
		      <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
			<h2 class="text-sm title-font text-gray-500 tracking-widest">AGENT</h2>
			<h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ agent.user.username }}</h1>
			<div class="flex mb-4">
			  <a href="{% url 'agents:agent-detail' agent.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
			  <a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		<!-- interchaged -->
			  <a href="{% url 'agents:agent-update' agent.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
			</div>
			<form method="post">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit">Submit</button>
			</form>
			<a href="{% url 'agents:agent-delete' agent.pk %}" class="w-1/2 mt-3 flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
		      </div>
		      <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
		    </div>
		  </div>
		</section>	
	{% endblock content %}
	```
- Create the templates/leads/agent_delete.html
    ```html
    {% extends "base.html" %}
    {% block content %}
        <a href="{% url 'agents:agent-list' %}"> Go back to agents</a>
        <hr />
        <h1>Are you sure you want to delete this agent?</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" >Submit</button>
        </form>
    {% endblock content %}
    ```
    Test: Go to `http://127.0.0.1:8000/agents` and create/delete/update an agent, check [`ver-1.5`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.5)
	<p align="center">
	    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step36-test-1.png">
	</p>

### 37 Filter the agents display only to their users counterparts
- Edit the agents/views.py file
    ```python
    :
    class AgentListView(LoginRequiredMixin, generic.ListView):
        template_name = "agents/agent_list.html"

        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization) #Changed this return Agent.objects.all()
    ```
    Test - Correctly filtering agents for the users: Go to `http://127.0.0.1:8000/admin/leads/agent` and add an AGENT (there must be two users already created under different categories: organization and without orgnization or simply users)<br>
    Assign to the Agent:<br>
    User: Test1<br>
    Organization: Test2<br>
    Now login to another user, like Jose, check in `http://127.0.0.1:8000/agents`, you should only see your agent(s), not the ones recently assigned to different users or organizations!

- Extend the filtering functionality where there is a queryset (where something is retrieved back to the client), in agents/views.py
    ```python
    from django.views import generic
    from django.contrib.auth.mixins import LoginRequiredMixin
    from leads.models import Agent
    from django.shortcuts import reverse
    from .forms import AgentModelForm

    class AgentListView(LoginRequiredMixin, generic.ListView):
        template_name = "agents/agent_list.html"
        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)
    
    class AgentCreateView(LoginRequiredMixin, generic.CreateView):
        template_name = "agents/agent_create.html"
        form_class = AgentModelForm

        def get_success_url(self):
            return reverse("agents:agent-list")

        def form_valid(self, form):
            agent = form.save(commit=False)
            agent.organization = self.request.user.userprofile  #agents have a organiz property, Check leads/models.py
            agent.save() #agent is save in the organization
            return super(AgentcreateView, self).form_valid(form)

    class AgentDetailView(LoginRequiredMixin, generic.DetailView):
        template_name = "agents/agent_detail.html"
        context_object_name = "agent"
        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)

    class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
        template_name = "agents/agent_update.html"
        form_class = AgentModelForm

        def get_success_url(self):
            return reverse("agents:agent-list")

        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)
    
    class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
        template_name = "agents/agent_delete.html"
        context_object_name = "agent"

        def get_success_url(self):
            return reverse("agents:agent-list")

        #here is even more important because we don't users to delete agents that belong to other users
        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)
    ```

### 38 Create 2 type of users: agents & organizers 
- Create the type of users in crm/leads/models.py
    ```python
    from django.db import models
    from djangodb.models.signals import post_save
    from django.contrib.auth.models import AbstractUser

    class User(AbstractUser):
        is_organizer = models.BooleanField(default=True)
        is_agent = models.BooleanField(default=False)
    ```
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
    Verify: Go to `http://127.0.0.1:8000/admin/leads/user/` choose a user and check the options down below for organizer(set to True as default) and agent.
    >Only users set to be organizers can create and see all agents available <br>
    >Users which are agents can only see the agent which is assigned to them. <br>
    >Sometimes there might be an error in makemigrations, so either delete the database: dbsqlite3, or delete the init files: 0001_initial.py, etc.

### 39 Render the tabs that agents/organizer should only see
    >In this case, organizers can see the correct left tabs: Agents & Leads, and agents can see only Leads<br>

- Edit the registration/navbar.html file
    ```html
    :
    {% if not request.user.is_authenticated %}
        <a href="{% url 'signup' %}" class="mr-5 hover:text-gra-900">Signup</a>
    {% else %}
        {% if request.user.is_organizer %}
            <a href="{% url 'agents:agent-list' %}" class="mr-5 hover:text-gra-900">Agents</a>
        {% endif %}
        <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gra-900">Leads</a>
    {% endif %}
    <!--
    {% if not request.user.is_authenticated %}
        <a href="{% url 'signup' %}" class="mr-5 hover:text-gra-900">Signup</a>
    {% else %}
        <a href="{% url 'agents:agent-list' %}" class="mr-5 hover:text-gra-900">Agents</a>
        <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gra-900">Leadss</a>
    {% endif %}
    -->
    :
    ```
    Test: create two users and configure one to is_organizer, the other to be `is_agent` (name this user as agent to be distringuishable).<br>
    Now procees to login with the agent user and verify that there is no agent tab in the right side of navbar.

- Restrict agents to hardcorde the url `http://127.0.0.1:8000/agents`, create the agents/templates/mixins.py to restrict to login and restrict see other agents if is not a organizer

    ```python
    from django.contrib.auth.mixins import AccessMixin
    from django.shortcuts import redirect

    class OrganizerAndLoginRequiredMixin(AccessMixin):
        """Verifiy that the current user is authenticated and is an organizer"""
        def dispatch(self, request, *args, **kwargs):
            if not request.user.is_authenticated or not request.user.is_organizer:
                return redirect("leads:lead-list")
            return super().dispatch(request, *args, **kwargs)
    ```

- Import the custom mixins: OrganizerAndLoginRequiredMixin (custom restriction for login and view of other agents) in agents/views.py
    ```python
    from django.views import generic
    from django.contrib.auth.mixins import LoginRequiredMixin
    from leads.models import Agent
    from django.shortcuts import reverse
    from .forms import AgentModelForm
    from .mixins import OrganizerAndLoginRequiredMixin

    class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
        template_name = "agents/agent_list.html"
        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)

    class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
        template_name = "agents/agent_create.html"
        form_class = AgentModelForm

        def get_success_url(self):
            return reverse("agents:agent-list")

        def form_valid(self, form):
            agent = form.save(commit=False)
            agent.organization = self.request.user.userprofile  #agents have a organiz property, Check leads/models.py
            agent.save() #agent is save in the organization
            return super(AgentcreateView, self).form_valid(form)

    class AgentDetailView(LOrganizerAndLoginRequiredMixin, generic.DetailView):
        template_name = "agents/agent_detail.html"
        context_object_name = "agent"
        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)

    class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
        template_name = "agents/agent_update.html"
        form_class = AgentModelForm

        def get_success_url(self):
            return reverse("agents:agent-list")

        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)
    
    class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
        template_name = "agents/agent_delete.html"
        context_object_name = "agent"

        def get_success_url(self):
            return reverse("agents:agent-list")

        #here is even more important because we don't users to delete agents that belong to other users
        def get_queryset(self):
            organization = self.request.user.userprofile
            return Agent.objects.filter(organization=organization)
    ```
- Restrict also in leads/views.py regarding leadcreateview, 
    ```python
    :
    from agents.mixins import OrganizerAndLoginRequiredMixin
    :
    class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    :
    class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    :
    class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    ```
- Show `Create a new lead` to only organizers in the templates/leads/lead_list.html
    ```html
    :
    {% if request.user.is_organizer %}
    <div>
		<a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">Create a new lead</a>
	</div>
    {% endif %}
    <!--
    <div>
		<a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">Create a new lead</a>
	</div>
    -->
    :
    ```
    Test: Login as an agent user, go to `http://127.0.0.1:8000/leads`, check the tab if available, and hop over to ``http://127.0.0.1:8000/leads/create`, the sites should redirect to `http://127.0.0.1:8000/leads/`

### 40 Leads queryset 
- Showing the leads to be seen by the agents that they belong to<br>
    Initially when leads are created, they shouldnt have set up an agent, so their agent will be null.<br>
    Go to ./leads/models.py and edit
    ```python
    class Lead(models.Model):
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        age = models.IntegerFiled(default=0)
        organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)# add the userprofile or organization that a Lead belongs
        agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL) # so when the agent is deleted, the lead wont be deleted and will just remain an a lead without agent 

        def __str__(self):
            return f"{self.first_name} {self.last_name}"
    ```
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    1
    exit
    python manage.py runserver
    ```
    Leads filtered by the user of the agent (matchs the user of the lead: self.reques.user)
- Edit the leads/views.py to configure the leads querysets so we end up restricting the shown of the leads based on the assigned agents
    ```python
    from django.shortcuts import render, redirect, reverse
    from django.http import HttpResponse
    from django.views.generic import (TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView)
    from .models import Lead, Agent
    from .forms import LeadModelForm

    class LandingPageView(TemplateView):
        template_name = "landing.html"

    class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization = user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
        
        queryset = queryset.filter(agent__user=user)
        return queryset

    class LeadDetailView(LoginRequiredMixin, generic.DetailView):
        template_name = "leads/lead_detail.html"
        context_object_name = "lead"
        def get_queryset(self):
            user = self.request.user
            # initial queryset of leads for the entrie organization
            if user.is_organizer:
                queryset = Lead.objects.filter(organization=user.userprofile)
            else:
                queryset = Lead.objects.filter(organization=user.agent.organization)
                #filter for the agent that is logged in
                queryset = queryset.filter(agent__user=user)
            return queryset
    

    class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
        template_name = "leads/lead_create.html"
        form_class = LeadModelForm
        def get_success_url(self):
            #return "/leads"
            return reverse("leads:lead-list")

        def form_valid(self, form):
            lead = form.save(commit=False)
            lead.organization = self.request.user.userprofile
            lead.save()
            send_mail(
                subject="A lead has been created",
                message="Go to the website to see the new lead",
                from_email="test@test.com",
                recipient_list=["test2@test.com"]
            )
            return super(LeadCreateView, self).form_valid(form)   

    class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
        template_name = "leads/lead_update.html"
        form_class = LeadModelForm
        
        def get_queryset(self):
            user = self.request.user
            # initial queryset of leads for the entrie organization
            return Lead.objects.filter(organization=user.userprofile)

        def get_success_url(self):
            return reverse("leads:lead-list")

    class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
        template_name = "leads/lead_delete.html"
        
        def get_success_url(self):
            return reverse("leads:lead-list")

        def get_queryset(self):
            user = self.request.user
            return Lead.objects.filter(organization=user.userprofile)
    ```

### 41 Invite an agent
- Modify agents/forms.py, so that when the agent is created, a user is immediately created as well.
    ```python
    from django import forms
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm

    User = get_user_model()
    class AgentModelForm(forms.ModelForm):
        class Meta:
            model = User
            fields = (
                'email',
                'username',
                'first_name',
                'last_name'
            )
    ```
- Edit agents/views.py, to create an agent user
    ```python
    :
    from django.core.mail import send_mail
    :
	class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
			template_name = "agents/agent_create.html"
			form_class = AgentModelForm

			def get_success_url(self):
				return reverse("agents:agent-list")

			def form_valid(self, form):
				#create the user type agent
				user = form.save(commit=False)
				user.is_agent = True
				user.is_organizer = False
				user.save()
				# create the agent for that user
				Agent.objects.create(
					user=user,
					organization=self.request.user.userprofile
				)
				send_mail
					subject="You are invited to be an agent",
					message="You were added as an agent on CRM. Please come login to stat working.",
					from_email="admin@test.com"
					recipient_list=[user.email]
				return super(AgentCreateView, self).form_valid(form)
    ```
    Test: Sign in like Jose and go to `http://127.0.0.1:8000/agents/create`, enter the details and submit, check the agent just created and the email on the terminal. <br>
    Also go to the admin website and check the user, it actually doesn't have a password so set it up like below, edit agents/views.py
    ```python
    import random
    	class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
			template_name = "agents/agent_create.html"
			form_class = AgentModelForm

			def get_success_url(self):
				return reverse("agents:agent-list")

			def form_valid(self, form):
				#create the user type agent
				user = form.save(commit=False)
				user.is_agent = True
				user.is_organizer = False
                user.set_password(f"{random.randint(0, 100000)}")  #ADDED, need to reset pass
				:
    ```
### 42 Password Reset
- Edit the templates/registration/login.html/

    ```html
    {% extends 'base.html' %}
    {% block content %}
    <form method = "post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type = 'submit'>Login</button>
        <hr />
        <a href='{% url 'reset-password' %}'>Forgot password?</a>
    </form>
    {% endblock content %}
    ```
- Create in templates/registration/ the html files: password_reset_done.html, password_reset_email.html, password_reset_form.html, password_reset_confirm.html
- Edit and add the class in crm/urls.py
    ```python
    from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    :
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', LandingPageView.as_view(), name='landing-page'),
        path('leads/', include('leads.urls', namespace="leads")),
        path('agents/', include('agents.urls', namespace='agents')),
        path('signup/', SignupView.as_view(), name='signup'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
        path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]
    ```
- Edit the password_reset_form.html in crm/templates/registration/
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type = 'submit'>Reset password</button>
        <hr />
        <a href='{% url 'login' %}'>Already have an account?</a>
    </form>
    {% endblock content %}
    ```
- Edit the password_reset_confirm.html in crm/templates/registration/
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1> Enter your new password</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type = 'submit'>Confirm new password</button>
    </form>
    {% endblock content %}
    ```
- Edit the password_reset_done.html in crm/templates/registration/
    ```html
    {% extends "base.html" %}
    {% block content %}
        <h1>We have sent you an email to confirm your password reset</h1>
    {% endblock content %}
    ```
- Edit the password_reset_email.html in crm/templates/registration/

    ```html
    You've requested to reset your password
    Please go to the following URL to enter your new password:
    {{ protocol }}://{{ domain }}/password-reset-confirm/{{ uid }}/{{ token }}/
    ```
- Edit the password_reset_complete.html in crm/templates/registration/
    ```html
    {% extends 'base.html' %}
    {% block content %}
    
        <h1>Password reset complete</h1>
        <p>You have successfully reset your password. 
            Click <a href="{% url 'login' %}"> here to login</a>
        </p>

    {% endblock content %}
    ```
    Test: Grab a user and its email already created, go to `http://127.0.0.1:8000/login`, choose Forgot password, and then fill the email.<br>
    Check the link of the email sent in the terminal, copy the link into the browser and reset the email. Login with the new user's password.

### 43 List leads that have not been assigned yet (only for the organizers)
- Edit the ./leads/views.py
    ```python
    class LeadListView(ListView):
        template_name = "leads/lead_list.html"
        context_object_name = "leads"
        def get_queryset(self):
            user = self.reques.user
            # initial queryset of leads for the entrie organization
            if user.is_organizer:
                queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
            else:
                queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
                #filter for the agent that is logged in
                queryset = queryset.filet(agent__user=user)
            return queryset

        def get_context_data(self, **kwargs):
            context = super(LeadListView, self).get_context_data(**kwargs)
            user = self.request.user
            if user.is_organizer:
                queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
                context.update({
                    "unassigned_leads": queryset
                })
            return context
    ```
- Update the lead_list.html of leads/templates/leads/
	```html
	{% extends "base.html" %}
	{% block content %}
	<section class="text-gray-600 body-font">
		<div class="container px-5 py-24 mx-auto flex flex-wrap">
		    <div class="w-full mb-6 py-6 flex justify-between items-center border-b border-gray-200">
		    	<div>
				    <h1 class="text-4xl text-gray-800">Lead</h1>
			    </div>
                {% if request.user.is_organizer %}
                <div>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">Create a new lead</a>
                </div>
                {% endif %}
		    </div>
		    <div class="flex flex-wrap -m-4">
                {% for lead in leads %}
                <div class="p-4 lg:w-1/2 md:w-full">
                    <div class="flex border-2 rounded-lg border-gray-200 border-opacity-50 p-8 sm:flex-row flex-col">
                        <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
                                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                            </svg>
                        </div>
                        <div class="flex-grow">
                            <h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ lead.first_name }} {{ lead.last_name }}</h2>
                            <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
                            <a href="{% url 'leads:lead-detail' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">
                                View this lead
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                    <path d="M5 12h14M12 5l7 7-7 7"></path>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
		    </div>
            {% if unassigned_leads.exists %}
                <div class="mt-5 flex flex-wrap -m-4">
                    <div class="p-4 w-full">
                        <h1 class="text-4xl text-gray-800">Unassigned leads</h1>
                    </div>
                    {% for lead in unassigned_leads %}
                    <div class="p-4 w-full lg:w-1/2 md:w-full">
                        <div class="flex border-2 rounded-lg border-gray-200 border-opacity-50 p-8 sm:flex-row flex-col">
                            <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
                                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                                </svg>
                            </div>
                            <div class="flex-grow">
                                <h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ lead.first_name }} {{ lead.last_name }}</h2>
                                <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
                                <a href="{% url 'leads:lead-detail' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">
                                    View this lead
                                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                {% endif %}
            </div>
		</div>
	</section>
	{% endblock content %}
	```

### 44 Assigns agents to unassigned leads
- In templates/leads/views.py
    ```python
    from .forms import LeadForm, LeadModelForm, CustomUserCreationForm, AssignAgentForm
    :
    class AssignAgentView(OrganizerAndLoginRequiredMixin, genereic.FormView): 
        template_name = "leads/assign_agent.html"
        form_class = AssignAgentForm

        def get_form_kwargs(self, **kwargs):
            kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
            kwargs.update({
                "request": self.request
            })
            return kwargs

        def get_success_url(self):
            return reverse("leads:lead-list")

        def form_valid(self, form):
            #print(form.cleaned_data["agent"])
            agent = form.cleaned_data["agent"]
            lead = Lead.objects.get(id=self.kwargs["pk"])
            lead.agent = agent
            lead.save()
            return super(AssignAgentView, self).form_valid(form)
    ```

- Create the file temlates/leads/assign_agent.html
    ```html
    {% extends "base.html" %}
    {% block content %}
        <a href="{% url 'leads:lead-list' %}"> Go back to leads</a>
        <hr />
        <h1> Assign an agent to this lead</h1>
        <form method="post"> <!-- form method="post" action="/leads/another-url/"> -->
            {% csrf_token %}
            {{ form.as_p }}
            <button type="Submit" >Submit</button>
        </form>
    {% endblock content %}
    ```
- In leads/forms.py create the form to assign an agent
    ```python
    from .models import Lead Agent
    class AssignAgentForm(forms.Form):
        agent = forms.ModelChoiceField(queryset=Agent.objects.none())
        
        def __init__(self, *args, **kwargs):
            request = kwargs.pop("request")
            agents = Agent.objects.filter(organization=request.user.userprofile)
            super(AssignAgentForm, self).__init__(*args, **kwargs)
            self.fields["agent"].queryset = agents
- Edit the ./leads/urls.py
    ```pthon
    from .views import ( ... AssignAgentView)

    urlpatterns = [
        path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    ]
    ```
- Update the leads/templates/lead_list.html
    ```html
	<div class="flex-grow">
		<h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ lead.first_name }} {{ lead.last_name }}</h2>
		<p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
		<a href="{% url 'leads:assign-agent' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center"> <!--this line-->
			Assign an agent
			<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
				<path d="M5 12h14M12 5l7 7-7 7"></path>
			</svg>
		</a>
	</div>
    ```
    Test 44.1: Assign a lead to an agent
    <p align="center">
    	<img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step44-test-1.png">
    </p>

### 45 Adding a feature to categorize via a model
- In ./leads/models.py
    ```python
    class Lead(models.Model):
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        age = models.IntegerFiled(default=0)
        organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
        category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

        def __str__(self):
            return f"{self.first_name} {self.last_name}"

    class Category(models.Model):
        name = models.CharField(max_length=30) #New, Contacted, Converted, Unconverted
        
        def __str__(self):
            return self.name
    ```
- Modify the ./leads/admin.py
    ```python
    from django.contrib import admin
    from .models import User, Lead, Agent. UserProfile, Category

    admin.site.register(Category)
    admin.site.register(User)
    admin.site.register(UserProfile)
    admin.site.register(Lead)
    admin.site.register(Agent)
    ```
    In the terminal: 
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
    Test 1: Create the categories {Contacted, Converted, Unconverted} from the admin site in `http://127.0.0.1:8000/admin/leads/category/add`

### 46 View the list of categories
- Edit ./leads/views.py
    ```python
    :
    class CategoryListView(LoginRequiredMixin, generic.ListView):
        template_name = "leads/category_list.html"
    ```
- Edit ./leads/models.py and migrate with null the default properties
    ```python
    :
    class Category(models.Model):
        name = models.CharField(max_length=30) #New, Contacted, Converted, Unconverted
        organization = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE) #adding null and blank so that when the migration is made, the parameters don't require default values
        def __str__(self):
            return self.name
    ```
    In the terminal run: `python manage.py makemigrations` and `python manage.py migrate`
- Modify again crm/leads/models.py and migrate without null and blank
    ```python
    :
    class Category(models.Model):
        name = models.CharField(max_length=30) #New, Contacted, Converted, Unconverted
        organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE) #adding null and blank so that when the migration is made, the parameters don't require default values
        def __str__(self):
            return self.name
    ```
    In the terminal run: `python manage.py makemigrations` and choose the option `2) Ignore for now...`, then apply `python manage.py migrate` and despite the error run the server `python manage.py runserver` which yields an uapplied migration error. Go to `http://127.0.0.1:8000/admin/leads/category/` and configure the organization of the categories, check Tes45.1 {Name: Contacted, Organization: jose, Name: Converted, Organization: jose, Name: Unconverted, Name: Jose}. Finally stop the server and migrate without problems `python manage.py migrate` and run the server

- In crm/leads/views.py
    ```python
    from .models import Lead, Agent, Category
    :
    class CategoryListView(LoginRequiredMixin, genereic.ListView):
        template_name = "leads/category_list.html"
        def get_queryset(self):
            user = self.request.user
            if user.is_organizer:
                queryset = Category.objects.filter(organization=user.userprofile)
            else:
                queryset = Category.objects.filter(organization=user.organization)
            return queryset
    ```
- Create ./leads/templates/leads/category_list.html and paste the grabbed code from Tailblock (PRICING last option) at `https://mertjf.github.io/tailblocks/` inside the block content

    ```html
    {% extends "base.html" %}

    {% block content %}
    <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-20">
        <h1 class="sm:text-4xl text-3xl font-medium title-font mb-2 text-gray-900">Categories</h1>
        <p class="lg:w-2/3 mx-auto leading-relaxed text-base">These categories segment the leads</p>
        </div>
        <div class="lg:w-2/3 w-full mx-auto overflow-auto">
        <table class="table-auto w-full text-left whitespace-no-wrap">
            <thead>
            <tr>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tl rounded-bl">Name</th>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">Lead Count</th>
            </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="px-4 py-3">Unassigned</td>
                    <td class="px-4 py-3">{{ unassigned_lead_count }}</td>
                </tr>
                {% for category in category_list %}
                    <tr>
                        <td class="px-4 py-3">{{ category.name }}</td>
                        <td class="px-4 py-3">TODO count</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        </div>
        <div class="flex pl-4 mt-4 lg:w-2/3 w-full mx-auto">
        <a class="text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0">Learn More
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
        </a>
        <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
        </div>
    </div>
    </section>
    {% endblock content %}
    ```
- Edit ./leads/views.py
    ```python
    class CategoryListView(LoginRequiredMixin, generic.ListView):
        template_name = "leads/category_list.html"
        context_object_name = "category_list"
        def get_context_data(self, **kwargs):
            context = super(CategoryListView, self).get_context_data(**kwargs)
            user = self.request.user

            if user.is_organizer:
                queryset = Lead.objects.filter(organization=user.userprofile)
            else:
                queryset = Lead.objects.filter(organization=user.agent.organization)

            context.update({
                "unassigned_lead_count": queryset.filter(category__isnull=True).count()})
            return context

        def get_queryset(self):
            user = self.request.user
            if user.is_organizer:
                queryset = Category.objects.filter(organization=user.userprofile)
            else:
                queryset = Category.objects.filter(organization=user.organization)
            return queryset
    ```
- Edit ./leads/urls.py
    ```python
    from views.py import( LeadsListViews, ..., AssignAgentView, CategoryListView)

    urlpattern = [
        :
        path('categories/', CategoryListView.as_view(), name='category-list'),
    ]
    ```
    Test 46.1: Go to `http://127.0.0.1:8000/leads/categories`
        <p align="center">
    <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step46-test-1.png">
    </p>

### 47 Configure the Category Detail View
- Edit ./leads/views.py
    ```python
    :
    class CategoryDetailView(LoginRequiredMixin, DetailView):
        template_name = "leads/category_detail.html"
        context_object_name = "category"

        def get_context_data(self, **kwargs):
            context = super(CategoryDetailView, self).get_context_data(**kwargs)
            leads = self.get_object().leads.all()

            context.update({
                "leads": leads
            })
            return context

        def get_queryset(self):
            user = self.request.user
            if user.is_organizer:
                queryset = Category.objects.filter(organization=user.userprofile)
            else:
                queryset = Category.objects.filter(organization=user.agent.organization)
            return queryset
    ```
- Before the previous step, add a tag name (`related_name`) to the Category in the Lead model of ./leads/models.py

    ```python
    :
    class Lead(models.Model):
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        age = models.IntegerFiled(default=0)
        organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
        category = models.ForeignKey("Category", related_name = "leads", null=True, blank=True, on_delete=models.SET_NULL)
        :
    ```
- Create ./leads/templates/leads/category_detail.html
    ```html
    {% extends "base.html" %}

    {% block content %}
    <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-20">
        <h1 class="sm:text-4xl text-3xl font-medium title-font mb-2 text-gray-900">{{ category.name }}</h1>
        <p class="lg:w-2/3 mx-auto leading-relaxed text-base">These are the leads under this category</p>
        </div>
        <div class="lg:w-2/3 w-full mx-auto overflow-auto">
        <table class="table-auto w-full text-left whitespace-no-wrap">
            <thead>
            <tr>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tl rounded-bl">First Name</th>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">Last Name</th>
            </tr>
            </thead>
            <tbody>
                {% for lead in leads %}
                    <tr>
                        <td class="px-4 py-3">{{ lead.first_name }}</td>
                        <td class="px-4 py-3">{{ lead.last_name }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        </div>
        <div class="flex pl-4 mt-4 lg:w-2/3 w-full mx-auto">
        <a class="text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0">Learn More
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
        </a>
        <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
        </div>
    </div>
    </section>
    {% endblock content %}
    ```
    Run in the terminal:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserverv
    ```
- Update the ./leads/urls.py to add the path of category-detail
    ```python
    from django.urls import path
    from .views import (LeadListView, ..., CategoryListView, CategoryDetailView)

    urlpatterns = [
        :
        path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    ]
    path
    ```
- Update the ./leads/templates/leads/category_list.html (See line 3438)
    ```html
    {% for category in category_list %}
    <tr>
        <td class="px-4 py-3">
            <a href="{% url 'leads:category-detail' category.pk %}"> {{ category.name }}</a>
        </td>
        <td class="px-4 py-3">TODO count</td>
    </tr>
    {% endfor %}
    ```
- Configure ./leads/templates/leads/lead_list.html (line 8)
    ```html
    {% extends "base.html" %}
    {% block content %}
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap">
            <div class="w-full mb-6 py-6 flex justify-between items-center border-b border-gray-200">
                <div>
                    <h1 class="text-4xl text-gray-800">Lead</h1>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:category-list' %}">
                        Vuew categories
                    </a>
                </div>
                {% if request.user.is_organizer %}
                <div>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">Create a new lead</a>
                </div>
                {% endif %}
            </div>
    ```
    Test: Go to `http://`127.0.0.1:8000/admin/leads/lead`, choose a lead a configure his category (i.e. contacted)<br>
    Then go to `http://`127.0.0.1:8000/leads/`, click on `View categories` and view the `contacted` in the Name column and verify that the user is listed there


- Simplify the selection of leads in the category, in crm/leads/templates/leads/category_detail.html (line 28)
    ```html
    <tbody>
        {% for lead in category.leads.all %} <!-- {% for lead in leads %} -->
            <tr>
                <td class="px-4 py-3">{{ lead.first_name }}</td>
                <td class="px-4 py-3">{{ lead.last_name }}</td>
            </tr>
        {% endfor %}
    </tbody>
    ```
    And comment the following section of crm/leads.views.py
    ```python
    :
    class CategoryDetailView(LoginRequiredMixin, DetailView):
        template_name = "leads/category_detail.html"
        context_object_name = "category"

        #def get_context_data(self, **kwargs):
        #    context = super(CategoryDetailView, self).get_context_data(**kwargs)
        #    leads self.get_object().leads.all()
        #
        #    context.update({
        #        "leads": leads
        #    })
        #    return context
    ```
### 48 Category Update view
- Update the category of a lead, in ./leads/category_datail.html (line 3468)
    ```html
    :
    <tbody>
        {% for lead in category.leads.all %}
            <tr>
                <td class="px-4 py-3">
                    <a class="hover:text-blue-500" href="{% url 'leads:lead-detail' lead.pk %}"> {{ lead.first_name }} </a>
                </td>
                <td class="px-4 py-3">{{ lead.last_name }}</td>
            </tr>
        {% endfor %}
    </tbody>
    ```
- Update leads/templates/leads/lead_detail.html line 15
    ```html
    {% extends "base.html" %}
    {% block content %}

        <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
            <div class="lg:w-4/5 mx-auto flex flex-wrap">
            <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
            <h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
            <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
            <div class="flex mb-4">
                <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
                <a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		<!-- interchaged -->
                <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
                <a href="#" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">
                    Category
                </a>
            </div>
        :
    ```
- Add the class in ./leads/forms.py
    ```python
    class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
    ```
- Add the model leadcategoryupdateview in ./leads/views.py
    ```python
    from .forms import LeadForm, ..., AssignAgentForm, LeadCategoryUpdateForm
    class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
            template_name = "leads/lead_category_update.html"
            form_class = LeadCategoryUpdateForm

            def get_queryset(self):
                user = self.request.user
                if user.is_organizer:
                    queryset = Lead.objects.filter(organization=user.userprofile)
                else:
                    queryset = Lead.objects.filter(organization=user.agent.organization)
                    queryset = queryset.filter(agent__user=user)
                return queryset

            def get_success_url(self):
                return reverse("leads:lead-detail", kwargs={"pk": self.get_object().id})
    ```
- Update in ./leads/urls.py
    ```python
    from .views import (LeadListView, ...,CategoryDetailView, LeadCategoryUpdateView)
    ;
    urlpatterns = [
        :
        path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    ]
- Update leads/templates/leads/lead_detail.html, line 15
   ```html
    {% extends "base.html" %}
    {% block content %}

        <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
            <div class="lg:w-4/5 mx-auto flex flex-wrap">
            <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
            <h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
            <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
            <div class="flex mb-4">
                <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
                <!--<a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>	 interchaged -->
                <a href="{% url 'leads:lead-category-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">
                    Category
                </a>
                <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
            </div>
        </a>
        :
    ```
- Create the template: leads/templates/leads/lead_category_update.html
	```html
	{% extends "base.html" %}
	{% block content %}
		<section class="text-gray-600 body-font overflow-hidden">
		  <div class="container px-5 py-24 mx-auto">
		    <div class="lg:w-4/5 mx-auto flex flex-wrap">
		      <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
			<h2 class="text-sm title-font text-gray-500 tracking-widest">LEAD</h2>
			<h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
			<div class="flex mb-4">
			  <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  
			  <a href="{% url 'leads:lead-category-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Category</a>
			  <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a>
			</div>
			<form method="post">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit">Submit</button>
			</form>
			<a href="{% url 'leads:lead-delete' lead.pk %}" class="w-1/2 mt-3 flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
		      </div>
		      <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
		    </div>
		  </div>
		</section>	
	{% endblock content %}
	```
    And edit the crm/leads/templates/leads/lead_update.html, line 15
    ```html
	{% extends "base.html" %}
	{% block content %}
		<section class="text-gray-600 body-font overflow-hidden">
		  <div class="container px-5 py-24 mx-auto">
		    <div class="lg:w-4/5 mx-auto flex flex-wrap">
		      <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
			<h2 class="text-sm title-font text-gray-500 tracking-widest">LEAD</h2>
			<h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
			<div class="flex mb-4">
			    <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>
			    <a href="{% url 'leads:lead-category-update' lead.pk %}" class = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-2">Category</a>
                <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Update Details</a>
			</div>
			<form method="post">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit">Submit</button>
			</form>
			<a href="{% url 'leads:lead-delete' lead.pk %}" class="w-1/2 mt-3 flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
		      </div>
		      <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
		    </div>
		  </div>
		</section>	
	{% endblock content %}
    ```
    Test 48.1 by going to: `http://127.0.0.1:8000/leads/1/category` and changing the category of the lead, check [`ver-1.6`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.6)
    <p align="center">
    	<img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step48-test-1.png">
    </p>
### 49 Installing crispy
- In the terminal
    ```bash
    pip install django-crispy-forms
    pip install crispy-tailwind
    pip freeze > requirements.txt
    ```
- Add the app in crm/settings.py
    ```python
    INSTALLED_APPS = [
        :
        'agents',
        'crispy_forms',
        'crispy_tailwind',
    ]
    : #in the bottom
    :
    CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
    CRISPY_TEMPLATE_PACK = "tailwind"
    ```
- In templates/registration/login.html, add `{% load tailwind_filters %}` after `{% extends 'base.html' %}` and replace {{ form.as_p }} with {{ form|crispy }} <br>
Also make the same changes in password_reset_{complete,confirm,done,email,form}.html, signup.html files <br>
For login.html:
    ```html
    {% extends 'base.html' %}
    {% load tailwind_filters %}

    {% block content %}
    <div class="max-w-lg mx-auto">

        <div class="py-5 border-t border-gray-200">
            <a class = "hover:text-blue-500" href="{% url 'signup' %}">Don't have an account?</a>
        </div>

        <form method = "post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Login</button>
        </form>
        <div class="py-5 border-t border-gray-200 mt-5">
            <a class = "hover:text-blue-500" href="{% url 'reset-password' %}">Forgot password?</a>
        </div>

    </div>

    {% endblock content %}
    ```
    Test: Go to `http://127.0.0.1:8000/login/` and see the changes <br>

    In password_reset_confirm.html
    ```html
        {% extends 'base.html' %}
        {% load tailwind_filters %}

        {% block content %}
        <div class = "max-w-lg mx-auto">
            <h1 class="text-4xl text-gray-800">Enter your new password</h1>

            <form method="post">
                {% csrf_token %}
                {{ form|crispy }}
                <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Confirm new password</button>
            </form>
        </div>
        {% endblock content %}
    ```
    In password_reset_form.html
    ```html
        {% extends 'base.html' %}
        {% load tailwind_filters %}

        {% block content %}
        <div class = "max-w-lg mx-auto">
            <h1 class="text-4xl text-gray-800">Enter your new password</h1>

            <form method="post" class="mt-5">
                {% csrf_token %}
                {{ form|crispy }}
                <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Reset password</button>
            </form>
            <div class = "py-5 border-t border-gray-200 mt-5">
                <a class="hover:text-blue-500" href="{% url 'login' %}">Already have an account?</a>
            </div>
        </div>
        {% endblock content %}
    ```
    In the ./templates/registration/signup.html
    ```html
    {% extends 'base.html' %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <form method = "post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button tpe='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Signup</button>
        </form>
        <div class="py-5 border-t border-gray-200 mt-5">
            <a class = "hover:text-blue-500" href="{% url 'login' %}">Already have an account?</a>
        </div>
    </div>

    {% endblock content %}
    ```
    Also edit in leads/templates/leads/lead_create.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <a class="hover:text-blue-500" href="{% url 'leads:lead-list' %}">Go back to leads</a>
        <div class="py-5 border-t border-gray-200">
            <h1>Create a new lead</h1>
        </div>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```
    In crm/templates/leads/lead_update.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
        <section class="text-gray-600 body-font overflow-hidden">
            <div class="container px-5 py-24 mx-auto">
                <div class="lg:w-4/5 mx-auto flex flex-wrap">
                    <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
                        <h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
                        <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
                        <div class="flex mb-4">
                        <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
                        <!--<a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		interchaged -->
                        <a href="{% url 'leads:lead-category-update' lead.pk %}" class = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Category</a>
                        <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
                        </div>
                        <form method="post">
                            {% csrf_token %}
                            {{ form|crispy }}
                            <button class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md type="submit">Submit</button>
                        </form>

                        <div class="mt-5 py-5 border-t border-gray-200">
                            <a href="{% url 'leads:lead-delete' lead.pk %}" class="w-1/2 mt-3 text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>	
    {% endblock content %}`
    ```
- Update the leads/templates/leads/lead_category_update.html
	```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
        <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
            <div class="lg:w-4/5 mx-auto flex flex-wrap">
            <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
            <h2 class="text-sm title-font text-gray-500 tracking-widest">LEAD</h2>
            <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
            <div class="flex mb-4">
            <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  
            <a href="{% url 'leads:lead-category-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Category</a>
            <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a>
            </div>
            <form method="post">
            {% csrf_token %}
            {{ form|crispy }}
            <button type="submit">Submit</button>
            </form>
            <a href="{% url 'leads:lead-delete' lead.pk %}" class="w-1/2 mt-3 flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
            </div>
            <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
            </div>
        </div>
        </section>	
    {% endblock content %}
	```
- Update agent/templates/agents/agent_create.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
        <div class="max-w-lg mx-auto">

            <div class="py-5 border-b border-gray-200">
                <a class="hover:text-blue-500" href="{% url 'agents:agent-list' %}">Go back to agents</a>
            </div>

            <h1 class="text-4xl text-gray-800"> Create a new agent</h1>
            <form method="post">
                {% csrf_token %}
                {{ form|crispy }}
                <button type="submit" class="w-full text-white bg-blue-500 hover:bg:blue-600 px-3 py-2 rounded-md">Submit</button>
            </form>
        </div>
    {% endblock content %}
    ```
    Update agents/templates/agents/agent_update.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
        <section class="text-gray-600 body-font overflow-hidden">
        <div class="container px-5 py-24 mx-auto">
            <div class="lg:w-4/5 mx-auto flex flex-wrap">
            <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
            <h2 class="text-sm title-font text-gray-500 tracking-widest">AGENT</h2>
            <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ agent.user.username }}</h1>
            <div class="flex mb-4">
            <a href="{% url 'agents:agent-detail' agent.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
            <a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		<!-- interchaged -->
            <a href="{% url 'agents:agent-update' agent.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
            </div>
            <form method="post">
                {% csrf_token %}
                {{ form|crispy }}
                <button type="submit" class="w-full text-white bg-blue-500 hover:bg:blue-600 px-3 py-2 rounded-md">Submit</button>
            </form>
            <div class="mt-5 py-5 border-t border-gray-200">
                <a href="{% url 'agents:agent-delete' agent.pk %}" class="w-1/2 mt-3 text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
            </div>
            <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
            </div>
        </div>
        </section>	
    {% endblock content %}
    ```
- Update the agent_delete.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}

    {% block content %}
    <div class="max-w-lg mx-auto">
        <div class="py-5 border-b border-gray-200">
            <a class="hover:text-blue-500" href="{% url 'agents:agent-list' %}">Go back to agents</a>
        </div>

        <h1 class="text-3xl text-gray-800">Are you sure you want to delete this agent?</h1>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type="submit" class="w-full text-white bg-blue-500 hover:bg:blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ``

- Update the lead_delete.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}

    {% block content %}
    <div class="max-w-lg mx-auto">
        <div class="py-5 border-b border-gray-200">
            <a class="hover:text-blue-500" href="{% url 'leads:lead-list' %}">Go back to leads</a>
        </div>

        <h1 class="text-3xl text-gray-800">Are you sure you want to delete this lead?</h1>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type="submit" class="w-full text-white bg-blue-500 hover:bg:blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```
- Update leads/templates/leads/assign_agent.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <div class="py-5 border-b border-gray-200">
            <a class="hover:text-blue-500" href="{% url 'leads:lead-list' %}">Go back to leads</a>
        </div>
        <hr />

        <h1 class="text-3xl text-gray-800">Assign an agent to this lead</h1>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type="submit" class="w-full text-white bg-blue-500 hover:bg:blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```

### 50 Styling a little bit more

- Go to leads/models.py and add {descrip, date, phone, email} to the model
    ```python
    class Lead(models.Model):
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)
        age = models.IntegerFiled(default=0)
        organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
        agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
        category = models.ForeignKey("Category", related_name = "leads", null=True, blank=True, on_delete=models.SET_NULL)
        description = models.TextField()
        date_added = models.DateTimmeField(auto_now_add=True)
        phone_number = models.CharField(max_length=20)
        email = models.EmailField()
        :
    ```
- In the terminal:
    ```bash
    python manage.py makemigrations
    Selection an otion: 1
    >> timezone.now
    ```
    Do for all the leads that were created and end with
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
- Edit the leads/forms.py
    ```python
    class LeadModelForm(forms.ModelForm):
        class Meta:
            model = Lead
            fields = (
                'first_name',
                'last_name',
                'age',
                'agent',
                'description',
                'phone_number',
                'email',
            )
    ```
    Then run again `python manage.py runserver`
- Fix in ./leads/view.py/ 50 - 4:40 Error at creating a lead in `http://127.0.0.1:8000/leads/create`, after clicking on submit
    ```python
    class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organization = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="A lead has been created",
            message="Go to the website to see the new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)   
    ```
- Edit the leads/templates/leads/lead_list.html file
    ```html
    {% extends "base.html" %}

    {% block content %}

    <section class="text-gray-700 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap">
            <div class="w-full mb-6 py-6 flex justify-between items-center border-b border-gray-200">
                <div>
                    <h1 class="text-4xl text-gray-800">Leads</h1>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:category-list' %}">
                        View categories
                    </a>
                </div>
                {% if request.user.is_organizer %}
                <div>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">
                        Create a new lead
                    </a>
                </div>
                {% endif %}
            </div>

            <div class="flex flex-col w-full">
                <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                    <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                First Name
                                </th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Last Name
                                </th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Age
                                </th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Email
                                </th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Cell Phone Number
                                </th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Category
                                </th>
                                <!--
                                <th scope="col" class="relative px-6 py-3">
                                <span class="sr-only">Edit</span>
                                </th>
                                -->
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                    Modify
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for lead in leads %}
                                <tr class="bg-white">
                                    <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                                        <a class="text-blue-500 hover:text-blue-800" href="{% url 'leads:lead-detail' lead.pk %}">{{ lead.first_name }}</a>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ lead.last_name }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ lead.age }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ lead.email }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                        {{ lead.phone_number }}
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        {% if lead.category %}
                                            <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                                                {{ lead.category.name }}
                                            </span>
                                        {% else %}
                                            <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-100 text-gray-800">
                                                Unassigned
                                            </span>
                                        {% endif %}
                                    </td>
                                    <td class="px-8 py-4 whitespace-nowrap  text-sm font-medium">
                                        <a href="{% url 'leads:lead-update' lead.pk %}" class="text-indigo-600 hover:text-indigo-900">
                                            Edit
                                        </a>
                                    </td>
                                </tr>

                            {% empty %}

                            <p>There are currently no leads</p>

                            {% endfor %}
                        </tbody>
                    </table>
                    </div>
                </div>
                </div>
            </div>
    
            {% if unassigned_leads.exists %}
                <div class="mt-5 flex flex-wrap -m-4">
                    <div class="p-4 w-full">
                        <h1 class="text-4xl text-gray-800">Unassigned leads</h1>
                    </div>
                    {% for lead in unassigned_leads %}
                    <div class="p-4 lg:w-1/2 md:w-full">
                        <div class="flex border-2 rounded-lg border-gray-200 p-8 sm:flex-row flex-col">
                            <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
                                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                                </svg>
                            </div>
                            <div class="flex-grow">
                                <h2 class="text-gray-900 text-lg title-font font-medium mb-3">
                                    {{ lead.first_name }} {{ lead.last_name }}
                                </h2>
                                <p class="leading-relaxed text-base">
                                    {{ lead.description }}
                                </p>
                                <a href="{% url 'leads:assign-agent' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">
                                    Assign an agent
                                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    </section>
    {% endblock content %}

    <!-- 
    extends "base.html" 
    block content
    <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap">
            <div class="w-full mb-6 py-6 flex justify-between items-center border-b border-gray-200">
                <div>
                    <h1 class="text-4xl text-gray-800">Lead</h1>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:category-list' %}">
                        Vuew categories
                    </a>
                </div>
                {% if request.user.is_organizer %}
                <div>
                    <a class="text-gray-500 hover:text-blue-500" href="{% url 'leads:lead-create' %}">Create a new lead</a>
                </div>
                {% endif %}
            </div>
            <div class="flex flex-wrap -m-4">
                {% for lead in leads %}
                <div class="p-4 lg:w-1/2 md:w-full">
                    <div class="flex border-2 rounded-lg border-gray-200 border-opacity-50 p-8 sm:flex-row flex-col">
                        <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
                                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                            </svg>
                        </div>
                        <div class="flex-grow">
                            <h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ lead.first_name }} {{ lead.last_name }}</h2>
                            <p class="leading-relaxed text-base">Blue bottle crucifix vinyl post-ironic four dollar toast vegan taxidermy. Gastropub indxgo juice poutine.</p>
                            <a href="{% url 'leads:lead-detail' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">
                                View this lead
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                    <path d="M5 12h14M12 5l7 7-7 7"></path>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
            {% if unassigned_leads.exists %}
                <div class="mt-5 flex flex-wrap -m-4">
                    <div class="p-4 w-full">
                        <h1 class="text-4xl text-gray-800">Unassigned leads</h1>
                    </div>
                    {% for lead in unassigned_leads %}
                    <div class="p-4 w-full lg:w-1/2 md:w-full">
                        <div class="flex border-2 rounded-lg border-gray-200 border-opacity-50 p-8 sm:flex-row flex-col">
                            <div class="w-16 h-16 sm:mr-8 sm:mb-0 mb-4 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
                                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-8 h-8" viewBox="0 0 24 24">
                                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                                </svg>
                            </div>
                            <div class="flex-grow">
                                <h2 class="text-gray-900 text-lg title-font font-medium mb-3">{{ lead.first_name }} {{ lead.last_name }}</h2>
                                <p class="leading-relaxed text-base">
                                    {{ lead.description }}
                                </p>
                                <a href="{% url 'leads:assign-agent' lead.pk %}" class="mt-3 text-indigo-500 inline-flex items-center">
                                    Assign an agent
                                    <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
                                        <path d="M5 12h14M12 5l7 7-7 7"></path>
                                    </svg>
                                </a>
                            </div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            {% endif %}
        </div>
    </section>
    endblock content
    -->
    ```
- Change the default redirect after loggin out, go to `crm/settings.py`
    ```python
    :
    AUTH_USER_MODEL = 'leads.User'
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    LOGIN_REDIRECT_URL = "/leads"
    LOGIN_URL = "/login"
    LOGOUT_REDIRECT_URL = "/"

    CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
    CRISPY_TEMPLATE_PACK = 'tailwind'
    ```
- Update the leads/templates/leads/lead_detail.html
	```html
	{% extends "base.html" %}
	{% block content %}
		<section class="text-gray-600 body-font overflow-hidden">
		  <div class="container px-5 py-24 mx-auto">
		    <div class="lg:w-4/5 mx-auto flex flex-wrap">
		      <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
			<h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
			<h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>

            <div class="flex mb-4">
			  <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  
			  <a href="{% url 'leads:lead-category-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Category</a>
			  <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Update Details</a>
			</div>

            <p class="leading-relaxed mb-4">{{ lead.description }}</p>
			<div class="flex border-t border-gray-200 py-2">
			  <span class="text-gray-500">Age</span>
			  <span class="ml-auto text-gray-900">{{ lead.age }}</span>
			</div>
			<div class="flex border-t border-gray-200 py-2">
			  <span class="text-gray-500">Email</span>
			  <span class="ml-auto text-gray-900">{{ lead.email }}</span>
			</div>
			<div class="flex border-t border-b mb-6 border-gray-200 py-2">
			  <span class="text-gray-500">Phone Number</span>
			  <span class="ml-auto text-gray-900">{{ lead.phone_number }}</span>
			</div>
			<div class="flex">
			  <!-- <span class="title-font font-medium text-2xl text-gray-900">$58.00</span> -->
			  <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
			  <button class="rounded-full w-10 h-10 bg-gray-200 p-0 border-0 inline-flex items-center justify-center text-gray-500 ml-4">
			    <svg fill="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
			      <path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 
			      1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"></path>
			    </svg>
			  </button>
			</div>
		      </div>
		      <img alt="ecommerce" class="lg:w-1/2 w-full lg:h-auto h-64 object-cover object-center rounded" src="https://dummyimage.com/400x400">
		    </div>
		  </div>
		</section>	
	{% endblock content %}
	```
 - Update ./leads/templates/leads/lead_update.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
        <section class="text-gray-600 body-font overflow-hidden">
            <div class="container px-5 py-24 mx-auto">
                <div class="lg:w-4/5 mx-auto flex flex-wrap">
                    <div class="w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0">
                    <!-- <div class="lg:w-1/2 w-full lg:pr-10 lg:py-6 mb-6 lg:mb-0"> -->
                        <h2 class="text-sm title-font text-gray-500 tracking-widest">Lead</h2>
                        <h1 class="text-gray-900 text-3xl title-font font-medium mb-4">{{ lead.first_name }} {{ lead.last_name }}</h1>
                        <div class="flex mb-4">
                        <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
                        <!--<a class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Reviews</a>		interchaged -->
                        <a href="{% url 'leads:lead-category-update' lead.pk %}" class = "flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Category</a>
                        <a href="{% url 'leads:lead-update' lead.pk %}" class="flex-grow text-indigo-500 border-b-2 border-indigo-500 py-2 text-lg px-1">Update Details</a> <!-- interchaged -->
                        </div>
                        <form method="post">
                            {% csrf_token %}
                            {{ form|crispy }}
                            <button class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md type="submit">Submit</button>
                        </form>

                        <div class="mt-5 py-5 border-t border-gray-200">
                            <a href="{% url 'leads:lead-delete' lead.pk %}" class="w-1/2 mt-3 text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Delete</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>	
    {% endblock content %}
    ```
	Test 50-1 Compiled in the branch of [`ver-1.7`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.7)
        <p align="center">
            <img src="https://raw.githubusercontent.com/jatolentino/Django-notes/main/sources/img/Step50-test-1.png">
        </p>
        
### 51 Install the environment packages
- In the terminal
    ```bash
    pip install django-environ
    pip freeze > requirements.txt
    ```
- Edit the crm/settings.py, add the environ package
    ```python
    from pathlib import Path
    import environ

    env = environ.Env(
        DEBUG = (bool, False)
    )
    environ.Env.read_env()
    :
    ```
- Create the new file crm/.env and copy the the secret_key of crm/settings.py
    ```bash
    DEBUG=True
    SECRET_KEY='9l=jjp#pg0-mbdfsntqww91&s9b^^a!kj44ljl4f5h!_uoft$h6u'
    ```
    
- Create another .env that will be shown uploaded with the projects and where the secret variables don't show up: .template.env
    ```bash
    DEBUG=True
    SECRET_KEY=
    ```
- Edit crm/settings.py to test the mechanism of variables, line 8
    ```python
    environ.ENV.read_env()

    DEBUG = env('DEBUG')
    SECRET_KEY = env('SECRET_KEY')
    print(DEBUG, SECRET_KEY)
    ```
    Test: Stop and Run the server `python manage.py runserver`, verify on the terminal the printed key

### 52 Configure the server using Postgrespl
- Download and install it from `https://postgresql.org/download/`
- Change PosgreSQL password, but before Reset Master Password in the program pgAdmin4.
    ```bash
    - Edit the file Files/PostgreSQL/14/data/pg_hba.conf, replace scram-sha-256 with trust
        # TYPE  DATABASE        USER            ADDRESS                 METHOD

        # "local" is for Unix domain socket connections only
        local   all             all                                     trust
        # IPv4 local connections:
        host    all             all             127.0.0.1/32            trust
        # IPv6 local connections:
        host    all             all             ::1/128                 trust
        # Allow replication connections from localhost, by a user with the
        # replication privilege.
        local   replication     all                                     trust
        host    replication     all             127.0.0.1/32            trust
        host    replication     all             ::1/128                 trust


    - Go to CMD and type, wont ask you a password
        psql -U postgres
        
    - In postgres=#, change the password
        \password postgres

    - Restore Program Files/PostgreSQL/14/data/pg_hba.conf
        # TYPE  DATABASE        USER            ADDRESS                 METHOD

        # "local" is for Unix domain socket connections only
        local   all             all                                     scram-sha-256
        # IPv4 local connections:
        host    all             all             127.0.0.1/32            scram-sha-256
        # IPv6 local connections:
        host    all             all             ::1/128                 scram-sha-256
        # Allow replication connections from localhost, by a user with the
        # replication privilege.
        local   replication     all                                     scram-sha-256
        host    replication     all             127.0.0.1/32            scram-sha-256
        host    replication     all             ::1/128                 scram-sha-256


    - Try to login again in CMD
        psql -U postgres
    ```
- Create the data base `dbcrm`, in the VS code terminal and being in the environment, run: <br>
Previously install postgreSQL extension for VS

    ```bash
    createdb -h localhost -p 5432 -U postgres dbcrm
    #(Input password of pgAdmin4 or the the admin's pass of the program in the installation process)
    ```

- Configure the database in crm/settings.py
    ```python
    :
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env("DB_NAME"),
            'USER': env("DB_USER"),
            'PASSWORD': env("DB_PASSWORD"),
            'HOST': env("DB_HOST"),
            'PORT': env("DB_PORT"),
        }
    }
    ```
- Configure the environment variables in crm/.env
    ```bash
    DEBUG=True
    SECRET_KEY='9l=jjp#pg0-mbdfsntqww91&s9b^^a!kj44ljl4f5h!_uoft$h6u'
    DB_NAME = dbcrm
    DB_USER = dbcrmuser
    DB_PASSWORD = dbcrm1234
    DB_HOST = localhost
    DB_PORT = 
    ```
- Access to the database from the terminal and create the user `dbcrmuser` that will take control over the database `dbcrm`
    ```bash
    psql -U postgres
        #password of the pgadmin4 (postgres)
    CREATE USER dbcrmuser WITH PASSWORD 'dbcrm1234';
    GRANT ALL PRIVILEGES ON DATABASE dbcrm TO dbcrmuser
    \q
    ```
- Copy the data to crm/.templates.env
    ```bash
    DEBUG=True
    SECRET_KEY=1234
    DB_NAME = 
    DB_USER = 
    DB_PASSWORD = 
    DB_HOST = 
    DB_PORT = 
    ```
- In the terminal, migrate the new database that's using PostgreSQL, be sure to delete all previous migrations files of the lead and agent apps, except `__init__.py`
    ```bash
    pip install psycopg2-binary
    python manage.py migrate
    python manage.py runserver
    ```
### 53 Installing whitenoise
- In the terminal
    ```bash
    pip install whitenoise
    pip freeze > requirements.txt
    ```
- Add the whitenoise in crm/settings.py
    ```bash
    :
    INSTALLED_APPS = [
        'whitenoise.runserver_nostatic',
    ]
    :
    MIDDLEWARE = [
        'whitenoise.middleware.WhiteNoiseMiddleware',
        :
    ]

    STATIC_ROOT = "static_root"
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    :
    ```
    Run in the terminal: 
    ```bash
    python manage.py collectstatic
    ```
### 54 Configurations for deployment
- Edit the crm/settings.py
    ```python
    :
    if not DEBUG:
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
        SECURE_SSL_REDIRECT = True
        SESSION_COOKIE_SECURE = True
        SECURE_CSRF_COOKIE_SECURE = True
        SECURE_BROWSER_XSS_FILTER = True
        SECURE_CONTENT_TYPE_NOSNIFF = True
        SECURE_HSTS_SECONDS = 31536000 #1YEAR
        SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
        SECURE_HSTS_PRELOAD = True
        X_FRAME_OPTIONS = "DENY"        

        ALLOWED_HOSTS = ["*"] #YOUR DOMAIN.CO
    ```
- Install gunicorn: `pip install gunicorn`
    ```bash
    pip install gunicorn
    pip freeze > requirements.txt
    ```

>Ommit this part for production
- Collect the static files, create ./runserver.sh(give executable permissions to this file)
    ```bash
    python manage.py collectstatic --no-input
    python manage.py migrate
    gunicorn --worker-tmp-dir /dev/shm crm.sdgi
    ```
    In the terminal give the permission `chmod +x runserver.h`. This won't run in the local server because the line of gunicorn --worker ... is meant to be run in a production server.

### 55 Configue the email SMTP for the productionn deployment
- Sign up in mailgun, then go to Sendinds>Domains>New Domain<br>
    SMTP credentials > Reset password: If there is no user, Create is on the tab Add new SMTP user: jose (jose@mg.yoursite.com)
- Edit the crm/settings.py
    ```python
    :
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = True
    EMAIL_PORT = env("EMAIL_PORT")
    DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
    ```
- Add it to the crm/.env
    ```bash
    :
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.mailgun.org"
    EMAIL_HOST_USER = "postmaster@mg.domain.com"
    EMAIL_HOST_PASSWORD = "" 
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = 
    ```
    In digital ocean add the environmet variables
### 56 Add your domain
- Go to digital ocean and add enter your custom domain

>Ommitted till here

### 57 Final fixes
- Go to leads/templates/leads/lead_list.html & agents/templates/agents/agent_list.html add before the {% endfor %}
    ```html
    :
    {% empty %}
    <p> There are currently no leads (agents) </p>
    {% endfor %}
    ```
- Edit the leads/templates/leads/assign_agent.html
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <a class="hover:text-blue-500" href="{% url 'leads:lead-list' %}">Go back to leads</a>
        <div class="py-5 border-t border-gray-200">
            <h1>Assign an agent to this lead</h1
        </div>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```
- Creat the category form in ./leads/forms.py
    ```python
    from .models import Lead, Agent, Category
    :
    class CategoryModelForm(forms.ModelForm):
        class Meta:
            model = Category
            fields = (
                'name',
            )
    ```
- Create a category view in ./leads/views.py
    ```python
    from .forms import (
        LeadForm,
        LeadModelForm,
        CustomUserCreationForm,
        AssignAgentForm,
        LeadCategoryUpdateForm,
        CategoryModelForm
    )
    :
    class CategoryCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
        template_name = "leads/category_create.html"
        form_class = CategoryModelForm

        def get_success_url(self):
            return reverse("leads:category-list")
        def form_valid(self, form):
            category=form.save(commit=False)
            category.organization = self.request.user.userprofile
            category.save()
            return super(CategoryCreateView, self).form_valid(form)

    class CategoryUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
        template_name = "leads/category_update.html"
        form_class = CategoryModelForm

        def get_success_url(self):
            return reverse("leads:category-list")
        
        def get_queryset(self):
            user = self.request.user
            if user.is_organizer:
                queryset = Category.objects.filter(organization=user.userprofile)
            else:
                queryset = Category.objects.filter(organization=user.agent.organization)
            return queryset

    class CategoryDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
        template_name = "leads/category_delete.html"

        def get_success_url(self):
            return reverse("leads:category-list")
        def get_queryset(self):
            user = self.request.user
            if user.is_organizer:
                queryset = Category.objects.filter(organization=user.userprofile)
            else:
                queryset = Category.objects.filter(organization=user.agent.organization)
            return queryset
    ```
- Create a category_create.html file in leads/templates/leads
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <a class="hover:text-blue-500" href="{% url 'leads:category-list' %}">Go back to categories</a>
        <div class="py-5 border-t border-gray-200">
            <h1 class="text-4xl text-gray-800">Create a new category</h1
        </div>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```
- Create a category_update.html file in leads/templates/leads
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <a class="hover:text-blue-500" href="{% url 'leads:category-list' %}">Go back to categories</a>
        <div class="py-5 border-t border-gray-200">
            <h1 class="text-4xl text-gray-800">Update {{ object.name }}</h1
        </div>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```
- Create a category_delete.html file in leads/templates/leads
    ```html
    {% extends "base.html" %}
    {% load tailwind_filters %}
    {% block content %}
    <div class="max-w-lg mx-auto">
        <a class="hover:text-blue-500" href="{% url 'leads:category-list' %}">Go back to categories</a>
        <div class="py-5 border-t border-gray-200">
            <h1 class="text-4xl text-gray-800">Are sure you want to delete {{ object.name }}?</h1
        </div>
        <form method="post" class="mt-5">
            {% csrf_token %}
            {{ form|crispy }}
            <button type='submit' class="w-full text-white bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded-md">Submit</button>
        </form>
    </div>
    {% endblock content %}
    ```
- Edit ./leads/templates/leads/category_list.html
    ```html
    {% extends "base.html" %}

    {% block content %}
    <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-20">
        <h1 class="sm:text-4xl text-3xl font-medium title-font mb-2 text-gray-900">Categories</h1>
        <p class="lg:w-2/3 mx-auto leading-relaxed text-base">These categories segment the leads</p>
        <a href="{% url 'leads:category-create' %}" class="hover:text-blue-500">Create a category</a>
        </div>
        <div class="lg:w-2/3 w-full mx-auto overflow-auto">
        <table class="table-auto w-full text-left whitespace-no-wrap">
            <thead>
            <tr>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tl rounded-bl">Name</th>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">Lead Count</th>
            </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="px-4 py-3">Unassigned</td>
                    <td class="px-4 py-3">{{ unassigned_lead_count }}</td>
                </tr>
                {% for category in category_list %}
                    <tr>
                        <td class="px-4 py-3">
                            <a href="{% url 'leads:category-detail' category.pk %}"> {{ category.name }}</a>
                        </td>
                        <td class="px-4 py-3">TODO count</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
        </div>
        <div class="flex pl-4 mt-4 lg:w-2/3 w-full mx-auto">
        <a class="text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0">Learn More
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
        </a>
        <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
        </div>
    </div>
    </section>
    {% endblock content %}
    ```
- Edit the ./leads/urls.py
    ```python
    :
    from .views import (LeadListView, ... LeadCategoryUpdateView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView)
    :
    urlpatterns = [
        :
        path('categories/', CategoryListView.as_view(), name='category-list'),
        path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
        path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
        path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
        path('create-category/', CategoryCreateView.as_view(), name='category-create'),

    ]
- Edit crm/leads/templates/leads/category_detail.html
    ```html
    {% extends "base.html" %}

    {% block content %}
    <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
        <div class="flex flex-col text-center w-full mb-20">
        <h1 class="sm:text-4xl text-3xl font-medium title-font mb-2 text-gray-900">{{ category.name }}</h1>
        <p class="lg:w-2/3 mx-auto leading-relaxed text-base">These are the leads under this category</p>
            <a href="{% url 'leads:category-update' category.pk %}" class="hover:text-blue-500">Update</a> <!--added-->
            <a href="{% url 'leads:category-delete' category.pk %}" class="hover:text-blue-500">Delete</a> <!--added-->
        </div>
        <div class="lg:w-2/3 w-full mx-auto overflow-auto">
        <table class="table-auto w-full text-left whitespace-no-wrap">
            <thead>
            <tr>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100 rounded-tl rounded-bl">First Name</th>
                <th class="px-4 py-3 title-font tracking-wider font-medium text-gray-900 text-sm bg-gray-100">Last Name</th>
            </tr>
            </thead>
            <tbody>
				{% for lead in category.leads.all %} <!-- {% for lead in leads %} -->
					<tr>
						<td class="px-4 py-3">{{ lead.first_name }}</td>
						<td class="px-4 py-3">{{ lead.last_name }}</td>
					</tr>
				{% endfor %}
            </tbody>
        </table>
        </div>
        <div class="flex pl-4 mt-4 lg:w-2/3 w-full mx-auto">
        <a class="text-indigo-500 inline-flex items-center md:mb-2 lg:mb-0">Learn More
            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-4 h-4 ml-2" viewBox="0 0 24 24">
            <path d="M5 12h14M12 5l7 7-7 7"></path>
            </svg>
        </a>
        <button class="flex ml-auto text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded">Button</button>
        </div>
    </div>
    </section>
    {% endblock content %}
    ```
    Test 57-1 Compiled in the branch of [`ver-1.8`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.8)
