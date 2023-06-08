from django.urls import reverse_lazy
from .models import BlogPostModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from OnlineTrainingPortal.userAuthentication.decorators import admin_required


admin_decorators_list = [login_required,admin_required]


# For All User
class BlogListView(ListView):
    model = BlogPostModel


class BlogDetailView(DetailView):
    model = BlogPostModel

    
# For Admin User
@method_decorator(admin_decorators_list,name='dispatch')
class AdminSiteBlogView(ListView):
    model = BlogPostModel
    template_name = 'blog/adminBlog_list.html'


@method_decorator(admin_decorators_list,name='dispatch')
class BlogUpdateView(UpdateView):
    model = BlogPostModel
    fields = fields = ['title','description','notice_file']
    success_url = reverse_lazy('notice:adminBlog')
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Update"
        context['form_title'] = "Post"
        return context


@method_decorator(admin_decorators_list,name='dispatch')
class BlogDeleteiew(DeleteView):
    model = BlogPostModel
    success_url = reverse_lazy('notice:adminBlog')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        post = BlogPostModel.objects.get(slug = self.kwargs['slug'])
        context['post_title'] = post.title
        return context


@method_decorator(admin_decorators_list,name='dispatch')
class PostCreateView(CreateView):
    model = BlogPostModel
    fields = ['title','description','notice_file']
    template_name="form.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['action'] = "Create"
        context['form_title'] = "Post"
        return context