from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return render_template("base.html", title="Главная")


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('astronaut_selection.html', title='Регистрация')
    elif request.method == 'POST':
        param = {}
        param['surname'] = request.form['surname']
        param['name'] = request.form['name']
        param['email'] = request.form['email']
        param['education'] = request.form['education']
        param['prof1'] = request.form['prof1']
        param['prof2'] = request.form['prof2']
        param['prof3'] = request.form['prof3']
        param['sex'] = request.form['sex']
        param['about'] = request.form['about']
        param['accept'] = request.form['accept']
        return render_template('success.html', data=param, title="Успешно")


@app.route("/success")
def success():
    return render_template("success.html", title="Успешно")
    

def main():
    app.run(port=5005)


if __name__ == '__main__':
    main()
