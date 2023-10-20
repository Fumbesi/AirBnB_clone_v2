from models import storage
from flask import Flask, render_template

app = Flask(__name)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of states."""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
