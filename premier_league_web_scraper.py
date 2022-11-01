#!/usr/bin/env python3
from os import times
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re


def get_page(url):
    page = requests.get(url)
    return page


def get_soup(page):
    # convert to beautiful soup
    soup = bs(page.content, features='lxml')
    return soup

def fbref_get_epl_standings():
    URL = f"https://fbref.com/en/comps/9/Premier-League-Stats"
    PAGE = get_page(url=URL)
    SOUP = get_soup(page=PAGE)
    rank_list = []
    logo_list=[]
    team_list = []
    games_list = []
    wins_list = []
    ties_list = []
    losses_list = []
    goals_for_list = []
    goals_against_list = []
    goal_diff_list = []
    points_list = []
    points_avg_list = []
    xg_for_list = []
    xg_against_list = []
    xg_diff_list = []
    xg_diff_per90_list = []
    last_5_list = []
    attendance_per_g_list = []
    get_epl_standings_dict = {}
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='rank']"):
        rank_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).findAll('img'):
        logo_list.append(team['src'])
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='team']"):
        team_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='games']"):
        games_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='wins']"):
        wins_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='ties']"):
        ties_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='losses']"):
        losses_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='goals_for']"):
        goals_for_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='goals_against']"):
        goals_against_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='goal_diff']"):
        goal_diff_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='points']"):
        points_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='points_avg']"):
        points_avg_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='xg_for']"):
        xg_for_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='xg_against']"):
        xg_against_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='xg_diff']"):
        xg_diff_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='xg_diff_per90']"):
        xg_diff_per90_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='last_5']"):
        last_5_list.append(team.get_text())
    for team in SOUP.find('table', id=re.compile('^results.*overall$')).select("[data-stat='attendance_per_g']"):
        attendance_per_g_list.append(team.get_text())
    get_epl_standings_dict['rank'] = rank_list[1:]
    get_epl_standings_dict['logo'] = logo_list
    get_epl_standings_dict['team'] = team_list[1:]
    get_epl_standings_dict['games'] = games_list[1:]
    get_epl_standings_dict['wins'] = wins_list[1:]
    get_epl_standings_dict['ties'] = ties_list[1:]
    get_epl_standings_dict['losses'] = losses_list[1:]
    get_epl_standings_dict['goals_for'] = goals_for_list[1:]
    get_epl_standings_dict['goals_against'] = goals_against_list[1:]
    get_epl_standings_dict['goal_diff'] = goal_diff_list[1:]
    get_epl_standings_dict['points'] = points_list[1:]
    get_epl_standings_dict['points_avg'] = points_avg_list[1:]
    get_epl_standings_dict['xg_for'] = xg_for_list[1:]
    get_epl_standings_dict['xg_against'] = xg_against_list[1:]
    get_epl_standings_dict['xg_diff'] = xg_diff_list[1:]
    get_epl_standings_dict['xg_diff_per90'] = xg_diff_per90_list[1:]
    get_epl_standings_dict['last_5'] = last_5_list[1:]
    get_epl_standings_dict['attendance_per_g'] = attendance_per_g_list[1:]
    get_epl_standings_df = pd.DataFrame(get_epl_standings_dict).rename(
        columns={"rank": "RANK",
                 "logo" : "LOGO_URL",
                 "team": "CLUB",
                 "games": "GAMES",
                 "wins": "WINS",
                 "ties": "TIES",
                 "losses": "LOSSES",
                 "goals_for": "GOALS_FOR",
                 "goals_against": "GOALS_AGAINST",
                 "goal_diff": "GOAL_DIFF",
                 "points": "POINTS",
                 "points_avg": "PONTS_AVG",
                 "xg_for": "xG_FOR",
                 "xg_against": "xG_AGAINST",
                 "xg_diff": "xG_DIFF",
                 "xg_diff_per90": "xG_DIFF_PER90",
                 "last_5": "LAST_5",
                 "attendance_per_g": "ATTENDANCE_PER_GAME"})
    return get_epl_standings_df

def fbref_get_squad_standard_stats():
    URL = f"https://fbref.com/en/comps/9/Premier-League-Stats"
    PAGE = get_page(url=URL)
    SOUP = get_soup(page=PAGE)
    teams_list = []
    no_players_used_in_game_list = []
    player_age_list = []
    possession_list = []
    goals_score_list = []
    assists_list = []
    non_penalty_goals_list = []
    pk_made_list = []
    pk_attempted_list = []
    yc_list = []
    rc_list = []
    xG_list = []
    xAG_list = []
    non_penalty_xG_list = []
    get_squad_standard_stats_dict = {}
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='team']"):
        teams_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='players_used']"):
        no_players_used_in_game_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='avg_age']"):
        player_age_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='possession']"):
        possession_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='goals']"):
        goals_score_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='assists']"):
        assists_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='goals_pens']"):
        non_penalty_goals_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='pens_made']"):
        pk_made_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='pens_att']"):
        pk_attempted_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='cards_yellow']"):
        yc_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='cards_red']"):
        rc_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='xg']"):
        xG_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='xg_assist']"):
        xAG_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_standard_for').select("[data-stat='npxg']"):
        non_penalty_xG_list.append(team.get_text())
    get_squad_standard_stats_dict['teams_list'] = teams_list[1:]
    get_squad_standard_stats_dict['no_players_used_in_game_list'] = no_players_used_in_game_list[1:]
    get_squad_standard_stats_dict['player_age_list'] = player_age_list[1:]
    get_squad_standard_stats_dict['possession_list'] = possession_list[1:]
    get_squad_standard_stats_dict['goals_score_list'] = goals_score_list[1:]
    get_squad_standard_stats_dict['assists_list'] = assists_list[1:]
    get_squad_standard_stats_dict['non_penalty_goals_list'] = non_penalty_goals_list[1:]
    get_squad_standard_stats_dict['pk_made_list'] = pk_made_list[1:]
    get_squad_standard_stats_dict['pk_attempted_list'] = pk_attempted_list[1:]
    get_squad_standard_stats_dict['yc_list'] = yc_list[1:]
    get_squad_standard_stats_dict['rc_list'] = rc_list[1:]
    get_squad_standard_stats_dict['xG_list'] = xG_list[1:]
    get_squad_standard_stats_dict['xAG_list'] = xAG_list[1:]
    get_squad_standard_stats_dict['non_penalty_xG_list'] = non_penalty_xG_list[1:]
    get_squad_standard_stats_df = pd.DataFrame(get_squad_standard_stats_dict).rename(
        columns={"teams_list": "CLUB",
                 "no_players_used_in_game_list": "PLAYERS_USED",
                 "player_age_list": "PLAYERS_AVG_AGE",
                 "possession_list": "POSSESSION",
                 "goals_score_list": "GOALS",
                 "assists_list": "ASSISTS",
                 "non_penalty_goals_list": "NON_PENALTY_GOALS",
                 "pk_made_list": "PENALTIES_MADE",
                 "pk_attempted_list": "PENALTIES_ATTEMPTED",
                 "yc_list": "YELLOW_CARDS",
                 "rc_list": "RED_CARDS",
                 "xG_list": "xG",
                 "xAG_list": "xAG",
                 "non_penalty_xG_list": "NON_PENALTY_xG"})
    return get_squad_standard_stats_df


def fbref_get_squad_goalkeeping_stats():
    URL = f"https://fbref.com/en/comps/9/Premier-League-Stats"
    PAGE = get_page(url=URL)
    SOUP = get_soup(page=PAGE)
    teams_list = []
    gk_goals_against_list = []
    gk_goals_against_per90_list = []
    gk_shots_on_target_against_list = []
    gk_saves_list = []
    gk_save_pct_list = []
    gk_clean_sheets_list = []
    gk_clean_sheets_pct_list = []
    gk_pens_att_list = []
    gk_pens_allowed_list = []
    gk_pens_saved_list = []
    gk_pens_missed_list = []
    gk_pens_save_pct_list = []
    get_squad_goalkeeping_stats_dict = {}
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='team']"):
        teams_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_goals_against']"):
        gk_goals_against_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_goals_against_per90']"):
        gk_goals_against_per90_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_shots_on_target_against']"):
        gk_shots_on_target_against_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_saves']"):
        gk_saves_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_save_pct']"):
        gk_save_pct_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_clean_sheets']"):
        gk_clean_sheets_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_clean_sheets_pct']"):
        gk_clean_sheets_pct_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_pens_att']"):
        gk_pens_att_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_pens_allowed']"):
        gk_pens_allowed_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_pens_saved']"):
        gk_pens_saved_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_pens_missed']"):
        gk_pens_missed_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_keeper_for').select("[data-stat='gk_pens_save_pct']"):
        gk_pens_save_pct_list.append(team.get_text())
    get_squad_goalkeeping_stats_dict['teams_list'] = teams_list[1:]
    get_squad_goalkeeping_stats_dict['gk_goals_against_list'] = gk_goals_against_list[1:]
    get_squad_goalkeeping_stats_dict['gk_goals_against_per90_list'] = gk_goals_against_per90_list[1:]
    get_squad_goalkeeping_stats_dict['gk_shots_on_target_against_list'] = gk_shots_on_target_against_list[1:]
    get_squad_goalkeeping_stats_dict['gk_saves_list'] = gk_saves_list[1:]
    get_squad_goalkeeping_stats_dict['gk_save_pct_list'] = gk_save_pct_list[1:]
    get_squad_goalkeeping_stats_dict['gk_clean_sheets_list'] = gk_clean_sheets_list[1:]
    get_squad_goalkeeping_stats_dict['gk_clean_sheets_pct_list'] = gk_clean_sheets_pct_list[1:]
    get_squad_goalkeeping_stats_dict['gk_pens_att_list'] = gk_pens_att_list[1:]
    get_squad_goalkeeping_stats_dict['gk_pens_allowed_list'] = gk_pens_allowed_list[1:]
    get_squad_goalkeeping_stats_dict['gk_pens_saved_list'] = gk_pens_saved_list[1:]
    get_squad_goalkeeping_stats_dict['gk_pens_missed_list'] = gk_pens_missed_list[1:]
    get_squad_goalkeeping_stats_dict['gk_pens_save_pct_list'] = gk_pens_save_pct_list[1:]
    get_squad_goalkeeping_stats_df = pd.DataFrame(get_squad_goalkeeping_stats_dict).rename(
        columns={"teams_list": "CLUB",
                 "gk_goals_against_list": "GOALS_AGAINST",
                 "gk_goals_against_per90_list": "GOALS_AGAINST_PER90",
                 "gk_shots_on_target_against_list": "SHOTS_ON_TARGET",
                 "gk_saves_list": "SAVES",
                 "gk_save_pct_list": "SAVES_PCT",
                 "gk_clean_sheets_list": "CLEAN_SHEETS",
                 "gk_clean_sheets_pct_list": "CLEAN_SHEETS_PCT",
                 "gk_pens_att_list": "PENALTIES_ATTEMPTED",
                 "gk_pens_allowed_list": "PENALTIES_ALLOWED",
                 "gk_pens_saved_list": "PENALTIES_SAVED",
                 "gk_pens_missed_list": "PENALTIES_MISSED",
                 "gk_pens_save_pct_list": "PENALTIES_SAVED_PCT"})
    return get_squad_goalkeeping_stats_df


def fbref_get_squad_shooting_stats():
    URL = f"https://fbref.com/en/comps/9/Premier-League-Stats"
    PAGE = get_page(url=URL)
    SOUP = get_soup(page=PAGE)
    teams_list = []
    goals_list = []
    shots_list = []
    shots_on_target_list = []
    shots_on_target_pct_list = []
    shots_per90_list = []
    shots_on_target_per90_list = []
    goals_per_shot_list = []
    goals_per_shot_on_target_list = []
    average_shot_distance_list = []
    shots_free_kicks_list = []
    pens_made_list = []
    pens_att_list = []
    xg_list = []
    npxg_list = []
    npxg_per_shot_list = []
    xg_net_list = []
    npxg_net_list = []

    get_squad_shooting_stats_dict = {}
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='team']"):
        teams_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='goals']"):
        goals_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='shots']"):
        shots_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='shots_on_target']"):
        shots_on_target_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='shots_on_target_pct']"):
        shots_on_target_pct_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='shots_per90']"):
        shots_per90_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='shots_on_target_per90']"):
        shots_on_target_per90_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='goals_per_shot']"):
        goals_per_shot_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='goals_per_shot_on_target']"):
        goals_per_shot_on_target_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='average_shot_distance']"):
        average_shot_distance_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='shots_free_kicks']"):
        shots_free_kicks_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='pens_made']"):
        pens_made_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='pens_att']"):
        pens_att_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='xg']"):
        xg_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='npxg']"):
        npxg_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='npxg_per_shot']"):
        npxg_per_shot_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='xg_net']"):
        xg_net_list.append(team.get_text())
    for team in SOUP.find('table', id='stats_squads_shooting_for').select("[data-stat='npxg_net']"):
        npxg_net_list.append(team.get_text())
    get_squad_shooting_stats_dict['teams_list'] = teams_list[1:]
    get_squad_shooting_stats_dict['goals_list'] = goals_list[1:]
    get_squad_shooting_stats_dict['shots_list'] = shots_list[1:]
    get_squad_shooting_stats_dict['shots_on_target_list'] = shots_on_target_list[1:]
    get_squad_shooting_stats_dict['shots_on_target_pct_list'] = shots_on_target_pct_list[1:]
    get_squad_shooting_stats_dict['shots_per90_list'] = shots_per90_list[1:]
    get_squad_shooting_stats_dict['shots_on_target_per90_list'] = shots_on_target_per90_list[1:]
    get_squad_shooting_stats_dict['goals_per_shot_list'] = goals_per_shot_list[1:]
    get_squad_shooting_stats_dict['average_shot_distance_list'] = average_shot_distance_list[1:]
    get_squad_shooting_stats_dict['shots_free_kicks_list'] = shots_free_kicks_list[1:]
    get_squad_shooting_stats_dict['pens_made_list'] = pens_made_list[1:]
    get_squad_shooting_stats_dict['pens_att_list'] = pens_att_list[1:]
    get_squad_shooting_stats_dict['xg_list'] = xg_list[1:]
    get_squad_shooting_stats_dict['npxg_list'] = npxg_list[1:]
    get_squad_shooting_stats_dict['npxg_per_shot_list'] = npxg_per_shot_list[1:]
    get_squad_shooting_stats_dict['xg_net_list'] = xg_net_list[1:]
    get_squad_shooting_stats_dict['npxg_net_list'] = npxg_net_list[1:]
    get_squad_shooting_stats_df = pd.DataFrame(get_squad_shooting_stats_dict).rename(
        columns={"teams_list": "CLUB",
                 "goals_list": "GOALS",
                 "shots_list": "SHOTS",
                 "shots_on_target_list": "SHOTS_ON_TARGET",
                 "shots_on_target_pct_list": "SHOTS_ON_TARGET_PCT",
                 "shots_per90_list": "SHOTS_PER90",
                 "shots_on_target_per90_list": "SHOTS_ON_TARGET_PER90",
                 "goals_per_shot_list": "GOALS_PER_SHOT",
                 "average_shot_distance_list": "AVG_SHOT_DISTANCE",
                 "shots_free_kicks_list": "SHOTS_FROM_FREEKICKS",
                 "pens_made_list": "PENALTIES_MADE",
                 "pens_att_list": "PENALTIES_ATTEMPTED",
                 "xg_list": "xG",
                 "npxg_list": "NON_PENALTY_xG",
                 "npxg_per_shot_list": "NON_PENALTY_xG_PER_SHOT",
                 "xg_net_list": "NET_xG",
                 "npxg_net_list": "NET_NON_PENALTY_xG"})
    return get_squad_shooting_stats_df


def main():
    pd.set_option('display.max_colwidth', None)
    print(fbref_get_squad_standard_stats())
    print(fbref_get_squad_goalkeeping_stats())
    print(fbref_get_squad_shooting_stats())
    print(fbref_get_epl_standings())


if __name__ == "__main__":
    main()