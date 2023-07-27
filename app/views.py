from django.shortcuts import render

# Create your views here.
d={'key':'pulihora raja','age':23}
def data_render(request):
    return render(request,'data_render.html',context=d)