from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def tr(prof):
    return render_template('base.html', prof=prof)

@app.route('/list_prof/<list1>')
def li(list1):
    items = [str(i) * 10 for i in range(10)]
    return render_template('list.html', list=list1, items=items)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
