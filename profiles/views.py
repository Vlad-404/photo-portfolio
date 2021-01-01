from django.shortcuts import render


# Display the user's profile
def profile(request):
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
