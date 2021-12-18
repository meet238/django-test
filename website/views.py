# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, FormView

from category_product.froms import ProductForm
from category_product.models import Product, Category


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_superuser:
            return render(request, template_name='staff_user/home_page.html')
        return render(request, template_name='admin_user/home_page.html')


class ListOfProductView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 3
    template_name = 'staff_user/list_of_product.html'


class ListOfCategoryView(LoginRequiredMixin, ListView):
    model = Category
    paginate_by = 3
    template_name = 'staff_user/list_of_category.html'


class ListOfProductViewUser(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 3
    template_name = 'admin_user/list_of_product.html'


class AddProductView(LoginRequiredMixin, FormView):
    form_class = ProductForm
    template_name = 'admin_user/add_product.html'
    success_url = 'add-product'

    def form_valid(self, form):
        form_data = form.cleaned_data
        form_data['owner'] = User.objects.get(pk=self.request.user.pk)
        product_created = Product.objects.create(**form_data)
        if product_created:
            messages.success(self.request, "Product added")
            return super().form_valid(form)
        else:
            messages.success(self.request, "Something Went Wrong")
            return super().form_valid(form)
    # def form_valid(self, form):
    #     form_data = form.cleaned_data
    #     form_data['owner'] = User.objects.get(pk=self.request.user.pk)
    #     product_created = Product.objects.create(**form_data)
    #     if product_created:
    #         messages.success(self.request, "Product added")
    #         return redirect('add-product')
    #     else:
    #         messages.success(self.request, "Something Went Wrong")
    #         return redirect('add-product')
