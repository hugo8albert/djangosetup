from django.urls import path
from.import views

urlpatterns=[
    path('register/', views.register_view, name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name="logout"),
    path('', views.home_view, name='home'),
    path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),
    path('create-post/', views.create_post_view,name='create_post'),
    
]
