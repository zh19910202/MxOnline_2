# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class OrgView(View):
    def get(self, request):
        # 课程机构
        all_org = CourseOrg.objects.all()
        org_nums = all_org.count()
        # 城市
        all_citys = CityDict.objects.all()

        # 取出筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_org, 3, request=request)

        orgs = p.page(page)
        return render(request, 'org-list.html', {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
        })
