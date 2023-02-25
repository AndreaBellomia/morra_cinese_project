Code Challenge 

“Creazione di una webApp per giocare al gioco della Morra Cinese utilizzando come linguaggio di programmazione HTML,CSS,JS e Python con il relativo Framework Django”

Per la realizzazione è stato usato Django Vanilla senza usare nessuna libreria REST (Django REST Framework ) o CSS (Crispy Forms, Tailwind Css, Bootstrap 5). 
Gran parte della logica è stata mantenuta nel BackEnd di Django, dove sono state usate le chiamate asincrone per il passaggio dei dati.


REQUISITI

Python 3.10 installato


STARTUP:

Avviare prompt dei comandi in windows,

spostarsi nella directory del programma che contiene:

morra_cinese
README.txt
requirements.txt

inviare il comando:

(per creare un ambiente virtuale python nel dir corrente)

python -m venv venv 


Successivamente lanciare il comando:

(Per attivare l'ambiente virtuale)



.\venv\Scripts\activate

pip -r requirements.txt



Ad installazione avvenuta spostarsi nella directory del programma:

cd ./morra_cinese/morra_cinese


Eseguire:

(per avviare il server)

python manage.py runserver
