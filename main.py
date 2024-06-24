from flask import Flask, render_template, request
import pymongo_connect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/allProperties")
def list_all():
    data = pymongo_connect.fetchAllRecords()
    return render_template("all_properties.html", data=data)


@app.route("/form")
def form_property():
    id = request.args.get('id')
    print("\nRequest For : ", id, " \n")
    return render_template("form.html", id=id)


@app.route("/book", methods=['POST'])
def book_property():
    property_id = request.form.get('property_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    pymongo_connect.pushToBooking(
        {
            "name": name,
            "phone": phone,
            "email": email,
            "property_id": property_id
        }
    )

    pymongo_connect.bookRemove(property_id)

    print(property_id, name)

    return '<html><head><link rel="stylesheet" href="./static/css/styles.css" /></head><body><script type="text/javascript">alert("Property has been booked");window.location = "/";</script></body></html>'


@app.route("/history", methods=['POST'])
def fetch_history():
    email = request.form.get('email')
    result = pymongo_connect.fetchHistory(email)
    r = []
    for x in result:
        r.append(x)
    return render_template("history.html", r=r)


if __name__ == "__main__":
    app.run(debug=True)
