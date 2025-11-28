from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """
    Admin configuration for Todo model.
    """
    list_display = ['title', 'due_date', 'is_completed', 'created_at', 'updated_at']
    list_filter = ['is_completed', 'due_date', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_completed']
    
    actions = ['mark_completed', 'mark_pending']
    
    def mark_completed(self, request, queryset):
        """Mark selected todos as completed."""
        updated = queryset.update(is_completed=True)
        self.message_user(request, f'{updated} todo(s) marked as completed.')
    mark_completed.short_description = 'Mark selected todos as completed'
    
    def mark_pending(self, request, queryset):
        """Mark selected todos as pending."""
        updated = queryset.update(is_completed=False)
        self.message_user(request, f'{updated} todo(s) marked as pending.')
    mark_pending.short_description = 'Mark selected todos as pending'
