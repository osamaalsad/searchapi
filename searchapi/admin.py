from django.contrib import admin
from searchapi.models import SearchingData, Category, UnknownSearch, CommentAnalysis
admin.site.register(SearchingData)
admin.site.register(Category)
admin.site.register(UnknownSearch)
admin.site.register(CommentAnalysis)
# Register your models here.
