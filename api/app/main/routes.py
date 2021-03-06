import logging
from datetime import datetime
from flask import current_app
from app.main import bp


@bp.route('/')
@bp.route('/index')
@bp.route('/error')
@bp.route('/words')
@bp.route('/games')
@bp.route('/register')
@bp.route('/login')
def index():
    """ index and available routes where user can press F5 """
    return current_app.send_static_file('index.html')


@bp.route('/time', methods=['GET'])
def get_time():
    """ Debug """

    return {'current_time': datetime.now()}


logger = logging.getLogger(__name__)
