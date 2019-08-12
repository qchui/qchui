from flask import Flask, render_template, request, url_for, redirect, session
from sqlalchemy import or_

import config
from models import User, Question, Answer
from exts import db
from decorater import login_check

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    question = Question.query.order_by(db.desc('create_time')).all()
    return render_template('index.html', question=question)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            # 保持session
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'有误'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password12 = request.form.get('password2')
        print(telephone, username, password1)

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机已注册'
        else:
            if password1 != password12:
                return u'密码不一致'
            else:
                user = User(telephone=telephone, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('index'))


@app.route('/question/', methods=['GET', 'POST'])
@login_check
def question():
    if request.method == "GET":
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        question.author_id = user_id
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    else:
        return {}


@app.route('/detail/<question_id>/')
def detail(question_id):
    question = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=question)


@app.route('/add_answer/', methods=['POST'])
@login_check
def add_answer():
    content = request.form.get('content')
    question_id = request.form.get('question_id')
    answer = Answer(content=content)
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    answer.user =user
    question = Question.query.filter(Question.id == question_id).first()
    answer.question = question
    print(answer)
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail' ,question_id=question_id))

@app.route('/search/',methods=['POST'])
def search():
    q = request.form.get('q')
    print(q)
    #或
    question=Question.query.filter(or_(Question.content.contains(q),Question.title.contains(q))).order_by(db.desc('create_time'))
    print(question)
    return render_template('index.html',question=question)


if __name__ == '__main__':
    app.run(port=8000)
