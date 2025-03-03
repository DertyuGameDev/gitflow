from flask import Flask, render_template, redirect

from loginform import LoginForm

app = Flask(__name__)


@app.route('/training/<prof>')
def tr(prof):
    return render_template('base1.html', prof=prof)


@app.route('/list_prof/<list1>')
def li(list1):
    items = [str(i) * 10 for i in range(10)]
    return render_template('list.html', list=list1, items=items)


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def login():
    param = {'title': 2}
    for i in 'title surname name education profession sex motivation ready'.split():
        param[i] = 1
    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
