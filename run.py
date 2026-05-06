import sys
import os
sys.path.insert(0, os.path.abspath("."))
from app.main import app

server = app.server