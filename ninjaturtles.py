from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninja/<notapril>')
def notApril(notapril):
    if notapril == 'blue':
        return render_template('blue.html')
    if notapril == 'orange':
        return render_template('orange.html')
    if notapril == 'red':
        return render_template('red.html')
    if notapril == 'purple':
        return render_template('purple.html')
    return render_template('notapril.html')
app.run(debug=True)