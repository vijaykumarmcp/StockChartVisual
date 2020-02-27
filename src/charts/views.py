from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company

# Create your views here.
def company_article_view(request):
    return render(request,'charts/plotly.html',{})

class ChartData(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self,request,format=None):
        articles=dict()
        for company in Company.objects.all():
            if company.articles>0:
                articles[company.name]=company.articles
        
        articles=sorted(articles.items(),key=lambda x:x[1])
        articles=dict(articles)

        data={
            'article_label':articles.keys(),
            'article_data':articles.values()

        }

        return Response(data)