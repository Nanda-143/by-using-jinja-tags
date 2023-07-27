from django.shortcuts import render

# Create your views here.
d={'key':'pulihora raja'}
def data_render(request):
    return render(request,'data_render.html',context=d)