from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from flash_model import database, save_database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', questions=database)

@app.route("/question/<int:index>")
def question(index):
    try:
        return render_template('questionnaire.html', card=database[index], count=index, max_count=len(database)-1)
    except IndexError:
        abort(404)

@app.route("/all_questions")
def all_questions():
    return render_template('all_questions.html', card=database)

@app.route("/api/all_questions")
def api_questions():
    return jsonify(database)

@app.route("/api/question/<int:index>")
def api_question(index):
    try:
        return database[index]
    except:
        abort(404)

@app.route("/add_question", methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question = {"Question":request.form['question'], "Answer":request.form['answer']}
        database.append(question)
        save_database("flash.json")
        return redirect(url_for('question', index=len(database)-1))
    else:
        return render_template('add_question.html')

@app.route("/del_question/<int:index>", methods=['GET', 'POST'])
def del_question(index):
    if request.method == 'POST':
        try:
            del database[index]
            save_database("flash.json")
            return redirect(url_for('all_questions'))
        except IndexError:
            abort(404)
        
    else:
        return render_template('del_question.html', question=database[index])