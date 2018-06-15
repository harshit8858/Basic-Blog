from django.shortcuts import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# from django.contrib.sessions.models import Session
# from django.core import serializers


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
            form = SignUpForm(request.POST)

            if form.is_valid():
                #username = form.cleaned_data.get('username')
                #email = form.cleaned_data.get('email')
                #password = form.cleaned_data.get('password')
                #User.objects.create_user(username=username, password=password, email=email)
                form.save()
                return HttpResponseRedirect('/')

        else:
            form = SignUpForm()

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
    num_visit = request.session.get('num_visit',1)
    request.session['num_visit']=num_visit+1
    if request.method == "POST":
        form = Boxform(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.username = request.user
            f.save()

            # print("hvhjsdgfkjsd")
            # form.save()
            return redirect('index')

    else:
        form = Boxform()

    n = Box.objects.all()
    n1 = Comment.objects.all()    # comment ka funct alag se bana hai...below!
    return render(request, 'home.html', {'num':num_visit, 'fullname':request.user.username, 'text':n, 'form':form})


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


def my_files(request):
    n = Box.objects.all()

    # for i in n:
    #     if i.username == request.user:
    #         print("1")
    #         m = [i.title,i.content,i.url,i.image]
    #         print(m)

    comment = Comment.objects.all()
    return render(request, 'my_files.html', {'text':n, 'comment':comment})


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
    print("box_id")
    print(box_id)
    box_obj = Box.objects.get(id=box_id)        # for grabbing particular post's comments
    print("box_obj")
    print(box_obj)
    if request.method == 'POST':
         form1 = Commentform(request.POST)
         print(form1.errors)
         if form1.is_valid():
            f1=form1.save(commit=False)
            f1.box=box_obj
            f1.user=request.user
            f1.save()
            # return HttpResponse("")
            return HttpResponseRedirect('/')
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


def comment_profile(request):
    # d = Comment.objects.get(id)
    # comment = Comment.objects.all()
    # comment_serialized = serializers.serialize('json', comment)
    box_id = request.POST["take_id"]
    print("box_id")
    print(box_id)
    box_obj = Box.objects.get(id=box_id)        # for grabbing particular post's comments
    print("box_obj")
    print(box_obj)
    if request.method == 'POST':
         form1 = Commentform(request.POST)
         print(form1.errors)
         if form1.is_valid():
            f1=form1.save(commit=False)
            f1.box=box_obj
            f1.user=request.user
            f1.save()
            return redirect('profile')
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
    return render(request, 'my_files.html', {'form1':form1})


def like(request,d):
    n1 = Comment.objects.all()
    print("like......vhjscvkjsdbjlsd")
    l = Box.objects.get(id=d)
    # k = Box.objects.get(user=request.user)
    n = Box.objects.all()
    print(l.like)
    # if l.like_count%2 == 0:
    l.like = l.like + int(1)       # increment the like button
    # else:
    # l.like = l.like - int(1)
    print(l.like)
    l.save()
    if request.method == 'POST':
        form = Boxform(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
        return redirect('home')
    else:
        form = Boxform()
    return render(request, 'home.html', {'form':form, 'text':n, 'like':l.like, 'comment':n1})


def like_profile(request,d):
    n1 = Comment.objects.all()
    print("like......vhjscvkjsdbjlsd")
    l = Box.objects.get(id=d)
    # k = Box.objects.get(user=request.user)
    n = Box.objects.all()

    # like_count(request)

    print(l.like)
    # if l.like_count%2 == 0:
    l.like = l.like + int(1)       # increment the like button
    # else:
    # l.like = l.like - int(1)
    print(l.like)
    l.save()
    if request.method == 'POST':
        form = Boxform(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
        return redirect('profile')
    else:
        form = Boxform()
    return render(request, 'my_files.html', {'form':form, 'text':n, 'like':l.like, 'comment':n1})


def dis(request,d):
    n1 = Comment.objects.all()
    print("dislike......vhjscvkjsdbjlsd")
    l = Box.objects.get(id=d)
    n = Box.objects.all()
    print(l.dis)
    l.dis = l.dis + int(1)
    print(l.dis)
    l.save()
    if request.method == 'POST':
        form = Boxform(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
        return redirect('home')
    else:
        form = Boxform()
    return render(request, 'home.html', {'form':form, 'text':n, 'dislike':l.dis, 'comment':n1})


def dis_profile(request,d):
    n1 = Comment.objects.all()
    print("dislike......vhjscvkjsdbjlsd")
    l = Box.objects.get(id=d)
    n = Box.objects.all()
    print(l.dis)
    l.dis = l.dis + int(1)
    print(l.dis)
    l.save()
    if request.method == 'POST':
        form = Boxform(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
        return redirect('profile')
    else:
        form = Boxform()
    return render(request, 'my_files.html', {'form':form, 'text':n, 'dislike':l.dis, 'comment':n1})


def profile_pic(request):
    pp = Profile_pic.objects.get(user=request.user)
    print(pp)
    n = Box.objects.all()
    comment = Comment.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'my_files.html', {'pp':pp, 'text':n, 'form':form, 'comment':comment})


def edit_profile_pic(request):
    p = Profile_pic.objects.get(user=request.user)
    print(p)
    n = Box.objects.all()
    comment = Comment.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=p)
    return render(request, 'edit_profiel_pic.html', {'text':n, 'form':form, 'comment':comment})

