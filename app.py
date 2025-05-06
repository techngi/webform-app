
from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
<!DOCTYPE html>
<html>
<head><title>Simple Web Form</title></head>
<body>
  <h2>Enter your details</h2>
  <form method="post">
    Name: <input type="text" name="name"><br><br>
    Phone: <input type="text" name="phone"><br><br>
    Email: <input type="email" name="email"><br><br>
    <input type="submit" value="Submit">
  </form>
  {% if submitted %}
  <h3>Thanks, {{ name }}! Your data has been received.</h3>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        print(f"Received: Name={name}, Phone={phone}, Email={email}")
        return render_template_string(form_html, submitted=True, name=name)
    return render_template_string(form_html, submitted=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
