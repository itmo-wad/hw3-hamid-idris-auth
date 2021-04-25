from flask import Flask, flash, redirect, render_template, request, url_for, session



app = Flask(__name__)

app.secret_key = 'homework3'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       if request.form['password'] == 'admin':
        session['username'] =request.form['username']
        flash('You have logged in successfully')
        return redirect(url_for('home'))
       else:
        flash('Validation failed')
              
    return render_template('login.html')

@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))
  
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)