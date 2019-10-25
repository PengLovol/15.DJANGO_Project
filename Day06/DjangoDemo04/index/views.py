from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
def request_views(request):
  # print(dir(request))
  # print(request.META)
  scheme = request.scheme
  body = request.body
  path = request.path
  host = request.get_host()
  method = request.method
  get = request.GET
  post = request.POST
  cookies = request.COOKIES
  return render(request,'01-request.html',locals())

def get_views(request):
  if 'name' in request.GET:
    print('name:'+request.GET['name'])
  if 'age' in request.GET:
    print('age:'+request.GET['age'])
  return HttpResponse('Get OK')

def post_views(request):
  # 判断请求方式，如果是get请求，则显示　03-post.html 模板
  if request.method == 'GET':
    return render(request,'03-post.html')
  # 如果是　post 请求，则获取请求提交的数据
  else:
    return HttpResponse('POST请求成功!')


def form_views(request):
  if request.method == 'GET':
    form = RemarkForm()
    return render(request,'04-form.html',locals())
  else:
    # subject = request.POST['subject']
    # email = request.POST['email']
    # message = request.POST['message']
    # topic = request.POST['topic']
    # isSaved = request.POST['isSaved']
    # print(subject,email,message,topic,isSaved)

    # 通过RemarkForm自动接收数据
    # 1.将request.POST数据传递给RemarkForm构造器
    form = RemarkForm(request.POST)
    # 2.验证form对象
    if form.is_valid():
      # 3.通过验证后获取具体的数据
      cd = form.cleaned_data
      subject = cd['subject']
      email = cd['email']
      isSaved = cd['isSaved']
      message = cd['message']
      topic = cd['topic']
      print(subject,email,isSaved,message,topic)
    return HttpResponse('Post OK')






