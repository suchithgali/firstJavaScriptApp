from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #creates a Flask instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/suchithgali/C++ Files/CSE_108/practice/class-registration/instance/test.db' #sets the database address
db = SQLAlchemy(app) #initializes the database

class regConfig(db.Model):
    crn = db.Column(db.Integer, primary_key = True)
    class_name = db.Column(db.String(200), nullable = False)
    teacher_name = db.Column(db.String(200), nullable = False)
    days_time = db.Column(db.String(200), nullable = False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_crn = request.form['crn']
        task_class_name = request.form['course_name']
        task_teacher_name = request.form['professor']
        task_days_time = request.form['days_time']

        new_task = regConfig(crn = task_crn, class_name = task_class_name, teacher_name = task_teacher_name, days_time = task_days_time)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return "There was an error completing the task"
    else:
        tasks = regConfig.query.order_by(regConfig.crn).all()
        return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:crn>')
def delete(crn):
    task_to_delete = regConfig.query.get_or_404(crn)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an error completing the task"

@app.route('/update/<int:crn>', methods=['POST', 'GET'])
def update(crn):
    task = regConfig.query.get_or_404(crn)

    if request.method == 'POST':
        task.crn = request.form['crn']
        task.class_name = request.form['course_name']
        task.teacher_name = request.form['professor']
        task.days_time = request.form['days_time']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Unable to complete task there was an error"
    else:
        tasks = regConfig.query.order_by(regConfig.crn).all()
        return render_template('update.html', task=task)


if __name__ == "__main__": #run the Flask instance if the current module is "main"
    app.run(debug=True)
