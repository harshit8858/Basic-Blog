from django.shortcuts import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core import serializers


def homepage(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'homepage.html')

def register(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                #username = form.cleaned_data.get('username')
                #email = form.cleaned_data.get('email')
                #password = form.cleaned_data.get('password')
                #User.objects.create_user(username=username, password=password, email=email)
                form.save()
                return HttpResponseRedirect('/')

        else:
            form = UserCreationForm()

        return render(request, 'register.html', {'form':form})

def auth_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/index/')

    else:
        return HttpResponseRedirect('/invalid/')

def invalid(request):
    return render(request, 'invalid.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def index(request):
    try:
        num_visit = request.session.get('num_visit',1)
        request.session['num_visit']=num_visit+1
        if request.user.is_authenticated():
            if request.method == "POST":
                form = Boxform(request.POST,request.FILES)
                # form1 = Commentform(request.POST)

                if form.is_valid():
                    print("hvhjsdgfkjsd")
                    f = form.save(commit = False)
                    f.username = request.user
                    f.save()
                    print("hvhjsdgfkjsd")
                    # form.save()
                    return HttpResponse("Success")
                else:
                    return HttpResponse("NOt valid!")

            else:
                form = Boxform()
                form1 = Commentform()

            n = Box.objects.all()
            print(n)

            n1 = Comment.objects.all()    # comment ka funct alag se bana hai...below!
            return render(request, 'home.html', {'num':num_visit, 'fullname':request.user.username, 'text':n, 'comment':n1, 'form':form})

        else:
            return HttpResponseRedirect('/index/')

    except Exception as e:
        print(e)
        return HttpResponse(e)


def delete(request,d):
    n = Box.objects.get(id=d)
    n.delete()
    return HttpResponseRedirect('/index/')

def search(request):
    if request.method == 'POST':
        s = request.POST['search']
        if s:
            sa = Box.objects.filter(Q(title__icontains=s)|Q(content__icontains=s)|Q(username__username__exact=s))
            if sa:
                return render(request, 'search.html', {'text': sa,'t':s})
            else:
                return render(request, 'notfound.html')
        else:
            return HttpResponseRedirect('/index/')

def edit(request,d):
    n = Box.objects.get(id=d)

    if request.method == 'POST':
        form = Boxform(request.POST,request.FILES,instance=n)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/')

    else:
        form = Boxform(instance=n)

    return render(request, 'edit.html', {'form':form})

def profile(request):
    # n = Box.objects.all()
    if request.method == 'POST':
        form = Profileform(request.POST,request.FILES)
        form1 = UserCreationForm(request.POST,instance = request.user)
        # form2 = Boxform(request.POST,request.FILES)

        if form.is_valid() and form1.is_valid():
            # user.username = form.cleaned_data.get('username')
            # user.first_name = form.cleaned_data.get('first_name')
            # user.last_name = form.cleaned_data.get('last_name')
            # user.email = form.cleaned_data.get('email')
            # user.password = form.cleaned_data.get('password')
            Profile.job = form.cleaned_data.get('job')
            Profile.profile_pic = form.cleaned_data.get('profile_pic')
            Profile.number = form.cleaned_data.get('number')
            Profile.address = form.cleaned_data.get('address')
            form1.save()
            # form2.save()
            return HttpResponseRedirect('/profile/')

    else:
        form = Profileform()
        form1 = UserCreationForm(instance=request.user)
        # form2 = Boxform()

    return render(request, 'profile.html', {'form':form, 'form1':form1, 'fullname':request.user.username})

def my_files(request):
    n = Box.objects.all()
    m = like.objects.all()
    if request.method == "POST":
        form = ChangeForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Not Valid")
    else:
        form = ChangeForm()
    return render(request, 'my_files.html', {'l':m ,'t':n, 'fullname':request.user.username, 'form':form})

def network(request):
    n = User.objects.all()
    n = n.exclude(id=request.user.id)
    return render(request, 'network.html', {'t':n, 'fullname':request.user.username})

def profile1(request,d):
    m = User.objects.get(id=d)
    n = Box.objects.all()
    return render(request, 'profile1.html',{'t': n, 'm':m, 'fullname': request.user.username})


def password(request):
    user = request.user
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            #new_password = form.cleaned_data['new_password']
            #user.set_password(new_password)
            #user.save()
            form.save()
            return redirect('login')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password.html', {'form': form})

def comment(request):
    # d = Comment.objects.get(id)
    # comment = Comment.objects.all()
    # comment_serialized = serializers.serialize('json', comment)
    box_id = request.POST["take_id"]
    print(box_id)
    box_obj = Box.objects.get(id=box_id)        # for grabbing particular post's comments
    if request.method == 'POST':
         form1 = Commentform(request.POST)
         print(form1.errors)
         if form1.is_valid():
            f1=form1.save(commit=False)
            f1.box=box_obj
            f1.save()
            return HttpResponse("")
         else:
             return HttpResponse("Something went wrong!")
            # return JsonResponse(comment_serialized,safe=False)
        # comment = request.POST['comment']
        #
        # Comment.objects.create(
        #     comment = comment
        # )
        # return HttpResponse("")

    else:
        form1 = Commentform()
    # comment = Comment.objects.all()
    return render(request, 'home.html', {'form1':form1})

def ajax_sample(request):
    n = User.objects.all()
    return render(request, 'ajax_sample.html', {'n':n})

# def like(request):
#     n = request.user.username
