from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('HomePage.Html')

@app.route('/gameselect')
def gameselect():
    return render_template('HomePage.Html')

@app.route('/pacman')
def pacman():
    return render_template('Pacman.html')

@app.route('/2048')
def game2048():
    return render_template('2048.html')

@app.route('/tictactoe')
def tictactoe():
    return render_template('Tic-Tac-Toenails.html')

@app.route('/memory')
def memory():
    return render_template('PatternMemoryGame.html')

@app.route('/cardmatch')
def cardmatch():
    return render_template('CardMatching.html')

@app.route('/ballmatch')
def ballmatch():
    return render_template('BallMatch.html')

if __name__ == '__main__':
    app.run(debug=True)