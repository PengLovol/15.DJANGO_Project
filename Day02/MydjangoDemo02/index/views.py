from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def temp_views(request):
    #1..通过 loader 加载模板
    t=loader.get_template('01_temp.html')
    # 2.将模板渲染成字符串
    html=t.render()
    # 3.将字符串通过HttpResponse响应给客户端
    return HttpResponse(html)

def temp02_views(request):
    return render(request,'01_temp.html')

# http://localhost:8000/03-var
def var_views(request):
    str = "模板中的变量－字符串"
    num = 3306
    tup = ('谢逊', '韦一笑', '殷素素', '金花婆婆')
    list = ['孙悟空', '猪八戒', '沙和尚']
    dic = {
        'BJ': '北京',
        'SZ': '深圳',
        'SH': '上海',
    }
    say = sayHi()
    dog = Dog()
    return render(request,'03_var.html',locals())

def sayHi():
  return "Hello,this is a view"

class Dog(object):
  name = '旺财'
  def eat(self):
    return '吃狗粮'

# http://localhost:8000/04-static
def static_views(request):
    return render(request,'04_static.html')

# http://localhost:8000/
def index_views(request):
  return render(request,'index_peng.html')
