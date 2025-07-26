from flask import Flask, render_template, request, redirect, url_for, flash
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

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just flash a success message
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 