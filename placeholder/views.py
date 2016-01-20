from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
import shelve


EMAIL_LIST_FILENAME = 'emails.txt'
EMAIL_DICT = {}


def index(request):
    return render(request, 'index.html')


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