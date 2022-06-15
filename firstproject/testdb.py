from urllib import response
from django.http import HttpResponse
from TestModel.models import Test

def add(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    sex = request.GET.get('sex')
    test = Test(name=name,age=age,sex=sex)
    test.save()
    return HttpResponse("<p>數據添加成功</p>")

def getAll(request):
    list = Test.objects.all()
    response = ""
    for var in list:
        response += str(var.id) + " "
        response += var.name + " "
        response += str(var.age) + " "
        response += var.sex + " "
        # if response.length < 2:
        #     response = "資料為空"
    return HttpResponse("<p>" + response + "</p>")

def update(request):
    id = request.GET.get('id')
    test = Test.objects.get(id = id)
    test.name = "crate"
    test.save()
    return HttpResponse("<p>修改成功</p>")

def delete(request):
    id = request.GET.get('id')
    test = Test.objects.get(id = id)
    test.delete()
    return HttpResponse("<p>刪除成功</p>")