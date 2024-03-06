from flask import render_template, current_app, Blueprint
from flask_login import login_required, current_user
from sqlalchemy import func

from . import db
from .models import Item

summary = Blueprint('summary', __name__)


@login_required
@summary.route('/summarise', methods=['POST'])
def summarise():
    data = db.session.query(func.sum(Item.price)).filter(
        Item.userid == current_user.id,
    ).group_by(Item.userid)
    if data.all():
        total = data.all()[0][0]
        current_app.logger.debug(f"Summarised Total £{total} for User {current_user.id}")
    else:
        total = 0
        current_app.logger.debug(f"No items found for User {current_user.id}, returning £0 summary")
    return render_template('summary.html', total=total)
