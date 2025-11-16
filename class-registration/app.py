from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #creates a Flask instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #sets the database address
db = SQLAlchemy(app) #initializes the database

if __name__ == "__main__": #run the Flask instance if the current module is "main"
    app.run()

class class_Config(db.Model):
    crn = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    #class_name = db.Column(db.String(200), nullable = False)
    #teacher_name = db.Column(db.String(200), nullable = False)
    #days_time = db.Column(db.String(200), nullable = False)

with app.app_context():
    db.create_all()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = class_Config(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding the task"
    else:
        tasks = class_Config.query.order_by(class_Config.crn).all()
        return render_template('index.html', tasks = tasks)

        
