Stacc code challenge 2021


Oppgavebeskrivelse:

Jeg valgte å løse oppgave a) jeg lagde en enkel webapp med django som gjør det mulig å utføre en KYC-sjekk av en person og bedrift. Videre valgte jeg å utvide oppgaven, ved å publisere webappen på heroku. Webappen min består av 3 html sider, PEP, roller, enheter. 

PEP siden er det mulig å gjennomføre en PEP sjekk av en person, ved å skrive inn et navn. Dataen blir hentet ved hjelp av et API, dataen blir så presentert på PEP.html. API henter data fra opensanctions.com

Roller gjør det mulig å hente ut diverse informasjon om nøkkelpersoner i et gitt selskap, ved å oppgi et organisasjonsnummer. Dataen blir hentet fra brønnøysundregisteret, ved hjelp av et API call. Dataen blir så presentert på roller.html  
Enheter henter ut generell basis informasjon om et foretak. Dataen blir igjen hentet fra brønnøysunds, via et api call. dataen presenters så på enheter.html. 


Hvordan kjøre prosjektet (windows):

Enten besøk webbappen på https://kycstacc.herokuapp.com/
Eller last ned prosjektet via https://github.com/Henrik123a/staccchallange
Etter man har lastet ned prosjektet kan man starte det via terminalen.
Man må først aktivierte et Virtual environment, for å gjøre det med terminal: naviger frem til mappen prosjektet ble lastet ned til, deretter:

“cd staccchallange” -> “cd Staccchallange” -> “cd Scripts” -> “activate” (staccchallange/Staccchallange/Scripts/activate) 

Vi har nå aktivert virtual environment, og er klar for å starte django serveren:

“cd..” -> “cd KYC_project” -> “python manage.py runserver” 
Når django serveren er startet, kan man koble til ved å skrive enten: http://127.0.0.1:8000/PEP/, http://127.0.0.1:8000/roller/,  http://127.0.0.1:8000/enheter/  i nettleseren.



Kommentarer:


Jeg merker jeg ikke “kom i land” med dette prosjektet, jeg møtte en del utfordringer som jeg ikke helt klarte å løse. 
Response objektet av api “roller” var ikke lett å jobbe med, jeg slet med å få hentet ut og presente dataen på en ryddig og oversiktlig måte. 
Jeg brukte mye tid her, tid som kunne vært bedre brukt andre plasser. 
Videre innså jeg at min “error handelig” / django struktur har en feil, første gang man går inn på en av nettsidene (PEP,enheter,roller) så sendet et api call. 
Og siden man ikke har fått skrevet inn enten navn eller org nummer, sendes et tomt api call, som resulterer i errorcode 400, og det vil da stå “something went wrong with api call, try again”.
Men feilmeldingen forsvinner når man skriver inn navn / org nummer, fordi da sendes fullverdig api call, og returnerer 200 kode. 
Det var mot slutten av prosjektet jeg innså at oppgaven kunne ha blitt løst på en lettere / bedre måte, da min django struktur ikke var helt optimal.