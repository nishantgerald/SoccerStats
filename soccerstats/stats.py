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
from premier_league_web_scraper import fbref_get_epl_standings

# DEFINING THE BLUEPRINT CALLED `standings`
bp = Blueprint("stats", __name__, url_prefix="/")

# DEFINING THE log_beer VIEW AND REGISTERING IT WITH THE checkin BLUEPRINT
@bp.route("/", methods=("GET", "POST"))
@bp.route("/standings", methods=("GET", "POST"))

def standings():
    epl_standings=fbref_get_epl_standings()
    return render_template("stats/standings.html", epl_standings=epl_standings)