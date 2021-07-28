from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse

# Create your views here.


# def index(request):
#     return HttpResponse('Its wokring')

challenges = {
    'january': 'I am January',
    'february': 'I am february',
    'march': 'I am march',
    'april': 'I am April',
    'may': 'I am may',
    'june': 'I am june',
    'july': 'I am july',
    'august': 'I am august',
    'septmeber': 'I am septmeber',
    'october': 'I am october',
    'november': 'I am november',
    'december': None
}


def index(request):
    months = list(challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # return_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(return_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_numbers(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month.capitalize()
        })
    except:
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        raise Http404()
