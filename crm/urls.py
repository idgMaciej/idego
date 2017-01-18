from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^companies$', views.companies, name='companies'),
    url(r'^main$', views.main),
    url(r'^users$', views.users, name="users"),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^$', auth_views.login, name='login'),
    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url='/users'
    )),
    url('^remove$', views.remove_user, name="remove"),
]
