import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = "Hello world"
    return f"Thanks {name}, you sent this message: \"{message}\""

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    length = 0
    for letter in text:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            length += 1
    return f"There are {length} vowels in \"{text}\""

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    if 'names' not in request.form:
        return "Please provide a list of names", 400
    else:
        name_list = request.form['names']
        new_list = name_list.split(',')
        new_list.sort()
        return ",".join(new_list)
    
@app.route('/names', methods = ['GET'])
def get_names():
    names = request.args['add']
    name_args = names.split(',')
    names_list = 'Alice, Julia, Karim'
    for name in name_args:
        names_list += f", {name}"
    names_split = names_list.split(", ")
    names_split.sort()
    return ', '.join(names_split)
# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

