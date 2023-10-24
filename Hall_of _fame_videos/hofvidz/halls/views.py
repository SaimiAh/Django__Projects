from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Hall
from django.contrib.auth.forms import UserCreationForm
def home(request):
    return render(request, 'halls/home.html')

class SignUp(generic.CreateView):
    form_class  = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registeration/signup.html'


class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('home')