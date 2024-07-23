from django.shortcuts import render,get_object_or_404,redirect
from .models import Property,BlogPost
from .forms import InquiryForm,ContactForm
from django.contrib import messages



def home(request):
    featured_properties = Property.objects.all()[:6]
    latest_posts = BlogPost.objects.order_by('-published_date')[:3]
    return render(request, 'home.html', {
        'featured_properties': featured_properties,
        'latest_posts': latest_posts
    })


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

from django.http import JsonResponse

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property = property
            inquiry.save()
            # Return a JsonResponse for AJAX requests
            return JsonResponse({"success": True, "message": "Your inquiry has been submitted successfully!"})
    else:
        form = InquiryForm()
    return render(request, 'property_detail.html', {'property': property, 'form': form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
            return redirect('listing:contact_us')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', {'post': post})

