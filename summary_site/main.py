from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user

from .models import Item

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@login_required
@main.route('/profile')
def profile():
    items = get_items_for_user(current_user.id)
    current_app.logger.debug(f"User {current_user.id} has {len(items)} items")
    return render_template('profile.html', name=current_user.name, data=items)


# @login_required
def get_items_for_user(user_id):
    items = Item.query.filter_by(userid=user_id).all()
    items = items if items else []
    return items
