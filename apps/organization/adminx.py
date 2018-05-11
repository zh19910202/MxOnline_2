# _*_ coding: utf-8 _*_
__author__ = 'HeYang'

from .models import CityDict, CourseOrg, Teacher
import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['click_nums', 'name', 'desc', 'fav_nums', 'image', 'address',
                    'city', 'add_time']
    search_fields = ['click_nums', 'name', 'desc', 'fav_nums', 'image', 'address',
                    'city']
    list_filter = ['click_nums', 'name', 'desc', 'fav_nums', 'image', 'address',
                    'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'wrok_years', 'wrok_company', 'wrok_position', 'points',
                    'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'wrok_years', 'wrok_company', 'wrok_position', 'points',
                    'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'wrok_years', 'wrok_company', 'wrok_position', 'points',
                    'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(CityDict, CityDictAdmin)