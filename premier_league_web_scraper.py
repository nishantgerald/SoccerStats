#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def get_page(url):
    page = requests.get(url)
    return page


def get_soup(page):
    # convert to beautiful soup
    soup = bs(page.content, features='lxml')
    return soup


def generate_standings_df(position_list, club_name_list, club_logo_url_list, stat_dictionary):
    df = pd.DataFrame()
    df['POSITION'] = position_list
    df['CLUB'] = club_name_list
    df['LOGO_URL'] = club_logo_url_list
    df['GP'] = stat_dictionary['GP']
    df['W'] = stat_dictionary['W']
    df['D'] = stat_dictionary['D']
    df['L'] = stat_dictionary['L']
    df['F'] = stat_dictionary['F']
    df['A'] = stat_dictionary['A']
    df['GD'] = stat_dictionary['GD']
    df['P'] = stat_dictionary['P']
    return df


def extract_table_data(soup):
    standings_table = soup.find('div', class_='standings__table')
    team_names_column = standings_table.find('tbody', class_="Table__TBODY")
    team_names_column = team_names_column.find_all(
        'tr', class_='Table__TR--sm')

    position_list = []
    club_name_list = []
    club_logo_url_list = []

    stat_dictionary = {'GP': [], 'W': [], 'D': [],
                       'L': [], 'F': [], 'A': [], 'GD': [], 'P': []}

    for team_tag in team_names_column:
        position_list.append(team_tag.find(
            'span', class_='team-position ml2 pr3').get_text())
        club_name_list.append(team_tag.find(
            'span', class_='hide-mobile').get_text())
        espn_clubhouse_id = team_tag.find('span', class_='TeamLink__Logo').find(
            'a').attrs['data-clubhouse-uid'][-3:]
        club_logo_url_list.append(
            f"https://a.espncdn.com/combiner/i?img=/i/teamlogos/soccer/500/{espn_clubhouse_id}.png")

    stats_table = standings_table.find(
        'table', class_='Table Table--align-right').find('tbody').find_all('tr')
    stats_id_map = {1: 'GP', 2: 'W', 3: 'D',
                    4: 'L', 5: 'F', 6: 'A', 7: 'GD', 8: 'P'}
    for team_stat in stats_table:
        stat_id = team_stat.find_all('td')
        for idx, id in enumerate(stat_id):
            stat_dictionary[stats_id_map[idx+1]].append(id.get_text())
    return position_list, club_name_list, club_logo_url_list, stat_dictionary


def get_standings(SEASON):
    URL = f"https://www.espn.com/soccer/standings/_/league/ENG.1/season/{SEASON}"
    PAGE = get_page(url=URL)
    SOUP = get_soup(page=PAGE)
    POSITION_LIST, CLUB_NAME_LIST, CLUB_LOG_URL_LIST, STAT_DICTIONARY = extract_table_data(
        SOUP)
    STANDING_DF = generate_standings_df(
        position_list=POSITION_LIST, club_name_list=CLUB_NAME_LIST, club_logo_url_list=CLUB_LOG_URL_LIST, stat_dictionary=STAT_DICTIONARY)
    return STANDING_DF


def main():
    pd.set_option('display.max_colwidth', None)
    # PICK YEAR BETWEEN 2001 TO CURRENT SEASON
    SEASON = "2022"
    print(get_standings(SEASON))


if __name__ == "__main__":
    main()
