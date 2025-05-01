from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from pipeline import CleaningPipeline

app = Flask(__name__)
CORS(app)

# 1. Load your persisted pipeline and formatter
PIPE_PATH = "models/cleaning_pipeline.pkl"
pipe = joblib.load(PIPE_PATH)


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    # Expecting {"input": ["10/11/2018", "surface", "pédiatrie", "cabine10", "oreiller"]}
    raw_inputs = payload.get("input")
    if not raw_inputs or len(raw_inputs) != 5:
        return jsonify({"error": "Input must be a list of 5 values"}), 400

    # 3. Run the pipeline
    #    Your pipeline’s __call__ returns two dicts (germ_dict, disinf_dict)
    germ_dict, disinf_dict = pipe(raw_inputs)

    # 4. Return JSON
    return jsonify({
        "germs": germ_dict,
        "disinfectants": disinf_dict
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
