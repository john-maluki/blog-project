from django.views.generic.edit import FormView
from contact.forms import ContactForm
from django.urls import reverse_lazy


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)
