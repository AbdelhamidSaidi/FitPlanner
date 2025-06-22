# FitPlanner

A Python terminal-based workout planner that creates a personalized weekly workout schedule based on your:

- Desired number of workout days per week (2 to 6)
- Fitness goal (lose weight, increase endurance, or build muscle)
- Height and weight (used to calculate BMI and suggest weights for exercises)

---

## Features

- **BMI Calculation:** Calculates and displays your Body Mass Index (BMI) with category.
- **Scientifically-backed workout splits:** Uses effective workout splits depending on workout days.
- **Exercise plans:** Generates daily workouts with exercises including sets, reps/time, and suggested weights.
- **Adaptive weights:** Estimates suggested weight loads based on your body weight and training goal.
- **Assisted/weighted bodyweight exercises:** Supports pull-ups, dips, and push-ups with assistance or added weights.
- **Even distribution:** Workout days are evenly spaced through the week, with Sunday always as a rest day.

---

## Workout Splits Used

| Workout Days | Split Type               |
|--------------|-------------------------|
| 2            | Upper Body / Lower Body |
| 3            | Push / Pull / Legs      |
| 4            | Upper Body / Lower Body (twice) |
| 5            | Push / Pull / Legs / Upper Body / Lower Body |
| 6            | Push / Pull / Legs (twice) |

---

## Usage

1. Make sure you have Python 3 installed.

2. Clone/download this repository or copy the script.

3. Run the script in your terminal or command prompt:

   ```bash
   python fitplanner.py
   ```

4. Follow the on-screen prompts to input:

   * Your height (in centimeters)
   * Your weight (in kilograms)
   * Number of workout days per week (between 2 and 6)
   * Your fitness goal:

     * 1: Lose Weight
     * 2: Increase Endurance
     * 3: Build Muscle

5. The program will display your BMI and a detailed weekly workout plan with exercises, sets/reps or time, and suggested weights.

---

## Example Output

```
Enter your height in cm: 175
Enter your weight in kg: 70
📏 Your BMI is 22.9 — Normal

Enter number of workout days per week (2–6): 3

Select your goal:
1. Lose Weight
2. Increase Endurance
3. Build Muscle
Enter the number of your goal: 3

📅 Your Weekly Workout Plan:
Sunday: Rest
Monday: Push - Bench Press (3–5 sets of 6–12 reps, use ~42 kg); Overhead Press (3–5 sets of 6–12 reps, use ~35 kg); Shoulder Taps (3 sets of 60 sec)
Tuesday: Rest
Wednesday: Pull - Dumbbell Rows (3–5 sets of 6–12 reps, use ~35 kg); Barbell Rows (3–5 sets of 6–12 reps, use ~42 kg); Jump Rope (3 sets of 60 sec)
Thursday: Rest
Friday: Legs - Romanian Deadlifts (3–5 sets of 6–12 reps, use ~56 kg); Squats (3–5 sets of 6–12 reps, use ~70 kg); Jump Squats (3 sets of 60 sec)
Saturday: Rest
```

---

## Notes

* The weight recommendations are approximations based on bodyweight ratios found in scientific literature and adjusted for your goal.
* Time-based exercises like planks and wall sits are given as seconds per set instead of reps.
* Workout days are spaced evenly Monday through Saturday; Sunday is always rest.
* This is a command-line program with no graphical interface.

---

## Future Improvements

* Export workout plan as PDF or CSV.
* Add progressive overload and periodization.
* Include equipment options (home/gym).
* Build a GUI or web app version.

---

## License

This project is open source and free to use and modify.

---

Feel free to contribute or request features!

---

