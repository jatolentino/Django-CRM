# Deploy in Django
### 19 Urls in the app, namespaces
- Create & edit leads/urls.py
  ```bash
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
```bash
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('leads/', include('leads.urls', namespace="leads"))
]
```bash

Test: navigate to 127.0.0.1:8000/leads/all
OR 127.0.0.1:8000/leads/


