import functools
from datetime import datetime
from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd
import hashlib
from premier_league_web_scraper import get_standings

# DEFINING THE BLUEPRINT CALLED `standings`
bp = Blueprint("stats", __name__, url_prefix="/")

# DEFINING THE log_beer VIEW AND REGISTERING IT WITH THE checkin BLUEPRINT
@bp.route("/", methods=("GET", "POST"))
@bp.route("/standings", methods=("GET", "POST"))

def standings():
    YEAR='2022'
    standings_table=get_standings(YEAR)
    # print(standings)
    return render_template("stats/standings.html", standings_table=standings_table)