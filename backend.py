from flask import Flask, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)

myCollection = mongo.db.g8

# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")

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
    return data

@app.route('/calculate/<ids>', methods=['GET'])
def calculate(ids):
    filt = {'park_id': int(ids)}
    query = myCollection.find_one(filt)
    start = query["time_start_min"]
    end = query["time_end_min"]
    price = (end - start) * 20
    return {'result' : price}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50002', debug=True)