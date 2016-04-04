import os
import shutil
from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = 'pL1+Pl0HJYRaJC7OQp6QxX7yaq90MwxFpqKBNy4hLwY='

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['zip'])

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Admin only area!')
            return redirect(url_for('index'))
    return wrap
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')
    
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
    
@app.route('/control')
@login_required
def control():
    savegames_path = app.config['UPLOAD_FOLDER'] + "savegames"
    mods_path = app.config['UPLOAD_FOLDER'] + "mods"
    all_savegames = os.listdir(savegames_path)
    all_mods = os.listdir(mods_path)
    for file in os.listdir(mods_path):
        if file.endswith(".zip"):
            all_zipped = []
            all_zipped.append(file)
    return render_template('control.html', all_savegames = all_savegames, all_mods = all_mods, all_zipped = all_zipped)
    
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

# Route that will process the file upload
@app.route('/uploadSavegame', methods=['POST'])
def uploadSave():
    file = request.files['savegame']
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/savegames", file.filename))
        #return redirect(url_for('uploaded_file', filename = file.filename))
        return redirect(url_for('control'))
    else:
        error = "Invalid file type"
        return redirect(url_for('control', error = error))
    
@app.route('/uploadMods', methods=['GET', 'POST'])
def uploadMod():
    file = request.files['mod']
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/mods", file.filename))
        #return redirect(url_for('uploaded_file', filename = file.filename))
        return redirect(url_for('control'))
    else:
        error = "Invalid file type"
        return redirect(url_for('control', error = error))

@app.route('/deleteSaves/<savegame>')
def deleteSave(savegame):
    os.remove(app.config['UPLOAD_FOLDER'] + "savegames/" + savegame)
    return redirect(url_for('control'))
    
@app.route('/deleteMods/<mod>')
def deleteMod(mod):
    os.remove(app.config['UPLOAD_FOLDER'] + "mods/" + mod)
    return redirect(url_for('control'))
    
@app.route('/deleteModFolder/<mod_folder>')
def deleteFolder(mod_folder):
    shutil.rmtree(app.config['UPLOAD_FOLDER'] + "mods/" + mod_folder)
    return redirect(url_for('control'))

# if wants to download
"""
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
"""

app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug = True)

if __name__ == '__main__':
    app.run()
