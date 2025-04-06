from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from app.models import User, VolunteerProfile, AssociationProfile
from app.forms import LoginForm, RegisterForm, VolunteerProfileForm, AssociationProfileForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # Replace with hash check
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/volunteer-profile', methods=['GET', 'POST'])
def volunteer_profile():
    form = VolunteerProfileForm()
    if form.validate_on_submit():
        profile = VolunteerProfile(
            name=form.name.data,
            email=form.email.data,
            interests=form.interests.data,
            availability=form.availability.data
        )
        db.session.add(profile)
        db.session.commit()
        flash('Volunteer profile created successfully!')
        return redirect(url_for('main.home'))
    return render_template('volunteer_profile.html', form=form)

@main.route('/association-profile', methods=['GET', 'POST'])
def association_profile():
    form = AssociationProfileForm()
    if form.validate_on_submit():
        profile = AssociationProfile(
            name=form.name.data,
            email=form.email.data,
            mission=form.mission.data,
            needs=form.needs.data
        )
        db.session.add(profile)
        db.session.commit()
        flash('Association profile created successfully!')
        return redirect(url_for('main.home'))
    return render_template('association_profile.html', form=form)
