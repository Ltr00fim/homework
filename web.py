from main import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html', candidates=load_candidates('candidates.json'))


@app.route('/candidates/<id>/')
def candidate(id):
    if 1 <= int(id) <= len(load_candidates('candidates.json')):
        return render_template('candidate.html', candidate=get_by_pk(int(id)))
    else:
        return render_template('none.html')


@app.route('/skills/<skill>/')
def candidate_skill(skill):
    return render_template('skills.html', candidates=get_by_skill(skill))


if __name__ == "__main__":
    app.run(debug=True)
