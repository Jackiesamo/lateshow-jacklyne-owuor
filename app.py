
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


# SERIALIZE FUNCTIONS


def episode_to_dict(episode, include_appearances=False):
    data = {
        "id": episode.id,
        "date": episode.date,
        "number": episode.number
    }
    if include_appearances:
        data["appearances"] = [
            {
                "id": a.id,
                "rating": a.rating,
                "guest_id": a.guest.id,
                "episode_id": a.episode.id,
                "guest": {
                    "id": a.guest.id,
                    "name": a.guest.name,
                    "occupation": a.guest.occupation
                }
            } for a in episode.appearances
        ]
    return data

def guest_to_dict(guest):
    return {
        "id": guest.id,
        "name": guest.name,
        "occupation": guest.occupation
    }

def appearance_to_dict(appearance):
    return {
        "id": appearance.id,
        "rating": appearance.rating,
        "episode_id": appearance.episode.id,
        "guest_id": appearance.guest.id,
        "episode": {
            "id": appearance.episode.id,
            "date": appearance.episode.date,
            "number": appearance.episode.number
        },
        "guest": {
            "id": appearance.guest.id,
            "name": appearance.guest.name,
            "occupation": appearance.guest.occupation
        }
    }


# ROUTES


# GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode_to_dict(e) for e in episodes]), 200

# GET /episodes/:id
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode_to_dict(episode, include_appearances=True)), 200

# GET /guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest_to_dict(g) for g in guests]), 200

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    rating = data.get("rating")
    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")

    # Validate
    errors = []
    if not rating or not isinstance(rating, int) or not (1 <= rating <= 5):
        errors.append("rating must be between 1 and 5")
    if not episode_id or not Episode.query.get(episode_id):
        errors.append("episode_id must exist")
    if not guest_id or not Guest.query.get(guest_id):
        errors.append("guest_id must exist")

    if errors:
        return jsonify({"errors": errors}), 400

    # Create appearance
    appearance = Appearance(rating=rating,
                            episode_id=episode_id,
                            guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify(appearance_to_dict(appearance)), 201



if __name__ == '__main__':
    app.run(debug=True)
