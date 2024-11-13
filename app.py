from todoList import create_app

app = create_app()

@app.route('/')
def home():
    return "Config successfully"

if __name__ == "__main__":
    app.run(debug = True)