from django.shortcuts import render
import random
from .models import Blog

# Create your views here.
def index(request):
   context=dict()
   
   if request.GET.get('로또'):
      print('로또를 눌렀습니다.')
      
      lotto_list=list(range(1,46))
      result_lotto=random.sample(lotto_list,6)
      
      context['result_lotto']=result_lotto
      
   all_blog=Blog.objects.all()
   context['all_blog']=all_blog
   
   one_blog=Blog.objects.get(id=1)
   context['one_blog']=one_blog
      
   #response=1
   return render(request,'index.html',context) #,response)