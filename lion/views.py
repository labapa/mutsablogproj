from django.shortcuts import render,redirect,get_object_or_404
from .models import Lion
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    lions = Lion.objects
    lion_list = Lion.objects.all()
    paginator = Paginator(lion_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'home.html', {'lions' : lions , 'posts':posts})

def detail(request , lion_id):
    lion_detail = get_object_or_404(Lion, pk = lion_id)
    return render(request,'detail.html' , {'lion' : lion_detail})

def write(request):
    return render(request, 'write.html')

def create(request):
    lion = Lion()
    lion.title = request.GET['title']
    lion.body = request.GET['body']
    lion.pub_date = timezone.datetime.now()
    lion.save()
    return redirect('/lion/' + str(lion.id))
