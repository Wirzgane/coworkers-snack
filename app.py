from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://snack_user:snack_password@db:5432/snack_db'
db = SQLAlchemy(app)

class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    votes = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<Snack {self.name}>'

# Ensure that the table is created when the application starts
with app.app_context():
    db.create_all()

# Route to handle the form submission for adding a new snack
@app.route('/add_snack', methods=['POST'])
def add_snack():
    name = request.form.get('name')
    new_snack = Snack(name=name, votes=0)
    db.session.add(new_snack)
    db.session.commit()
    return redirect(url_for('index'))

# Route to display snacks ordered by most votes
@app.route('/')
def index():
    snacks = Snack.query.order_by(Snack.votes.desc()).all()
    return render_template('index.html', snacks=snacks)

# Define the route to vote for a snack
@app.route('/vote/<int:id>', methods=['POST'])
def vote(id):
    snack = Snack.query.get_or_404(id)
    snack.votes += 1
    db.session.commit()
    return redirect(url_for('index'))

# Route to handle the form submission for deleting a snack
@app.route('/delete_snack/<int:id>', methods=['POST'])
def delete_snack(id):
    snack = Snack.query.get_or_404(id)
    db.session.delete(snack)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
