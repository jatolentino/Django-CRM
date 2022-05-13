# Deploy in Django
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
### 2 
### 3
### 4
### 5
### 6
### 7
### 8
### 9
### 10
### 11
### 12
### 13
### 14
### 15
### 16
### 17
### 18
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

Test: navigate to `https://127.0.0.1:8000/leads/all` OR `https://127.0.0.1:8000/leads/` <br>
Compiled in the branch of [`ver-1.0`](https://github.com/jatolentino/Django-notes/tree/jatolentino-ver-1.0)

### 20 Lead's list
- Change home_page.html name to lead_list.html (leads/templates/leads/lead_list.html)
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
Test in: `https://127.0.0.1:8000/leads/`

- Create another view for the details of the leads in leads/views.py
	```python
	def lead_detail(request, pk):
		print(pk)
		lead = Lead.objects.get(id=pk)
		return HttpResponse("here is the detail view")
	```
- Import lead_detail in lead/urls.py
	```python
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
Test: `https://127.0.0.1:8000/leads/1/`
- Modify the lead_detail, in leads/views.py
	```python
	def lead_detail(request, pk):
		lead = Lead.objects.get(id=pk)
		context = {
			"lead": lead
		}
		return render(request, "leads/lead_detail.html", context)
	```
- Create & edit the html file templates/leads/lead_details.html
	```html
	<!DOCTYPE html>
	<html lang="end">
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
### 21  create leads with Forms
- Create the lead_create in leads/views.py
	```python
	def lead_create(request):
		return render(request, "leads/lead_create.html")

- Create the html file: templates/leads/lead_create.html
	```html
	<!DOCTYPE html>
	<html lang="end">
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
		path('<int:pk>', lead_detail),
		path('create', lead_create),
	]
	```
Test: `https://127.0.0.1/leads/create`

- Create & edit the file forms in templates/leads/forms.py
	```github
	from django import forms
	
	class Leadform(forms.Form):
		first_name = forms.CharField()
		last_name = forms.CharField()
		age=forms.IntegerField(min_values=0)
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
				print("the form in valid"P)
				print(form.cleaned_data)
				first_name = form.cleaned_data['first_name']
				last_name = form.cleaned_data['last_name']
				age = form.cleaned_nadata['age']
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
- Test: Go to `https://127.0.0.1:8000/leads/create/` and create a lead, then SUBMIT <br>
	Verify in `https://127.0.0.1:8000/leads/` <br>
	Verify the prompt in the VS code or check in `https://127.0.0.1:8000/admin/leads/lead/`
	
- Redirect the create page to another tab
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
	from .forms import LeadForm, LeadModelForm
	
	def lead_create(request):
		form = LeadModelForm()
		if request.method == "POST":
			form = LeadModelForm(request.POST)
			if form.is_valid():
				form.save()
				return rediret("/leads")
		context = {
			"form": LeadForm()
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
	from .views import lead_list, lead_detail, lead_create
	app_name = "leads"
	
	urlpatterns = [
		path('', lead_list),
		path('<int:pk>/', lead_detail),
		path('<int:pk>/update/', lead_update),
		path('create'/, lead_create),
		]
		```
- Create the templates/leads/lead_update.html file
	```html
	<!DOCTYPE html>
	<html lang="end">
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
- Simplify the lead_update model with LeadModelform
	```python
	def lead_update(request, pk):
		lead = Lead.objects.get(id=pk)
		form = LeadModelForm(instance=lead)
		if reques.method == "POST":
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
### 24 Create the model delete
- in lead/views.py, create the lead_delete model
	```python
	lead = Lead.objects.get(id=pk)
	lead.delete()
	return redirect("/leads")
	```
- Edit the leads/urls.py
	```python
	from .views import lead_list, lead_detail, lead_create, lead_update
	app_name = "lead"
	
	urlpatterns = [
		path('', lead_list),
		path('<int:pk>', lead_detail),
		path('<int:pk>/update/', lead_update),
		path('<int:pk>/delete/', lead_delete),
		path('create/', lead_create),
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
### 25 Change URLs' names
- Edit the leads/urls.py
	```html
	:
	urlpatterns = [
		path('', lead_list, name='lead-list'),
		path('<int:pk>/', lead_detail, name='lead-detail'),
		path('<int:pk>/update/', lead_update, name='lead-update'),
		path('<int:pd>/delete/', lead_delete, name='lead-delete'),
		path('create/', lead_create, name='lead-create'),     <!-- i.e. path('create-a-lead/', lead_create, name='lead-create'),-->
	]
- Change to the URL's name in leads/lead_detail.html: from this `<a href="/leads"> Go back..`  -> `<a href="{% url 'leads:lead-list' %"> Go back..`
	```html
	<body>
		<a href="{% url 'leads:lead-list' %">Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
		<hr />
		<a href="{% url 'lead:lead-update' lead.pk %}">Update</a>
		<a href="{% url 'lead:lead-delete' lead.pk %}">Delete</a>
	</body>
	```
	
- Change to the URL's name in leads/lead_list.html: from this `<a href="/leads/create">Create..`  -> `<a href="{% url 'leads:lead-create' %">Create..`
	```html
	<body>
		<a href="{% url 'leads:lead-create' %">Create a new lead</a>
		<h1> This is all of our leads</h1>
		{% for lead in leads %}
			<div class="lead">
				<a href="{% url 'lead:lead-detail' lead.pk %}"> {{ lead.first_name }} {{ lead.last_name }}</a>. Age: {{ lead.age }}
			</div>
		{% endfor %}
	</body>
	```
	
- Change to the URL's name in leads/lead_create.html: `<a href="/lead">Go back...` -> `<a href="{% url 'leads:lead-detail' %}">Go back...`
	```html
	<body>
		<a href="{% url 'lead:lead-list' %}"> Go back to leads</a>
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
### 26 Create a template
- Create base.html in crm/templates/
	```html
	<!DOCTYPE html>
	<html lang="end">
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
		<a href="{% url 'leads:lead-create' %">Create a new lead</a>
		<h1> This is all of our leads</h1>
		{% for lead in leads %}
			<div class="lead">
				<a href="{% url 'lead:lead-detail' lead.pk %}"> {{ lead.first_name }} {{ lead.last_name }}</a>. Age: {{ lead.age }}
			</div>
		{% endfor %}
	{% endblock content %}
	```
- Update the leads/lead_detail.html file
	```html
	{% extends "base.html" %}
	{% block content %}
		<a href="{% url 'leads:lead-list' %">Go back to leads</a>
		<hr />
		<h1>This is the details of {{ lead.first_name }}</h1>
		<p>This persons age: {{ lead.age }} </p>
		<p>The agent responsible for this lead is : {{ lead.agent }}</p>
		<hr />
		<a href="{% url 'lead:lead-update' lead.pk %}">Update</a>
		<a href="{% url 'lead:lead-delete' lead.pk %}">Delete</a>
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
		<a href="{% url 'lead:lead-list' %}"> Go back to leads</a>
		<hr />
		<h1> Create a new lead</h1>
		<form method="post">		<!-- form method="post" action="/leads/another-url/"> -->
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
		<h1> This is all of our lead lead</h1>
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
### 27 Adding Tailwindcss
- Go to https://v2.tailwindcss.com/docs/installation#using-tailwind-via-cdn and edit templates/base.html
	```html
		<!DOCTYPE html>
		<html lang="end">
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

- Create the file templates/navbar.html and add the navbar header from https://tailblocks.cc/
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
	      <a href="{% url 'leads:lead-list' %}" class="mr-5 hover:text-gray-900">Leads/a>
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
		<html lang="end">
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
			  <a href="{% url 'leads:lead-detail' lead.pk %}" class="flex-grow border-b-2 border-gray-300 py-2 text-lg px-1">Overview</a>  <!-- interchaged -->
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








