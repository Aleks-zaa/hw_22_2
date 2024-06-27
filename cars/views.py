from django.forms import inlineformset_factory
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from cars.forms import CarForm, VersionForm
from cars.models import Product, Version


class CarListView(ListView):
    model = Product

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(is_active=True)
    #     return queryset


class CarDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object




class CarCreateView(CreateView):
    model = Product
    form_class = CarForm
    success_url = reverse_lazy('cars:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        CarFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = CarFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = CarFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        car = form.save()
        user = self.request.user
        car.owner = user
        car.save()
        return super().form_valid(form)

    # def form_valid(self, form):
    #     context_data = self.get_context_data()
    #     formset = context_data["formset"]
    #     if form.is_valid() and formset.is_valid():
    #         self.object = form.save()
    #         formset.instance = self.object
    #         formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, formset=formset))


class CarUpdateView(UpdateView):
    model = Product
    form_class = CarForm
    success_url = reverse_lazy('cars:product_list')

    def get_success_url(self):
        return reverse('cars:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        CarFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data["formset"] = CarFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = CarFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class CarDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('cars:product_list')
