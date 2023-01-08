from werkzeug.exceptions import HTTPException
from flask import Flask, url_for, session, request, abort
from flask import render_template, redirect
from functools import wraps
from dotenv import load_dotenv, find_dotenv
import os
import pymongo

load_dotenv(find_dotenv())

APP_SECRET_KEY = os.getenv('APP_SECRET_KEY')
OSU_CLIENT_ID = os.getenv('OSU_CLIENT_ID')
OSU_CLIENT_SECRET = os.getenv('OSU_CLIENT_SECRET')
OAUTH_STATE = os.getenv('OAUTH_STATE')
MONGO_URI = os.getenv('MONGO_URI')


app = Flask(__name__)
app.secret_key = APP_SECRET_KEY


client = pymongo.MongoClient(MONGO_URI)

