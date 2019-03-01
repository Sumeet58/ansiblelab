from django.conf.urls import url
#from django.urls import path
from myapp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url('c_hostname/', views.my_view1,name='my_view_name1'),
    url('p_install/', views.my_view2,name='my_view_name2'),

]
