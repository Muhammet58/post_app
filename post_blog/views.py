from django.shortcuts import render, redirect, get_object_or_404
from .models import post_model
from .forms import post_model_form
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def home_page(request):
    post_models = post_model.objects.all()

    if request.method == "GET":
        auth = request.GET.get("author")
        if auth:
            posts = post_model.objects.filter(author__username__icontains=auth)
            posts_count = posts.count()
            return render(request, "post_blog/home.html", {'post_model':posts, "p_count":posts_count})

    items_per_page = 4
    paginator = Paginator(post_models, items_per_page)

    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    data = {
        "post_model": page,
    }
    return render(request, "post_blog/home.html", data)


def post_details(request, slug, id):
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


def edit_post(request, post_slug):
    if not request.user.is_authenticated:
        return redirect("home")

    # post = get_object_or_404(post_model, id=post_slug)
    post = post_model.objects.get(slug=post_slug)

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
