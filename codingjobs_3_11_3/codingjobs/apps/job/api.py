import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Job

def api_search(request):
    joblist = []
    data = json.loads(request.body)
    query = data['query']
    company_size = data['company_size']
    jobs = Job.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(long_description__icontains=query) | Q(company_name__icontains=query) | Q(company_address__icontains=query) | Q(company_zipcode__icontains=query) | Q(company_place__icontains=query) | Q(company_country__icontains=query) | Q(company_size__icontains=query))
    
    if company_size:
        jobs = jobs.filter(company_size=company_size)
        
    for job in jobs:
        obj = {
            'id' : job.id,
            'title' : job.title,
            'company_name' : job.company_name,
            'url' : '/jobs/%s/' % job.id
        }
        joblist.append(obj)
        
    return JsonResponse({'jobs': joblist})