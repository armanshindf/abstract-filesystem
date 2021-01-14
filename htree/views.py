from django.shortcuts import render

from .models import Pseudofs
from .utils import create_file_tree


def base_view(request):
    pseudofs: object = Pseudofs.objects.first()
    result = create_file_tree(pseudofs)
    return render(request, 'base.html', {'ffile': pseudofs.ffile})

