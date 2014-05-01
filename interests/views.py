from django.shortcuts import render
# Only useful for stub methods, don't need it for templates
from django.http import HttpResponse

from interests.models import Book

def index(request):
  book_list = Book.objects.order_by('-date_read')
  context = {'book_list': book_list}
  return render(request, 'interests/index.html', context)

def detail(request, book_id):
  book = Book.objects.get(id=book_id)
  context = {'book': book}
  return render(request, 'interests/detail.html', context)
