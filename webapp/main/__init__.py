from flask import Blueprint

main = Blueprint('main', __name__)

# from . import views, errors
from . import da_views, ml_views, others_views, errors
