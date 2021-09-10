from .models import Bookmark
from django.utils import timezone
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import Bookmark_serializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
search_str = ""
class home(View):
    
    def get(self,request):
        global search_str
        search_str = ""
        return render(request,template_name='saveit/home.html',context={'entries':Bookmark.objects.all()})
    def post(self,request):
        global search_str
        search_str = request.POST['search_text']
        
        return redirect('/saveit/search')
# @api_view(['POST'])
class add_tags(View):
    def get(self,request,id):
        return render(request,template_name='saveit/tags.html',context={'entry':Bookmark.objects.get(id = id)})
    
    def post(self,request,id):
        entry = Bookmark.objects.get(id = id) #Getting the specific bookmark entry
        if request.POST['tags'] != "" :
            tags = request.POST['tags'] 
            entry.tags.create(name = tags)
            entry.save()
            return redirect('/saveit')
        else:    
            return redirect('/saveit')

class search(View):
        def get(self,request):
            search_result = []
            
            for entry in Bookmark.objects.all():
                
                if search_str in entry.name or search_str in str(entry.date) or search_str in entry.url or search_str in [tag.name for tag in entry.tags.all()] :
                    search_result.append(entry)
            return render(request,template_name='saveit/search.html',context={'entries':search_result})

@csrf_exempt
def save_api(request):
    
    if request.method == "POST" :
    
        print(request.body)
        json_data = request.body
        stream = io.BytesIO(json_data)
        jsdata = JSONParser().parse(stream)
        serializer = Bookmark_serializer(data = jsdata)
        print(serializer)
        
        if serializer.is_valid():

            serializer.save()
            res={'msg':'ok'}
                # json_data = JSONRenderer(res)
            return JsonResponse(res)
        else:
            print('not valid')
            res={'msg':'ok'}
                # json_data = JSONRenderer(res)
            return JsonResponse(res)
    
            

            

