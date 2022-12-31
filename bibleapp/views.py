from re import sub
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import docx
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")

def video(request):
    video = Video.objects.all().order_by('-date')
    return render(request,"video.html",{"video":video})

def audio(request):
    audio = Audio.objects.all().order_by('-date')
    return render(request,"audio.html",{"audio":audio})

def contact(request):
    return render(request,"contact.html")

def home(request):
    # cat = category.objects.get(pk=1)
    # a = {}
    # con = []
    head = header.objects.all()
    test =[]
    for i in head:
        
        doc = docx.Document("C://Users//VAkoma//Videos//Projects//heresy//bible//bibleapp//NEW_.docx")
        for para in doc.paragraphs:
            num = para.text.split(i.header)
            test.append(num)
    #     my_json_obj = json.load(f)
    
    # for i in my_json_obj:
        
    #     if i['content'] or i['page'] != '':
    #         if len(i['content']) > 3 and i['page'] == '': 
    #             a['sub'] = i['content']
                    
    #         elif len(i['content']) > 3 and i['page'] != '':
    #             a['header']=i['content']
    #             # print(a)

    #             cop = a.copy()
    #             con.append(cop) 

    # for i in con:
    #     subcategory.objects.create(
    #         category = cat,
    #         name = i['sub']
    #     )
        # s = subcategory.objects.get(name=i['sub'])
        
        # head = header.objects.create(
        #     subcategory = s,
        #     header = i['header']
        # )

    return HttpResponse(test)

@api_view(['GET'])
def view_data(request,pk):
    data = []
    cat = category.objects.get(id=pk)
    subcat = subcategory.objects.filter(category=cat)
    
    for i in subcat:
        sub = {}
        head = []
        sub['subcategory'] = i.name
        load = header.objects.filter(subcategory=i)
        # print(i)
        for a in load:
            # print(a)
            head.append({
                'item':a.header,
                'description': a.description
            })

        sub['Content']=head
        # print(sub)
        co = sub.copy()
        data.append(co)
    # serializer2 = subcategorySerializer(subcat,many=True)
    # serializer = headerSerializer(load,many=True)
    # data2 = serializer2.data
    # data = serializer.data

    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : {'Category':pk,'header':data},
    },status=status.HTTP_200_OK)


def login_view(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(request, username = username , password = password)

        if user is not None:
            login(request, user)
            return redirect('category',pk=2)
        else:
            messages.info(request,'username or password is incorrect')
    
    context={"form":form}
    return render(request,'login.html',context)

# Read
@login_required(login_url='login')
def subcategories(request,pk):
    categories = category.objects.get(id=pk)
    subcategories = subcategory.objects.filter(category=categories)
    sub = []
    val = {}
    for i in subcategories:
        val['id'] = i.id
        val['Category'] = i.name
        val['Count'] = header.objects.filter(subcategory=i.id).count()
        cop = val.copy()
        sub.append(cop)

    context = {"subcategories":sub}
    return render(request,'home.html',context)

@login_required(login_url='login')
def headers(request,pk):
    subcategories = subcategory.objects.get(id=pk)
    headers = header.objects.filter(subcategory=subcategories)
    context = {"headers":headers,"subcategory":subcategories}
    return render(request,'headers.html',context)


# Update
@login_required(login_url='login')
def update_headers(request,pk,extra):
    subcategories = subcategory.objects.get(id=pk)
    headers = header.objects.filter(subcategory=subcategories,header=extra)[0]
    data = {"description":headers.description}
    form = descriptionForm(initial=data)
    

    if request.method == 'POST':
        form = descriptionForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            header.objects.filter(subcategory=subcategories,header=extra).update(description=description)

            return redirect('list',pk=pk)
     
    context = {"headers":headers,"form":form}
    return render(request,'edit.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')