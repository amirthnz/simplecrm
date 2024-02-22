from django.urls import path
from crm import views

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:person_id>/edit', views.edit_person, name='edit'),
    path('reason/<int:reason_id>/edit', views.edit_reason, name='editreason'),
    path('person/<int:person_id>/', views.person, name='person'),
    path('reason/<int:reason_id>/', views.reason, name='reason'),
    path('add/', views.add_person, name='add'),
    path('add_reason/', views.add_reason, name='addreason'),
]