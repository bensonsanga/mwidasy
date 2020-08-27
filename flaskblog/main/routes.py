from flask import render_template, request, Blueprint
from flaskblog.models import Post
from .data import *

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route("/entourage")
def entourage():
    return render_template('entourage.html', title='Entourage', articles=articles)


@main.route("/assets")
def assests():
    return render_template('assets.html', title='Assets')
