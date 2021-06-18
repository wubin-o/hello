from flask import Flask
from markupsafe import escape
from rondom import rondom
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

...
<html>
<head>
<title>testyyy</title>
</head>
<body>
<h1>ni shi sha bi<h1>
</body>
</html>
...

@app.route('/hello')
def hello():
    return 'Hello, World'