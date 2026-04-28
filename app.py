"""
app.py - Main entry point

This is the main application file that starts the Flask server.
It registers the API routes and configures the application.
"""
from database import init_db

from flask import Flask, jsonify

from routes import tasks_bp


def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__)
    
    init_db()
    
    # Configure the app
    app.config["JSON_SORT_KEYS"] = False
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    
    # Register the tasks blueprint
    # This connects all the routes from routes.py
    app.register_blueprint(tasks_bp)
    
    # Add a root route to verify the API is running
    @app.route("/")
    def index():
        return jsonify({
            "message": "Task API is running",
            "endpoints": {
                "GET /tasks": "Get all tasks",
                "GET /tasks/<id>": "Get a specific task",
                "POST /tasks": "Create a new task",
                "PUT /tasks/<id>": "Update a task",
                "DELETE /tasks/<id>": "Delete a task",
                "PATCH /tasks/<id>/complete": "Mark task as completed"
            }
        }), 200
    
    # Error handlers for common HTTP errors
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 Not Found errors."""
        return jsonify({"error": "Resource not found"}), 404
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        """Handle 405 Method Not Allowed errors."""
        return jsonify({"error": "Method not allowed"}), 405
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 Internal Server errors."""
        return jsonify({"error": "Internal server error"}), 500
    
    return app


# Create the app instance
app = create_app()


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)