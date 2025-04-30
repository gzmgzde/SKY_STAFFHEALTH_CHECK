from django.contrib import admin
from .forms import UserRegisterForm
from .models import Administrator, Department,  Team,  User

# Register your models here.
@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('admin_id', 'email')
    search_fields = ('email',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name')
    search_fields = ('department_name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'team_name')
    search_fields = ('team_name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'name', 'role')
    search_fields = ('email', 'name')
    list_filter = ('role',)
    list_editable = ('role',)
    ordering = ('role',)
    list_per_page = 25
    list_max_show_all = 100
    form = UserRegisterForm  
    

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('department', 'team')