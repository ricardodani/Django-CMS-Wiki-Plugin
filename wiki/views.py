# -*- encoding: utf-8 -*-

from models import WikiPostPlugin as WikiPost
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import WikiPostForm

def viewPost(request, id=None, post=None):

    if post is None:
        try:
            post = WikiPost.objects.get(pk=id)
        except:
            post = None

    context = {
        "post":post,
    }

    return render_to_response("wiki/post.html", context, context_instance=RequestContext(request))
    

def editPost(request, id=None):
    
    try:
        post = WikiPost.objects.get(pk=id)
        
        if request.method == 'POST':
            form = WikiPostForm(request.POST, instance=post)
            try:
                form.save()
                return viewPost(request, post=post)
            except:
                pass
        else:
            form = WikiPostForm(instance=post)

    except:
        post = None
        form = None

    
    context = {
        "post":post,
        "form":form,
    }
    
    return render_to_response("wiki/edit.html", context, context_instance=RequestContext(request))
    
