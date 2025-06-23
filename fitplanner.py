import random

def get_workout_split(days):
    if days == 2:
        return ['Upper Body', 'Lower Body']
    elif days == 3:
        return ['Push', 'Pull', 'Legs']
    elif days == 4:
        return ['Upper Body', 'Lower Body', 'Upper Body', 'Lower Body']
    elif days == 5:
        return ['Push', 'Pull', 'Legs', 'Upper Body', 'Lower Body']
    elif days == 6:
        return ['Push', 'Pull', 'Legs', 'Push', 'Pull', 'Legs']
    else:
        raise ValueError("Workout days must be between 2 and 6.")

workout_bank = {
    'Push': {
        'reps': ['Bench Press', 'Overhead Press', 'Triceps Dips'],
        'time': ['Shoulder Taps', 'Plyo Push-ups']
    },
    'Pull': {
        'reps': ['Barbell Rows', 'Face Pulls', 'Dumbbell Rows', 'Pull-ups'],
        'time': ['Jump Rope', 'Resistance Band Pulls']
    },
    'Legs': {
        'reps': ['Squats', 'Romanian Deadlifts', 'Lunges'],
        'time': ['Mountain Climbers', 'Wall Sits', 'Jump Squats']
    },
    'Upper Body': {
        'reps': ['Pull-ups', 'Bench Press', 'Shoulder Press'],
        'time': ['Plank', 'Shadow Boxing']
    },
    'Lower Body': {
        'reps': ['Deadlifts', 'Leg Curl', 'Step-ups'],
        'time': ['Wall Sits', 'Jump Lunges']
    }
}

TIME_BASED = {
    'Plank', 'Wall Sits', 'Mountain Climbers', 'Jump Rope',
    'Shadow Boxing', 'Plyo Push-ups', 'Shoulder Taps',
    'Resistance Band Pulls', 'Jump Lunges'
}

def get_format(goal, exercise):
    if exercise in TIME_BASED:
        if goal == 1:
            return "3–4 sets of 30–45 sec"
        elif goal == 2:
            return "3–4 sets of 45–60 sec"
        elif goal == 3:
            return "3 sets of 60 sec"
    else:
        if goal == 1:
            return "3–4 sets of 12–20 reps"
        elif goal == 2:
            return "3–4 sets of 15–25 reps"
        elif goal == 3:
            return "3–5 sets of 6–12 reps"
    return ""

def recommend_weight(goal, exercise, bodyweight, gender):
    supported_bodyweight = {'Pull-ups', 'Triceps Dips', 'Push-ups'}

    ratios = {
        'Bench Press': 0.6,
        'Overhead Press': 0.5,
        'Squats': 1.0,
        'Romanian Deadlifts': 0.8,
        'Deadlifts': 1.2,
        'Barbell Rows': 0.6,
        'Dumbbell Rows': 0.5,
        'Shoulder Press': 0.5,
        'Face Pulls': 0.4,
        'Leg Curl': 0.6,
        'Step-ups': 0.5
    }

    gender_factor = 1.0 if gender == 'm' else 0.7

    if exercise in supported_bodyweight:
        if goal == 1:
            load = round(-0.15 * bodyweight * gender_factor)
            return f"{round(bodyweight * gender_factor)} kg – {abs(load)} kg assist"
        elif goal == 2:
            return f"{round(bodyweight * gender_factor)} kg (bodyweight)"
        elif goal == 3:
            load = round(0.15 * bodyweight * gender_factor)
            return f"{round(bodyweight * gender_factor)} kg + {load} kg"
        else:
            return f"{round(bodyweight * gender_factor)} kg (bodyweight)"

    ratio = ratios.get(exercise, 0.4)
    if goal == 1:
        ratio *= 0.6
    elif goal == 2:
        ratio *= 0.7
    elif goal == 3:
        ratio *= 1.0

    weight = round(bodyweight * ratio * gender_factor)
    return f"~{weight} kg"

def distribute_workout_days(days):
    valid_days = [1, 2, 3, 4, 5, 6]  # Monday to Saturday
    interval = len(valid_days) / days
    return [valid_days[round(i * interval)] for i in range(days)]

def create_schedule(days, goal, weight, gender):
    split = get_workout_split(days)
    days_idx = distribute_workout_days(days)
    schedule = ['Rest'] * 7  # Sunday to Saturday

    for i, day in enumerate(days_idx):
        split_type = split[i]
        rep_exs = random.sample(workout_bank[split_type]['reps'], 2)
        time_ex = random.choice(workout_bank[split_type]['time'])
        all_exs = rep_exs + [time_ex]

        formatted = f"{split_type} - "
        ex_lines = []
        for ex in all_exs:
            sets_reps = get_format(goal, ex)
            if ex in TIME_BASED:
                ex_lines.append(f"{ex} ({sets_reps})")
            else:
                load = recommend_weight(goal, ex, weight, gender)
                ex_lines.append(f"{ex} ({sets_reps}, use {load})")
        schedule[day] = formatted + "; ".join(ex_lines)

    return schedule

def get_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 1)

def get_protein_intake(weight, goal):
    if goal == 1:  # Lose weight
        avg_p = (2.0 + 2.7) / 2 * weight
        return f"Recommended daily protein intake for fat loss: ~{round(avg_p)} g"
    elif goal == 2:  # Endurance
        avg_p = (1.2 + 1.6) / 2 * weight
        return f"Recommended daily protein intake for endurance: ~{round(avg_p)} g"
    elif goal == 3:  # Build muscle
        avg_p = (1.6 + 2.2) / 2 * weight
        return f"Recommended daily protein intake for muscle gain: ~{round(avg_p)} g"
    return ""

# Main
def main():
    print("🏋️ Personalized Workout Planner 🏋️")

    try:
        gender = input("Enter your gender (M/F): ").strip().lower()
        if gender not in ['m', 'f']:
            raise ValueError("Gender must be M or F.")

        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
        bmi = get_bmi(weight, height)

        print(f"📏 Your BMI is {bmi} — ", end='')
        if bmi < 18.5:
            print("Underweight")
        elif bmi < 25:
            print("Normal")
        elif bmi < 30:
            print("Overweight")
        else:
            print("Obese")

        days = int(input("\nHow many days per week do you want to work out? (2–6): "))
        if not 2 <= days <= 6:
            raise ValueError

        print("\nChoose your goal:")
        print("1. Lose Weight")
        print("2. Increase Endurance")
        print("3. Build Muscle")
        goal = int(input("Enter the number of your goal: "))
        if goal not in [1, 2, 3]:
            raise ValueError

        # Show protein recommendation
        protein_info = get_protein_intake(weight, goal)
        print(f"\n {protein_info}")

        schedule = create_schedule(days, goal, weight, gender)
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        print("\n Workout Plan:")
        for i in range(7):
            print(f"{days_of_week[i]}: {schedule[i]}")

    except ValueError as e:
        print(f"Error!!! {e}")

if __name__ == "__main__":
    main()
