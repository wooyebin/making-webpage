from django.shortcuts import render

# Create your views here.
# index.html 페이지를 부르는 index 함수
def index(request):
    return render(request, 'main/index.html')
