from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    """
    Display all todos with filtering options.
    """
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    
    def get_queryset(self):
        """Filter todos based on status if requested."""
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        
        if status == 'completed':
            queryset = queryset.filter(is_completed=True)
        elif status == 'pending':
            queryset = queryset.filter(is_completed=False)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        """Add additional context for the template."""
        from datetime import date
        context = super().get_context_data(**kwargs)
        context['status_filter'] = self.request.GET.get('status', 'all')
        context['completed_count'] = Todo.objects.filter(is_completed=True).count()
        context['pending_count'] = Todo.objects.filter(is_completed=False).count()
        context['total_count'] = Todo.objects.count()
        context['today'] = date.today()
        return context


class TodoCreateView(CreateView):
    """
    Create a new todo.
    """
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')
    
    def form_valid(self, form):
        """Add success message when todo is created."""
        messages.success(self.request, 'Todo created successfully!')
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    """
    Update an existing todo.
    """
    model = Todo
    form_class = TodoForm
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')
    
    def form_valid(self, form):
        """Add success message when todo is updated."""
        messages.success(self.request, 'Todo updated successfully!')
        return super().form_valid(form)


class TodoDeleteView(DeleteView):
    """
    Delete a todo with confirmation.
    """
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
    
    def delete(self, request, *args, **kwargs):
        """Add success message when todo is deleted."""
        messages.success(self.request, 'Todo deleted successfully!')
        return super().delete(request, *args, **kwargs)


def toggle_todo(request, pk):
    """
    Toggle the completion status of a todo.
    """
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    
    status = 'completed' if todo.is_completed else 'pending'
    messages.success(request, f'Todo marked as {status}!')
    
    return redirect('todo_list')
