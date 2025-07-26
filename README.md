# Vaibhav Gupta - Personal Portfolio

A modern, responsive personal portfolio website built with Flask, featuring a beautiful night sky theme with frosted glass effects and smooth animations.

## 🌟 Features

- **Modern Design**: Night sky theme with animated stars and frosted glass effects
- **Responsive Layout**: Fully responsive design that works on all devices
- **Interactive Elements**: Smooth animations, hover effects, and progress bars
- **Multiple Pages**: Home, Skills, Certifications, Projects, Education, and Contact
- **Contact Form**: Functional contact form with validation
- **Smooth Navigation**: Mobile-friendly navigation with smooth scrolling

## 🚀 Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## 📋 Pages/Sections

### Home
- Landing page with animated hero section
- Quick navigation cards
- Statistics display

### Skills
- Categorized skills with progress bars
- Programming Languages, Data Science, Machine Learning, Web Development, Cloud Computing, Game Development

### Certifications
- Professional certifications with hover effects
- Completion status indicators
- Statistics overview

### Projects
- Detailed project cards with descriptions
- Technology tags
- GitHub and demo links

### Education
- Timeline-style education display
- Academic achievements
- Language proficiency

### Contact
- Contact form with validation
- Contact information
- Social media links
- Availability status

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project**
   ```bash
   # If using git
   git clone <repository-url>
   cd Portfolio
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
Portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── resume.txt            # Resume data
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── skills.html       # Skills page
│   ├── certifications.html # Certifications page
│   ├── projects.html     # Projects page
│   ├── education.html    # Education page
│   └── contact.html      # Contact page
└── static/              # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── script.js     # JavaScript functionality
```

## 🎨 Customization

### Colors
The color scheme uses dark purples, blues, and soft whites. You can modify the colors in `static/css/style.css`:

```css
/* Main gradient background */
background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533483 100%);

/* Accent colors */
--primary-color: #667eea;
--secondary-color: #764ba2;
```

### Content
- Update personal information in the HTML templates
- Modify skills, certifications, and projects in their respective template files
- Update contact information in `templates/contact.html`

### Images
- Add project images to `static/images/`
- Update image paths in the project cards

## 📱 Responsive Design

The website is fully responsive and includes:
- Mobile-first design approach
- Hamburger menu for mobile devices
- Flexible grid layouts
- Optimized typography for all screen sizes

## 🔧 Configuration

### Flask Configuration
- Debug mode is enabled for development
- Secret key should be changed for production
- Static files are served from the `static/` directory

### Contact Form
The contact form is currently set up to show a success message. To make it functional:
1. Add email service configuration
2. Update the contact route in `app.py`
3. Configure SMTP settings for email sending

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
For production deployment, consider:
1. Using a production WSGI server (Gunicorn, uWSGI)
2. Setting up a reverse proxy (Nginx)
3. Using environment variables for configuration
4. Disabling debug mode

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 About

**Vaibhav Gupta**
- Student | Tech Enthusiast
- AI Software Engineering student
- Vellore Institute of Technology
- Contact: bibhu.2005ssj@gmail.com

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📞 Support

For any questions or support, please contact:
- Email: bibhu.2005ssj@gmail.com
- LinkedIn: [Your LinkedIn]
- GitHub: [Your GitHub]

---

**Note**: This portfolio is designed to showcase technical skills and projects. Update the content with your own information before deploying. 