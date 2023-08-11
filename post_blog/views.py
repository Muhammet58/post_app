from django.shortcuts import render, redirect, get_object_or_404
from .models import post_model
from .forms import post_model_form
from django.core.paginator import Paginator


def home_page(request):
    post_models = post_model.objects.all()
    auth = request.GET.get("author")
    sort_by_old = request.GET.get("sort_by_old")
    sort_by_new = request.GET.get("sort_by_new")
    sort_by_A_Z = request.GET.get('sort_by_A-Z')
    sort_by_Z_A = request.GET.get('sort_by_Z-A')

    if auth:
        posts = post_model.objects.filter(author__username__icontains=auth)
        posts_count = posts.count()
        return render(request, "post_blog/home.html", {'post_model':posts, "p_count":posts_count})
    
    if sort_by_old:
        post_models = post_models.order_by("publish_date")
        return render(request, "post_blog/home.html", {'post_model':post_models})
    
    if sort_by_new:
        post_models = post_models.order_by("-publish_date")
        return render(request, "post_blog/home.html", {"post_model":post_models})
    
    if sort_by_A_Z:
        post_models = post_models.order_by("title")
        return render(request, 'post_blog/home.html', {'post_model':post_models})
    
    if sort_by_Z_A:
        post_models = post_models.order_by("-title")
        return render(request, "post_blog/home.html", {"post_model":post_models})
        
         
    items_per_page = 4
    paginator = Paginator(post_models, items_per_page)

    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)


    data = {
        "post_model": page,
    }
    return render(request, "post_blog/home.html", data)


def post_details(request, id, slug):
    post = post_model.objects.get(id=id)
    return render(
        request,
        "post_blog/post_details.html",
        {"post": post},
    )


def create_post_view(request):
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = post_model_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = post_model_form()

    return render(
        request,
        "post_blog/create_post.html",
        {"form": form, "post": post_model},
    )


def edit_post(request, id, post_slug):
    if not request.user.is_authenticated:
        return redirect("home")

    # post = get_object_or_404(post_model, id=post_slug)
    post = post_model.objects.get(id=id)

    form = post_model_form(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect("home")

    else:
        form = post_model_form(instance=post)

    return render(request, "post_blog/edit_post.html", {"form": form})


def post_delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect("home")

    post = get_object_or_404(post_model, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("home")
