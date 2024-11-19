from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the 'hello' endpoint
@app.route('/hello', methods=['GET'])
def hello():
    """
    Endpoint to greet the cyber range training participants.
    :return: JSON response with a greeting message
    """
    return jsonify({
        "message": "Hello, welcome to our cyber range training!"
    }), 200

# Main entry point of the application
if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000, debug=True)
