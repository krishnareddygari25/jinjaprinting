from django.shortcuts import render

# Create data_renderyour views here.
def data_render (request):
    data='this is the jinja assume tags'
    d={'assume':data}
    return render(request,'data_render.html',context=d)


def login(request):
    d={'username':'Anusha','age':'21'}
    return render(request,'login.html',context=d)
