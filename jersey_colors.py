# jersey colors

import pandas as pd
import random


def create_league_contrast_even_spacing(num_teams, contrast):
    """
    Returns a pandas dataframe that represents a league, where each team (row) has been assigned two colors according
    to an "evenly spaced" method, where for a league with n teams and c contrast, the ith team's two colors will be
    equal to (360/n)*i and (360/n)*i + c
    :param num_teams: the number of rows in the returns dataframe
    :param contrast: the value in degrees that separates the two colors assigned to each team (0 <-> 180)
    :return: a pandas dataframe with num_teams rows, each representing a team (index = team number), and
    columns color1 and color2 (integers, 0 - 359).
    """
    # init output
    rows = []

    # append a new row num_teams times, color pairs that are 'contrast' apart, and where
    # contrast between two teams (color1) i and j is equal to abs((360i / num_teams) - (360j / num_teams))
    for i in range(num_teams):
        color1 = int((360 / num_teams) * i)
        color2 = (color1 + contrast) % 360
        rows.append((color1, color2))

    return pd.DataFrame(rows, columns=['color1', 'color2'])


def create_league_contrast_random_spacing(num_teams, contrast):
    """
    Returns a pandas dataframe that represents a league, where each team (row) has been assigned two colors according
    to a "random spacing" method, where for a league with n teams and c contrast, the ith team's two colors will be
    equal to random number r in range(360) and r + c % 360
    :param num_teams: the number of rows in the returns dataframe
    :param contrast: the value in degrees that separates the two colors assigned to each team (0 <-> 180)
    :return: a pandas dataframe with num_teams rows, each representing a team (index = team number), and
    columns color1 and color2 (integers, 0 - 359).
    """
    # init output
    rows = []

    # append a new row num_teams times, color pairs that are 'contrast' apart, and where
    # contrast between teams is random
    for i in range(num_teams):
        color1 = random.randrange(360)
        color2 = (color1 + contrast) % 360
        rows.append((color1, color2))

    return pd.DataFrame(rows, columns=['color1', 'color2'])


def create_league_true_random(num_teams):
    """
    Returns a pandas dataframe that represents a league, where each team (row) has been assigned two colors by
    random assignment
    :param num_teams: the number of rows in the returns dataframe
    :return: a pandas dataframe with num_teams rows, each representing a team (index = team number), and
    columns color1 and color2 (integers, 0 - 359)
    """
    # init output
    rows = []

    # append a new row num_teams times, with random color assignments
    for i in range(num_teams):
        color1 = random.randrange(360)
        color2 = random.randrange(360)
        rows.append((color1, color2))

    return pd.DataFrame(rows, columns=['color1', 'color2'])


def jersey_contrast(jersey1, jersey2):
    """
    Returns the contrast between two given jersey colors. Calculation needed because colors are circular around
    the color wheel (in range(360)), so jersey_contrast(10, 350) -> 20, not 340.
    :param jersey1: integer in range(360)
    :param jersey2: integer in range(360)
    :return: an integer representing the contrast (difference) between the two given values
    """
    contrast1 = abs(jersey1 - jersey2)
    contrast2 = min(jersey1, jersey2) + 360 - max(jersey1, jersey2)
    return min(contrast1, contrast2)


def team_contrast(team1a, team1b, team2a, team2b):
    """
    Returns the highest achievable contrast between two teams, each with two jerseys assigned
    :param team1a: integer in range(360), representing team1 color1
    :param team1b: integer in range(360), representing team1 color2
    :param team2a: integer in range(360), representing team2 color1
    :param team2b: integer in range(360), representing team2 color2
    :return: an integer which is the highest contrast achievable between two teams, if they can wear either jersey
    """
    dif1 = jersey_contrast(team1a, team2a)
    dif2 = jersey_contrast(team1a, team2b)
    dif3 = jersey_contrast(team1b, team2a)
    dif4 = jersey_contrast(team1b, team2b)

    return max(dif1, dif2, dif3, dif4)


def league_contrast(league):
    """
    Takes a league's dataframe and outputs a dataframe with a row representing each
    possible matchup and the corresponding contrast
    :param league dataframe containing a row for each team with two color assignments
    :return: a dataframe with columns for first team, second team, and contrast
    """
    # init output
    rows = []

    # for each row (team) in the league, create a matchup between the team and every other team in the league
    # calculate the contrast for the matchup, and add it to the output
    for i in range(league.shape[0]):
        for j in range(i+1, league.shape[0]):
            contrast = team_contrast(league.iloc[i, league.columns.get_loc('color1')],
                                     league.iloc[i, league.columns.get_loc('color2')],
                                     league.iloc[j, league.columns.get_loc('color1')],
                                     league.iloc[j, league.columns.get_loc('color2')])
            rows.append((i, j, contrast))

    return pd.DataFrame(rows, columns=['team1', 'team2', 'contrast'])


"""
print(create_league_true_random(10))
print(create_league_contrast_even_spacing(36, 70))
print(create_league_contrast_random_spacing(10, 50))

print(jersey_contrast(0, 0))
print(jersey_contrast(0, 50))
print(jersey_contrast(10, 350))

print(team_contrast(0, 60, 10, 100))
print(team_contrast(0, 180, 0, 90))
print(team_contrast(0, 120, 120, 240))
print(team_contrast(0, 90, 90, 270))
print(team_contrast(0, 20, 330, 350))

league1 = create_league_contrast_even_spacing(10, 10)
print('league1:\n', league1)

league1_contrast = league_contrast(league1)
print('league1_contrast:\n', league1_contrast)
"""
