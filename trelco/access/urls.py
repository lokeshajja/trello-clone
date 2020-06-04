from django.contrib import admin
from django.urls import path, include
from access.views.board_view import BoardListApi, BoardDetailView, index
from access.views.list_view import ListListApi, ListDetailView

urlpatterns = [
    path('', index, name='index'),
    path('boards', BoardListApi.as_view(), name='boards_listing_view'),
    path('boards/<board_id>', BoardDetailView.as_view(), name = 'boards_detail_view'),
    path('lists', ListListApi.as_view(), name='lists_listing_view'),
    path('lists/<list_id>', ListDetailView.as_view(), name = 'lists_detail_view'),


    
]