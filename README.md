Artist API

This is a simple Flask-based API that allows users to perform CRUD operations on an artist database. The API connects to a MySQL database and supports operations such as retrieving artists by ID, name, birth year, death year, and more. It also allows users to add, update, or delete artists from the database.

#### Features

- Retrieve a list of all artists
- Retrieve artists by ID, name, known titles, birth year, or death year
- Add new artists
- Update existing artist details
- Delete artists from the database

#### Installation

Follow these steps to set up and run the application:

#### Clone the repository:
```
git clone https://github.com/stwins60/artistAPI.git
```

#### Navigate to the project folder:
```
cd artistAPI
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Set up environment variables:

Create a .env file in the root directory of the project and define the following variables:

```
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_NAME=your_database_name
```

Replace the placeholders with your actual database credentials.

Run the application:
```
python app.py
```

This will start the Flask server, and the application will be available at http://127.0.0.1:5000.

#### API Endpoints

```
GET /api/v1/artists

Fetch all artists.

Response:

[
  {
    "nconst": "nm0000001",
    "primaryName": "Artist Name",
    "birthYear": 1950,
    "deathYear": 2020,
    "primaryProfession": "Actor",
    "knownForTitles": "Movie Title"
  },
  ...
]

GET /api/v1/artists/id?id=<artist_id>

Fetch an artist by their ID.

Example URL:

/api/v1/artists/id?id=nm0000001

Response:

[
  {
    "nconst": "nm0000001",
    "primaryName": "Artist Name",
    "birthYear": 1950,
    "deathYear": 2020,
    "primaryProfession": "Actor",
    "knownForTitles": "Movie Title"
  }
]

GET /api/v1/artists/name?name=<artist_name>

Fetch artists by their name.

Example URL:

/api/v1/artists/name?name=Artist Name

GET /api/v1/artists/knownForTitles?title=<title>

Fetch artists known for a specific title.

Example URL:

/api/v1/artists/knownForTitles?title=Movie Title

GET /api/v1/artists/deathYear?deathYear=<year>

Fetch artists who died in a specific year.

Example URL:

/api/v1/artists/deathYear?deathYear=2020

GET /api/v1/artists/birthYear?birthYear=<year>

Fetch artists born in a specific year.

Example URL:

/api/v1/artists/birthYear?birthYear=1950

POST /api/v1/artists

Add a new artist to the database.

Request Body:

{
  "nconst": "nm0000002",
  "primaryName": "New Artist",
  "birthYear": 1970,
  "deathYear": null,
  "primaryProfession": "Singer",
  "knownForTitles": "Album Title"
}

Response:

{
  "nconst": "nm0000002",
  "primaryName": "New Artist",
  "birthYear": 1970,
  "deathYear": null,
  "primaryProfession": "Singer",
  "knownForTitles": "Album Title"
}

PUT /api/v1/artists

Update an existing artist's details.

Request Body:

{
  "nconst": "nm0000002",
  "primaryName": "Updated Artist",
  "birthYear": 1975,
  "deathYear": null,
  "primaryProfession": "Musician",
  "knownForTitles": "Updated Album"
}

Response:

{
  "nconst": "nm0000002",
  "primaryName": "Updated Artist",
  "birthYear": 1975,
  "deathYear": null,
  "primaryProfession": "Musician",
  "knownForTitles": "Updated Album"
}

DELETE /api/v1/artists

Delete an artist from the database.

Request Body:

{
  "nconst": "nm0000002"
}

Response:

{
  "nconst": "nm0000002"
}
```
##### Database

The application connects to a MySQL database, which must be set up with the following table structure:
artist Table
```
CREATE TABLE artist (
  nconst VARCHAR(20) PRIMARY KEY,
  primaryName VARCHAR(255),
  birthYear INT,
  deathYear INT,
  primaryProfession VARCHAR(255),
  knownForTitles TEXT
);
```

Environment Variables

Make sure the following environment variables are set in a .env file:

    DB_USER: Your database username
    DB_PASSWORD: Your database password
    DB_HOST: Your database host (e.g., localhost or 127.0.0.1)
    DB_NAME: Your database name

Requirements

    Python 3.x
    Flask
    mysql-connector
    python-dotenv

You can install the required dependencies by running:
```
pip install -r requirements.txt
```
