from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from ns1.models import Ns1_detail,Ns1_3d_detail,R16srna,Fungus_detail,Cell_detail,Plasmid_detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import json


def near_range(pagination):
	half_range = 3
	current = pagination.number
	start = current-half_range
	if start<1:
		start = 1
	end = current+half_range
	if end>pagination.paginator.num_pages:
		end = pagination.paginator.num_pages

	return range(start, end+1)
def log_in(request):
    state = ""
    if request.method=="POST":
        username=request.POST["user"]
        password=request.POST["pwd"]
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            state="user_login"
            return redirect("show/homes.html")
        else:
            state="用户名或密码错误"
    content = {
        'state': state,
        'user': None,
    }
    return render(request,"login.html",locals())

def home(request):
    return render(request,"home.html")

def ns1(request,Subtype=""):
    if Subtype and len(Subtype.split("=")) == 2:
        dt = Subtype.split("=")[0]
        detail = Subtype.split("=")[1]
        if dt == "Subtype":
            datas = Ns1_detail.objects.filter(Subtype__icontains=detail)
        elif dt == "Collection_year":
            datas = Ns1_detail.objects.filter(Collection_year__icontains=detail)
        elif dt == "Host":
            datas = Ns1_detail.objects.filter(Host__icontains=detail)
        else:
            datas = Ns1_detail.objects.filter(Sequence_name__icontains=detail)
    else:
        datas = Ns1_detail.objects.all()
    paginator = Paginator(datas, 25)
    page = request.GET.get('page')
    try:
        knowledges = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        knowledges = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        knowledges = paginator.page(paginator.num_pages)
    rs = near_range(knowledges)
    return render(request, "ns1.html", locals())

def ns1_list(request):
    seqs = Ns1_detail.objects.values_list("Subtype").distinct().order_by("Subtype")
    cys = Ns1_detail.objects.values_list("Collection_year").distinct().order_by("Collection_year")
    cts = Ns1_detail.objects.values_list("Host").distinct().order_by("Host")
    cyse = []
    ctse = []
    for cy in cys:
        if cy[0] and cy[0].isdigit() and 1000 < int(cy[0]) < 2020:
            cyse.append((cy))
    for cy in cts:
        if cy[0] and len(cy[0]) < 8:
            ctse.append((cy))


    return render(request, "ns1_list.html", locals())

def ns1_detail(request,Accession_id):
    objs = Ns1_detail.objects.filter(Accession_id=Accession_id)
    if objs:
        obj = objs[0]
        return render(request, "ns1_detail.html", locals())
    else:
        return HttpResponse("404 not find!")


def ns1_3d(request):
    datas = Ns1_3d_detail.objects.all()

    return render(request, "ns13d.html", locals())
def ns1_3d_detail(request,PDB_ID):
    datas = Ns1_3d_detail.objects.filter(PDB_ID=PDB_ID)
    if datas:
        obj = datas[0]
        return render(request, "ns13d_detail.html", locals())
    else:
        return HttpResponse("404 not find")

def r16srna(request,value=""):
    if request.method=="GET":
        if value:
            datas = R16srna.objects.filter(Q(Genus__icontains=value)|Q(Species__icontains=value)|Q(Subspecies__icontains=value)|Q(NO__icontains=value))
        else:
            datas = R16srna.objects.all()
        paginator = Paginator(datas, 15)
        page = request.GET.get('page')
        try:
            knowledges = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            knowledges = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            knowledges = paginator.page(paginator.num_pages)
        rs = near_range(knowledges)
        return render(request, "r16srna.html", locals())
    if request.method=="POST":
        no = request.POST.get("no")
        res = []
        if no:
            rna = R16srna.objects.get(NO=no)
            res = [rna.NO,rna.Genus,rna.Species,rna.Subspecies,rna.Typestrain,rna.NCBI,rna.Sequence]

        return HttpResponse(json.dumps(res))

def germ(request,value=""):
    if value:
        datas = Fungus_detail.objects.filter(Q(pre_no__contains="LNUB")&(Q(pre_no__icontains=value)|Q(名称__icontains=value)|Q(别名__icontains=value)|Q(属__icontains=value)|Q(种__icontains=value)))
    else:
        datas = Fungus_detail.objects.filter(pre_no__contains="LNUB")
    paginator = Paginator(datas, 25)
    page = request.GET.get('page')
    try:
        knowledges = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        knowledges = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        knowledges = paginator.page(paginator.num_pages)
    rs = near_range(knowledges)
    return render(request, "germ.html", locals())

def fungus(request):
    datas = Fungus_detail.objects.filter(pre_no__contains="F")

    return render(request, "fungus.html", locals())

def plasmid(request):
    datas = Plasmid_detail.objects.all()

    return render(request, "plasmid.html", locals())

def cell(request):
    datas = Cell_detail.objects.all()

    return render(request, "cell.html", locals())

def germ_detail(request,pre_no):
    if pre_no:
        datas = Fungus_detail.objects.filter(pre_no=pre_no)
        if datas:
            obj = datas[0]
            return render(request, "germ_detail.html", locals())
        else:
            return HttpResponse("404 not find")

def plasmid_detail(request,pre_no):
    if pre_no:
        datas = Plasmid_detail.objects.filter(保藏号=pre_no)
        if datas:
            obj = datas[0]
            return render(request, "plasmid_detail.html", locals())
        else:
            return HttpResponse("404 not find")

def cell_detail(request,pre_no):
    if pre_no:
        datas = Cell_detail.objects.filter(保藏号=pre_no)
        if datas:
            obj = datas[0]
            return render(request, "cell_detail.html", locals())
        else:
            return HttpResponse("404 not find")


def regist(request):
    state = None
    if request.method == "POST":
        username = request.POST["user"]
        password = request.POST["pwd"]
        if User.objects.filter(username=username):
            print("user 已存在")
            state = 'user_exist'
            print(User.objects.all().values("username","password"))
        else:
            new_user = User.objects.create_user(username=username, password=password)
            print(username,password)
            new_user.save()
            return redirect("/")
    content = {
        'state': state,
        'user': None,
    }
    return render(request,"regist.html")