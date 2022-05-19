from django.urls import path
from .views import (LeadListView, LeadDetailView, LeadCreateView, LeadDeleteView, 
LeadUpdateView)
#from .views import (lead_list, lead_detail, lead_create, lead_update,
#lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadDeleteView, 
#LeadUpdateView)

#from .views import lead_list

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