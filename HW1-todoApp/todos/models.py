from django.db import models


class Todo(models.Model):
    """
    Model representing a todo item.
    """
    title = models.CharField(max_length=200, help_text="Title of the todo item")
    due_date = models.DateField(null=True, blank=True, help_text="Due date for the todo")
    is_completed = models.BooleanField(default=False, help_text="Whether the todo is completed")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the todo was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the todo was last updated")

    class Meta:
        ordering = ['due_date', '-created_at']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """String representation of the Todo model."""
        return self.title
