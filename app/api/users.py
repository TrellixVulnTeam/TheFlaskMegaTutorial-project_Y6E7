from app.api import bp

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

@bp.route('/users', method=['GET'])
def get_users():
    pass
@bp.route('/users/<int:id>/followed', method=['GET'])
def get_followed(id):
    pass

@bp.route('/users', method=['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', method=['PUT'])
def update_user(id):
    pass