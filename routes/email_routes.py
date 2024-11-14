from flask import request, jsonify, Blueprint, blueprints

from kafka_settings.producer import produce

email_blueprint = blueprints.Blueprint('email',__name__)

@email_blueprint.route("/", methods=['POST'])
def email_route():
    data = request.json
    produce(
        'all_messages',
        data['email'],
        data
    )
    return jsonify("email received"), 200
