from multiprocessing import context
from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def profile(request, pk):
    user_profile = UserProfile.objects.get(profile_id=pk)
    context={'profile':user_profile}
    return render(request, 'profiles/profile.html', context)

def account(request):
    user_account = request.user.userprofile
    context = {'account':user_account}
    return render(request, 'profiles/account.html', context)