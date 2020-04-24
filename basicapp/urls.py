from django.urls import path
from basicapp import views
urlpatterns = [
    path('',views.form_view,name='forms'),
]
