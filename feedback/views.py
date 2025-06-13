from django.shortcuts import render
from .forms import FeedbackForm

def index(request):
    success = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = FeedbackForm()
    return render(request, 'feedback/index.html', {'form': form, 'success': success})