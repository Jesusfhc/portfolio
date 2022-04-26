from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from forms import ContactForm
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap(app)

MY_EMAIL = "jh.pythondeveloper@gmail.com"
PS = "Hola1234."


def send_email(mail, subject, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: {subject}\n\n Message: {msg}, from: {mail}"
        )


@app.route("/", methods=["POST", "GET"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        send_email(
            mail=form.mail.data,
            subject=form.subject.data,
            msg=form.message.data
        )
        flash("Email Send!")
        return redirect(url_for("home"))
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
