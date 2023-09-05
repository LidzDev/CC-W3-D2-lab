from flask import Blueprint
from flask import render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)
indiv_order_blueprint = Blueprint("indiv", __name__)

@orders_blueprint.route("/orders")
def index():    
    return render_template('index.jinja', title="Shop Order List", orders = orders)

@indiv_order_blueprint.route("/indiv")
def indiv():
    return render_template('indiv.jinja')