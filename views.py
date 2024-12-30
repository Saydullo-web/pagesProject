from django.views.generic import TemplateView


# HomePageView klassi
class HomePageView(TemplateView):
    template_name = 'home.html'


# AboutPageView klassi
class AboutPageView(TemplateView):
    template_name = 'about.html'


# IndexPageView klassi
class IndexPageView(TemplateView):
    template_name = 'index.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
