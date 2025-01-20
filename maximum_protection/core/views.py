from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = [
            {'name': 'Oryx Burkina', 'logo_url': 'logo_clients/oryx.png'},
            {'name': 'SONABHY', 'logo_url': 'logo_clients/sonabhy.png'},
            {'name': 'SONABEL', 'logo_url': 'logo_clients/sonabel.png'},
            {'name': 'ARCEP', 'logo_url': 'logo_clients/arcep.png'},
            {'name': 'BUMIGEB', 'logo_url': 'logo_clients/bumigeb.png'},
            {'name': 'rtb', 'logo_url': 'logo_clients/rtb.png'},
            {'name': 'Microaid', 'logo_url': 'logo_clients/microaid.png'},
            {'name': 'ACFIME', 'logo_url': 'logo_clients/acfime.png'},
            {'name': 'Pan-African Microfinance', 'logo_url': 'logo_clients/panafrica.png'},
            {'name': 'TotalEnergies', 'logo_url': 'logo_clients/total_energy.png'},
            {'name': 'EBT-TRADING SARL', 'logo_url': 'logo_clients/ebt_trading.png'},
            {'name': 'Ministère du Commerce de l\'Industri et de l\'Artisanat', 'logo_url': 'logo_clients/mcia.png'}
        ]
        context['clients'] = clients
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