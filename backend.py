from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)

myCollection = mongo.db.g8

@app.route('/update', methods=['PUT'])
def update_one():
    data = request.json
    filt = {'park_id' : data["park_id"]}
    hour = data["hour"]
    minute = data["minute"]
    second = data["second"]
    time_str = str(hour) + ":" + str(minute) + ":" + str(second)
    if second > 0 :
        minute += 1
    time = (hour * 60) + minute

    if data['status'] == 0:
        updated_content = {"$set": {
            'status': 0,
            'time_end': time_str, 
            'time_end_min': time}}
    if data['status'] == 1:
        updated_content = {"$set": {
            'status': 1,
            'time_start': time_str, 
            'time_start_min': time}}
    myCollection.update_one(filt, updated_content)
    return render_template("index.html")

@app.route('/calculate', methods=['GET'])
def calculate():
    data = request.json
    filt = {'park_id': data["park_id"]}
    query = myCollection.find_one(filt)
    start = query["time_start_min"]
    end = query["time_end_min"]
    price = (end - start) * 20
    return render_template("index.html", price = price)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50002', debug=True)