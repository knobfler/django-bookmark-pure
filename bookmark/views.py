from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkAddView(CreateView):
    model = Bookmark
    fields = ['site_title', 'site_url']
    template_name_suffix = '_add'

    def form_valid(self, form):
        if form.is_valid():
            form.instance.save()
            return redirect(reverse('bookmark:detail', kwargs={'pk': form.instance.id}))
        else:
            return self.render_to_response({'form': form})


class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_title', 'site_url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
