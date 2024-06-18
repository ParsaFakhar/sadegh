# import request
from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from .country_by_ip import get_lang_by_ip


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'admin_posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        admin_posts = Post.objects.all()
        return admin_posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'LANGUAGE_CODE' not in self.request.session:
            language_code = get_lang_by_ip(self.request)
            context['LANGUAGE_CODE'] = language_code
            self.request.session['LANGUAGE_CODE'] = language_code
        else:
            context['LANGUAGE_CODE'] = self.request.session['LANGUAGE_CODE']

        return context
