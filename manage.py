from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
	return 'Welcome!'


@app.route('/greetings/christmas')
def  merrychristmas():
	return 'Merry Christmas!'

@app.route('/greetings/newyear')
def  newyear():
        return 'Happy New Year!'


if __name__ == "__main__":
        app.run()
