from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


# UI 설정부분(템플릿) 처리하는 view
def hello_world_template(request):
    return render(request, 'accountapp/hello_world.html')


# 로직 처리하는 view
@api_view(['GET', 'POST'])
def hello_world(request):

    # POST 방식
    if request.method == 'POST':
        input_data = request.data.get('input_data')
        return Response({'message': input_data})

    # GET 방식
    return Response({'message': 'Return Text'})