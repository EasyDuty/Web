from django.shortcuts import render

# Create your views here.
def main(request):
    context = {

    }
    return render(request, 'calendars/main.html', context)


def ward(request):
    context = {

    }
    return render(request, 'claender/ward.html', context)


def apply_off(request):
    if request.method=='POST':
        pass
    else:
        pass
    context = {

    }
    return render(request, 'calendars/apply-off.html', context)


def make_duty(request):
    if request.method=='POST':
        pass
    else:
        pass
    context = {

    }
    return render(request, 'calendars/make-duty.html', context)