from flask import Flask, request, jsonify
import uuid
app = Flask(__name__)

class MasterNode:
    def __init__(self, coordinator):
        self.coordinator = coordinator

    def api_construct(self):

        @app.route('/')
        def root():
            return "Home page"

        @app.route('/master', methods=['GET', 'POST'])
        def api_handler():
            if request.method == 'GET': # Returns the users information, based on the packet they send
                return jsonify({'currentFold': f"{self.coordinator.current_iter}"})

            if request.method == 'POST':
                data = request.get_json(force=True)  # Get JSON data from the request
                if not data:
                    return jsonify({"error": "Invalid JSON data"}), 400 # Graceful error handling
                # Process the data

                if self.coordinator.verify(data):
                    response = self.coordinator.generate_response(identity=data["header"])
                    self.coordinator.current_iter += self.coordinator.batch_size

                return jsonify(response), 200

        @app.route('/rights', methods=['POST'])
        def rights_handler():
            if request.method == 'POST':
                data = request.get_json(force=True)  # Get JSON data from the request
                if not data:
                    return jsonify({"error": "Invalid JSON data"}), 400  # Graceful error handling

            gen_uuid = uuid.uuid4()
            self.coordinator.add_node(f"{gen_uuid}")

            return jsonify({"allocated_identity": f"{gen_uuid}"}), 200

    def initate(self):
        app.run(host='0.0.0.0', port=5000)