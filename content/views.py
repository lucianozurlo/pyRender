from django.contrib.admin.views.decorators import staff_member_required
from django.core.management import call_command
from django.shortcuts import redirect
from django.contrib import messages

@staff_member_required
def build_static(request):
    call_command('buildstatic')
    messages.success(request, "Static site pushed to main")
    return redirect('home')
