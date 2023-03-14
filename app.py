# import  the modules we need
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os

app = Flask(__name__)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///countries.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT'] = 16 * 1024 * 1024
ALLOWED_EXTENSION = ['png', 'jpeg', 'jpg', 'gif']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


# Creating an SQLAlchemy instance


db = SQLAlchemy(app)


class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(50), unique=False, nullable=False)
    capital_name = db.Column(db.String(20), unique=False, nullable=False)
    official_language = db.Column(db.String(50), unique=False, nullable=False)
    country_currency = db.Column(db.String, unique=False, nullable=True)
    video = db.Column(db.String, unique=False, nullable=True)
    book = db.Column(db.String, unique=False, nullable=True)
    filename = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return f"Country name:{self.country_name},Capital{self.capital_name}"

class Hotels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(50), unique=False, nullable=False)
    stars = db.Column(db.Integer, unique=False, nullable=True)
    file_hotel = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return f"Country name:{self.hotel_name},Capital{self.stars}"

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    countries_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=True)

    def _repr_(self):
        return f"Name: {self.name}, Content: {self.review_text}, Rating: {self.rating}"

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=False, nullable=False)
    msg_text = db.Column(db.String, unique=False, nullable=False)

    def _repr_(self):
        return f"Name: {self.name}, Content: {self.email}, msg: {self.msg_text}"

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

    def _repr_(self):
        return f"Name: {self.name}"


# settings for migrations
migrate = Migrate(app, db)


# function to home page
@app.route('/')
def home():
    countries_data = Countries.query.all()
    return render_template("index.html", countries_data=countries_data)


# function to add countries
@app.route('/add_data')
def add_data():
    return render_template('add_profile.html')

@app.route('/add_hotels')
def add_hotels():
    return render_template('add_hotels.html')

# function to about us page
@app.route('/about_us')
def about_us():
    return render_template('aboutus.html', )


# function to contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# In this function we will input data from the
# add_data page and store it in our database.
@app.route('/add', methods=['POST', 'GET'])
def countries_management():

    if request.method == "POST":
        country_name = request.form.get("country_name")
        capital_name = request.form.get("capital_name")
        official_language = request.form.get("official_language")
        country_currency = request.form.get("country_currency")
        video = request.form.get("video")
        book = request.form.get("book")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # store data as a row in our database
        countries_row = Countries(country_name=country_name, capital_name=capital_name,
                                  official_language=official_language, book=book, country_currency=country_currency, video=video,
                                  filename=file.filename)

        db.session.add(countries_row)
        db.session.commit()
        return redirect('/')


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename))

@app.route('/add_hotels', methods=['POST', 'GET'])
def hotel_management():
    if request.method == "POST":
        hotel_name = request.form.get("hotel_name")
        file = request.files.get("file_hotel")
        rating = request.form.get("rating")
        country_id = request.form.get("country_id")
        if allowed_file(file.file_hotel):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.file_hotel))
        # store data as a row in our database
        hotels_row = Countries(hotel_name=hotel_name, rating=rating, file_hotel=file.file_hote)

        db.session.add(hotels_row)
        db.session.commit()
        return redirect(url_for("country_info", country_id=country_id))




@app.route('/country_info/<country_id>')
def country_info(country_id):
    country_specific = Countries.query.get(country_id)
    hotels_specific = Hotels.query.filter(Reviews.countries_id == country_id)
    reviews_specific = Reviews.query.filter(Reviews.countries_id == country_id)
    return render_template("country_info.html", country_specific=country_specific, hotels_specific=hotels_specific,  reviews_specific=reviews_specific)


@app.route("/add_review", methods=["POST", "GET"])
def review_management():
    if request.method == "POST":
        name = request.form.get("name")
        review_text = request.form.get("review_text")
        rating = request.form.get("rating")
        country_id = request.form.get("country_id")
        review_row = Reviews(name=name, rating=rating, review_text=review_text, countries_id=country_id)
        db.session.add(review_row)
        db.session.commit()
        return redirect(url_for("country_info", country_id=country_id))

@app.route("/contact", methods=["POST", "GET"])
def msg_management():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        msg_text = request.form.get("msg_text")
        msg_row = Msg(name=name, email=email, msg_text=msg_text)
        db.session.add(msg_row)
        db.session.commit()
        return redirect(url_for("contact"))

@app.route("/open_register")
def open_register():
    return render_template("register.html", first_time=True)

@app.route("/register", methods=["POST" , "GET"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        users = Users.query.filter(Users.name == name).all()
        if len(users) > 0:
            return render_template("register.html", first_time=False)

        new_user = Users(name=name, password=password)
        db.session.add(new_user)
        db.session.commit()

        countries = Countries.query.all()
        return render_template("add_profile.html", countries=countries, countries_len=len(countries))


@app.route("/open_login")
def open_login():
    return render_template("login.html", first_time=True)

@app.route("/login", methods=["POST" , "GET"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        users = Users.query.filter(Users.name == name, Users.password == password).all()
        if len(users) == 0:
            return render_template("login.html", first_time=False)

        countries = Countries.query.all()
        return render_template("add_profile.html", countries=countries, countries_len=len(countries))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{0}%".format(search_value)
        countries_data = Countries.query.filter(Countries.country_name.like(search)).all()
        return render_template('index.html', countries_data=countries_data, pageTitle='THE BEST COUNTRIES TO VISIT',
                               legend="Search Results")
    else:
        return redirect("/")


@app.route("/delete/<int:id>")
def erase(id):
    data = Countries.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.countries_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")


@app.route("/alter_country/<int:id>", methods=["POST", "GET"])
def alter_country(id):
    if request.method == "POST":
        data = Countries.query.get(id)
        country_name = request.form.get("country_name")
        capital_name = request.form.get("capital_name")
        official_language = request.form.get("official_language")
        country_currency = request.form.get("country_currency")
        video = request.form.get("video")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        if request.form.get("country_name"):
            data.country_name = country_name
        if request.form.get("capital_name"):
            data.capital_name = capital_name
        if request.form.get("official_language"):
            data.official_language = official_language
        if request.form.get("video"):
            data.video = video
        if request.form.get("country_currency"):
            data.country_currency = country_currency
        if request.files.get("filename"):
            data.filename = file_name
        db.session.commit()
        return redirect(url_for('country_info', country_id=id))

    else:
        return render_template("alter_country.html")


if __name__ == "__main__":
    app.run()
