from flask import Flask, request, jsonify
from models import EC2Instance, EC2InstanceConfig

app = Flask(__name__)

@app.route("/instances", methods=["GET"])
def get_instances():
    """
    Get all instances.
    """
    # Implementation details

@app.route("/instances", methods=["POST"])
def create_instance():
    """
    Create a new instance.
    """
    # Implementation details

@app.route("/instances/<id>", methods=["GET"])
def get_instance(id):
    """
    Get an instance by ID.
    """
    # Implementation details
