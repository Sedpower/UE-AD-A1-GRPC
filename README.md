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

### Question 3 et 4 

_Écrivez les fichiers d’API proto pour le service Times_

_Écrivez le code du service Times et testez ce code_







<br><br><br><br><br><br><br>

Nous avons implémenté toutes les routes spécifiées dans le fichier `UE-archi-distribuees-Showtime-1.0.0-resolved.yaml`

### Question 4

_Coder le service Booking à partir de la spécification OpenAPI disponible (UE-archi-distribuees-Booking-1.0.0-resolved.yaml) et testez votre service avec Postman._

Nous avons implémenté toutes les routes spécifiées dans le fichier `UE-archi-distribuees-Booking-1.0.0-resolved.yaml`

### Question 5 et 6

_Regarder le contenu du fichier user.json et imaginez une spécification openAPI pour le service User en conséquence de façon à ce qu’il utilise à la fois les services Booking et Movie. Des exemples :<br>
• Un point d’entrée permettant d’obtenir les réservations à partir du nom ou de l’ID d’un utilisateur ce qui demandera à interroger le service Booking pour vérifier que la réservation est bien disponible à la date demandée<br>
• Un point d’entrée permettant de récupérer les informations des films pour les réservations d’un utilisateur ce qui demandera à interroger à la fois Booking et Movie_

- Nous avons ajouté le point d'entrée `/user/booking/<userId>/<date>`. 
Ce point d'entrée permet de récupérer les `Booking` d'un `user` à une date spécifiée dans
le path de la requête (ainsi que l'ID du `User`). <br>
Ce point d'entrée fait appel à l'API `Booking`.

```JSON
{
    "date": "20151201",
    "movies": [
      "267eedb8-0f5d-42d5-8f43-72426b9fb3e6"
    ]
}

http://192.168.1.11:3203/user/booking/garret_heaton/20151201
```

- Nous avons également ajouté le point d'entrée `/user/booking/<userid>`. Ce point d'entrée permet de récupérer tout
les `Booking` d'un `User` mais à la place de renvoyer simplement des ID de films, la route 
renvoie le film associé à l'ID récupéré. <br>
Ce point d'entrée fait appel à l'API `Booking` et `Movie`. 

```JSON
{
    "movies": [
        {
            "director": "Ryan Coogler",
            "id": "267eedb8-0f5d-42d5-8f43-72426b9fb3e6",
            "rating": 8.8,
            "title": "Creed"
        },
        {
            "director": "Tom Hooper",
            "id": "276c79ec-a26a-40a6-b3d3-fb242a5947b6",
            "rating": 5.3,
            "title": "The Danish Girl"
        }
    ]
}

http://192.168.1.11:3203/user/booking/garret_heaton
```

## TP BLEU

_Modifier certains points d’entrée du service Movie pour faciliter la découverte de l’API et mettez à jour la spécification de votre API._

Nous avons ajouté deux points d'entrée pour ce TP :
- `[GET]/movies/date/<date>` Ce point d'entrée permet de récupérer les ID de `Movie` stockés
dans `ShowTime` selon la date spécifiée dans le path et qui renvoie la liste des `Movie`
associés à ces ID.
- `[GET]/movies/name/<title>` Ce point d'entrée permet de récupérer des `Movie` selon un 
titre, mais avec la spécificité que si le titre est mal écrit mais néanmoins assez proche,
le `Movie` sera tout de même retourné grâce à une verification de la distance de levenshtein.

## TP ROUGE

_Améliorer l’application en utilisant l’API REST de la base de données IMDB https://imdb-api.com/API_

Nous avons ajouté deux points d'entrée pour ce TP :
- `[GET]/imdb/movie/<title>` Ce point d'entrée permet de récupérer des `Movie` selon le titre
spécifié dans le path.
- `[GET]/imdb/trailer/<movieId>` Ce point d'entrée permet de récupérer le lien de la
bande-annonce d'un `Movie` selon l'ID spécifié dans le path. 

## Instructions Docker Compose

Nous n'avons pas utilisé Docker Compose

## Instructions PyCharm

Faire un run des 4 fichiers `.py`