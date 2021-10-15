from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("v1/",views.v1, name = "view 1"),
    path("v1/<int:id>", views.v1, name="view 1"),

]
