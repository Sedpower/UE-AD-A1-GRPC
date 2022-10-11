# UE-AD-A1-GRPC
## TP VERT
### Questions 1

_Terminer l’écriture du service Movie en utilisant gRPC_

Nous avons passé toutes les routes de l'API REST en route gRPC dans le fichier `movie.py` et généré les `pb2` 
correspondants et copiés dans `/client`

### Question 2

_Reprenez votre service REST User, remplacez-y les requêtes REST vers Movie par des appels de procédures distantes en 
utilisant les stub associés. En effet, User devient un client gRPC et reste un serveur REST dans ce TP._

Nous avons remplacé tous les appels REST à `Movie` par des appels gRPC

### Questions 3 et 4 

_Écrivez les fichiers d’API proto pour le service Times_

_Écrivez le code du service Times et testez ce code_

Nous avons passé l'API `Time` en API gRPC

### Question 5

_Reprenez votre service REST Booking, remplacez-y les requêtes REST vers Times par des appels de procédures distantes
en utilisant les stub associés. En effet, Booking devient un client gRPC et reste un serveur REST dans ce TP._

Nous avons remplacé tous les appels REST à `Time` par des appels gRPC

## Instructions Docker Compose

Nous n'avons pas utilisé Docker Compose

## Instructions PyCharm

Executer le fichier `generate.sh` pour générer les fichiers pb2 des différents services gRPC<br>
Faire un run des 4 fichiers `.py` (`showtime.py`,`user.py`,`movie.py`,`booking.py`)

Lancer ensuite le fichier `client.py`
