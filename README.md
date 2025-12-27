# Recipe Community

A modern, animated Django web application for sharing and discovering recipes. Features a sleek neumorphic UI design with dark theme and smooth animations.

## Features

- **User Authentication**: Register, login, and manage user profiles
- **Recipe Management**: Create, view, edit, and delete recipes
- **Photo Support**: Add recipe photos via URL links
- **Comments & Ratings**: Interact with recipes through comments and star ratings
- **Search Functionality**: Search recipes by title or ingredients
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Neumorphic design with smooth animations and dark theme

## Tech Stack

- **Backend**: Django 5.1.5
- **Frontend**: HTML, Tailwind CSS, Custom CSS animations
- **Database**: SQLite (default)
- **Styling**: Neumorphic design with glass morphism effects

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd recipe_community
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

### User Registration & Login
- Register a new account or login with existing credentials
- Access your profile to edit information and manage your recipes

### Creating Recipes
- Click "Add Recipe" to create new recipes
- Include title, ingredients, instructions, and photo URL
- Photos are added via direct URL links (no file uploads)

### Browsing Recipes
- View all recipes on the recipes page
- Use search to find specific recipes
- Click on any recipe to view details, comments, and ratings

### Interacting with Recipes
- Leave comments on recipe detail pages
- Rate recipes with 1-5 stars
- Edit or delete your own recipes from your profile

## Project Structure

```
recipe_community/
├── recipe_community/          # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── recipes/                   # Main app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── forms.py              # Form definitions
│   ├── urls.py               # URL patterns
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS files
│   └── migrations/           # Database migrations
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── README.md                 # This file
```

## Key Features Explained

### Neumorphic Design
The application uses neumorphism - a modern design trend that creates soft, tactile elements using subtle shadows instead of traditional borders. This gives buttons and cards a "pressed" or "elevated" appearance.

### Animations
- Page load fade-ins
- Hover effects on interactive elements
- Smooth transitions throughout the UI
- Staggered animations for content lists

### Dark Theme
- Consistent dark color scheme (grays, blacks, whites)
- High contrast for readability
- Modern aesthetic suitable for extended use

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue on the GitHub repository.
