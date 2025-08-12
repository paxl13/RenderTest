import os
from flask import Flask, render_template, request, redirect, url_for, flash
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Initialize Supabase client
supabase_url = os.environ.get('SUPABASE_URL')
supabase_key = os.environ.get('SUPABASE_KEY')

if not supabase_url or not supabase_key:
    raise ValueError('SUPABASE_URL and SUPABASE_KEY must be set in environment variables')

supabase: Client = create_client(supabase_url, supabase_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        category = request.form.get('category')
        notes = request.form.get('notes')
        
        # Insert data into Supabase
        result = supabase.table('mytable').insert({
            'name': name,
            'email': email,
            'phone': phone,
            'compagny': company,  # Note: using 'compagny' to match schema
            'category': category,
            'notes': notes
        }).execute()
        
        if result.data:
            return render_template('index.html', success=True)
        else:
            return render_template('index.html', error='Failed to save data')
            
    except Exception as e:
        print(f"Error saving to database: {e}")
        return render_template('index.html', error='Database error occurred')

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'App is running'}

@app.route('/api/data')
def get_data():
    return {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
        ],
        'total': 2,
        'timestamp': '2025-01-01T12:00:00Z'
    }

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)