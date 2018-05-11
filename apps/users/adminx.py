# _*_ coding: utf-8 _*_
__author__ = 'HeYang'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banner, UserProfile

from django.contrib.auth.admin import UserAdmin


# class UserProfileAdmin(object):
#     list_display = ['username', 'email', 'is_active', 'gender', 'address']
#     search_fields = ['username', 'email', 'is_active', 'gender', 'address']
#     list_filter = ['username', 'email', 'is_active', 'gender', 'address']


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "HeYang后台管理系统"
    site_footer = "HeYang在线学习网站"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time', 'active_status']
    search_fields = ['code', 'email', 'send_type', 'active_status']
    list_filter = ['code', 'email', 'send_type', 'send_time', 'active_status']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)