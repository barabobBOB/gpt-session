from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm  # 게시글을 입력할 폼이 필요한 경우


def create_post(request):
    post_saved = False  # 초기에는 저장되지 않은 상태로 설정

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            post_saved = True  # 게시글이 성공적으로 저장됨

    else:
        form = PostForm()

    context = {'form': form, 'post_saved': post_saved}
    return render(request, 'post/create_post.html', context)
