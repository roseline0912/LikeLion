from django.shortcuts import render

# Create your views here.
def index(request):
    context ={}
    
    if request.GET.get("myword"):
        mysentence = request.GET.get("myword")
        
        context["wordlen"] = len(mysentence.replace(" ", ""))
        
        myword = mysentence.split(" ")
        
        checkcnt = dict()
        
        for i in myword:
            if i in checkcnt:
                checkcnt[i] += 1
            else:
                checkcnt[i] = 1
                
        context["checkcnt"] =checkcnt
        
    return render(request,'index.html',context)
    
  