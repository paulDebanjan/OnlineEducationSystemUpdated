from django.shortcuts import render
from .models import Enquiry
from django.views.generic import CreateView

# Create your views here.

class EnquiryView(CreateView):
    model=Enquiry
    fields = ['first_name']
# def enquiry(request):
    
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         specification = request.POST.get('specification')
#         message = request.POST.get('message')
#         save_data = Enquiry(first_name=first_name,last_name=last_name,email=email,enquiry_specification= specification, message=message)
#         save_data.save()

#     data= {
#         'title' : 'Enquity',
#     }
#     return render(request,'enquiry/enquiry.html',data)