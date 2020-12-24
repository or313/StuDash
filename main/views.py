from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required(login_url='/accounts/log-in'), name='dispatch')
class IndexPageView(TemplateView):
    template_name = 'layouts/default/page.html'
