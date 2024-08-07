from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':    
    app.run(debug=True)