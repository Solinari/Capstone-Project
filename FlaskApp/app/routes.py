from flask import Flask, render_template, request
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from PandaTree import *
# Why this works: https://docs.python.org/2/tutorial/modules.html

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()]) 
  
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')

def test(var):
    '''print var!'''
    return "You pushed: {}!".format(var)

@app.route("/form", methods = ["GET", "POST"])
def form(tree=None):


    if request.method == "POST":


        button = request.form['choice1'] #this retrieves which radio button was pressed
        # print("\n\nBUTTONBUTTONBUTTON")
        # print(button)
        # print("BUTTONBUTTONBUTTON")

        if button == 'Animator': #if the button with attribute value = "A' is pressed

                #what you want to do when button A is pressed
            tree = majorAnimator()
            # print("TREETREETREE")
            # print(tree)
            # print("$TREETREETREE")

            # put a dict to list processor? make elements to return?  
            
            return render_template("form.html",tree=tree)

        elif button == 'TechArtist':
                #what you want to do when button B is pressed
            tree = majorTechnicalArtist()
			return render_template("form.html",tree=tree)
			
        elif button == 'BusinessIT':
                #what you want to do when button C is pressed
			tree = majorBusinessIT()
            return render_template("form.html",tree=tree)
       
	   elif button == 'Production':
                #what you want to do when button C is pressed
			tree = majorProduction()
            return render_template("form.html",tree=tree)
			
        elif button == 'PostProduction':
                #what you want to do when button C is pressed
			tree = majorPostProduction()
            return render_template("form.html",tree=tree)
		
		elif button == "Sound"
		
		tree = majorSound()
		return render_template("form.html",tree=tree)

    
    return render_template("form.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)




if __name__ == '__main__':
  app.run(debug=True)


