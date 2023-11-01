from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context ={
        "variable":"hello."
    }
    return render (request ,'index.html',context)
    # return HttpResponse('this is a homepage')
# def about(request):
#     # return HttpResponse('this is a about-page')
#     return render (request ,'about.html')
# def skills(request):
#     # return HttpResponse('this is a contact-page')
#     return render (request ,'skills.html')
# def projects(request):
#     # return HttpResponse('this is a contact-page')
#     return render (request ,'projects.html')
# def contact(request):
#     # return HttpResponse('this is a contact-page')
#     return render (request ,'contact.html')
