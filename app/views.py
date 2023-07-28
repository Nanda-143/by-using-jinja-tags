from django.shortcuts import render

# Create your views here.
d={'a':100,'b':230,'c':50}
def data_render(request):
    return render(request,'data_render.html',context=d)