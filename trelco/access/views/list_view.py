from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from access.models import Board, List, Card, CheckList, SubTask, Comment 
from access.serializers import ListSerializer


class ListListApi(APIView):

    def get(self, request):
        all_lists = List.objects.filter(is_archive=False, is_active=True).all()
        serializer = ListSerializer(all_lists, many=True)
        return JsonResponse(serializer.data, safe=False)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ListDetailView(APIView):

    def get(self, request, list_id):

        list = None
        cards_belonging_to_list = None
        data = {}

        list = List.objects.filter(id= list_id, is_archive=False, is_active=True).first()
        if list is None:
            return HttpResponse(status=404)
            
        cards_belonging_to_list = Card.objects.filter(list_id = list_id, is_archive=False, is_active=True).all()

        data['list'] = list
        data['cards_belonging_to_list'] = cards_belonging_to_list

        return JsonResponse(data, status=200)


    def put(self, request, list_id):

        list = None

        list = List.objects.filter(id= list_id, is_active=True).first()
        if list is None:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = ListSerializer(list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    def delete(self, request, list_id):

        list = List.objects.filter(id= list_id, is_active=True).first()
        if list is None:
            return HttpResponse(status=404)

        list.is_active = False
        list.save()
        response = { "list id" : list_id,
                     "status" : "deleted" }

        return HttpResponse( response, status=204)
     