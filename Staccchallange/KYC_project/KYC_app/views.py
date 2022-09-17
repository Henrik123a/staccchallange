from django.shortcuts import render
import requests
# Create your views here.


def PEP_check(request):
    #gets name from name forum, from home.html
    name =  request.GET.get("name")
    #pull data stacc PEP api
    url = f'https://code-challenge.stacc.dev/api/pep?name={name}'
    response = requests.get(url)
    # convert reponse data into json
    data = response.json()
    #selects hits object from dict
    hits = data["hits"]

    context = {
        'hits': hits
    }
    #sends data to home.html
    return render(request, "KYC_app/home.html",context)
    pass

