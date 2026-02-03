from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category, Tag


def product_list(request):
    """Display list of products with optional category filter"""
    products = Product.objects.filter(is_active=True).select_related('category').prefetch_related('tags')
    categories = Category.objects.all()
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=selected_category)
    
    # Filter by tag if provided
    tag_slug = request.GET.get('tag')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags=tag)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        ).distinct()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, slug):
    """Display product detail page"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/product_detail.html', context)


def page_detail(request, slug):
    """Render generic content page"""
    from .models import Page
    page = get_object_or_404(Page, slug=slug, is_active=True)
    return render(request, 'shop/page_detail.html', {'page': page})

