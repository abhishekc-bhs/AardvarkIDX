from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        snippet = request.POST.get('snippet')
        print(snippet)
        return redirect('home')
    return render(request, 'core/index.html')