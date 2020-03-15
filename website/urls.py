from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1, name='index1'),
    path('index1',views.index1, name='index1'),
    path('college',views.college, name='college'), 
    path('search',views.search, name='search'),
    path('about',views.about, name='about'),
    path('courses',views.courses, name='courses'),
    path('catagory',views.catagory, name='catagory'),
    path('filtered',views.filtered,name='filtered'),
    path('filterincatagory',views.filterincatagory, name="filterincatagory"),
    
]