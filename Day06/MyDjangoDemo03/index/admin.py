from django.contrib import admin
from .models import *

#声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
    #指定再列表页中显示的字段们
    list_display = ('name','age','email')
    # 指定能够连接到详情页的字段们
    list_display_links = ('name', 'email')
    #指定在列表页中就允许被修改的字段们
    list_editable = ('age',)
    #指定条件的搜索字段们
    search_fields = ('name','email')
    # 指定右侧过滤器
    list_filter = ('name',)
    # 指定显示的字段以及显示的顺序
    # fields = ('name','isActive','email')
    # 指定显示的字段分组
    fieldsets = (
        # 分组１
        ('基本信息', {
            'fields': ('name', 'email'),
        }),
        # 分组２
        ('可选信息', {
            'fields': ('age', 'isActive','picture'),
            'classes': ('collapse',),
        })
    )

class BookAdmin(admin.ModelAdmin):
    #指定时间选择器
    date_hierarchy = 'publicate_date'

class PublisherAdmin(admin.ModelAdmin):
    # 练习：完成Publisher的高级管理功能
    # 1.在列表页中显示
    # name, address, city, website属性
    # 2. address和city是可编辑的
    # 3.右侧增加过滤器，允许按照address和city进行筛选
    # 4.顶部增加搜索框，允许按照name和website进行搜索
    # 5.详情页中分组显示
    #   1. name, address, city为"基本选项"
    #   2.country, website为"高级选项"并可以折叠
    list_display = ('name','address','city','website')
    list_editable = ('address','city')
    list_filter = ('address','city')
    search_fields = ('name','website')
    fieldsets = (
        ('基本选项',{
            'fields':('name','address','city'),
        }),
        ('高级选项',{
            'fields':('country','website'),
            'classes':('collapse',),

        })
    )

# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Wife)