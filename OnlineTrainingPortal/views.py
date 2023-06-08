from django.shortcuts import render,redirect
from OnlineTrainingPortal.course.models import Course
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.forms import UserCreationForm  


def home(request):
    
    if not request.user.is_authenticated:
        pass
    elif request.user.is_teacher:
        if request.user.is_approved:
            return redirect ('teacher:home')
        else:
            return redirect('userAuthentication:unApproved')
    elif request.user.is_student:
        return redirect('course:home')
    elif request.user.is_admin:
        return redirect('administration:home')
            
    
    # subject = "HTML Mail Testing"
    # from_mail = 'work.anjon@gmail.com'
    # to = 'debanjan35-2044@diu.edu.bd'
    # msg = 'I am <b>sending</b> my <strong>first HTML message</strong> using mail form my Django project.'
    # msg  = EmailMultiAlternatives(subject,msg,from_mail,[to])
    # msg.content_subtype = 'html'
    # msg.send()
    # send_mail(
    #     'Testing Mail',
    #     'This is the First message i am sending from my Django website.',
    #     'work.anjon@gmail.com',
    #     ['debanjan35-2044@diu.edu.bd'],
    #     fail_silently=False,
    # )

    data = {
        'title' : 'Home Page',
    }
    return render(request, 'index.html', data)

def navbar(request):
    
    courselist = Course.objects.all().order_by('-updated')
    for course in courselist:
        print(course)
    sp = ''
    if request.method == 'GET':
        sb = request.GET.get('search')
        print(sb)
        if sb != None:
            courselist = Course.objects.filter(course_title__icontains = sb)
            data = {
                        'search' : sp,
                        'courselist' : courselist,
                    }
            return render(request, 'course/course.html', data)

    return render(request,'navbar.html',data)

def about(request):
    data = {
        'title' : 'About Us',
        'banner' : 'About page is loading....',
        'programmer_list' : [
            {'name' : 'Debanjan Paul', 'title' : 'Fontend Developer'},
            {'name' : 'Anjon Paul', 'title' : 'Backend Developer'},
            {'name' : 'Banamala Paul', 'title' : 'Management'},
            {'name' : 'Pankag Kanti Paul', 'title' : 'Management'},
            {'name' : 'Pappu Paul', 'title' : 'Management'},
        ],
    }
    return render(request, 'about.html', data)


def thank(request):
    if request.method == 'GET':
        output = request.GET.get('output')
    return render(request,'thank.html',{'output': output})

def gideLine(request):
    return render (request,'website_gideline.html')