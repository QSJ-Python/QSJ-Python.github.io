from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404


def index(request):
    """博客的主页"""
    return render(request, 'my_blogs/index.html')


@login_required
def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return  render(request, 'my_blogs/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及所有条目"""
    topic = Topic.objects.get(id = topic_id)
    #确认请求的主题使当前用户的
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'my_blogs/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据，创建一个表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('my_blogs:topics'))

    context = {'form':form}
    return render(request, 'my_blogs/new_topic.html', context)


# 删除主题
# @login_required



@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        form =EntryForm()
    else:
        form = EntryForm(data= request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return  HttpResponseRedirect(reverse('my_blogs:topic',args=[topic_id]))

    context = {'topic':topic, 'form':form}
    return render(request, 'my_blogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form =EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data= request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_blogs:topic',args=[topic.id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'my_blogs/edit_entry.html', context)


# 删除条目
# @login_required