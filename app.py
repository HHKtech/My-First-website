from flask import Flask, render_template

app = Flask (__name__)

#  For Testing
@app.route('/index')
def my_function1():
    return render_template ('index.html')

@app.route('/')
def my_function():
    return render_template ('home.html')

@app.route('/home')
def home():
    return render_template ('home.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/membership')
def membership():
    return render_template ('membership.html')

@app.route('/signup')
def signup():
    return render_template ('Sign Up.html')

@app.route('/signin')
def signin():
    return render_template ('Sign In.html')

if __name__=='__main__':
    app.run(debug=True)