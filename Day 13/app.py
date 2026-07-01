from flask import Flask
from routes.routes import generate_routes

app = Flask(__name__)

generate_routes(app)

if __name__ == "__main__":
    app.run(debug=True)