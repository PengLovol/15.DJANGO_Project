from django.http import HttpResponse


def show_views(request):
  return HttpResponse("我的第一个Django程序")

def sh_views(request):
  return HttpResponse('这是sh的视图处理函数')

#匹配　show/两位数字　的视图处理函数
# url(r'^show/(\d{2})',show1_views),
def show1_views(request,num1):
  return HttpResponse("传递进来的参数为:"+num1)

#访问路径是　/四位数字/两位数字/两位数字
#url(r'^(\d{4})/(\d{2})/(\d{2})/$',show2_views),
def show2_views(request,year,month,day):
  return HttpResponse("生日：%s年%s月%s日"%(year,month,day))

#访问路径是　/show3 的时候，交给show3_views　去处理
#url(r'^show3/$',show3_views,{'name':'naruto','age':18})
def show3_views(request,name,age):
  return HttpResponse('姓名:'+name+',年龄:'+str(age))






