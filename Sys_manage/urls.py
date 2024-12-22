from django.urls import path
from . import views


urlpatterns = [
    path('' , views.HomePage , name="Favorie"),
    path('Favorie' , views.FavoriteSection , name="Favorie"),
    path('contrat', views.ContratSection , name="Contrat"),
    path('Employes', views.EmployesSection , name="Contrat"),
    path('Congee', views.HolidaySection , name="Contrat"),
    path('Evaluation', views.EvaluationSection , name="Contrat"),
    path('Analyse_Tab-Bord', views.AnalyseSection , name="Contrat"),
    path('Salary', views.SalarySection , name="Contrat"),
    path('Recrutments', views.RecruitmentSection , name="Contrat"),
    path('SignUp/', views.SignUp, name='SignUp'),
]