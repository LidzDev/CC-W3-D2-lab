from flask import Blueprint
from flask import render_template
#from models.task_list import tasks

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")

def index():    
    return render_template('index.jinja') #, title="My Task List", tasks = tasks)