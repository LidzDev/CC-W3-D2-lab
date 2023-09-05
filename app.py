from flask import Flask
from controllers.order_controller import orders_blueprint
from controllers.order_controller import indiv_order_blueprint



app = Flask(__name__)
app.register_blueprint(orders_blueprint)
app.register_blueprint(indiv_order_blueprint)
