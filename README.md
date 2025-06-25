# FitPlanner

A Python terminal-based workout planner that creates a personalized weekly workout schedule based on your:

- Desired number of workout days per week (2 to 6)
- Fitness goal (lose weight, increase endurance, or build muscle)
- Height and weight (used to calculate BMI and suggest weights for exercises)
- Age and gender (used to estimate maintenance and goal-specific calories)

---

## 🚀 Features

- **🧮 BMI Calculation:** Calculates your Body Mass Index and classifies it.
- **🧠 Science-based Splits:** Applies goal-appropriate, evidence-backed splits.
- **🦾 Personalized Workouts:** Reps- or time-based training plans tailored to your goal.
- **📊 Protein Recommendations:** Calculates optimal daily protein intake for your selected goal.
- **🔥 Calorie Targets:** Estimates your maintenance calories (TDEE) and adjusts for goal.
- **🏋️ Weight Suggestions:** Recommends loads for weighted exercises using sex-based strength standards.
- **🤸 Bodyweight Assist/Resist Logic:** Supports assistance (for beginners) and overload (for strength gain) in pull-ups, dips, and push-ups.
- **📅 Even Weekly Distribution:** Spaces workouts evenly from Monday to Saturday with Sunday rest.

---

## 🧱 Workout Splits

| Workout Days | Split Type                                      |
|--------------|-------------------------------------------------|
| 2            | Upper Body / Lower Body                         |
| 3            | Push / Pull / Legs                              |
| 4            | Upper Body / Lower Body (twice)                 |
| 5            | Push / Pull / Legs / Upper / Lower              |
| 6            | Push / Pull / Legs (twice)                      |

---

## 🖥️ Usage

1. Ensure you have **Python 3** installed.
2. Clone or download this repository.
3. Run the script from terminal or command prompt:

   ```bash
   python fitplanner.py
   ```

4. Follow the prompts to enter:

   * Your gender (M/F)
   * Age
   * Height (cm)
   * Weight (kg)
   * Number of workout days (2 to 6)
   * Fitness goal:

     * 1 : Lose Weight
     * 2 : Increase Endurance
     * 3 : Build Muscle

5. You’ll receive:

   * BMI + category
   * Maintenance & target calories
   * Recommended protein intake
   * A 7-day weekly plan with sets, reps/time, and loads

---

## 🧾 Example Output

```
🏋️ Personalized Workout Planner 🏋️
Enter your gender (M/F): m
Enter your age: 20
Enter your height in cm: 180
Enter your weight in kg: 70
📏 Your BMI is 21.6 — Normal

How many days per week do you want to work out? (2–6): 4

Choose your goal:
1. Lose Weight
2. Increase Endurance
3. Build Muscle
Enter the number of your goal: 3

🔥 Maintenance Calories: 2682 kcal
🎯 Target Calories for your goal: 3084 kcal
you have a calorie surplus of: 402 kcal

Recommended daily protein intake for muscle gain: ~133 g

Workout Plan:
Sunday: Rest
Monday: Upper Body - Pull-ups (3–5 sets of 6–12 reps, use 70 kg + 10 kg); Bench Press (3–5 sets of 6–12 reps, use ~42 kg); Shadow Boxing (3 sets of 60 sec)
Tuesday: Rest
Wednesday: Lower Body - Leg Curl (3–5 sets of 6–12 reps, use ~42 kg); Deadlifts (3–5 sets of 6–12 reps, use ~84 kg); Jump Lunges (3 sets of 60 sec)
Thursday: Upper Body - Shoulder Press (3–5 sets of 6–12 reps, use ~35 kg); Pull-ups (3–5 sets of 6–12 reps, use 70 kg + 10 kg); Plank (3 sets of 60 sec)
Friday: Lower Body - Step-ups (3–5 sets of 6–12 reps, use ~35 kg); Deadlifts (3–5 sets of 6–12 reps, use ~84 kg); Wall Sits (3 sets of 60 sec)
Saturday: Rest
```

---

## 📚 Scientific Backing

FitPlanner’s design is based on peer-reviewed research and official guidelines that u can find in the sources.md file

## 👥 Contributions & Feedback

Want to suggest an improvement, add more logic, or report a bug?
Feel free to open an issue or submit a pull request!

---
