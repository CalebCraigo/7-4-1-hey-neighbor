from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from .models import Tool

User = get_user_model()

def is_super_user_check(user):
    return user.is_superuser


class IndexView(generic.ListView):
    template_name = 'hey_neighbor/index.html'

    def get_queryset(self):

        if 'selection' in self.kwargs:
            tools = Tool.objects.filter(types=self.kwargs['selection'].upper())
        else:
            tools = Tool.objects.all()

        context = {
            'tools': tools,
            'headings': ['Yard', 'Woodworking', 'Plumbing', 'Auto']
        }

        return context

class DetailView(generic.DetailView):
    model = Tool
    template_name = 'hey_neighbor/detail.html'


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Tool
    template_name = 'hey_neighbor/create.html'
    fields = ['tool', 'types', 'availability']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def handle_no_permission(self):
        return redirect('login')

    success_url = reverse_lazy('hey_neighbor:my_tool')

class MyToolView(LoginRequiredMixin, generic.ListView):
    model = Tool
    template_name = 'hey_neighbor/mytools.html'
    fields = '__all__'
    def get_queryset(self):
        return Tool.objects.filter(owner=self.request.user)



class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tool
    def get_object(self, queryset=None):
        tool = super(DeleteView, self).get_object()
        if not tool.owner == self.request.user:

            raise Http404

        return tool
# def delete_view(request, pk):
#     tool = get_object_or_404(Tool, pk=pk)
#     tool.delete()
#     return HttpResponseRedirect(reverse_lazy('hey_neighbor_index'))
