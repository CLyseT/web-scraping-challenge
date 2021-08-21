from flask import Flask, render_template
import os

import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

mars_data = client.data

mars_data.data.insert_many(
[{'Title':'Cerberus Hemisphere Enhanced','Image_URL':'https://marshemispheres.com/images/cerberus_enhanced.tif'},
{'Title':'Schiaparelli Hemisphere Enhanced', 'Image_URL':'https://marshemispheres.com/images/schiaparelli_enhanced.tif'},
{'Title':'Syrtis Major Hemisphere Enhanced', 'Image_URL': 'https://marshemispheres.com/images/syrtis_major_enhanced.tif'},
{'Title':'Valles Marineris Hemisphere Enhanced', 'Image_URL':'https://marshemispheres.com/images/valles_marineris_enhanced.tif'}]
)

@app.route('/')
def title():
    return render_template("index.html", title="NASA's Mars Reconnaissance Orbiter Undergoes Memory Update")

@app.route('/')
def paragraph():
    return render_template("index.html", paragraph="Other orbiters will continue relaying data from Mars surface missions for a two-week period.")

@app.route('/')
def index():
    name = [{"title_1": "Cerberus",
                "title_2": "Schiaparelli",
                "title_3": "Syrtis-Major",
                "title_4": "Valles-Marineris"}]
    return render_template("index.html", dict=name)


if __name__ == "__main__":
    app.run(debug=True)
