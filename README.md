# Simple CMS with Flask and AdminLTE

A simple Content Management System (CMS) built with Flask and AdminLTE template.

## Features

- User authentication
- Admin dashboard
- Create, edit, and delete posts
- Draft and published post status
- Responsive design using AdminLTE

## Requirements

- Python 3.8 or higher
- Flask and other dependencies listed in requirements.txt

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd cms
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

5. Create an admin user:
```bash
flask shell
>>> from app import db, User
>>> admin = User(username='admin', email='admin@example.com', is_admin=True)
>>> admin.set_password('your-password')
>>> db.session.add(admin)
>>> db.session.commit()
>>> exit()
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Login with your admin credentials at `/login`
2. Access the admin dashboard at `/admin`
3. Create new posts using the "New Post" button
4. Manage your posts from the dashboard

## Project Structure

```
cms/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, JS, images)
└── templates/         # HTML templates
    ├── base.html      # Base template
    ├── index.html     # Home page
    ├── login.html     # Login page
    └── admin/         # Admin templates
        ├── dashboard.html
        └── new_post.html
```

## License

This project is licensed under the MIT License. 