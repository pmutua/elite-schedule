[![Build Status](https://travis-ci.org/pmutua/elite-schedule.svg?branch=master)](https://travis-ci.org/pmutua/elite-schedule) [![Coverage Status](https://coveralls.io/repos/github/pmutua/elite-shedule-api/badge.svg?branch=master)](https://coveralls.io/github/pmutua/elite-schedule?branch=master) [![Code Climate](https://codeclimate.com/github/pmutua/elite-schedule-api/badges/gpa.svg)](https://codeclimate.com/github/pmutua/elite-schedule-api)

# EliteSchedule :soccer:

Elite Schedule is an open source football API providing historical results & odds to help football enthusiasts analyse many years of data quickly and efficiently to gain an edge over the bookmaker. Whilst other football results and odds databases do exist, Elite Schedule is unique in making available computer-ready data by accessing data in JSON format for quantitative analysis. Elite Schedule collects data from [Football-Data](http://football-data.co.uk/) organizes it and data is available through accesing it's end points.

Alternatively, if you are just looking for the latest results, tables and team stats, try [Football-Data's livescore service](http://livescore.football-data.co.uk/), with minute-by-minute scores as the goals go in.

Currently Elite Schedule API supports matches from England,Spain,Germany and Italy but there is accommodation to enhance the API to have matches from other countries.

- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Tests](#tests)
- [API Endpoints](#api-endpoints)
- [Responses](#responses)
- [Error handling](#error-handling)
- [Versions](#versions)
- [Request & Response Examples](#request--response-examples)
- [Contributing](#contributing)
- [Swagger/Redoc Documentation](http://docs.elite_schedule.apiary.io)

## API Features

1. User authentication with [JWT](http://jwt.io).
2. API will seed data to DB from csv files when you run `python manage.py import_matches_from_csv`
3. Redoc and Swagger documentation for easier integration

## Getting Started

1. `git clone https://github.com/pmutua/elite_schedule.git`
2. `cd elite_schedule`
3. `virtualenv -p python env`
4. `source env/bin/activate`
5. `cd src`
6. `pip install -r requirements/base.txt`
7. `.manage.py runserver`

The above will get you a copy of the project up and running on your local machine for development and testing purposes.

### Dependencies

1. [Python 3 +](https://github.com/python)
2. [Pip](https://github.com/pypa/pip)
3. [Virtualenv](https://virtualenv.pypa.io/en/latest/)
4. [PostgreSQL](https://www.postgresql.org/)

[View all the other dependencies](./requrements/base.txt)


## API Endpoints

All endpoints except `signup/` require a token for authentication. The API call should have the token in Authorization header.

    http http://elite-schedule.herokuapp.com/api/elite_schedule/matches/ \
    Authorization: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0Njc2MTkxNDV9.R6VLZD4qtsdVHXZwU8bEo6S16cbNQfo7lICsNdAq00I"

| EndPoint                                    |                       Functionality |
| ------------------------------------------- | ----------------------------------: |
| POST /signup/                               |                            Register |
| POST /rest-auth/password/reset              |                      Reset Password |
| POST /rest-auth/password/reset/confirm/     |                       Reset Confirm |
| POST /rest-auth/login/                      |                          Login user |
| GET /rest-auth/user/                        |                            Get User |
| GET /rest-auth/logout/                      |                         Logout user |
| POST /rest-auth/password/change/            |                     Change Password |
| GET /elite_schedule/matches/                |                List all the matches |
| GET /elite_schedule/team/search/?q=Juventus |                    Search Team name |
| GET /elite_schedule/england/                |  List all English Divisions matches |
| GET /elite_schedule/spain/                  |  List all Spanish Divisions matches |
| GET /elite_schedule/germany/                |   List all German Divisions matches |
| GET /elite_schedule/italy/                  |  List all Italian Divisions matches |
| GET /elite_schedule/england/premier_league  |     List all Premier League matches |
| GET /elite_schedule/england/conference      | List all English Conference matches |
| GET /elite_schedule/england/league_1        |           List all League 1 matches |
| GET /elite_schedule/england/league_2        |           List all League 2 matches |
| GET /elite_schedule/spain/la_liga_primiera  |   List all La Liga Primiera matches |
| GET /elite_schedule/spain/la_liga_segunda   |    List all La Liga Segunda matches |
| GET /elite_schedule/germany/bundesliga_1    |       List all Bundesliga 1 matches |
| GET /elite_schedule/germany/bundesliga_2    |       List all Bundesliga 2 matches |
| GET /elite_schedule/italy/serie_a           |            List all Serie A matches |
| GET /elite_schedule/italy/serie_b           |            List all Serie B matches |

## Responses

The API responds with JSON data by default.

## Error Handling

The API responds with an error message and http status code whenenever it encounters an error.

    {
      "error": "Not Found",
      "status": "404"
    }

## Request & Response examples

Request GET /elite_schedule/team/search/?q=Juventus

curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" https://elite-schedule.herokuapp.com/api/elite_schedule/team/search/?q=swansea

Returns json data about a single team,this will list all games a team has played both home or way.

## Application Limitations

1. The API only responds with JSON

## Contributing

1. Fork it! :fork_and_knife:
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git add -A && git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature` :rocket:
5. Submit a pull request :sunglasses:



## License

This project is licensed under the MIT License - see the [LICENSE.md](https://opensource.org/licenses/MIT) file for details
