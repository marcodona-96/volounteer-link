# VolunteerLink App

VolunteerLink is a platform to connect volunteers and organizations. Volunteers can create profiles to showcase their skills and availability, while organizations can create profiles to post their needs and missions.

## Project Structure

volunteerlink_project/
├── app/                                # Main app folder containing all application-related files
│   ├── __init__.py                     # Initialization of the app, setting up configurations and extensions
│   ├── models.py                       # Database models for Volunteer and Association profiles
│   ├── forms.py                        # Forms used for profile creation (Volunteer and Association)
│   ├── routes.py                       # Routes that handle user navigation and form submissions
│   ├── static/                         # Folder for static files like CSS, images, JS
│   │   └── styles.css                  # Main stylesheet for the application
│   └── templates/                      # Folder for HTML templates
│       ├── home.html                   # Homepage template
│       ├── volunteer_profile.html      # Volunteer profile creation page template
│       └── association_profile.html    # Association profile creation page template
├── config.py                           # Configuration settings for the app (database, secrets, etc.)
├── .env                                # Environment variables file (database URI, secret key)
├── run.py                              # Entry point to run the app
├── .gitignore                          # Git ignore file to exclude unnecessary files
└── README.md                           # Documentation for the project

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- python-dotenv (for environment variable management)

You can install these dependencies by running:

pip install -r requirements.txt

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/volunteerlink.git

2. Navigate into the project folder:

cd volunteerlink

3. Install the dependencies:

pip install -r requirements.txt

4. Set up the environment variables:
   - Create a `.env` file in the root of the project.
   - Add the following content:

FLASK_APP=run.py FLASK_ENV=development SECRET_KEY=your_secret_key_here SQLALCHEMY_DATABASE_URI=sqlite:///app.db

5. Initialize the database:

flask db init flask db migrate flask db upgrade

6. Run the app:

python run.py

The app will be accessible at `http://127.0.0.1:5000/`.

## Folder Structure

- **app/**: This is the main application folder that contains all the app-specific files.
  - **__init__.py**: Initializes the app, configures the database, and sets up login functionality.
  - **models.py**: Contains the database models for `VolunteerProfile` and `AssociationProfile`.
  - **forms.py**: Contains the forms for creating Volunteer and Association profiles.
  - **routes.py**: Defines the routes and their associated functions.
  - **static/**: This folder contains static files like CSS files.
  - **templates/**: This folder contains HTML templates for various pages in the app.
- **config.py**: Configuration file containing app settings like database URI and secret key.
- **.env**: Contains environment-specific variables like database URI and the secret key.
- **run.py**: Entry point for running the app. It initializes and starts the Flask server.
- **.gitignore**: Git ignore file to exclude unnecessary files from being tracked by Git.
- **README.md**: This file.

## File Descriptions

### `config.py`
Contains configuration settings for the Flask app, including:
- **SQLALCHEMY_DATABASE_URI**: The URI for connecting to the database.
- **SQLALCHEMY_TRACK_MODIFICATIONS**: Disables Flask-SQLAlchemy's modification tracking.
- **SECRET_KEY**: A key used to secure session data.