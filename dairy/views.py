from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import done

# Create your views here.

class index(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('HIIIII')


class DoneView(CreateView):
    model = done
    template_name = 'dairy/done.html'
    fields = ['title','description']
    success_url = reverse_lazy('index')