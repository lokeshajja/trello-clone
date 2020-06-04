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
from access.serializers import BoardSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the HOMEPAGE :).")

  
class BoardListApi(APIView):

    def get(self, request):
        all_boards = Board.objects.filter(is_archive=False, is_active=True).all()
        serializer = BoardSerializer(all_boards, many=True)
        return JsonResponse(serializer.data, safe=False)


    def post(self, request):
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class BoardDetailView(APIView):

    def get(self, request, board_id):

        board = None
        lists_belonging_to_board = None
        data = {}

        board = Board.objects.filter(id= board_id, is_archive=False, is_active=True).first()
        if board is None:
            return HttpResponse(status=404)
            
        lists_belonging_to_board = List.objects.filter(board_id = board_id, is_archive=False, is_active=True).all()

        data['board'] = board
        data['lists_belonging_to_board'] = lists_belonging_to_board

        return JsonResponse(data, status=200)


    def put(self, request, board_id):

        board = None

        board = Board.objects.filter(id= board_id, is_active=True).first()
        if board is None:
            return HttpResponse(status=404)
        data = JSONParser().parse(request)
        serializer = BoardSerializer(board, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    def delete(self, request, board_id):

        board = Board.objects.filter(id= board_id, is_active=True).first()
        if board is None:
            return HttpResponse(status=404)

        board.is_active = False
        board.save()
        response = { "board id" : board_id,
                     "status" : "deleted" }

        return HttpResponse( response, status=204)
     