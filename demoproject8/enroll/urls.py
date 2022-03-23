from django.urls import path
from . import views

urlpatterns=[
    path('registration/',views.user_regis),
    path('delete_data/',views.Delete_data),
    path('success/',views.register_redirect),
    path('update_data/',views.update_data),
    path('update/',views.update),
]