from django.urls import path,include
from . import views

# extra_patterns  = [
#     path('/index1',views.index,name='idx1'),
#     path('/index2',views.index2,name='idx2'),
#     path('/index3',views.index3,name='idx3'),
# ]

urlpatterns = [
    path('my',views.hello,name='hello'),
    
    path("myvi/<int:id>/",views.my_view, name="ioerd"),
    path(
        'idx/',
        include(
            [
               
                path('index2/',views.index2,name='idx2'),
                path('index3/',views.index3,name='idx3'),
            ]
        ),
    ),   
]
