from datetime import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("monthly_challenge", args=[month])
        list_items += f"<li style='margin: 10px; list-style-type: \"📆\"; padding-inline-start: 1ch;'> <a href=\"{month_path}\">{month.capitalize()}</a></li>"

    response_data = f"<h1>Monthly Challenges</h1><ul>{list_items}</ul>"
    return HttpResponse(response_data)

def current_month(request):
    current_month = datetime.now().strftime("%B").lower()
    redirect_path = reverse("monthly_challenge", args=[current_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<span style='color: red;'>This month is not supported!</span>")
    forward_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    challenge_text = None
    if month in monthly_challenges:
        challenge_text = monthly_challenges[month]
    else:
        return HttpResponseNotFound("<span style='color: red;'>This month is not supported!</span>")
    return render(request, "challenges/challenge.html", {
        "month_name": month.capitalize(),
        "text": challenge_text
    })