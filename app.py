from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Flask-side fallback (if not using Formspree)
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('contact'))

        # With Formspree the form POSTs directly to Formspree's endpoint,
        # so this branch only runs if someone hits /contact POST directly.
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact') + '?sent=1')

    return render_template('contact.html')

@app.route('/download-resume')
def download_resume():
    try:
        return send_file('Resume.pdf', as_attachment=True, download_name='Vaibhav_Gupta_Resume.pdf')
    except FileNotFoundError:
        flash('Resume file not found.', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render provides the port
    app.run(host="0.0.0.0", port=port, debug=True)