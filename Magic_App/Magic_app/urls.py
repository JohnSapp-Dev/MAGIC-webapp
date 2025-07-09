from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("<int:wait_time_id>/", views.wait_time_view, name="waittime"),
    path("load_attraction/", views.load_attraction, name="load_attraction"),
    path("wait_times/", views.index, name="wait_time_graph"),
    path("heat_map/", views.heatmap,name="heatmap"),
]

""" wait_times/

path("", views.homepage, name="home"), """