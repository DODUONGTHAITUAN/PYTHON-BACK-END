from src import create_app
from os import environ
import sys

sys.dont_write_bytecode = True
PORT = environ.get("PORT") or 8080

app = create_app()
# ahihi
if __name__ == "__main__":

    app.run(debug=True, port=PORT)
