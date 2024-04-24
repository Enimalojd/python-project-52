from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
from django.contrib.auth.models import User


class Index(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'
    


class UserCreateView(CreateView):
    template_name = 'users/create_user.html'

    def get(self, request):

        return render(request, self.template_name)


class UserUpdateView(FormView):
    template_name = 'users/update_user.html'


class DeleteUserView(FormView):
    template_name = 'users/delete_user.html'
