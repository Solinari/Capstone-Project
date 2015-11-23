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

        if button == 'Animator': 

            tree = majorAnimator()
            return render_template("form.html",tree=tree)

        elif button == 'TechArtist':

            tree = majorTechnicalArtist()
            return render_template("form.html",tree=tree)
			
        elif button == 'BusinessIT':

            tree = majorBusinessIT()
            return render_template("form.html",tree=tree)

        elif button == 'Production':

            tree = majorProduction()
            return render_template("form.html",tree=tree)

			
        elif button == 'PostProduction':

            tree = majorPostProduction()
            return render_template("form.html",tree=tree)

        elif button == "Sound":

            tree = majorSound()
            return render_template("form.html",tree=tree)

        ##majorComputationalFinance()
        elif button == "ComputationalFinance":

            tree = majorComputationalFinance()
            return render_template("form.html",tree=tree)

        ##majorComputerGameDev()
        elif button == "ComputerGameDev":

            tree = majorComputationalFinance()
            return render_template("form.html",tree=tree)


        ##majorComputerScience()
        elif button == "ComputerScience":

            tree = majorComputerScience()
            return render_template("form.html",tree=tree)

        ##majorComputerSecurity()
        elif button == "ComputerSecurity":

            tree = majorComputerSecurity()
            return render_template("form.html",tree=tree)

        ##majorGovtRiskMgmtCompl()
        elif button == "GovtRiskMgmtCompl":

            tree = majorGovtRiskMgmtCompl()
            return render_template("form.html",tree=tree)

        ##majorNetworkSecurity()
        elif button == "NetworkSecurity":

            tree = majorNetworkSecurity()
            return render_template("form.html",tree=tree)

        ##majorMediaArts()
        elif button == "MediaArts":

            tree = majorMediaArts()
            return render_template("form.html",tree=tree)

        ##majorECommerceTech()
        elif button == "ECommerceTech":

            tree = majorECommerceTech()
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


