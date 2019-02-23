from django.urls import path

from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view , name="logout"),
    path("spam", views.spam_view , name="spam"),
    path("signup", views.signup_view , name="signup"),
    path("project", views.project_view , name="project"),
    path('project/<slug:projectname>', views.projectsort_view , name="projectsort"),
    path("formalinformal", views.formalinformal_view , name="formalinformal"),
    path("about", views.about_view , name="about"),
    path("delete", views.del_user , name="delete")
]
