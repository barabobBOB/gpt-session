from django.urls import path
from . import views

urlpatterns = [
    # 기타 URL 패턴...
    path('create/', views.create_post, name='create_post'),  # 게시글 저장 뷰
]
