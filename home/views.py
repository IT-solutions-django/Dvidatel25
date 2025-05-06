from django.shortcuts import render
from django.views import View 
from .models import (
    CompanyInfo, 
    Service, 
    Work, 
    CompanyStat, 
    Request, 
    PrivacyPolicy, PersonalDataPolicy
)
import requests
from django.http import JsonResponse


class HomeView(View): 
    template_name = 'home/home.html'

    def get(self, request): 
        company_info = CompanyInfo.get_instance() 
        services = Service.objects.all()
        company_stats = CompanyStat.objects.all()
        works = Work.objects.all()
        privacy_policy = PrivacyPolicy.get_instance()
        personal_data_policy = PersonalDataPolicy.get_instance()
        context = {
            'company_info': company_info,
            'services': services,
            'works': works,
            'company_stats': company_stats,
            'privacy_policy': privacy_policy,
            'personal_data_policy': personal_data_policy,
        }
        return render(request, self.template_name, context)


class SaveRequestView(View):
    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        Request.objects.create(name=name, phone=phone)

        recipient = 'mr.energia25@mail.ru'
        ip = '82.202.128.97'
        url = 'https://sendemail.space/send-email/'
        data = {
            'recipient': recipient, 
            'subject': 'Новая заявка с сайта', 
            'content': f'Имя: {name}\nТелефон: {phone}',
            'ip': ip,
        }
        response = requests.post(url, data=data) 

        return JsonResponse({'success': True})


