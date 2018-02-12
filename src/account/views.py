from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cbt.models import Ulangan


# pylint: disable=E1101
@login_required
def dashboard(request):
    ulangan = Ulangan.objects.all()

    return render(
        request,
        'account/dashboard.html',
        {
            'ulangan': ulangan,
        }
    )
