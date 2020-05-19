from flask import Flask, render_template

app= Flask(__name__)

#index route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__==  "__main__":
    app.run(debug=True)
