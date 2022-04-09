from multiprocessing import context

from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    template_name = 'index.html'
    context = {
        'title': 'Birth project',
        'paragraph': 'Birth project created by Mehedi Hasan Tayef'
    }
    def get(self,request):
        return render(request,self.template_name,self.context)
