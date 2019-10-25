from django.db.models import Avg, Sum, F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from .models import *


def parent_views(request):
  list = ['首页','服装鞋帽','食品','夺宝']
  return render(request,'01-parent.html',locals())

def child_views(request):
  list = ['首页', '服装鞋帽', '食品', '夺宝']
  return render(request,'02-child.html',locals())

def arguments_views(request,year,month):
  return HttpResponse('年份:'+year+',月份:'+month)

def reverse_views(request):
  # url = reverse('parent')
  url = reverse('arg',args=('2018','12'))
  return HttpResponse('解析的地址为:'+url)

#http://localhost:8000/05-add
def add_views(request):
  # 方案１：Entry.objects.create()
  # obj = Author.objects.create(name='王老师',age=32,email='wang.wc@163.com')
  # print(obj.id,obj.name,obj.age,obj.email)

  # 方案２: obj.save()
  # obj = Author(name='隔壁老王',age=32,email='laowang.gebi@163.com')
  # obj.save()

  # 方案３：obj.save()
  # dic = {
  #   'name':'超哥哥',
  #   'age' : 32,
  #   'email' : 'brother_chao@163.com',
  #   'isActive' : False
  # }
  # obj = Author(**dic)
  # obj.save()
  # print(obj.id, obj.name, obj.age, obj.email,obj.isActive)

  #向　Publisher 表中增加数据
  # Publisher.objects.create(name='北京大学出版社',address='北大东路125号',city='北京',country='中国',website='http://www.beida.com')
  #
  # obj = Publisher(name='清华大学出版社',address='清华东路125号',city='北京',country='中国',website='http://www.qinghua.com')
  # obj.save()
  #
  # dic = {
  #   'name':'人民教育出版社',
  #   'address':'珠市口大街',
  #   'city':'北京',
  #   'country':'中国',
  #   'website':'http://www.people.com'
  # }
  # obj1 = Publisher(**dic)
  # obj1.save()

  #向　Book 表中插入数据
  Book.objects.create(title='老王的一天',publicate_date='2015-10-12')

  book = Book(title='老王的一生',publicate_date='2017-09-12')
  book.save()

  dic = {
    'title':'王老师的幸福生活',
    'publicate_date':'2018-01-01'
  }
  book1 = Book(**dic)
  book1.save()


  return HttpResponse("Add OK")

def query_views(request):
  # 所有的查询接口必须通过　Entry.objects 去调用

  # all() : 查询　Author 实体中所有的数据
  # authors = Author.objects.all()
  # print(authors.query)
  # print(authors)
  # 循环便利 authors 得到每一个数据
  # for au in authors:
  #   print(au.id,au.name,au.age,au.email)

  # values() : 查询部分列数据封装到字典中再封装到列表中
  # 查询Author实体中所有行所有列封装到字典再封装到列表中
  # authors = Author.objects.values()
  # 查询Author实体中所有行的name和age列封装到字典再封装到列表中
  # authors = Author.objects.values('name','age')

  # authors = Author.objects.all().values()
  # print(authors)
  # for au in authors:
  #   print(au['name'])


  #values_list : 将查询结果封装到元组中再封装到列表中
  # authors = Author.objects.values_list()
  # print(authors)

  #get() : 查询只返回一条记录
  # 错误，查询返回多于一条数据了
  # author = Author.objects.get(id__gt=1)
  # author = Author.objects.get(id=1)
  # print(author)

  #filter() : 根据条件筛选数据
  # authors = Author.objects.filter(id=1)
  # print(authors.query)
  # print(authors)

  # authors=Author.objects.filter(age__gte=30).values()
  # print(authors)

  # 聚合函数
  # result = Author.objects.all().aggregate(avg=Avg('age'))
  # print(result['avg'])

  # 聚合函数(带分组)
  # result = Author.objects.values('isActive').annotate(sum=Sum('age')).filter(isActive=True).all()
  # print(result)

  #排序
  authors = Author.objects.order_by('-id')
  for au in authors:
    print(au.id,au.name,au.age,au.email)
  return HttpResponse("Query OK")


def queryall_views(request):
  # authors = Author.objects.all()
  #　查询isActive的值为True的信息来表示未被删除的
  authors = Author.objects.filter(isActive=True)
  return render(request,'07-queryall.html',locals())

def update_views(request,id):
  author = Author.objects.get(id=id)
  return render(request,'08-update.html',locals())

def update09_views(request):
  #修改id为2的Author的信息
  # au = Author.objects.get(id=2)
  # au.age = 38
  # au.email = "gblw@163.com"
  # au.isActive = False
  # au.save()
  #修改isActive为False的数据，将isActive更改为True
  Author.objects.filter(isActive=False).update(isActive=True)
  return HttpResponse('Update Success')

def delete_views(request,id):
  author = Author.objects.get(id=id)
  #通过　isActive=False　模拟删除
  author.isActive = False
  author.save()
  # 使用转发查看　queryall_views中的内容
  # return queryall_views(request)

  #使用重定向定位到 /07-queryall
  # return HttpResponseRedirect('/07-queryall')
  return redirect('/07-queryall')


def doF_views(request):
  Author.objects.all().update(age=F('age')+10)
  return redirect('/07-queryall')

def raw_views(request):
  sql = "select * from index_author where age>45"
  authors = Author.objects.raw(sql)
  for au in authors:
    print(au.name,au.age,au.email)
  return HttpResponse("Query OK")

def authors_views(request):
  authors = Author.objects.all()
  return render(request,'13-authors.html',locals())

def oto_views(request):
  # wife = Wife()
  # wife.name = '王夫人'
  # wife.age = 26
  # #直接指定author_id的值(author_id是由OneToOneField隐式增加的属性)
  # wife.author_id = 1
  # wife.save()

  # wife = Wife()
  # wife.name = "超夫人"
  # wife.age = 18
  # author = Author.objects.get(name='超哥哥')
  # wife.author = author
  # wife.save()

  #正向查询
  wife = Wife.objects.get(id=1)
  wife_author = wife.author
  #反向查询
  author = Author.objects.get(id=1)
  author_wife = author.wife
  return render(request,'14-oto.html',locals())


def otm_views(request):
  # 正向查询：通过Book查询Publisher,在15-otm.html中显示每个book对应的publisher
  books = Book.objects.all()
  # 反向查询
  pub = Publisher.objects.get(id=1)
  pub_books = pub.book_set.all()
  return render(request,'15-otm.html',locals())

def mtm_views(request):
  #正向查询:通过　book 查询　authors
  book = Book.objects.get(id=1)
  authors = book.authors.all()
  #反向查询:通过　author 查询　book
  author = Author.objects.get(id=2)
  books = author.book_set.all()
  return render(request,'16-mtm.html',locals())

