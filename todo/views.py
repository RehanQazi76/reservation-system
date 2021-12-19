

from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView 
from .models import Task, Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from todo.forms import UserForm
from django.contrib.auth import login
class CustomerloginView(LoginView):
    template_name='todo/login.html'
    fields='__all__' 
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy("tasks")

class RegisterPage(FormView) :
    template_name='todo/register.html'
    form_class=UserForm
    redirect_authenticated_user=True 
    success_url=reverse_lazy("tasks") 
    def form_valid(self, form): 
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)     
    def get(self,  *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        
        return super(RegisterPage,self).get( *args, **kwargs)
class TaskList(LoginRequiredMixin,ListView):
    model = Ticket
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)




class TaskDetail(LoginRequiredMixin,DetailView):
    model= Ticket

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Ticket
    fields=['flight_no','seat_no','date','month','fromm','to'] 
    success_url=reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form) 

class TaskUpdate(LoginRequiredMixin,UpdateView) :
    model=Ticket
    fields=['flight_no','seat_no','date','month','fromm','to']  
    success_url=reverse_lazy("tasks")

class DeleteView(LoginRequiredMixin,DeleteView) :
    model=Ticket
    fields='__all__'   
    success_url=reverse_lazy("tasks")            



    

    

