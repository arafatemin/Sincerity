from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
from .models import Project, Education, Experience
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Projects.models import Manager, Project




def not_account(request):
    return render(request, "Decorators/not_account.html")




def handler404(request, exception):
    return render(request, 'Decorators/errors_404.html', status=404)



# @login_required(login_url="not_account")
def project(request):
    paginator = Paginator(Project.objects.all(), 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'projects': Project.objects.all(),
        'page_obj': page_obj
    }
    return render(request, 'Education_Experience/projects.html', context)


@login_required(login_url="not_account")
def school(request):
    context = {
        'schools': Education.objects.filter(categoryEducation__category="School"),
    }
    return render(request, 'Education_Experience/school.html', context)


@login_required(login_url="not_account")
def course(request):
    context = {
        'courses': Education.objects.filter(categoryEducation__category="Course")
    }
    return render(request, 'Education_Experience/course.html', context)


@login_required(login_url="not_account")
def experience(request):
    context = {
        'experiences': Experience.objects.all()
    }
    return render(request, 'Education_Experience/experience.html', context)


# @method_decorator(login_required, name="dispatch")
class AboutMe(ListView):
    model = Manager
    context_object_name = 'managers'
    template_name = 'Education_Experience/about_Me.html'

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Education_Experience/contact.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'Education_Experience/contact.html', context)

