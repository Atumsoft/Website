from django.shortcuts import render
from django.shortcuts import redirect
from email.mime.text import MIMEText
import smtplib

# Create your views here.
import shelve
import subprocess, os
from django_project.settings import TEMPLATE_DIRS
import thread

EMAIL_LIST_FILENAME = 'emails.txt'
EMAIL_DICT = {}


# need to dynamically make the connection
# MAILSERVER = smtplib.SMTP('outlook.office365.com', 587)
# MAILSERVER.starttls()
# MAILSERVER.ehlo()
# MAILSERVER.login("info@atumsoft.com", "\"d~XsN*9;+<Ec:ZB")
# FROMADDR = 'info@atumsoft.com'
# TOADDR = 'olemaitre@atumsoft.com'


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def product(request):
    return render(request, 'product.html')


def solution(request):
    return render(request, 'solution.html')


def oops(request):
    return render(request, 'oops.html')


def contact_form(request):
    return render(request, 'contact-form.html')


def contact(request):
    # simple caller, disguard output
    phpPath = os.path.join(TEMPLATE_DIRS[0], 'contact.php')
    print phpPath
    subprocess.call("php %s" % phpPath)
    # return render(request, 'contact.html')


def submit_email(request):
    if request.method == 'POST':

        email = str(request.POST['email'])
        name = str(request.POST['name'])
        message = str(request.POST['message'])

        if not (email or not name) and message:
            return redirect('index')

        body = name + "," + email + "," + message

        msg = MIMEText(body)

        thread.start_new_thread(sendmail, (msg,))

        return render(request, 'thankyou.html')

    else:
        pass


def team(request):
    # import pdb; pdb.set_trace()
    return render(request, 'team.html')


def press(request):
    return render(request, 'press.html')


# need to make this connection every time so server doesn't time out
def sendmail(msg):
    MAILSERVER = smtplib.SMTP('outlook.office365.com', 587)
    MAILSERVER.starttls()
    MAILSERVER.ehlo()
    MAILSERVER.login("info@atumsoft.com", "\"d~XsN*9;+<Ec:ZB")
    FROMADDR = 'info@atumsoft.com'
    TOADDR = 'olemaitre@atumsoft.com'

    msg['Subject'] = 'Contact form received'
    msg['From'] = FROMADDR
    msg['To'] = TOADDR

    MAILSERVER.sendmail(FROMADDR, [TOADDR], msg.as_string())

    MAILSERVER.close()
