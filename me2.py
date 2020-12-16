from flask import Flask,render_template,url_for
 
W = Flask(__name__)
@W.route('/')
def index():
  return render_template('index.html')

W.run()


