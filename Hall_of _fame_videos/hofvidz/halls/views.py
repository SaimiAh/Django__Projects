from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Hall,Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import VideoForm,SearchForm



def home(request):
    return render(request, 'halls/home.html')

def dashboard(request):
    return render(request, 'halls/dashboard.html')

def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = Video()
            video.url = form.cleaned_data['url']
            video.title = form.cleaned_data['title']
            video.youtube_id = form.cleaned_data['youtube_id']
            video.hall = Hall.objects.get(pk=pk)
            video.save()
    return render(request, 'halls/add_video.html', {'form':form, 'search_form':search_form})

class SignUp(generic.CreateView):
    form_class  = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registeration/signup.html'
   
    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

#CRUD CLASS BASED
class CreateHall(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/create_hall.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('home')
    

class DetailHall(generic.DetailView):
    model = Hall
    template_name = 'halls/detail_hall.html'

class UpdateHall(generic.UpdateView):
    model = Hall
    template_name = 'halls/update_hall.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')

class DeleteHall(generic.DeleteView):
    model = Hall
    template_name = 'halls/delete_hall.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')