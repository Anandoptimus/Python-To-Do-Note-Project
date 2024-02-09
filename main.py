from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
db = SQLAlchemy()
db.init_app(app)


class lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.String(30), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    print("hello my boy")
    query = db.session.execute(select([lists])).scalars().all()
    return render_template("index.html", all_post=query)


@app.route('/save', methods=["GET", "POST"])
def save():
    if request.method == "POST":
        query = lists(
            title=request.form.get('title'),
            description=request.form.get('description'),
            date=request.form.get('date')
        )
        db.session.add(query)
        db.session.commit()
        return redirect(url_for('home'))





if __name__ == "__main__":
    app.run(debug=True)