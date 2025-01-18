from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = "Oryx Burkina,SONABHY,SONABEL,ARCEP,BUMIGEB,Ecobank,Microaid,ACEFIME".split(',')
        context['clients'] = clients  # Ajoute la liste des clients au contexte
        return context

class ServicesView(TemplateView):
    template_name = 'services.html'

class ProductsView(TemplateView):
    template_name = 'products.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')