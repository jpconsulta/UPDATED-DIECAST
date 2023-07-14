from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manufacturer')
def manufacturer():
    return render_template('manufacturer.html')


@app.route('/model-scale')
def model_scale():
    return render_template('scale.html')


@app.route('/about-us')
def about_us():
    return render_template('kami.html')


@app.route('/manufacturer/<carbrand>')
def diecasts(carbrand):
    diecasts_list = read_diecast_by_carbrand(carbrand)
    for i in diecasts_list:
        print(i, "\n\n\n")
    return render_template("carbrand.html", carbrand=carbrand, diecast_template=diecasts_list)


@app.route('/manufacturer/<int:diecast_id>')
def carname(diecast_id):
    carname_id = read_diecast_by_id(diecast_id)
    return render_template("carname.html", carname=carname_id)


@app.route('/new-listing')
def new_listing():
    return render_template('newlisting.html')


@app.route('/processed', methods=['POST'])
def processing():
    diecast_data = {
        "manufacturer": request.form['manufacturer'],
        "carbrand": request.form['car_brand'],
        "carname": request.form['car_name'],
        "series": request.form['series'],
        "releaseyear": request.form['release_year'],
        "color": request.form['color'],
        "material": request.form['material'],
        "price": request.form['price'],
        "url": request.form['url'],
        "scale": request.form['scale'],
    }
    insert_diecast(diecast_data)
    return redirect(url_for('manufacturer', carbrand=request.form['carbrand']))


@app.route('/modify', methods=['post'])
def modify():
    if request.form["modify"] == "edit":
        diecast_id = request.form['diecast_id']
        diecast = read_diecast_by_id(diecast_id)
        return render_template('update.html', diecast=diecast)
    elif request.form["modify"] == "delete":
        diecast_id = request.form["diecast_id"]
        delete_diecast_id = delete_diecast(diecast_id)
        return redirect(url_for('manufacturer', carbrand=request.form['carbrand']))


@app.route('/update', methods=['post'])
def update():
    diecast_data = {
        "diecast_id": request.form["diecast_id"],
        "manufacturer": request.form['manufacturer'],
        "carbrand": request.form['car_brand'],
        "carname": request.form['car_name'],
        "series": request.form['series'],
        "releaseyear": request.form['release_year'],
        "color": request.form['color'],
        "material": request.form['material'],
        "price": request.form['price'],
        "url": request.form['url'],
        "scale": request.form['scale']
    }
    update_diecast(diecast_data)
    return redirect(url_for('carname', diecast_id=request.form['diecast_id']))


@app.route('/search', methods=['get'])
def search():
    query = request.args.get('query', '')
    results = search_diecast(query)
    return render_template('searchpage.html', query_template=query, results_template=results)


if __name__ == "__main__":
    app.run(debug=True)
