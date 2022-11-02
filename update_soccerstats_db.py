#!/usr/bin/env python3
import sqlite3
import datetime
from premier_league_web_scraper import (
    fbref_get_squad_standard_stats,
    fbref_get_squad_goalkeeping_stats,
    fbref_get_squad_shooting_stats,
    fbref_get_epl_standings,
)

def recreating_database_with_schema():
    # OPEN SCHEMA FILE
    with open("schema.sql", "r") as sql_file:
        create_db_script = sql_file.read()

    # CREATE DB
    db = sqlite3.connect("soccerstats.db")
    cursor = db.cursor()
    cursor.executescript(create_db_script)
    return cursor, db


def update_epl_standing_data(cursor):
    # GET DATA
    epl_standings_df = fbref_get_epl_standings()
    # INSERT EPL STANDING DATA
    for index, row in epl_standings_df.iterrows():
        cursor.execute(
            "INSERT INTO epl_standings (club,rank,logo_url,games,wins,ties,losses,goals_for,goals_against,goal_difference,points_average,xg_for,xg_against,xg_difference,xg_difference_per90,last_five,attendance_per_game) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                row["CLUB"],
                row["RANK"],
                row["LOGO_URL"],
                row["GAMES"],
                row["WINS"],
                row["TIES"],
                row["LOSSES"],
                row["GOALS_FOR"],
                row["GOALS_AGAINST"],
                row["GOAL_DIFF"],
                row["POINTS_AVG"],
                row["xG_FOR"],
                row["xG_AGAINST"],
                row["xG_DIFF"],
                row["xG_DIFF_PER90"],
                row["LAST_5"],
                row["ATTENDANCE_PER_GAME"],
            ),
        )


def update_epl_standard_stats_data(cursor):
    # GET DATA
    squad_standard_stats_df = fbref_get_squad_standard_stats()
    # INSERT SQUAD STANDARD STATS DATA
    for index, row in squad_standard_stats_df.iterrows():
        cursor.execute(
            "INSERT INTO squad_standard_stats (club, players_used, players_average_age, posession, goals, assists, non_penalty_goals, penalties_made, penalties_attempted, yellow_cards, red_cards, xg, xag, non_penalty_xg) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                row["CLUB"],
                row["PLAYERS_USED"],
                row["PLAYERS_AVG_AGE"],
                row["POSSESSION"],
                row["GOALS"],
                row["ASSISTS"],
                row["NON_PENALTY_GOALS"],
                row["PENALTIES_MADE"],
                row["PENALTIES_ATTEMPTED"],
                row["YELLOW_CARDS"],
                row["RED_CARDS"],
                row["xG"],
                row["xAG"],
                row["NON_PENALTY_xG"],
            ),
        )


def update_epl_goalkeeping_stats_data(cursor):
    # GET DATA
    squad_goalkeeping_stats_df = fbref_get_squad_goalkeeping_stats()
    # INSERT SQUAD GOALKEEPING STATS DATA
    for index, row in squad_goalkeeping_stats_df.iterrows():
        cursor.execute(
            "INSERT INTO squad_goalkeeping_stats (club, goals_against, goals_against_per90, shots_on_target, saves, saves_percentage, clean_sheets, clean_sheets_percentage, penalties_attempted, penalties_allowed, penalties_saved, penalties_saved_percentage, penalties_missed) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                row["CLUB"],
                row["GOALS_AGAINST"],
                row["GOALS_AGAINST_PER90"],
                row["SHOTS_ON_TARGET"],
                row["SAVES"],
                row["SAVES_PCT"],
                row["CLEAN_SHEETS"],
                row["CLEAN_SHEETS_PCT"],
                row["PENALTIES_ATTEMPTED"],
                row["PENALTIES_ALLOWED"],
                row["PENALTIES_SAVED"],
                row["PENALTIES_SAVED_PCT"],
                row["PENALTIES_MISSED"],
            ),
        )


def update_epl_shooting_stats_data(cursor):
    # GET DATA
    squad_shooting_stats_df = fbref_get_squad_shooting_stats()
    # INSERT SQUAD SHOOTING STATS DATA
    for index, row in squad_shooting_stats_df.iterrows():
        cursor.execute(
            "INSERT INTO squad_shooting_stats (clubs, goals, shots, shots_on_target, shots_on_target_percentage, shots_per90, shots_on_target_per90, goals_per_shot, average_shot_distance, shots_from_freekicks, penalties_made, penalties_attempted, xg, non_penalty_xg, non_penalty_xg_per_shot, net_xg, net_non_penalty_xg) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                row["CLUB"],
                row["GOALS"],
                row["SHOTS"],
                row["SHOTS_ON_TARGET"],
                row["SHOTS_ON_TARGET_PCT"],
                row["SHOTS_PER90"],
                row["SHOTS_ON_TARGET_PER90"],
                row["GOALS_PER_SHOT"],
                row["AVG_SHOT_DISTANCE"],
                row["SHOTS_FROM_FREEKICKS"],
                row["PENALTIES_MADE"],
                row["PENALTIES_ATTEMPTED"],
                row["xG"],
                row["NON_PENALTY_xG"],
                row["NON_PENALTY_xG_PER_SHOT"],
                row["NET_xG"],
                row["NET_NON_PENALTY_xG"],
            ),
        )

def clean_up(db):
    # CLEAN UP
    db.commit()
    db.close()
    current_time=datetime.datetime.now()
    with open('last_updated.txt','a+') as out:
        print(current_time, file=out)

def main():
    cursor, db = recreating_database_with_schema()
    print("DATABASE RECREATED WITH DEFINED SOCCERSTATS SCHEMA")

    update_epl_standing_data(cursor)
    print("EPL STANDING DATA UPDATED")

    update_epl_standard_stats_data(cursor)
    print("EPL STANDARD SQUAD STATS DATA UPDATED")

    update_epl_goalkeeping_stats_data(cursor)
    print("EPL GOALKEEPING STATS DATA UPDATED")

    update_epl_shooting_stats_data(cursor)
    print("EPL SHOOTING STATS DATA UPDATED")

    clean_up(db)
    print("CLEANING UP OPEN CONNECTIONS")

if __name__ == "__main__":
    main()