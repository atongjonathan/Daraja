from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index(request):
    return {"message":"Callback Api Running"}
@app.route('/callback', methods=['POST'])
def receive_callback():
    try:
        data = request.json  # Assuming the callback data is in JSON format
        print("Received callback data:", data)

        # Process the callback data as needed

        # Send a response if necessary
        response = {"status": "Callback received successfully"}
        return jsonify(response), 200

    except Exception as e:
        print("Error processing callback:", str(e))
        return jsonify({"error": "Error processing callback"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
