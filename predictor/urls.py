# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.home, name="home"),
# ]

# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.welcome, name="home"),
    path("predict/", views.index, name="predict"),
    # path("admin/", admin.site.urls),
    # path('', include('predictor.urls')),
]
