from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

units = {"length":
             {"mm": 0.001,
              "cm": 0.01,
              "m": 1,
              "km": 1000,
              "in": 0.0254,
              "ft": 0.3048,
              "yd": 0.9144,
              "mi": 1609.34},
         "weight":
            {"mg": 0.000001,
              "g": 0.001,
              "kg": 1,
              "oz": 0.0283495,
              "lb": 0.453592}
         }
temprature = {
        ("celsius", "fahrenheit"): lambda c: (c * 9/5) + 32,
        ("celsius", "kelvin"): lambda c: c + 273.15,
        ("fahrenheit", "celsius"): lambda f: (f - 32) * 5/9,
        ("fahrenheit", "kelvin"): lambda f: (f - 32) * 5/9 + 273.15,
        ("kelvin", "celsius"): lambda k: k - 273.15,
        ("kelvin", "fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32
    }


@app.route("/convert")
def convert():
    value = float(request.args.get("value", 0))
    from_ = request.args.get("fromun")
    to_ = request.args.get("toun")
    type_ = request.args.get("type")

    try:
        from_, to_, type_ = from_.lower(), to_.lower(), type_.lower()

        if from_ == to_:
            formatted_value = f"{value: .6e}" if len(str(value)) > 9 else value
            return jsonify({"result": formatted_value})

        if type_ == "temprature":
             value = float(temprature.get((from_, to_), lambda x: None)(value))
             formatted_value = f"{value: .6e}" if len(str(value)) > 9 else value
             return jsonify({"result": formatted_value})
        else:
            value = float(value * units[type_][from_] / units[type_][to_])
            formatted_value = f"{value: .6e}" if len(str(value)) > 9 else value
            return jsonify({"result": formatted_value})
        
    except (KeyError, TypeError, ValueError):
        return jsonify({"result": "Wrong unit"})


if __name__ == "__main__":
    app.run(debug=True)
