[![Build Status](https://travis-ci.org/pmutua/elite-schedule.svg?branch=master)](https://travis-ci.org/pmutua/elite-schedule) [![Coverage Status](https://coveralls.io/repos/github/pmutua/elite-shedule-api/badge.svg?branch=master)](https://coveralls.io/github/pmutua/elite-schedule?branch=master) [![Code Climate](https://codeclimate.com/github/pmutua/elite-schedule-api/badges/gpa.svg)](https://codeclimate.com/github/pmutua/elite-schedule-api)

# EliteSchedule :soccer:

WHAT IS Elite Schedule?

Football-Data is an open source football API providing historical results & odds to help football enthusiasts analyse many years of data quickly and efficiently to gain an edge over the bookmaker. Whilst other football results and odds databases do exist, Football-Data is unique in making available computer-ready data in Excel and CSV format for quantitative analysis. Simply download for free the available files, and learn more about how to use the data in Football-Data's free guide to rating systems plus Football-Data's comprehensive betting guide.

Alternatively, if you are just looking for the latest results, tables and team stats, try Football-Data's livescore service, with minute-by-minute scores as the goals go in. For the latest information about teams, players and transfers, Football-Data's football news site brings together all the best football and betting news wires under one roof. Altneratively, had a look at Football-Data's football betting articles.

Football-Data also brings to the football punter the best free bets and bonuses from online sports bookmakers, including £25, £50 and £100 free bet offers. The partnerships Football-Data has made with these advertising bookmakers help keep the site free for you. Use the free bet links or any of the banners on this page to find out more about these great offers.

Elite Schedule is a simple sports data API allowing consumers to get soccer statistics based on different leagues.

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
2. User can perform CRUD operations on Elite Schedule and items resources
3. API accepts paginated requests with limit
4. API uses Accept header to version api calls
5. Redoc and Swagger documentation for easier integration

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

# Settings

When running `manage.py` commands you need to specify the settings environment to run the api with as  shown below.

`python manage.py runserver --settings=core.settings.development`

OR

`python manage.py migrate --settings=core.settings.production`

## Tests

    1. cd elite-schedule
    2. `.manage.py test.py`

## API Endpoints

All endpoints except `signup/` require a token for authentication. The API call should have the token in Authorization header.

    http http://elite-schedule.herokuapp.com/api/elite_schedule/matches/ \
    Authorization: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0Njc2MTkxNDV9.R6VLZD4qtsdVHXZwU8bEo6S16cbNQfo7lICsNdAq00I"

| EndPoint                               |                     Functionality |
| -------------------------------------- | --------------------------------: |
| POST /signup                           |                     Signup a user |
| POST /rest-auth/login                  |                        Login user |
| GET /auth/logout                       |                       Logout user |
| POST /bucketlists/                     |          Create a new bucket list |
| GET /bucketlists/                      | List all the created bucket lists |
| GET /bucketlists?page=1&limit=5        | List five bucketlists from page 1 |
| GET /bucketlists?q=bucket              |             Search for bucketlist |
| GET /bucketlists/:id                   |            Get single bucket list |
| PUT /bucketlists/:id                   |            Update this bucketlist |
| DELETE /bucketlists/:id                |     Delete this single bucketlist |
| POST /bucketlists/:id/items/           |   Create a new item in bucketlist |
| PUT /bucketlists/:id/items/:item_id    |          Update a bucketlist item |
| DELETE /bucketlists/:id/items/:item_id |  Delete an item in a bucket lists |

## Responses

The API responds with JSON data by default.

## Error Handling

The API responds with an error message and http status code whenenever it encounters an error.

    {
      "error": "Not Found",
      "status": "404"
    }

## Versions

The API uses Accept header to version api calls e.g. `Accept:application/vnd.buckyy.v1+json`.
No breaking changes. :smiley:

## Request & Response examples

Request GET /bucketlists?page=2&limit=2

     http https://buckyy.herokuapp.com/bucketlists?page=2&limit=2 \
     Authorization: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0Njc2MTkxNDV9.R6VLZD4qtsdVHXZwU8bEo6S16cbNQfo7lICsNdAq00I'

Response (application/json)

    [
        {
            "created_by": "1",
            "id": 3,
            "items": [
                {
                    "bucketlist_id": 3,
                    "done": false,
                    "id": 3,
                    "name": "Obi-Wan Kenobi",
                    "date_created": "2016-07-04  5:16:12",
                    "date_modified": "2016-07-04  5:16:12",
                }
            ],
            "name": "eaque"
        },
        {
            "created_by": "1",
            "id": 4,
            "items": [
                {
                    "bucketlist_id": 4,
                    "done": false,
                    "id": 4,
                    "name": "Chewbacca",
                    "date_created": "2016-07-04  5:16:12",
                    "date_modified": "2016-07-04  5:16:12",
                }
            ],
            "name": "non"
        }
    ]

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

6. Install DrfYasg
   For additional usage examples, you can take a look at the test project in the testproj directory:

$git clone https://github.com/axnsan12/drf-yasg.git$ cd drf-yasg
$virtualenv venv$ source venv/bin/activate
(venv) $cd testproj
(venv)$ pip install -U -r requirements.txt
(venv) $python manage.py migrate
(venv)$ python manage.py shell -c "import createsuperuser"
(venv) $python manage.py runserver
(venv)$ firefox localhost:8000/swagger/

# Notes for Football Data in csv files

All data is in csv format, ready for use within standard spreadsheet applications. Please note that some abbreviations are no longer in use (in particular odds from specific bookmakers no longer used) and refer to data collected in earlier seasons. For a current list of what bookmakers are included in the dataset please visit http://www.football-data.co.uk/matches.php

# Key to results data:

Div = League Division
Date = Match Date (dd/mm/yy)
HomeTeam = Home Team
AwayTeam = Away Team
FTHG and HG = Full Time Home Team Goals
FTAG and AG = Full Time Away Team Goals
FTR and Res = Full Time Result (H=Home Win, D=Draw, A=Away Win)
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

# Match Statistics (where available)

Attendance = Crowd Attendance
Referee = Match Referee
HS = Home Team Shots
AS = Away Team Shots
HST = Home Team Shots on Target
AST = Away Team Shots on Target
HHW = Home Team Hit Woodwork
AHW = Away Team Hit Woodwork
HC = Home Team Corners
AC = Away Team Corners
HF = Home Team Fouls Committed
AF = Away Team Fouls Committed
HFKC = Home Team Free Kicks Conceded
AFKC = Away Team Free Kicks Conceded
HO = Home Team Offsides
AO = Away Team Offsides
HY = Home Team Yellow Cards
AY = Away Team Yellow Cards
HR = Home Team Red Cards
AR = Away Team Red Cards
HBP = Home Team Bookings Points (10 = yellow, 25 = red)
ABP = Away Team Bookings Points (10 = yellow, 25 = red)

Note that Free Kicks Conceeded includes fouls, offsides and any other offense commmitted and will always be equal to or higher than the number of fouls. Fouls make up the vast majority of Free Kicks Conceded. Free Kicks Conceded are shown when specific data on Fouls are not available (France 2nd, Belgium 1st and Greece 1st divisions).

Note also that English and Scottish yellow cards do not include the initial yellow card when a second is shown to a player converting it into a red, but this is included as a yellow (plus red) for European games.

# Key to 1X2 (match) betting odds data:

B365H = Bet365 home win odds
B365D = Bet365 draw odds
B365A = Bet365 away win odds
BSH = Blue Square home win odds
BSD = Blue Square draw odds
BSA = Blue Square away win odds
BWH = Bet&Win home win odds
BWD = Bet&Win draw odds
BWA = Bet&Win away win odds
GBH = Gamebookers home win odds
GBD = Gamebookers draw odds
GBA = Gamebookers away win odds
IWH = Interwetten home win odds
IWD = Interwetten draw odds
IWA = Interwetten away win odds
LBH = Ladbrokes home win odds
LBD = Ladbrokes draw odds
LBA = Ladbrokes away win odds
PSH and PH = Pinnacle home win odds
PSD and PD = Pinnacle draw odds
PSA and PA = Pinnacle away win odds
SOH = Sporting Odds home win odds
SOD = Sporting Odds draw odds
SOA = Sporting Odds away win odds
SBH = Sportingbet home win odds
SBD = Sportingbet draw odds
SBA = Sportingbet away win odds
SJH = Stan James home win odds
SJD = Stan James draw odds
SJA = Stan James away win odds
SYH = Stanleybet home win odds
SYD = Stanleybet draw odds
SYA = Stanleybet away win odds
VCH = VC Bet home win odds
VCD = VC Bet draw odds
VCA = VC Bet away win odds
WHH = William Hill home win odds
WHD = William Hill draw odds
WHA = William Hill away win odds

Bb1X2 = Number of BetBrain bookmakers used to calculate match odds averages and maximums
BbMxH = Betbrain maximum home win odds
BbAvH = Betbrain average home win odds
BbMxD = Betbrain maximum draw odds
BbAvD = Betbrain average draw win odds
BbMxA = Betbrain maximum away win odds
BbAvA = Betbrain average away win odds

MaxH = Oddsportal maximum home win odds
MaxD = Oddsportal maximum draw win odds
MaxA = Oddsportal maximum away win odds
AvgH = Oddsportal average home win odds
AvgD = Oddsportal average draw win odds
AvgA = Oddsportal average away win odds

# Key to total goals betting odds:

BbOU = Number of BetBrain bookmakers used to calculate over/under 2.5 goals (total goals) averages and maximums
BbMx>2.5 = Betbrain maximum over 2.5 goals
BbAv>2.5 = Betbrain average over 2.5 goals
BbMx<2.5 = Betbrain maximum under 2.5 goals
BbAv<2.5 = Betbrain average under 2.5 goals

GB>2.5 = Gamebookers over 2.5 goals
GB<2.5 = Gamebookers under 2.5 goals
B365>2.5 = Bet365 over 2.5 goals
B365<2.5 = Bet365 under 2.5 goals

# Key to Asian handicap betting odds:

BbAH = Number of BetBrain bookmakers used to Asian handicap averages and maximums
BbAHh = Betbrain size of handicap (home team)
BbMxAHH = Betbrain maximum Asian handicap home team odds
BbAvAHH = Betbrain average Asian handicap home team odds
BbMxAHA = Betbrain maximum Asian handicap away team odds
BbAvAHA = Betbrain average Asian handicap away team odds

GBAHH = Gamebookers Asian handicap home team odds
GBAHA = Gamebookers Asian handicap away team odds
GBAH = Gamebookers size of handicap (home team)
LBAHH = Ladbrokes Asian handicap home team odds
LBAHA = Ladbrokes Asian handicap away team odds
LBAH = Ladbrokes size of handicap (home team)
B365AHH = Bet365 Asian handicap home team odds
B365AHA = Bet365 Asian handicap away team odds
B365AH = Bet365 size of handicap (home team)

# Closing odds (last odds before match starts)

PSCH = Pinnacle closing home win odds
PSCD = Pinnacle closing draw odds
PSCA = Pinnacle closing away win odds

Football-Data would like to acknowledge the following sources which have been utilised in the compilation of Football-Data's results and odds files.

# Current results (full time, half time)

Xcores - http://www.xcores .com

# Match statistics

Sportinglife, ESPN Soccer, Bundesliga.de, Gazzetta.it and Football.fr

# Bookmakers betting odds

Betbrain - http://www.betbrain.com
Oddsportal - http://www.oddsportal.com
Individual bookmakers

Betting odds for weekend games are collected Friday afternoons, and on Tuesday afternoons for midweek games.

Additional match statistics (corners, shots, bookings, referee etc.) for the 2000/01 and 2001/02 seasons for the English, Scottish and German leagues were provided by Sports.com (now under new ownership and no longer available).


