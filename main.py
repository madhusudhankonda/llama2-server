from flask import Flask, request,jsonify,make_response
import requests

server_url = "http://localhost:4502"
app = Flask(__name__)

@app.route('/call',methods=['POST'])
def call_llama2_server():
    req = request.json
    print("1. Input is: ",req)
    question = req.get('question')
    response = requests.post(server_url+"/invoke_llm", json=req)
    print("anser from the service:",response.json())
    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to get response from the llma2_server"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4500, debug=True, threaded=True)