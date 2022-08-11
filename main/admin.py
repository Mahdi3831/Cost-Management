from django.contrib import admin
from .models import Expenses, Category

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount', 'category_to_str', 'month', 'year')
    list_filter = ('month', 'year', 'amount')


admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Category)