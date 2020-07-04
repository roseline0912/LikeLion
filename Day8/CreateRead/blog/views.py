from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def index(request):
    context=dict()
    mypost=Post.objects.all()
    context['dispaly_post']=mypost
    return render(request,'index.html',context) 
    
def second(request):
    # context=dict()
    # context['result']='없어'
    return render(request,'second.html') 
    

def create(request):
    # tmp_post=Post()  # Post 모델 사용
    # tmp_post.title=request.GET.get('title')   
    # tmp_post.body=request.GET.get('body')
    # tmp_post.author=request.GET.get('nickname') #html내의 name 속성에 해당하는 정보를 잡아 활용가능
    # tmp_post.save()
    
    Post.objects.create(title=request.POST.get('title'),
                        body=request.POST.get('body'),
                        author=request.POST.get('nickname'))
    
    return redirect('index')