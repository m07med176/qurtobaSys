from django.contrib import admin
from .models import Customer_info,Customer,Customer_account #Customer_Image,
from search_admin_autocomplete.admin import SearchAutoCompleteAdmin
#admin.site.register(models.Customer_info)
# admin.site.register(Customer_Image)
admin.site.register(Customer_account)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    change_list_template = 'admin/cusomer_info_list.html'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        response.context_data['summary'] = list(
            qs
        
        )
        return response


@admin.register(Customer_info)
class Customer2Admin(admin.ModelAdmin):
    search_fields = ['name', ]
    change_list_template = 'admin/cusomer_info_list2.html'
    list_display = (
        'name',
        'idNo',
        'shopName',
        'shopKind',
        'phoneNo',
        'address',
        'date',
        'time' ,
    )

  


"""         
        'images',
        'account',
metrics = {
            'total': Count('id'),
            'total_sales': Sum('price'),
        }
         """
        
        
