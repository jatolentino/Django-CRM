# Deploy in Django
### 1 Create & activate the virstual enviroment (VSCODE)
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

Test: navigate to `https://127.0.0.1:8000/leads/all` OR `https://127.0.0.1:8000/leads/`


