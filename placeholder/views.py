from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
import shelve
import subprocess, os
from django_project.settings import TEMPLATE_DIRS


EMAIL_LIST_FILENAME = 'emails.txt'
EMAIL_DICT = {}


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def solution(request):
    return render(request, 'solution.html')

def contact_form(request):
    return render(request, 'contact-form.html')

def contact(request):
    #simple caller, disguard output
    phpPath = os.path.join(TEMPLATE_DIRS[0], 'contact.php')
    subprocess.call("php %s" % phpPath)


def submit_email(request):
    if request.method == 'POST':


        import pdb;

        pdb.set_trace()
        print "WE WENT HERE"

        email = str(request.POST['email'])
        name = str(request.POST['name'])
        message = str(request.POST['message'])

        if not (email or not name) and message:
            return redirect('index')

        inquiry = name + "," + email + "," + message

        if EMAIL_DICT.get(inquiry):
            return render(request, 'thankyou.html')
        else:
            EMAIL_DICT[inquiry] = True

        emailshelve = shelve.open('emails.shl')
        emailshelve[inquiry] = True
        emailshelve.sync()
        emailshelve.close()
        # with open(EMAIL_LIST_FILENAME, 'a+') as emailFile:
        #     emailFile.write('{}\n'.format(email))

        return render(request, 'thankyou.html')

    else:
        pass


def team(request):
    #import pdb; pdb.set_trace()
    return render(request, 'team.html')


def press(request):
    return render(request, 'press.html')


def thankyou(request):
    return render(request, 'thankyou.html')