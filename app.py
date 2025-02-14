from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
	<title>Course Query Form</title>
</head>
<body>
	<h2>Submit Your Query</h2>
	<form action="/submit" method="post">
	<label for="name">Name:</label>
	<input type="text" name="name" required> <br><br>

	<label for="course">course:</label>
	<input type="text" name="course" required> <br><br>

	<label for="email">email:</label>
	<input type="text" name="email" required>

	<label for="query">Query:</label><br>
	<textarea id="query" name="query" rows="4" cols="30" required></textarea>

	<input type="submit" value="Submit">
	</form>
</body>
</html>
"""

@app.route('/')
def form():
	return render_template_string(html_template)

@app.route('/submit', methods=['POST'])
def submit():
	name = request.form.get('name')
	course = request.form.get('course')
	query = request.form.get('query')
	email = request.form.get('email')

	filename = f"{name}_query.txt"
	with open(filename, 'w') as file:
		file.write(f"Name: {name}\n")
		file.write(f"Course: {course}\n")
		file.write(f"Query: {query}\n")
		file.write(f"Email: {email}\n")
	return email


app.run()
