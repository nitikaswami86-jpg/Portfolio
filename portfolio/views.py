from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.views import View
from .models import Project, Contact

class HomeView(View):

    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'portfolio/index.html', {
            'projects': projects
        })

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('home')
    
