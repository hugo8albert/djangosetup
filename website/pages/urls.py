from django.urls import path

from.import views

urlpatterns=[path('',views.home_view,name='home'),
        path('page/<int:page_id>/', views.page_view, name='page'),     
             ]