from django.urls import path
from . import views

app_name = 'setup'

urlpatterns = [
    # levels
    path('levels', views.level_list, name='levels'),
    path('create_level', views.create_level, name='create_level'),
    path('update_level/<int:id>/', views.update_level, name='update_level'),
    path('change_status/<int:id>/', views.change_status, name='change_status'),
    path('delete_level/<int:id>/', views.delete_level, name='delete_level'),

    # terms
    path('terms', views.term_list, name='terms'),
    path('create_term', views.create_term, name='create_term'),
    path('update_term/<int:id>/', views.update_term, name='update_term'),
    path('change_term_status/<int:id>/', views.change_term_status, name='change_term_status'),
    path('delete_term/<int:id>/', views.delete_term, name='delete_term'),

    # grades
    path('grades', views.grade_list, name='grades'),
    path('create_grade', views.create_grade, name='create_grade'),
    path('update_grade/<int:id>/', views.update_grade, name='update_grade'),
    path('change_grade_status/<int:id>/', views.change_grade_status, name='change_grade_status'),
    path('delete_grade/<int:id>/', views.delete_grade, name='delete_grade'),

    # subjects
    path('subjects', views.subject_list, name='subjects'),
    path('create_subject', views.create_subject, name='create_subject'),
    path('update_subject/<int:id>/', views.update_subject, name='update_subject'),
    path('change_subject_status/<int:id>/', views.change_subject_status, name='change_subject_status'),
    path('delete_subject/<int:id>/', views.delete_subject, name='delete_subject'),

    # houses
    path('houses', views.house_list, name='houses'),
    path('create_house', views.create_house, name='create_house'),
    path('update_house/<int:id>/', views.update_house, name='update_house'),
    path('change_house_status/<int:id>/', views.change_house_status, name='change_house_status'),
    path('delete_house/<int:id>/', views.delete_house, name='delete_house'),
]