from django.views.generic import View, ListView

from .models import Entry


class IndexView(ListView):

    model = Entry
    paginate_by = 50
    template_name = 'home/index.html'
    context_object_name = 'entries'