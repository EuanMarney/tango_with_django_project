from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect


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

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            # For now, just redirect the user back into the index view
            return redirect('/rango/')
        else:
            print(form.errors)

    # Will handle the bad form, new form or no form supplied cases
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})
