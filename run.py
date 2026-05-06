import sys
import os
sys.path.insert(0, os.path.abspath("."))
from app.main import app

server = app.server

if __name__ == "_main_":
    app.run(debug=False, port=8050)
