from flask import Flask, render_template, jsonify, abort, request

app = Flask(__name__)
#just a trial
# Enriched core configurations from your version 2 logic matrix
PROGRAMS = {
    "fat_loss": {
        "name": "Fat Loss (FL)",
        "workout": "Mon: Back Squat 5x5 + Core\nTue: EMOM 20min Assault Bike\nWed: Bench Press + 21-15-9\nThu: Deadlift + Box Jumps\nFri: Zone 2 Cardio 30min",
        "diet": "Breakfast: Egg Whites + Oats\nLunch: Grilled Chicken + Brown Rice\nDinner: Fish Curry + Millet Roti\nTarget: ~2000 kcal",
        "color": "#e74c3c",
        "calorie_factor": 22
    },
    "muscle_gain": {
        "name": "Muscle Gain (MG)",
        "workout": "Mon: Squat 5x5\nTue: Bench 5x5\nWed: Deadlift 4x6\nThu: Front Squat 4x8\nFri: Incline Press 4x10\nSat: Barbell Rows 4x10",
        "diet": "Breakfast: Eggs + Peanut Butter Oats\nLunch: Chicken Biryani\nDinner: Mutton Curry + Rice\nTarget: ~3200 kcal",
        "color": "#2ecc71",
        "calorie_factor": 35
    },
    "beginner": {
        "name": "Beginner (BG)",
        "workout": "Full Body Circuit:\n- Air Squats\n- Ring Rows\n- Push-ups\nFocus: Technique & Consistency",
        "diet": "Balanced Tamil Meals\nIdli / Dosa / Rice + Dal\nProtein Target: 120g/day",
        "color": "#3498db",
        "calorie_factor": 26
    }
}

@app.route('/')
def home():
    return render_template('index.html', programs=PROGRAMS)

@app.route('/api/programs/<program_id>', methods=['GET'])
def get_program(program_id):
    if program_id not in PROGRAMS:
        abort(404, description="Profile not found")
    return jsonify(PROGRAMS[program_id])

@app.route('/api/calculate', methods=['POST'])
def calculate_calories():
    data = request.get_json() or {}
    weight = data.get('weight', 0)
    program_id = data.get('program')
    
    if not program_id or program_id not in PROGRAMS:
        return jsonify({"error": "Invalid program selection"}), 400
        
    try:
        weight_val = float(weight)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid weight matrix"}), 400

    factor = PROGRAMS[program_id]['calorie_factor']
    estimated_calories = int(weight_val * factor) if weight_val > 0 else 0
    return jsonify({"estimated_calories": estimated_calories})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
