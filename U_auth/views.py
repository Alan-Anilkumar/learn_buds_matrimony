from django.shortcuts import render

# Create your views here.

# def demo(request):
    # return render(request, 'base_files/base.html')

def login_view(request):
    return render(request, 'login.html')
def perdet_view(request):
    return render(request, 'personal details.html')
def jobst(request):
    return render(request, 'job status.html')
def jobd(request):
    return render(request, 'Job Details.html')
def jobd1(request):
    return render(request, 'Job Details2.html')
def relation(request):
    return render(request, 'Relationship.html')
def interest(request):
    return render(request, 'Interested.html')
def adddet(request):
    return render(request, 'Additional details.html')

def user_details(request):
    return render(request, 'User_profile_templates/user_pr_1.html')

def user_details_2(request):
    return render(request, 'User_profile_templates/user_pr_2.html')


def user_details_3(request):
    return render(request, 'User_profile_templates/user_pr_3.html')

def user_details_4(request):
    return render(request, 'User_profile_templates/user_pr_4.html')


def user_details_5(request):
    return render(request, 'User_profile_templates/user_pr_5.html')

def user_details_6(request):
    return render(request, 'User_profile_templates/user_pr_6.html')

def AuthPage(request):
    context = {
        'experance_level': ['Beginner', 'Intermediate', 'Expert'],
        'marital_status': ['Unmarried', 'Divorced']
    }
    return render(request, 'auth/auth.html',context)


def error_404(request):
    return render(request, 'Errors/404.html')


def error_403(request):
    return render(request, 'Errors/403.html')
