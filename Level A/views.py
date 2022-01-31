from django.views.generic import CreateView
from .models import Person

class UserCreateView(CreateView):
    model = User
    template_name =  'accounts/login.html'
    fields = ('name', 'email', 'password')