# Game-backend

I use aiohttp because it is more clear to me.

## Technology stack:
- Python 3.8.5
- Aiohttp 3.7.4
- PostgreSQL 5.2

## Сommands to start the service:
- python -m venv
- .\game-backend\Scripts\activate
- pip install -r requirements.txt
- python app.py

## Database:
- Create Database 'games'
- Run all SQL queries from the [file "queries"](https://github.com/uzhegovaelena/game-backend/blob/master/db/queries.sql) (creating the necessary tables).

## Enviroment variables: 
```
PORT=8080

# variables for DB connection:
DB_DATABASE=games
DB_USER=replace_me
DB_PASSWORD=replace_me
DB_HOST=localhost
DB_PORT=5432
```

## Endpoints

### Games
```
curl --request POST \
  --url http://localhost:8080/games \
  --header 'Content-Type: application/json' \
  --data '{
    "email": "test@gmail.com"
}'
```
