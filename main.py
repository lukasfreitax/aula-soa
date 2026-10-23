from flask import Flask
from database import engine, Base
from controller.veiculo_controller import veiculo_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(veiculo_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(port=9000, debug=True)
    
    