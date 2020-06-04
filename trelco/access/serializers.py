from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField, RelatedField
from access.models import Board, Card, List, CheckList, SubTask, Comment

'''alternative way'''
# from rest_framework import serializers
# class BoardSerializer(serializers.Serializer):


class BoardSerializer(ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'


class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'


class ListSerializer(ModelSerializer):

    class Meta:
        model = List
        fields = '__all__'


class CheckListSerializer(ModelSerializer):

    class Meta:
        model = CheckList
        fields = '__all__'


class SubTaskSerializer(ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
