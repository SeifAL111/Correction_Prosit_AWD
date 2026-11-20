# Atelier AWD — Service Discovery (Eureka) & Observabilité (Spring Boot Actuator)

## Membres de l'équipe
* Seifeddine Alaimi

## Récapitulatif des travaux réalisés
* **Serveur Eureka (`port 8761`) :** Mise en place du registre de découverte de services.
* **Microservices clients Spring Boot & multi-instance :**
  * `CANDIDAT` lancé en double instance (`8081` et `8091`, base H2).
  * `CANDITATURE` (`8085`) et `JOB` (`8082`, base MySQL).
* **Observabilité avec Spring Boot Actuator (`/health`, `/info`, `/metrics`) :**
  * Vérification de l'état de santé (`UP`), des métadonnées (`/info`) et des métriques (`/metrics`).
  * Simulation de panne MySQL : passage de `/actuator/health` sur `JOB` (`8082`) à `DOWN` (`CannotGetJdbcConnectionException`), reflété en `DOWN (1)` dans Eureka, puis retour à `UP (1)` après redémarrage de MySQL.
* **Services non-Java intégrés à Eureka :**
  * `MEETING` (`8083`, Node.js / Express) avec endpoints `/health`, `/info` et `/api/meetings/hello`.
  * `NOTIFICATION` (`8084`, Python / FastAPI) avec endpoints `/health`, `/info`, `/api/notifications/hello` et enregistrement Eureka (`/eureka/apps/NOTIFICATION`).

## Réponses aux questions métriques (`CANDIDAT` — `8081`)
Après génération de trafic sur `GET /mic1/candidates` via Swagger UI :
* **Nombre total de requêtes HTTP traitées (`COUNT`) :** `18` (`18.0`).
* **Durée de la requête la plus lente (`MAX`) :** `1.1557198` seconde.
* **Résultat de `/actuator/metrics/http.server.requests?tag=status:200` :** Filtre uniquement les requêtes ayant retourné le statut HTTP `200` (`outcome: SUCCESS`), avec `COUNT = 17` (`17.0`), `TOTAL_TIME = 1.9082254` seconde et `MAX = 0.2983148` seconde.

## Captures d'écran
Les preuves d'exécution (Dashboard Eureka, multi-instance, Actuator `/health` `UP`/`DOWN`, `/info`, `/metrics`, Swagger UI, `MEETING` et `NOTIFICATION`) sont disponibles dans le dossier [`screenshots/`](./screenshots).