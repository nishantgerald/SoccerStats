DROP TABLE IF EXISTS epl_standings;

DROP TABLE IF EXISTS squad_standard_stats;

DROP TABLE IF EXISTS squad_goalkeeping_stats;

DROP TABLE IF EXISTS squad_shooting_stats;

CREATE TABLE epl_standings (
  club TEXT PRIMARY KEY,
  rank INT NOT NULL,
  logo_url TEXT NOT NULL,
  games INT NOT NULL,
  wins INT NOT NULL,
  ties INT NOT NULL,
  losses INT NOT NULL,
  goals_for INT NOT NULL,
  goals_against INT NOT NULL,
  goal_difference INT NOT NULL,
  points_average FLOAT NOT NULL,
  xg_for FLOAT NOT NULL,
  xg_against FLOAT NOT NULL,
  xg_difference FLOAT NOT NULL,
  xg_difference_per90 FLOAT NOT NULL,
  last_five TEXT NOT NULL,
  attendance_per_game TEXT NOT NULL
);

CREATE TABLE squad_standard_stats (
  club TEXT PRIMARY KEY,
  players_used INT NOT NULL,
  players_average_age FLOAT NOT NULL,
  posession FLOAT NOT NULL,
  goals INT NOT NULL,
  assists INT NOT NULL,
  non_penalty_goals INT NOT NULL,
  penalties_made INT NOT NULL,
  penalties_attempted INT NOT NULL,
  yellow_cards INT NOT NULL,
  red_cards INT NOT NULL,
  xg FLOAT NOT NULL,
  xag FLOAT NOT NULL,
  non_penalty_xg FLOAT NOT NULL
);

CREATE TABLE squad_goalkeeping_stats (
  club TEXT PRIMARY KEY,
  goals_against INT NOT NULL,
  goals_against_per90 FLOAT NOT NULL,
  shots_on_target INT NOT NULL,
  saves INT NOT NULL,
  saves_percentage FLOAT NOT NULL,
  clean_sheets INT NOT NULL,
  clean_sheets_percentage FLOAT NOT NULL,
  penalties_attempted INT NOT NULL,
  penalties_allowed INT NOT NULL,
  penalties_saved INT NOT NULL,
  penalties_saved_percentage FLOAT NOT NULL,
  penalties_missed INT NOT NULL
);

CREATE TABLE squad_shooting_stats (
  clubs TEXT PRIMARY KEY,
  goals INT NOT NULL,
  shots INT NOT NULL,
  shots_on_target INT NOT NULL,
  shots_on_target_percentage FLOAT NOT NULL,
  shots_per90 FLOAT NOT NULL,
  shots_on_target_per90 FLOAT NOT NULL,
  goals_per_shot FLOAT NOT NULL,
  average_shot_distance FLOAT NOT NULL,
  shots_from_freekicks INT NOT NULL,
  penalties_made INT NOT NULL,
  penalties_attempted INT NOT NULL,
  xg FLOAT NOT NULL,
  non_penalty_xg FLOAT NOT NULL,
  non_penalty_xg_per_shot FLOAT NOT NULL,
  net_xg FLOAT NOT NULL,
  net_non_penalty_xg FLOAT NOT NULL
);