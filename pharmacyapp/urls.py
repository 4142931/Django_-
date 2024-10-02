from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import create_review_and_score, dashboard, SignUpView, delete_score
from .views import review_list_view, board_detail_view

urlpatterns = [
    path('', views.review_list_view, name='home'),
    path('join_page/', SignUpView.as_view(), name='register'),  # 회원가입
    path('login/', LoginView.as_view(template_name='base.html'), name='login'),  # 로그인
    path('logout/', LogoutView.as_view(), name='logout'),  # 로그아웃
    path('review_create/<int:pharmacy_id>/', create_review_and_score, name='review_create'),
    path('score/delete/<int:score_id>/', views.delete_score, name='delete_score'),  # 리뷰 삭제
    path('review_list/<int:pharmacy_id>/', create_score, name='review_list'),
    path('review_update/<int:pharmacy_id>/', create_score, name='review_update'),
    path('dashboard/', dashboard, name='dashboard'),
    path('reviews/', review_list_view, name='review-list'),  # 함수 기반 뷰로 변경
    path('boards/<int:pk>/', board_detail_view, name='board-detail'),  # 함수 기반 뷰로 변경
]