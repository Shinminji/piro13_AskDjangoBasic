from django.shortcuts import render

def post_list(request):
    #첫 번째부터 순차적으로 경로 찾기 시작
    return render(request, 'blog/post_list.html')