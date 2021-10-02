from flask import Blueprint,render_template

adminapp = Blueprint("admin",__name__,static_folder="static",template_folder="templates")

@adminapp.route("/admindashboard")
@adminapp.route("/")
def admindashboard():
    return "admindashboard"