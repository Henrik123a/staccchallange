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

    #basic error handeling,
    if response.status_code == 200: #success
        #selects hits,numberOfHits keys from dict
        hits = data["hits"]
        n_hits = data["numberOfHits"]
        context = {
            'hits': hits,
            'n_hits': n_hits
        }
        #sends data to PEP.html
        return render(request, "KYC_app/PEP.html",context)
        pass
    elif response.status_code == 400: #error
        context = {
            'error_message': 'something went wrong with api call'
        }
        return render(request, "KYC_app/PEP.html", context)


def roller(request):

    # gets org_number from org_number forum, from roller.html
    org_nummer = request.GET.get("org_nummer")
    # pull data stacc roller api
    url = f'https://code-challenge.stacc.dev/api/roller?orgNr={org_nummer}'
    response = requests.get(url)
    # convert reponse data into json
    data = response.json()

    # basic error handeling,
    if response.status_code == 200:  # success
        # selects hits object from dict
        context = {
            "data": data
        }
        # sends data to roller.html
        return render(request, "KYC_app/roller.html", context)
        pass
    elif response.status_code == 400: #error
        context = {
            'error_message': 'something went wrong with api call'
        }
        return render(request, "KYC_app/roller.html", context)


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

    # basic error handeling,
    if response.status_code == 200:  # success
        context = {
            'enheter_data': enheter_data
        }
        # sends data to enheter.html
        return render(request, "KYC_app/enheter.html", context)
        pass
    elif response.status_code == 400: #error
        context = {
            'error_message': 'something went wrong with api call'
        } # sends data to enheter.html
        return render(request, "KYC_app/enheter.html", context)


