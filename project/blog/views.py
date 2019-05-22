from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
# Create your views here.
def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def modified(request,blog.id):
    selectedItem = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'modify.html', {'selectedItem': selectedItem})


def modifiedContents(request, blog_id):
    if request.method == 'POST':

        modifideTitle = request.POST['modify_title']
        modifideBody = request.POST['modify_body']
        modifideDate = timezone.datetime.now()

        modifiedItem = blog.BlogContents.objects.get(id=blog_id)

        modifiedItem.title = modifideTitle
        modifiedItem.body = modifideBody
        modifiedItem.modify_date = modifideDate
        modifiedItem.save()

        return redirect('/home/detail/?title=' + modifiedItem.title)

