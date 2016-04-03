import os
from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = 'pL1+Pl0HJYRaJC7OQp6QxX7yaq90MwxFpqKBNy4hLwY='

app.config['UPLOAD_FOLDER'] = 'static/uploads/'

def login_required(test):
    wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('Admin only area!')
            return redirect(url_for('index'))
    return wrap

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/control')
@login_required
def control():
    return render_template('control.html')
    
@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/loginSubmit', methods=['POST'])
def loginSubmit():
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        session['logged_in'] = True
        return redirect(url_for('control'))
    else:
        error = "Invalid username or password"
    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

# Route that will process the file upload
@app.route('/uploadSavegame', methods=['POST'])
def uploadSave():
    file = request.files['savegame']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/savegames", file.filename))
    #return redirect(url_for('uploaded_file', filename = file.filename))
    return redirect(url_for('index'))
    
@app.route('/uploadMods', methods=['POST'])
def uploadMod():
    file = request.files['mod']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/mods", file.filename))
    #return redirect(url_for('uploaded_file', filename = file.filename))
    return redirect(url_for('index'))

# if wants to download
"""
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
"""

app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app.run(debug=True)
