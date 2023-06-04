import subprocess
from django.shortcuts import render   

def main_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def study_view(request):
    return render(request, 'study.html')

def coffees_view(request):
    return render(request, 'coffees.html')

def shop_view(request):
    return render(request, 'shop.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')

def run_script(request):    
    grade = request.GET.get('grade')
    subject = request.GET.get('subject')
    input1 = request.GET.get('input1')
    print("\nThis a simple function\n")
    print("\ngrade : ", grade)
    print("\nsubject : ", subject)
    print("\ninput : ", input1)
    print("\nThis a simple function\n")
    script_path = r"D:/coding_play/django/study/download_exam.py"
    subprocess.Popen(["python", script_path])