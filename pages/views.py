from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from . models import Category, Place
from django.db.models import F

# Create your views here.
class HomePageView(ListView):
    model = Category
    template_name = 'home.html'

class CategoryDetailView(ListView):
    model = Place

    #queryset = place.objects.filter(categorry__name='category')
    template_name = 'category_detail.html'
    #category_model = Category

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs.get('title'))#notice use get
        return Place.objects.filter(category=self.category)

""" def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['object_list'] = self.category
        return context"""


"""
def CategoryDetailView(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('category_detail.html', {
        'category':category,
        'place':place.objects.filter(category=category)
    })"""
