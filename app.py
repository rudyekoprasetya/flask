from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

# fungsi perkalian
def perkalian():
    angka1 = request.form['angka1']
    angka2 = request.form['angka2']
    hasil_kali = int(angka1) * int(angka2)
    return render_template('calc.html',title='calculator Page', result=hasil_kali)

def do_upload():
    file = request.files['filesaya']
    file.save(f"uploads/{secure_filename(file.filename)}")
    return render_template('upload.html', title='Upload File', hasil='berhasil upload') 

# index 
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# parameter url text
@app.route('/user/<username>')
def show_user(username):
    return f'User {escape(username)}'

# parameter url int
@app.route('/id/<int:post_id>')
def show_id(post_id):
    return f'Post ID {post_id}'

# page about
@app.route('/about')
def about():
    return "<h1>Page About</h1>"

#page render
@app.route('/render/<name>')
def render_html(name=None):
    return render_template('hello.html',person=name)

#page calculator
@app.route('/calculator', methods=['GET', 'POST'])
def show_calc(hasil=0):
    if request.method == 'GET':
        return render_template('calc.html',title='calculator Page', result=hasil)
    else:
        return perkalian()
    
# upload file 
@app.route('/upload', methods=['GET','POST'])
def show_upload():
    if request.method == 'GET':
        return render_template('upload.html', title='Upload File', hasil='belum upload')
    else:
        return do_upload()