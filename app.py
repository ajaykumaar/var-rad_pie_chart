from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500


@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")




@app.route("/data", methods=["GET"])
def read_json():


    
    genre_list = ['Sci-Fi', 'Comedy', 'Action', 'Romance', 'Drama']

    percent_list = [20, 20, 25, 30, 5]
    
                

    result_dict = {
        'genre': genre_list,
        'title': 'Movie preference in India ',
        'subtitle': 'Source: IDC 2021',
        'percent': percent_list,
        
    }

    return jsonify(result_dict)

    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
