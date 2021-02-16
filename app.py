from flask import Flask
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = """
    <h3>Cloud DevOps Engineer Captone project</h3>
    <p>
    <ul>
    <li>This project demonstrates automatic update capabilities of CICD pipeline. </li> <br />
    <li>Every change of the main branch of the github repository will triger the update of this application. </li> <br />
    <li>The infrastructure as code starts a Kubernetes cluster on AWS that the app is running in. </li> <br />
    <li>Code linting and automated tests are performed before any update takes place. </li> <br /> 
    <ul>
    <br /> 
    Source code: <br />
    <a href="https://github.com/gajdulj/ml-microservice-kubernetes">Cloud DevOps Enigneer capstone</a>
    </p>
    Jakub Gajdul, 2021
    """
    return html.format(format)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
