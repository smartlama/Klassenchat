from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = []
next_message_id = 1

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_message_id
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        text = request.form.get('text', '').strip()
        if username and text:
            messages.append({
                'message_id': next_message_id,
                'username': username[:40],
                'text': text[:500],
                'timestamp': datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            })
            next_message_id += 1
        return redirect(url_for('index'))
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
