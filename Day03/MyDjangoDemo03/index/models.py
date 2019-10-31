from django.db import models

# Create your models here.
#创建一个实体类-Publisher(出版社)
#1.name:出版社名称（varchar(30)）
#2.address:出版社所在地址（varchar(200)）
#3.city:出版社所在城市(varchar(50))
#4.country:出版社所在国家（varchar（50））
#5.website:出版社的网址（varchar（200））

class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    websize=models.URLField()

#创建Author实体类
class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.ImageField()
    email=models.EmailField(null=True)
    #增加一个字段：isActive用于表示用户的激活状态
    #类型为BooleanField(),
    #True表示用户已激活，False表示用户未激活
    isActive=models.BooleanField(default=True)



#创建Book实体类
class Book(models.Model):
    title=models.CharField(max_length=50)
    publicate_date=models.DateField()

