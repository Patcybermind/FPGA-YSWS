from flask import Flask, render_template
import sys
import threading
from md_to_html import generate_html
from time import sleep

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts/<post_name>')
def show_post(post_name):
    # Extract the post name from the URL
    # and use it as a variable in your code
    return render_template(f"{post_name}.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def gen(): # generate templates
    generate_html()

def exit_app():
    print("exiting app")
    sys.exit(0)
    

def command_default():
    print("Unknown command")

def skip():
    pass

command_switch = {
    "gen": gen,
    "exit": exit_app,
    "": skip
}

def command_loop():
    sleep(1)
    while True:
        command = input("Enter a command: ")
        command_switch.get(command, command_default)()

# Start the command loop in a separate thread
command_thread = threading.Thread(target=command_loop)
command_thread.daemon = True
command_thread.start()

if __name__ == '__main__':
    app.run(debug=True)