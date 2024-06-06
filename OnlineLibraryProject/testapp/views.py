from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.models import Book,Magagin,NewsPaper
from testapp.forms import BookForm,MagaginForm,NewsForm


def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def book_view(request):
    all_data=Book.objects.all()
    return render(request,'testapp/book.html',{'all_data':all_data})

def bookform_view(request):
    form=BookForm()
    if request.POST:
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/book')
    return render(request,'testapp/bookform.html',{'form':form})

def bookdelete_view(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/book')

def bookupdate_view(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(instance=book)
    if request.POST:
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
           form.save()
        return redirect('/book')
    return render(request,'testapp/bookupdate.html',{'form':form})
        


@login_required
def magagin_view(request):
    all_data=Magagin.objects.all()
    return render(request,'testapp/magagin.html',{'all_data':all_data})

def magaginform_view(request):
    form=MagaginForm()
    if request.POST:
        form=MagaginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/magagin')
    return render(request,'testapp/magaginform.html',{'form':form})

def magagindelete_view(request,id):
    book=Magagin.objects.get(id=id)
    book.delete()
    return redirect('/magagin')

def magaginupdate_view(request,id):
    book=Magagin.objects.get(id=id)
    form=MagaginForm(instance=book)
    if request.POST:
        form=MagaginForm(request.POST,instance=book)
        if form.is_valid():
           form.save()
        return redirect('/magagin')
    return render(request,'testapp/magaginupdate.html',{'form':form})
        


@login_required
def news_view(request):
    all_data=NewsPaper.objects.all()
    return render(request,'testapp/news.html',{'all_data':all_data})


def newsform_view(request):
    form=NewsForm()
    if request.POST:
        form=NewsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/news')
    return render(request,'testapp/newsform.html',{'form':form})

def newsdelete_view(request,id):
    book=NewsPaper.objects.get(id=id)
    book.delete()
    return redirect('/news')

def newsupdate_view(request,id):
    book=NewsPaper.objects.get(id=id)
    form=NewsForm(instance=book)
    if request.POST:
        form=NewsForm(request.POST,instance=book)
        if form.is_valid():
           form.save()
        return redirect('/news')
    return render(request,'testapp/newsupdate.html',{'form':form})
        


def logout_view(request):
    return render(request,'testapp/logout.html')

from testapp.forms import SignUpFrom
def signup_view(request):
    form=SignUpFrom()
    if request.POST:
        form=SignUpFrom(request.POST)
        details=form.save()
        details.set_password(details.password)
        details.save()
        return redirect('/accounts/login/')
    return render(request,'testapp/signup.html',{'form':form})


# Create your views here.
