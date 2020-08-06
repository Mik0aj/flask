from flask import Flask, render_template, url_for
app = Flask(__name__)
posts=[{
	'title':'post 1',
	'date':'20.05.2020',
	'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ac.'	
},{
	'title':'post 2',
	'date':'24.06.2020',
	'content':'Etiam auctor arcu nibh, a rhoncus orci pharetra non. Nullam.'	
}]


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/index')
def index():
    return 'index'



if __name__ == '__main__':
	app.run(debug=True)