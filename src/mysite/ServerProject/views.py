from ServerProject import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServerProject
from .forms import UpdateServerProjectForm, newServerProjectForm, SearchRequirementForm
from django.contrib.auth.models import User

from Schedule.models import Schedule
from Accounts.models import customer, provider
from AuditControl.models import Audit

# Create your views here.

'''
初始页面函数
按条件查询服务项目,条件为空则查询全部已有项目
'''
def indexServerProject(request):
    if request.method == 'POST':
        form = SearchRequirementForm(request.POST)
        if form.is_valid():
            ServerProjectList = ServerProject.objects.filter(
                name__icontains = form.cleaned_data['SearchRequirement'],
            )
        else:
            ServerProjectList = ServerProject.objects.all()
    else:
        ServerProjectList = ServerProject.objects.all()
    context = {
        'ServerProjectList': ServerProjectList,
    }
    return render(request, 'ServerProject/index.html', context)

'''
新建项目函数
需要用户登陆且用户具有服务商身份
应该额外自建一个函数修饰器用于检查
'''
@login_required
def newServerProject(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = newServerProjectForm(request.POST)
        if form.is_valid():
            serverproject = ServerProject(
                name = form.cleaned_data['name'], 
                description = form.cleaned_data['description'], 
                status = 'normal',
                price = form.cleaned_data['price'],
                who_create = user.id,
                length = form.cleaned_data['length'],
            )
            serverproject.save()
            return redirect('indexServerProject')
    else:
        form = newServerProjectForm()
    context = {
        'form': form,
    }
    return render(request, 'ServerProject/new.html', context)

'''
服务项目详情函数
'''
def detailServerProject(request, pk):
    ServerProjectItem = get_object_or_404(ServerProject, pk=pk)
    context = {
        'ServerProjectItem': ServerProjectItem,
    }
    return render(request, 'ServerProject/detail.html', context)

'''
更新项目内容函数
需要用户具有创建该项目的服务商信息
优化应该额外自建函数修饰器
'''
@login_required
def updateServerProject(request, pk):
    ServerProjectItem = get_object_or_404(ServerProject, pk=pk)
    if request.method == 'POST':
        form = UpdateServerProjectForm(request.POST)
        if form.is_valid():
            ServerProjectItem.name = form.cleaned_data['name']
            ServerProjectItem.description = form.cleaned_data['description']
            ServerProjectItem.price = form.cleaned_data['price']
            ServerProjectItem.save()
        return redirect('detailServerProject', pk=pk)
    else:
        form = UpdateServerProjectForm(
            initial={
                'name': ServerProjectItem.name,
                'description': ServerProjectItem.description,
                'price': ServerProjectItem.price,
            }
        )
        context = {
            'form': form,
        }
        return render(request, 'ServerProject/update.html', context)

'''
项目购买函数
优化应额外自建函数修饰器
'''
@login_required
def buyServerProject(request, pk):
    # 获取项目信息
    ServerProjectItem = get_object_or_404(ServerProject, pk=pk)
    # 当请求方法为POST时
    if request.method == 'POST':
        # 获取当前用户, 并扣费
        c = customer.objects.get(userId=request.user.id)
        c.remain = c.remain - ServerProjectItem.price
        c.save()

        # 获取项目的服务商
        p = provider.objects.get(userId=ServerProjectItem.who_create)

        # 创建一个审计记录, 并保存
        a = Audit(
            who_customer = c,
            who_provider = p,
            what_project = ServerProjectItem,
            price = ServerProjectItem.price,
        )
        a.save()

        return redirect('detailServerProject', pk=pk)
    else:
        context = {
            'ServerProjectItem': ServerProjectItem,
        }
        return render(request, 'ServerProject/buy.html', context)