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

class TreeForm(Form, inTree):
    '''represent the output of a tree to be rendered'''
    # maybe im misisng something with this.
    # the idea is to set the result of the tree to a field here
    # and then render it as a form
    tree = inTree

  
app = Flask(__name__)
  
@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')



@app.route("/form", methods = ["GET", "POST"])
def form():

    button = request.form.get('choice1', None) #this retrieves which radio button was pressed

    if request.method == "POST":       

        if button == 'Animator': #if the button with attribute value = "A' is pressed

                #what you want to do when button A is pressed
            tree = PandaTree.majorAnimator()
            form = TreeForm(request.form, tree)
            return render_template("form.html",form=form)

        elif button == 'B':
                #what you want to do when button B is pressed
            pass
        elif button == 'C':
                #what you want to do when button C is pressed
            pass
        elif button == 'D':
                #what you want to do when button D is pressed
            pass
        elif button == 'E':
                #what you want to do when button E is pressed
            pass

    elif request.method == "GET":
        return render_template("form.html", button=button)

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


