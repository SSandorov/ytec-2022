# YTEC Assignment

A customer wants a site where he can track his table soccer scores.

## Customer requirements:

    Teams can be made up of a variable number of players, such as 1vs1, 2vs2 but also 1vs2 or 3vs3.
    The interface should be easy to use.
    There should be a ranking overview. A game won is worth 2 points, a draw worth 1 point and a lost game is worth 0 points.
    A team with 10 points in 3 matches is ranked lower than a person with 10 points in 9 matches.
    It should be possible to give a team a special name.
    Ranking should happen at team level.
        Example: When there are three matches played as follows:
            Ying vs. Ceesjan: 10-8
            Ceesjan vs. Ying+John: 10-6
            John vs. Ying: 4-4
        The ranking will look like this:
            Ying: 3 points in 2 matches
            Ceesjan: 2 points in 2 matches
            John: 1 point in 1 match
            Ying+John: 0 points in 1 match
    The ranking should be made visual, fe. with a bar graph
    There should be an option for a game match maker: You select a number of people and the game will suggest 
    teams with about the same strength (edge case: what kind of strength does a team with 0 games have?)
    Each team should have a summary page with some statistics such as games played, total points scored, total close victories
    There should be a week overview page, with statistics about the games played in the last week

## Our requirements:

    Must be Django 3 (or newer) and Python3.
    Views must be class based.
    Don't spend (a lot of) time on CSS and makeup: Normally we have a designer and a dedicated front-end 
    developer that handle the look of a page.
    Make sure we can easily get your code running - you're free to use things like virtualenv/buildout
    Don't use the admin as part of your UI (feel free to use it for development purposes)
    
## How to use:

Inside of your virtual environment go to the directory of the project and
```
pip install -r requirements.txt
```
if it does not work try
```
pip3 install -r requirements.txt
```
