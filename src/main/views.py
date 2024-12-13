from django.shortcuts import redirect
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/main.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        
        if not request.user.is_authenticated:
            return redirect('sign_up')
        
        return self.render_to_response(context)
