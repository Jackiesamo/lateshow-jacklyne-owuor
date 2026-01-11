from flask import request, jsonify
from config import create_app
from models import db, Episode, Guest, Appearance

app = create_app()

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes]), 200

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "episode_id": a.episode_id,
                "guest_id": a.guest_id,
                "guest": a.guest.to_dict()
            }
            for a in episode.appearances
        ]
    }), 200

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests]), 200

