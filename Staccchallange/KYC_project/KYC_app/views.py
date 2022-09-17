from django.shortcuts import render
import requests
# Create your views here.


def PEP(request):
    #gets name from name forum, from PEP.html
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
    #sends data to PEP.html
    return render(request, "KYC_app/PEP.html",context)
    pass


def roller(request):
    # gets org_number from org_number forum, from roller.html
    org_nummer = request.GET.get("org_nummer")
    # pull data stacc roller api
    url = f'https://code-challenge.stacc.dev/api/roller?orgNr={org_nummer}'
    response = requests.get(url)
    # convert reponse data into json
    rolle_data = response.json()

    context = {
        'rolle_data': rolle_data
    }
    # sends data to roller.html
    return render(request, "KYC_app/roller.html", context)
    pass


def enheter(request):
    # gets org_number from org_nummer forum, from enheter.html
    org_nummer = request.GET.get("enheter")
    # pull data stacc enheter api
    url = f'https://code-challenge.stacc.dev/api/enheter?orgNr={org_nummer}'
    response = requests.get(url)
    # convert reponse data into json
    data = response.json()

    #sends data as key-value pair
    enheter_data = data.items()

    context = {
        'enheter_data': enheter_data
    }
    # sends data to enheter.html
    return render(request, "KYC_app/enheter.html", context)
    pass

