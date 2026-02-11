from django.urls import path
from . import views

urlpatterns = [
    path("", views.diary_list, name="diary_list"),
    path("<int:diary_id>/", views.diary_detail, name="diary_detail"),
    path("add/", views.add_diary, name="add_diary"),
    path("<int:diary_id>/add_entry/", views.add_entry, name="add_entry"),
]
