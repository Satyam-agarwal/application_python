from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'personal/home.html')

def contact(request):
	return render(request,'personal/basic.html', {'content':["If you like to contact me,email me ","agar1satyam@gmail.com"]}) #we are using dictionary now


