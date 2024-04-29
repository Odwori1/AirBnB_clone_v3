#!/usr/bin/python3
"""
create flask app; app_views
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def get_status():
    """am method that returns a JSON: status: OK"""
    return jsonify(status='OK')


@app_views.route('/stats', strict_slashes=False)
def get_stats():
    """ retrieves the number of each objects by type"""
    todos = {
        'states': State, 'users': User, 'amenities':
            Amenity, 'cities': City, 'places': Place, 'reviews': Review}
    for key in todos:
        todos[key] = storage.count(todos[key])
    return jsonify(todos)