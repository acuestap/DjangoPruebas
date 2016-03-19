from django.conf.urls import url
from .import views


urlpatterns = [
    url(r'^formulario/', views.new_francis_form, name="francis_formualrio"),
]
