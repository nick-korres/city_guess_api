# City Guess (Api)

This is the Api for my City Guess web app whose code is ![here](https://github.com/nick-korres/city_guess_app).

There are 2 routes 
  * [https://city-guess-api-nick-korres.vercel.app/](https://city-guess-api-nick-korres.vercel.app/)images/<numOfCities>
      
      Where a GET request like [https://city-guess-api-nick-korres.vercel.app/](https://city-guess-api-nick-korres.vercel.app/)images/10 will return 10 random city JSON objects containing the id,name, of each city.
      
  * [https://city-guess-api-nick-korres.vercel.app/](https://city-guess-api-nick-korres.vercel.app/)image/<name>
  
    Where a GET request like [https://city-guess-api-nick-korres.vercel.app/](https://city-guess-api-nick-korres.vercel.app/)image/Paris.jpg will return the image of the city of Paris

# Installation
  Assuming you have python 3+ installed :
  * Clone the repository and cd into the folder ( example in Windows PowerShell)
  ```
  git clone https://github.com/nick-korres/city_guess_api.git
  cd .\city_guess_api\
  ``` 
  * Install the dependencies. You might want to do it in a python virtual enviroment.
  ```
  pip install -r requirements.txt
  ```
  * Install ![PostgreSQL](https://www.postgresql.org/)
  * Create file named ```.env``` containing the folowing :
  ```
  DATABASE_URL=postgresql+psycopg2://username:password@localhost/dbName
  ```
   The default username is postgres and the password the one set at installation.
   create a database and set the name at the variable above.

# Usage
  * To create the tables in the database :
  ```
  flask shell
  from app import Setup
  Setup()
  exit()
  ```

  * To run it locally at http://127.0.0.1:5000/ use :
  ```
  flask  run 
  ```
