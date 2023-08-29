from flask import Blueprint, render_template, request, redirect,url_for,flash
from car_inventory.models import User,db
from car_inventory.forms import UserSignupForm


auth = Blueprint('auth', __name__, template_folder = 'auth_templates')
@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            print(email,password)

            user = User(first_name, last_name, email, password = password)
            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'user-created')

            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please Check your form')
    return render_template('signup.html', form=form)