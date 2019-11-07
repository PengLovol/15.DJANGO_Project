from django.db import models
#自定义EntryManager类，用于覆盖实体类中的objects
class BookManager(models.Manager):
  def title_count(self,keywords):
    return self .filter(title__contains=keywords).count()

#为 Author 实体自定义objects对象，增加一个函数，用于查询年龄小于指定年龄值的作者的QuerySet
class AuthorManager(models.Manager):
  def age_lt(self,age):
    return self.filter(age__lt=age)



# Create your models here.
#创建一个实体类 - Publisher
#用于表示出版社信息，属性如下
#1.name：出版社名称(varchar)
#2.address：出版社所在地址(varchar)
#3.city：出版社所在城市(varchar)
#4.country：出版社所在国家(varchar)
#5.website：出版社的网址(varchar)
class Publisher(models.Model):
  name = models.CharField(max_length=30,verbose_name='出版社名')
  address = models.CharField(max_length=200,verbose_name='地址')
  city = models.CharField(max_length=50,verbose_name='所在城市')
  country = models.CharField(max_length=50,verbose_name='所在国家')
  website = models.URLField(verbose_name='网站')


  # #重写__str__，来定义该对象的字符串的表现形式
  def __str__(self):
    return self.name
  # 增加内部类Meta来定义其展现形式
  class Meta:
    # 1.修改表名为publisher
    db_table = 'publisher'
    # 2.指定后台管理时要显示的名字
    verbose_name = '出版社'
    verbose_name_plural = verbose_name






#创建　Author 的实体类
#1.name - 姓名(CharField -> varchar)
#2.age - 年龄(IntegerField -> int)
#3.email - 电子邮件(EmailField -> varchar)
class Author(models.Model):
  #使用AuthorManager对象覆盖本类中的objects
  objects = AuthorManager()
  name = models.CharField(max_length=30,verbose_name='姓名')
  age = models.IntegerField(verbose_name='年龄')
  email = models.EmailField(null=True,verbose_name='邮箱')
  #表示用户的激活状态：True,表示已激活,False,表示未激活
  #由于是新增列，所以必须要给默认值或允许为空
  #由于BooleanField默认是不允许为空的，所以此处选择了增加默认值
  isActive = models.BooleanField(default=True,verbose_name='激活用户')
  # 增加一个字段，表示用户的头像，可以上传的
  picture=models.ImageField(upload_to="static/uploda",null=True,verbose_name='头像')

  #重写__str__，来定义该对象的字符串的表现形式
  def __str__(self):
    return self.name

  # 增加内部类Meta来定义其展现形式
  class Meta:
    #1.修改表名为author
    db_table='author'
    #2.指定后台管理时要显示的名字
    verbose_name='作者'
    verbose_name_plural=verbose_name
    #3.指定排序规则
    ordering = ['-age']
  def __repr__(self):
    return "<Author:%r>" % self.name



class Book(models.Model):
  #重新为objects指定对象
  objects=BookManager()
  title = models.CharField(max_length=50,verbose_name='书名')
  publicate_date = models.DateField(verbose_name='出版日期')
  #增加对publisher的引用(1:M）
  publisher=models.ForeignKey(Publisher,null=True)
  #增加对Author的引用(多对多)
  authors=models.ManyToManyField(Author)

  # 重写__str__，来定义该对象的字符串的表现形式
  def __str__(self):
    return self.title

  class Meta:
    db_table='book'
    verbose_name='书籍'
    verbose_name_plural=verbose_name
    ordering=['-publicate_date']


class Wife(models.Model):
  name=models.CharField(max_length=30,verbose_name='姓名')
  age=models.IntegerField(verbose_name='年龄')
  #引用Author,实现一对一映射
  author=models.OneToOneField(Author,verbose_name='相公')

  def __str__(self):
    return self.name

  class Meta:
    db_table='wife'
    verbose_name='夫人'
    verbose_name_plural=verbose_name


