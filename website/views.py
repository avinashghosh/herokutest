from .models import College,Coursedetails,Collegecatagories
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.db.models import Count
# Create your views here.
d=0

def index1(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    '''b = College.objects.all().count()
    a = ["Engineering","Management","Science"]
    
    for i in range(0,len(engcollg)):
        if 
        countcollg[i] = College.objects.filter(Q(collegecatagory__icontains=a[i])).count()'''
    collg = Collegecatagories.objects.order_by().values_list('catagory',flat=True)
    collgs = Collegecatagories.objects.all().order_by('catagory')

    b = College.objects.values_list('collegecatagory',flat=True)
    

    if collgs:
        return render(request, 'index1.html',{'data':match1,"m1":m1,"engcollg":collgs,"en":b,"scount":5})
    return render(request,'index1.html')
def college(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    if request.GET['sub']:
        item = College.objects.filter(Q(name=request.GET['sub']))
        if item:
            return render(request, 'college.html',{'dests':item,'data':match1,"m1":m1,"scount":2})
        else:
            HttpResponse(request,'no results found')
    return render(request,'college.html')  
def courses(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    cur_col = College.objects.filter(Q(ccode=request.GET['cour']))
    sublist = Coursedetails.objects.filter(Q(ccode1=request.GET['cour']) & Q(coursetype=request.GET['crstype']))
    return render(request, 'courses.html',{'data':match1,"m1":m1,'sub':sublist,'current':cur_col,"scount":2})
def search(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    if request.method=='POST':
        srch = request.POST['srh']
        
    if request.method=='GET':
        cit = request.GET['cityf']
        ctyp = request.GET['ctype']
        cours = request.GET['course']
        stre = request.GET["stream"]
    
    cities = College.objects.values_list('city',flat=True).distinct()
    coursef = Coursedetails.objects.values_list('course',flat=True).distinct()
    streamf = Coursedetails.objects.values_list('stream',flat=True).distinct()


    if srch:
        match = College.objects.filter(Q(name__icontains=srch) | Q(address__icontains=srch) | Q(ccode__icontains=srch))
        if match:
            return render(request, 'search.html',{'dests':match,'data':match1,"m1":m1,"scount":2,"cities":cities,"coursef":coursef,"streamf":streamf})
        else:
            HttpResponse(request,'no results found')
    else:
        return HttpResponseRedirect('/search')
    return render(request,'search.html',{'dests':match,'data':match1,"m1":m1,"scount":2,"cities":cities,"sts":2,"scount":2,"cities":cities,"coursef":coursef,"streamf":streamf})

def filtered(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)

    if request.method=='GET':
        cit = request.GET['cityf']
        ctyp = request.GET['ctype']
        cours = request.GET['course']
        stre = request.GET["stream"]
    
    cities = College.objects.values_list('city',flat=True).distinct()
    coursef = Coursedetails.objects.values_list('course',flat=True).distinct()
    streamf = Coursedetails.objects.values_list('stream',flat=True).distinct()

    '''filterre = College.objects.filter(Q(city=cit))'''
    UGC = Coursedetails.objects.values_list('ccode1',flat=True).distinct()
    FILT = Coursedetails.objects.values_list('ccode1',flat=True).filter(Q(coursetype__icontains=ctyp)&Q(course__icontains=cours)&Q(stream__icontains=stre)).distinct()

    CIT = College.objects.values_list('ccode',flat=True).filter(Q(city__icontains=cit)).distinct()

    FILFINAL = CIT.intersection(FILT)
    match=[]
    if UGC:
        for itere in FILFINAL:
            match.extend(list(College.objects.filter(Q(ccode__icontains=itere))))
        if match:
            return render(request, 'filtered.html',{'dests':match,'data':match1,"m1":m1,"scount":2,"cities":cities,"coursef":coursef,"streamf":streamf})
        else:
            HttpResponse(request,'no results found')
    else:
        return HttpResponseRedirect('/filtered')
    return render(request,'filtered.html',{'dests':match,'data':match1,"m1":m1,"scount":2,"cities":cities})


def filterincatagory(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)

    if request.method=='GET':
        cit = request.GET['cityf']
        ctyp = request.GET['ctype']
        cours = request.GET['course']
        stre = request.GET["stream"]
        currcatagory = request.GET['currcatagory']
    
    cities = College.objects.values_list('city',flat=True).distinct()
    coursef = Coursedetails.objects.values_list('course',flat=True).distinct()
    streamf = Coursedetails.objects.values_list('stream',flat=True).distinct()

    '''filterre = College.objects.filter(Q(city=cit))'''
    UGC = Coursedetails.objects.values_list('ccode1',flat=True).distinct()
    FILT = Coursedetails.objects.values_list('ccode1',flat=True).filter(Q(coursetype__icontains=ctyp)&Q(course__icontains=cours)&Q(stream__icontains=stre)).distinct()

    CIT = College.objects.values_list('ccode',flat=True).filter(Q(city__icontains=cit)).distinct()

    FILFINAL = CIT.intersection(FILT)
    match=[]
    print(currcatagory)
    if UGC:
        for itere in FILFINAL:
            match.extend(list(College.objects.filter(Q(ccode__icontains=itere))))
            
        if match:
            return render(request, 'filtered.html',{'dests':match,'data':match1,"m1":m1,"scount":2,"cities":cities,"coursef":coursef,"streamf":streamf,"currcatagory":currcatagory})
        else:
            HttpResponse(request,'no results found')
    else:
        return HttpResponseRedirect('/filtered')
    return render(request,'filtered.html',{'dests':match,'data':match1,"m1":m1,"scount":2,"cities":cities,"coursef":coursef,"streamf":streamf,"currcatagory":currcatagory})
   
def catagory(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)

    cities = College.objects.values_list('city',flat=True).distinct()
    coursef = Coursedetails.objects.values_list('course',flat=True).distinct()
    streamf = Coursedetails.objects.values_list('stream',flat=True).distinct()


    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match = College.objects.filter(Q(collegecatagory__icontains=srch))
            if match:
                return render(request, 'catagory.html',{'dests':match,'data':match1,"m1":m1,"currcatagory":srch,"scount":2,"cities":cities,"coursef":coursef,"streamf":streamf})
            else:
                HttpResponse(request,'no results found')
        else:
            return HttpResponseRedirect('/search')
    return render(request,'catagory.html',{'data':match1,"m1":m1,"currcatagory":srch,"scount":2,"vis":2})


def about(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    if request.method == 'POST':
        contact_email = request.POST['email']
        contact_name =request.POST['name'] +' / '+ contact_email
        
        contact_message = request.POST['message']
        send_mail(contact_name, contact_message, contact_email, ['avinashghoshpullur@gmail.com'])
    return render(request,'about.html',{'data':match1,"m1":m1,"scount":2})



'''from .models import College,Coursedetails,Collegecatagories
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from django.db.models import Count
countcollg = {}
# Create your views here.
def index1(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    b = College.objects.all().count()
    a = ["Engineering","Management","Science"]
    
    for i in range(0,len(engcollg)):
        countcollg[i] = College.objects.filter(Q(collegecatagory__icontains=a[i])).count()
    collg = Collegecatagories.objects.order_by().values('catagory').count()
    collgs = Collegecatagories.objects.all()

    b = College.objects.all().count()
    a = Collegecatagories.objects.values('catagory')
    for i in range(0,b):
        for j in range(0,b):
            countcollg[0] = College.objects.filter(Q(collegecatagory__icontains="engineering")).count()
            countcollg[1] = College.objects.filter(Q(collegecatagory__icontains="science")).count()
            countcollg[2] = College.objects.filter(Q(collegecatagory__icontains="management")).count()


    if collgs:
        return render(request, 'index1.html',{'data':match1,"m1":m1,"engcollg":collgs,"en":countcollg,"a":a})
    return render(request,'index1.html')
def college(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    if request.GET['sub']:
        item = College.objects.filter(Q(name=request.GET['sub']))
        if item:
            return render(request, 'college.html',{'dests':item,'data':match1,"m1":m1})
        else:
            HttpResponse(request,'no results found')
    return render(request,'college.html')  
def courses(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    cur_col = College.objects.filter(Q(ccode=request.GET['cour']))
    sublist = Coursedetails.objects.filter(Q(ccode1=request.GET['cour']) & Q(coursetype=request.GET['crstype']))
    return render(request, 'courses.html',{'data':match1,"m1":m1,'sub':sublist,'current':cur_col})
def search(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match = College.objects.filter(Q(name__icontains=srch) | Q(address__icontains=srch))
            if match:
                return render(request, 'search.html',{'dests':match,'data':match1,"m1":m1})
            else:
                HttpResponse(request,'no results found')
        else:
            return HttpResponseRedirect('/search')
    return render(request,'search.html',{'data':match1,"m1":m1})


def about(request):
    match1 = College.objects.all()
    m1 = College.objects.get(id=4)
    if request.method == 'POST':
        contact_email = request.POST['email']
        contact_name =request.POST['name'] +' / '+ contact_email
        
        contact_message = request.POST['message']
        send_mail(contact_name, contact_message, contact_email, ['avinashghoshpullur@gmail.com'])
    return render(request,'about.html',{'data':match1,"m1":m1})

'''