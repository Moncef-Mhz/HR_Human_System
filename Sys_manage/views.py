from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect

# Create your views here.

def HomePage(request) :
    return render(request , 'home.html' , { 'PageTitle' : 'Home Page'});

def FavoriteSection(request) :
    return render(request , 'Section/Favorie.html' , { 'PageTitle' : 'Section des Favorie'});

def ContratSection(request) :
    return render(request , 'Section/Contrat.html' , { 'PageTitle' : 'Section des Contrat'});

def EmployesSection(request) :
    return render(request , 'Section/Employes.html' , { 'PageTitle' : 'Section des Employes'});

def HolidaySection(request) :
    return render(request , 'Section/Conge.html' , { 'PageTitle' : 'Section des Congé'});

def EvaluationSection(request) :
    return render(request , 'Section/Evaluation.html' , { 'PageTitle' : 'Section des Evaluation'});

def AnalyseSection(request) :
    return render(request , 'Section/Analyse_Bord.html' , { 'PageTitle' : 'Section des Analyse et tableau Bord'});

def RecruitmentSection(request) :
    return render(request , 'Section/Recrutements.html' , { 'PageTitle' : 'Section des Recrutements'});

def SalarySection(request) : 
    return render(request , 'Section/Salary.html' , { 'PageTitle' : 'Section des Salaires et de la Paie'});

def SignUp(request):
    if request.method == 'POST':  
        Email = request.POST.get('email')  
        Password = request.POST.get('password')
        
        if Email and Password:  # Ensure both fields are filled
            print(Email)
            print(Password)
            return HttpResponseRedirect('/Favorie') 
        else:
            return render(request, 'Login/Signup.html', {
                'PageTitle': 'SignUp',
                'error': 'Please fill in all fields.'
            })
    
    return render(request, 'Login/Signup.html', {'PageTitle': 'SignUp'})

    


