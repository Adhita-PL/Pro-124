from flask import Flask, jsonify, request

app = Flask(__name__) 

tasks = [
    {
        'contact' : '7661932173',
        'name' : 'adhita bharadwaj',
        'done' : False,
        'id' : 1
    },
    {
        'contact' : '1234567890',
        'name' : 'Harry potter',
        'done' : False,
        'id' : 1
    },
]
@app.route('/add-data', methods = ['POST'])
def add_task() :
    if not request.json :
        return jsonify({
            'status' : 'error',
            'message' : 'Please provide the data'
        }, 400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'name' : request.json['name'],
        'contact' : request.json.get('contact', ''),
        'done' : False
    }
    tasks.append(task)
    return jsonify({
        'status' : 'success',
        'message': 'Task added successfully'
    })

@app.route('/get-data')
def get_task() :
    return jsonify({
        'data' : tasks
    })

if (__name__ == '__main__') :
    app.run(debug=True)
