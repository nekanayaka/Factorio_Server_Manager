"""
Programmer: Nimna Ekanayaka
Date: April 4, 2016
Purpose: Factorio server manager and user interface
"""
import os
import shutil
import zipfile
import glob
import subprocess
import commands
import shlex
import re
from os.path import *
from flask import *
from functools import wraps
from subprocess import *

app = Flask(__name__)

app.secret_key = 'pL1+Pl0HJYRaJC7OQp6QxX7yaq90MwxFpqKBNy4hLwY='

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['zip'])

# wrapper that requires admin users to be logged in
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Admin only area!')
            # error = "Admin only area!"
            return redirect(url_for('index'))
    return wrap

# checks the uploaded files extention
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

"""
def get_directories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
"""
# if logged in the admin login link disappear from the page
@app.route('/')
def index():
    if 'logged_in' in session:
        login_status = True
    else:
        login_status = False

    system_output = commands.getstatusoutput("grep username ~/factorio/factorio-current.log")
    system_output_grep = commands.getstatusoutput("grep 'success(true)' ~/factorio/factorio-current.log | grep removing | grep network | awk '{print $6}'")
    #game_status = re.findall(r"'(.*?)'", system_output, re.DOTALL)
    #system_output = "{}".format(system_output)
    #game_status = system_output[system_output.find("'")+1:system_output.find("'")]
    #print system_output_grep
    removed_peers_array_dump = system_output_grep[1].split()
    system_output_array_dump = system_output[1].split()
    # print removed_peers_array_dump[0]
    #username_peer_dump = system_output[1]
    #print str(username_peer_dump_array).strip('[]')
    global username_and_peer_array_dump
    username_and_peer_array_dump = []
    for word in system_output_array_dump:
            if(word.startswith('username') == True):
                    word_index = system_output_array_dump.index(word)
                    #peer.append()
                    username_and_peer_array_dump.extend([word, system_output_array_dump[word_index - 1]])
    # print str(username_and_peer_array_dump).strip('[]')
    global removed_users
    removed_users = []
    global removed_peers
    removed_peers = []
    for peer in removed_peers_array_dump:
        if (peer in username_and_peer_array_dump):
            removed_peers.append(peer)
    #print removed_peers
    
    for index, user in enumerate(username_and_peer_array_dump):
        # print index, user
        if(user in removed_peers):
            removed_users.append(username_and_peer_array_dump[index - 1])
    print removed_users
        
    # removed_users = (removed_peers == str(removed_peers_array_dump).strip('[]') for removed_peers in str(username_and_peer_array_dump).strip('[]'))
    # for value in g:
        # print value
    # print str(removed_users).strip('[]')
    
    # raise
    #print removed_peers_array_dump
    # print len(removed_peers_array_dump)
    
    #print str(removed_users).strip('[]')
    #       print word
    #for xpeer in peer:
    #       print xpeer
    #print system_output[1]
    #print system_output[1].find("peer(")
    return render_template('index.html', login_status = login_status)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginSubmit', methods=['POST'])
def loginSubmit():
    if request.form['username'] == 'admin' and request.form['password'] == 'opensesame':
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
    all_folders = os.walk(mods_path).next()[1]
    """
    for file in os.listdir(mods_path):
        if file.endswith(".zip"):
            all_mods = []
            all_mods.append(file)
    """
    all_zipped = glob.glob(mods_path + '/*.zip')
    all_mods = [basename(mod_zip) for mod_zip in all_zipped]
    #cmd = shlex.split("ps aux | grep factorio/bin/x64 | grep -v grep | awk '{print $2}'")
    system_output = commands.getstatusoutput("ps aux | grep factorio/bin/x64 | grep -v grep | awk '{print $2}'")
    # print cmd
    # game_status = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    # game_status = subprocess.Popen(['ps', 'aux', '|', 'grep', 'factorio/bin/x64', '|', 'grep', '-v', 'grep', '|', 'awk', '\'{print $2}\''], stdout=subprocess.PIPE).communicate()[0]
    game_status = system_output[1]
    print game_status
    # if game_status != "(0, '')":
    #     return render_template('control.html', all_savegames = all_savegames, all_folders = all_folders, all_mods = all_mods, game_status = game_status)
    # else:
    #     return render_template('control.html', all_savegames = all_savegames, all_folders = all_folders, all_mods = all_mods)
    return render_template('control.html', all_savegames = all_savegames, all_folders = all_folders, all_mods = all_mods, game_status = game_status)
    # return render_template('control.html', all_savegames = all_savegames, all_folders = all_folders, all_mods = all_mods)


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
        # error = "Invalid file type"
        flash("Invalid file type")
        return redirect(url_for('control'))

@app.route('/uploadMods', methods=['GET', 'POST'])
def uploadMod():
    file = request.files['mod']
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] + "/mods", file.filename))
        #return redirect(url_for('uploaded_file', filename = file.filename))
        return redirect(url_for('control'))
    else:
        # error = "Invalid file type!"
        flash("Invalid file type")
        return redirect(url_for('control'))

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

@app.route('/extractArchive/<zipFile>')
def extractArchive(zipFile):
    file_unzip = zipfile.ZipFile(app.config['UPLOAD_FOLDER'] + "mods/" + zipFile, 'r')
    file_unzip.extractall(app.config['UPLOAD_FOLDER'] + "mods/")
    file_unzip.close()
    return redirect(url_for('control'))

@app.route('/runGame/<savegame>')
def runGame(savegame):
    os.system('~/factorio/bin/x64/./factorio --disallow-commands --start-server ' + savegame + "&")
    return redirect(url_for('control'))

@app.route('/stopGame')
def stopGame():
    #works for multiple running instances of factorio. just has to grep the unique the factorio directory path
    os.system("kill -9 `ps aux | grep factorio/bin/x64 | grep -v grep | awk '{print $2}'`")
    #print("kill -9 `ps aux | grep " +  savegame_running + " | grep -v grep | awk '{print $2}'`")
    #works if only one version of factorio running
    #os.system("kill -9 pidof factorio")
    return redirect(url_for('control'))

# if wants to download
"""
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
"""

app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)), debug = True)

if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0')
