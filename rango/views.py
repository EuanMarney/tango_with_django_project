from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context = context_dict)

def index(request):
    # query for all categories, order by likes, retrive only top 5 or less
    category_list = Category.objects.order_by('-likes')[:5]

    page_list = Page.objects.order_by('-views')[:5]

    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!', 'categories': category_list, 'pages': page_list}

    # Return a rendered response to send to the client.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
        # Construct a dictionary to pass to the template engine as its context.
        context_dict = {'boldmessage': 'This tutorial has been put together by Euan Marney'}

        # Return a rendered response to send to the client.
        return render(request, 'rango/about.html', context=context_dict)
