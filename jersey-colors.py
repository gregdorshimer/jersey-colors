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
    columns color1 and color2 (integers, 0 - 359).
    """

    # init output
    rows = []

    # append a new row num_teams times, with random color assignments
    for i in range(num_teams):
        color1 = random.randrange(360)
        color2 = random.randrange(360)
        rows.append((color1, color2))

    return pd.DataFrame(rows, columns=['color1', 'color2'])


"""
print(create_league_true_random(10))
print(create_league_contrast_even_spacing(36, 70))
print(create_league_contrast_random_spacing(10, 50))
"""
