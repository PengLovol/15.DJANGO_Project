from django.contrib import admin
from .models import *

#声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
  #指定在列表页中显示的字段们
  list_display = ('name','age','email')
  #指定能够连接到详情页的字段们
  list_display_links = ('name','email')
  #指定在列表页中就允许被修改的字段们
  list_editable = ('age',)
  #指定条件的搜索字段们
  search_fields = ('name','email')
  #指定右侧过滤器
  list_filter=('name',)
  #指定显示的字段以及显示的顺序
  # fields = ('name','isActive','email')
  #指定显示的字段分组
  fieldsets = (
    #分组１
    ('基本信息',{
      'fields':('name','email'),
    }),
    #分组２
    ('可选信息',{
      'fields':('age','isActive','picture'),
      'classes':('collapse',),
    })
  )


class BookAdmin(admin.ModelAdmin):
  #指定时间选择器
  date_hierarchy = "publicate_date"


class PublisherAdmin(admin.ModelAdmin):
  list_display = ('name','address','city','website')
  list_editable = ('address','city')
  list_filter = ('address','city')
  search_fields = ('name','website')
  fieldsets = (
    ('基本选项',{
      'fields':('name','address','city'),
    }),
    (
      '高级选项',{
        'fields':('country','website'),
        'classes':('collapse',)
      }
    )
  )


# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Wife)
