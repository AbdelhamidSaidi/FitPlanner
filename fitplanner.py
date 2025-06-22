import random

# Define splits and workouts
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

# Exercise database
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

# Time based workout
TIME_BASED = {
    'Plank', 'Wall Sits', 'Mountain Climbers', 'Jump Rope',
    'Shadow Boxing', 'Plyo Push-ups', 'Shoulder Taps',
    'Resistance Band Pulls', 'Jump Lunges'
}

# Training goal to format sets and reps or sets and time
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

# bodyweight related workouts
def recommend_weight(goal, exercise, bodyweight):
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

    if exercise in supported_bodyweight:
        if goal == 1:
            load = round(-0.15 * bodyweight)
            return f"{bodyweight} kg – {abs(load)} kg assist"
        elif goal == 2:
            return f"{bodyweight} kg (bodyweight)"
        elif goal == 3:
            load = round(0.15 * bodyweight)
            return f"{bodyweight} kg + {load} kg"
        else:
            return f"{bodyweight} kg (bodyweight)"

    ratio = ratios.get(exercise, 0.4)
    if goal == 1:
        ratio *= 0.6
    elif goal == 2:
        ratio *= 0.7
    elif goal == 3:
        ratio *= 1.0

    weight = round(bodyweight * ratio)
    return f"~{weight} kg"

# Distribute workout days evenly across the week (Monday to Saturday)
def distribute_workout_days(days):
    valid_days = [1, 2, 3, 4, 5, 6]  # Monday to Saturday
    interval = len(valid_days) / days
    return [valid_days[round(i * interval)] for i in range(days)]

# Create weekly workout schedule
def create_schedule(days, goal, weight):
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
            if ex in TIME_BASED or recommend_weight(goal, ex, weight) == "bodyweight":
                ex_lines.append(f"{ex} ({sets_reps})")
            else:
                load = recommend_weight(goal, ex, weight)
                ex_lines.append(f"{ex} ({sets_reps}, use {load})")
        schedule[day] = formatted + "; ".join(ex_lines)

    return schedule

# calculate bmi
def get_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 1)

# Main 
def main():
    print("🏋️ Workout Planner 🏋️")

    try:
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

        days = int(input("\nEnter number of workout days per week (2–6): "))
        if not 2 <= days <= 6:
            raise ValueError

        print("\nSelect your goal:")
        print("1. Lose Weight")
        print("2. Increase Endurance")
        print("3. Build Muscle")
        goal = int(input("Enter the number of your goal: "))
        if goal not in [1, 2, 3]:
            raise ValueError

        schedule = create_schedule(days, goal, weight)
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        print("\n📅🏋️ Your Weekly Workout Plan:")
        for i in range(7):
            print(f"{days_of_week[i]}: {schedule[i]}")

    except ValueError:
        print(" Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
