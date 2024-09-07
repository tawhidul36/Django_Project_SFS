from django.urls import path,include
from . import views

urlpatterns = [
    path('list/', views.emp_list, name='emp_list'),
    path('form/', views.emp_form, name='emp_insert'),
    path('delete/<int:id>/',views.emp_delete,name='emp_delete'),
      # Create operation
    path('<int:id>/', views.emp_form, name='emp_update'),  # Update operation
    # Add other URL patterns if needed
]
