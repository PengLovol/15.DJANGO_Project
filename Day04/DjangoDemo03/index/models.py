from django.db import models

# Create your models here.
#创建一个实体类 - Publisher
#用于表示出版社信息，属性如下
#1.name：出版社名称(varchar)
#2.address：出版社所在地址(varchar)
#3.city：出版社所在城市(varchar)
#4.country：出版社所在国家(varchar)
#5.website：出版社的网址(varchar)
class Publisher(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  website = models.URLField()

#创建　Author 的实体类
#1.name - 姓名(CharField -> varchar)
#2.age - 年龄(IntegerField -> int)
#3.email - 电子邮件(EmailField -> varchar)
class Author(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
  email = models.EmailField(null=True)
  #表示用户的激活状态：True,表示已激活,False,表示未激活
  #由于是新增列，所以必须要给默认值或允许为空
  #由于BooleanField默认是不允许为空的，所以此处选择了增加默认值
  isActive = models.BooleanField(default=True)

  def __repr__(self):
    return "<Author:%r>" % self.name

class Book(models.Model):
  title = models.CharField(max_length=50)
  publicate_date = models.DateField()





