from flask import Flask, jsonify, request
from service import PokemonService
from authn import requires_auth, initialize_jwt, login
from config import Config
import logging

# Initialize Flask app and Pokemon service
app = Flask(__name__)
app.config.from_object(Config)
pokemon_service = PokemonService()

# Initialize JWT with the app
initialize_jwt(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/login', methods=['POST'])
def login_user():
    return login()


@app.route('/pokemon/count', methods=['GET'])
@requires_auth
def get_number_of_pokemon():
    try:
        logger.info("Received request for number of Pokemon")
        num_pokemon = pokemon_service.get_number_of_pokemon()
        return jsonify({"count": num_pokemon}), 200
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon/types', methods=['GET'])
@requires_auth
def get_pokemon_types():
    try:
        logger.info("Received request for Pokemon types")
        types = pokemon_service.get_pokemon_types()
        return jsonify({"types": types}), 200
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon', methods=['GET'])
@requires_auth
def get_pokemon_data():
    try:
        logger.info("Received request for all Pokemon data")
        return jsonify(pokemon_service.get_pokemon_data()), 200
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon/type/<name>', methods=['GET'])
@requires_auth
def get_pokemon_type(name):
    try:
        logger.info(f"Received request for Pokemon type: {name}")
        pokemon_type = pokemon_service.get_pokemon_type(name)
        return jsonify({"type": pokemon_type}), 200
    except ValueError as e:
        logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon/random', methods=['GET'])
@requires_auth
def get_random_pokemon():
    try:
        poke_type = request.args.get('type')
        logger.info(f"Received request for random Pokemon of type: {poke_type}")
        pokemon = pokemon_service.get_random_pokemon_by_type(poke_type)
        return jsonify({"name": pokemon["name"], "type": pokemon["type"]}), 200
    except ValueError as e:
        logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon/shortest-name', methods=['GET'])
@requires_auth
def get_pokemon_with_shortest_name():
    try:
        poke_type = request.args.get('type')
        logger.info(f"Received request for Pokemon with shortest name of type: {poke_type}")
        pokemon = pokemon_service.get_pokemon_with_shortest_name(poke_type)
        return jsonify({"name": pokemon["name"], "type": pokemon["type"]}), 200
    except ValueError as e:
        logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon/longest-name', methods=['GET'])
@requires_auth
def get_pokemon_with_longest_name():
    try:
        poke_type = request.args.get('type')
        logger.info(f"Received request for Pokemon with longest name of type: {poke_type}")
        pokemon = pokemon_service.get_pokemon_with_longest_name(poke_type)
        return jsonify({"name": pokemon["name"], "type": pokemon["type"]}), 200
    except ValueError as e:
        logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/pokemon/names/<poke_type>', methods=['GET'])
@requires_auth
def get_pokemon_names_by_type(poke_type):
    try:
        logger.info(f"Received request for names of all Pokemon of type: {poke_type}")
        pokemon_names = pokemon_service.get_pokemon_names_by_type(poke_type)
        return jsonify({"type": poke_type, "names": pokemon_names}), 200
    except ValueError as e:
        logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
