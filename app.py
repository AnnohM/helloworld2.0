from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Annoh Mienza! ' 'This is my first HTML page.'


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/favorite-course')
def favorite_course():
    print('favorite course entered:' + request.args.get('favorite_course_name'))
    print('favorite_subject entered:' + request.args.get('favorite_subject_name'))
    return render_template('favorite-course.html')


if __name__ == '__main__':
    app.run()
