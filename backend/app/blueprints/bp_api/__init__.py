from flask import Blueprint

bp_api = Blueprint('bp_api',__name__,url_prefix='/')

from .resources import (
    index,categoria,nivel,autor,curso,topicos)
