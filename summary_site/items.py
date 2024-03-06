from flask import Blueprint, request, url_for, redirect, flash, current_app
from flask_login import login_required, current_user

from . import db
from .models import Item

items = Blueprint('items', __name__)


@login_required
@items.route('/additem', methods=['POST'])
def add_item():
    item_name = request.form.get('name').strip()
    item_price = request.form.get('price').strip()

    exists = Item.query.filter_by(
        userid=current_user.id,
        name=item_name
    )
    if exists.all():
        flash('This item already exists for you. Please refresh the page.')
        current_app.logger.debug(f"User {current_user.id} tried to add {item_name} but it already exists for them")
        return redirect(url_for('main.profile'))

    try:
        db.session.add(Item(userid=current_user.id, name=item_name, price=item_price))
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        flash('Problem adding new item. Please refresh page.')

    return redirect(url_for('main.profile'))
