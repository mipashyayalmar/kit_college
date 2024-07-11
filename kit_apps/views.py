from django.shortcuts import render, HttpResponse
from .models import StudentSuggestion
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('/')

def home(request):
    return render(request, "home.html")

def suggestion_list(request):
    suggestions = StudentSuggestion.objects.all()
    message = None  # Initialize message variable

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        about = request.POST.get('about', '')
        
        if first_name and email and phone and subject and about:  # Check if all fields are filled
            new_suggestion = StudentSuggestion.objects.create(
                f_name=first_name,
                email=email,
                phone=phone,
                subject=subject,
                about=about
            )
            new_suggestion.save()
            message = "Suggestion uploaded successfully!"  # Set success message
        else:
            message = "Error: All fields are required!"  # Set error message
    else:
        message = None  # No message if it's a GET request
    
    return render(request, 'suggestions.html', {'suggestions': suggestions, 'message': message})
def suggestion_table(request):
    suggestions = StudentSuggestion.objects.all()
    return render(request, 'suggestions_table.html', {'suggestions': suggestions})

def event(request):
    return render(request,'events.html')