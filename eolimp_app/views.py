from django.shortcuts import redirect, render


def home(request):
    # if request.user.is_authenticated:
    #     return redirect('my_account')
    return render(request, 'pre_login.html')
