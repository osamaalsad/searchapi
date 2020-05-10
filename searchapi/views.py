from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, SearchingData
from .serializers import CategorySerializer, SearchSerializer
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect
from searchapi.models import Category, SearchingData, UnknownSearch, CommentAnalysis
import nltk
from django.core.paginator import Paginator
nltk.download('stopwords')
nltk.download('punkt')
from searchapi.ProjectFunctionality.Preprocessing import Preprocess as pre
import searchapi.ProjectFunctionality.CommentAnlysis as CA

# Create your views here.
class CategoryView(APIView):
    def get(self,request):
        C = Category.objects.all()
        serializer = CategorySerializer(C, many=True)
        return Response(serializer.data)

class SearchResultView(ListAPIView):
    serializer_class = SearchSerializer
    def get_queryset(self, *args, **kwargs):  # new
        # variables initiolaization
        query = self.request.GET.get('q').lower()
        q2 = self.request.GET.get('drop1')
        object_list1 = SearchingData.objects.filter(ID__ID=q2)

        object_list = list()
        # searching query
        newstring = preprocessing(query).strip()
        oldstring = pre.limitazation(newstring).strip()
        for data in object_list1:
            if newstring in data.Name.lower() or newstring in data.Description:
                object_list.append(data)
        for data in object_list1:
            if oldstring in data.Name.lower() or oldstring in data.Description:
                object_list.append(data)
        if len(object_list) != 0:
            return set(object_list)
        else:
            object_list = pre.ifNoResult(object_list1, newstring, oldstring)
            Un1 = UnknownSearch(Name=query, num=q2)
            Un1.save()
            return set(object_list)

def preprocessing(query):
    temp = pre.cleanSymbol(query)
    temp = pre.reduce_lengthening(temp)
    temp = pre.wildcard(temp)
    temp = temp.split(' ')
    newstring = str()
    commonWord = ['google', 'facebook', 'twitter', 'kaggle']
    for index in range(len(temp)):
        if temp[index] not in commonWord:
            if temp[index] != pre.spellChecker(temp[index]):
                newstring += pre.spellChecker(temp[index]) + " "
            else:
                newstring += temp[index] + " "
        else:
            newstring += temp[index] + " "
    newstring = pre.stopWord(newstring)
    return newstring