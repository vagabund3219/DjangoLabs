from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        check = request.POST.get("check")
        choose = request.POST.get("choose")
        email = request.POST.get("email")
        reg = request.POST.get("reg")
        urlText = request.POST.get("urlText")
        filePath = request.POST.get("filePath")
        file = request.POST.get("file")
        output="<h2>User</h2><h3>Name - {0}, Age - {1}</h3><p>check - {2}</p><p>check - {2} \n choose - {3} \n email - {4} \n reg - {5} \n urlText - {6} \n filePath - {7}\n file - {8}</p>".format(name, age,check, choose, email, reg, urlText, filePath, file)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
def about(request):
    return HttpResponse("<h2>О сайте</h2>")
def contact(request):
    return HttpResponse("<h2>Contacts</h2>")
def products(request, productid=1):
    output = "<h2>Продукт # {0}</h2>".format(productid)
    return HttpResponse(output)
def users(request, id, name):
    output = "<h2>Пользователь</h2> <h3>id:{0} Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)