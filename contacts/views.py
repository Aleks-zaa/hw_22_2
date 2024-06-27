from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from contacts.models import Contact


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = ("name", "surname", "email", "contact_img")
    success_url = reverse_lazy('contacts:contact_list')

    def form_valid(self, form):
        if form.is_valid():
            contact_new = form.save()
            contact_new.slug = slugify(contact_new.name)
            contact_new.save()

        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ("name", "surname", "email", "contact_img")
    success_url = reverse_lazy('contacts:contact_list')

    def get_success_url(self):
        return reverse('contacts:contact_detail', args=[self.kwargs.get('pk')])


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:contact_list')
