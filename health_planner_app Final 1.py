import sys

# Data structure for sample meal plans
MEAL_PLANS = {
    # This structure is now nested by Region -> Diet Type -> Health Goal
    # For this example, we use a "Generic" region that can be expanded.
    "Generic": {
        "Non-Vegetarian": {
            "Weight Loss": {
                "description": "This plan focuses on lean protein, high fiber, and controlled portions to support weight loss.",
                "Breakfast": "Scrambled eggs (2) with spinach and a side of berries.",
                "Lunch": "Grilled chicken salad with mixed greens, cucumber, tomatoes, and a light vinaigrette.",
                "Dinner": "Baked salmon with roasted broccoli and quinoa.",
                "Snack": "Greek yogurt or a small apple.",
                "Grocery_Brands": {
                    "US": [
                        "Kirkland Signature (Costco) for bulk chicken breast and salmon.",
                        "Fage Total 0% Milkfat Plain Greek Yogurt.",
                        "Dave's Killer Bread (Thin-Sliced) for controlled portions."
                    ],
                    "IN": [
                        "Godrej Real Good or Zorabian for chicken.",
                        "Epigamia or Nestle a+ Grekyo for Greek yogurt.",
                        "Britannia Whole Wheat Bread."
                    ]
                }
            },
            "Maintenance": {
                "description": "A balanced diet to maintain current weight and energy levels.",
                "Breakfast": "Oatmeal with nuts, seeds, and a banana.",
                "Lunch": "Turkey and avocado sandwich on whole-wheat bread with a side salad.",
                "Dinner": "Lean beef stir-fry with a variety of colorful vegetables and brown rice.",
                "Snack": "A handful of almonds or a protein bar.",
                "Grocery_Brands": {
                    "US": [
                        "Bob's Red Mill for oatmeal and whole grains.",
                        "Applegate Naturals for turkey slices.",
                        "Blue Diamond for almonds."
                    ],
                    "IN": [
                        "Quaker or Saffola for oats.",
                        "Happilo or Nutraj for almonds and nuts.",
                        "Amul or Mother Dairy for dairy products."
                    ]
                }
            },
            "Weight Gain": {
                "description": "This plan includes calorie-dense, nutrient-rich foods to support healthy weight gain.",
                "Breakfast": "Large bowl of oatmeal with peanut butter, banana, and whole milk.",
                "Lunch": "Chicken and rice bowl with black beans, corn, and avocado.",
                "Dinner": "Pasta with meat sauce, served with a side of garlic bread.",
                "Snack": "Protein shake or a handful of mixed nuts and dried fruit.",
                "Grocery_Brands": {
                    "US": [
                        "Optimum Nutrition for protein powder.",
                        "Barilla Protein+ Pasta for extra protein.",
                        "Jif or Skippy Natural Peanut Butter."
                    ],
                    "IN": [
                        "Myprotein or Optimum Nutrition (IN) for protein powder.",
                        "Borges or Barilla for pasta.",
                        "Pintola or Alpino for peanut butter."
                    ]
                }
            }
        },
        "Vegetarian": {
            "Weight Loss": {
                "description": "A vegetarian plan focused on plant-based protein and fiber for weight loss.",
                "Breakfast": "Greek yogurt with berries and a sprinkle of chia seeds.",
                "Lunch": "Lentil soup with a side of whole-grain crackers.",
                "Dinner": "Tofu stir-fry with mixed vegetables and brown rice.",
                "Snack": "An apple with a tablespoon of almond butter.",
                "Grocery_Brands": {
                    "US": [
                        "Chobani or Fage for Greek yogurt.",
                        "Amy's Kitchen for organic lentil soup.",
                        "Nasoya for organic tofu."
                    ],
                    "IN": [
                        "Epigamia for Greek yogurt.",
                        "MTR or Gits for soup mixes.",
                        "Mori-Nu or local brands for tofu (paneer is a common alternative)."
                    ]
                }
            },
            "Maintenance": {
                "description": "A balanced vegetarian diet for maintaining weight and health.",
                "Breakfast": "Scrambled tofu with turmeric, spinach, and whole-wheat toast.",
                "Lunch": "Quinoa salad with black beans, corn, bell peppers, and a lime-cilantro dressing.",
                "Dinner": "Chickpea curry with a side of naan bread.",
                "Snack": "A handful of walnuts.",
                "Grocery_Brands": {
                    "US": [
                        "365 by Whole Foods Market for quinoa and organic produce.",
                        "House Foods for tofu.",
                        "S&W for canned beans."
                    ],
                    "IN": [
                        "24 Mantra Organic or Fabindia for quinoa.",
                        "Amul or Britannia for paneer (as tofu alternative).",
                        "Tata Sampann for dals and chickpeas."
                    ]
                }
            },
            "Weight Gain": {
                "description": "A calorie-dense vegetarian plan for healthy weight gain.",
                "Breakfast": "Smoothie with protein powder, banana, peanut butter, and soy milk.",
                "Lunch": "Large bean and cheese burrito with guacamole and sour cream.",
                "Dinner": "Vegetable lasagna with a side salad.",
                "Snack": "Avocado toast on whole-grain bread.",
                "Grocery_Brands": {
                    "US": [
                        "Orgain for plant-based protein powder.",
                        "Mission for large flour tortillas.",
                        "Tillamook for cheese."
                    ],
                    "IN": [
                        "Oziva or Plix for plant-based protein powder.",
                        "Amul or Gowardhan for cheese and paneer.",
                        "Veeba for sauces and dressings."
                    ]
                }
            }
        },
        "Vegan": {
            "Weight Loss": {
                "description": "A vegan plan designed for weight loss with whole foods.",
                "Breakfast": "Oatmeal with berries and flax seeds.",
                "Lunch": "Large salad with chickpeas, various greens, and a tahini dressing.",
                "Dinner": "Roasted vegetable and lentil bowl.",
                "Snack": "A pear.",
                "Grocery_Brands": {
                    "US": [
                        "Quaker Oats for oatmeal.",
                        "Earthbound Farm for organic greens.",
                        "Simple Truth (Kroger) for lentils and beans."
                    ],
                    "IN": [
                        "Saffola or Quaker for oats.",
                        "Urban Platter for seeds and vegan products.",
                        "Organic Tattva for lentils."
                    ]
                }
            },
            "Maintenance": {
                "description": "A balanced vegan diet for sustained energy and health.",
                "Breakfast": "Avocado toast with nutritional yeast and red pepper flakes.",
                "Lunch": "Vegan chili with a side of cornbread.",
                "Dinner": "Sweet potato stuffed with black beans, corn, and avocado.",
                "Snack": "A small bowl of edamame.",
                "Grocery_Brands": {
                    "US": [
                        "Bragg for nutritional yeast.",
                        "Gardein for plant-based meat alternatives.",
                        "Ezekiel 4:9 for sprouted grain bread."
                    ],
                    "IN": [
                        "Goodmylk or So Good for plant-based milk.",
                        "Blue Tribe or Imagine Meats for plant-based meat.",
                        "Urban Platter for nutritional yeast."
                    ]
                }
            },
            "Weight Gain": {
                "description": "A nutrient-rich vegan plan for gaining weight.",
                "Breakfast": "Large smoothie with vegan protein powder, almond butter, banana, and oat milk.",
                "Lunch": "Seitan sandwich with vegan mayo and a side of sweet potato fries.",
                "Dinner": "Coconut curry with tofu and jasmine rice.",
                "Snack": "A handful of mixed nuts and dried fruit.",
                "Grocery_Brands": {
                    "US": [
                        "Beyond Meat for calorie-dense plant-based options.",
                        "Califia Farms for oat milk.",
                        "Nature's Path for granola and cereals."
                    ],
                    "IN": [
                        "Unived or Olena for vegan protein.",
                        "So Good or Oatly for oat milk.",
                        "Pintola for nut butters."
                    ]
                }
            }
        }
    },
    "Mediterranean": {
        "Non-Vegetarian": {
            "Weight Loss": {
                "description": "A Mediterranean plan focused on lean protein, healthy fats, and fresh vegetables for weight loss.",
                "Breakfast": "Greek yogurt with a handful of berries and walnuts.",
                "Lunch": "Grilled sea bass with a large Greek salad (tomatoes, cucumbers, olives, feta) and an olive oil vinaigrette.",
                "Dinner": "Chicken souvlaki skewers with a side of tzatziki and roasted vegetables.",
                "Snack": "An orange or a handful of olives.",
                "Grocery_Brands": {
                    "US": ["Fage or Chobani for Greek yogurt.", "Athenos for feta cheese.", "California Olive Ranch for olive oil."],
                    "IN": ["Epigamia for Greek yogurt.", "Amul or Milky Mist for feta.", "Figaro or Borges for olive oil."]
                }
            },
            "Maintenance": {
                "description": "A balanced Mediterranean diet rich in whole grains, fish, and vegetables.",
                "Breakfast": "Whole-grain toast with avocado and a poached egg.",
                "Lunch": "Lentil soup with a side of whole-grain pita bread.",
                "Dinner": "Lamb chops with lemon-herb potatoes and a green bean salad.",
                "Snack": "Hummus with carrot and cucumber sticks.",
                "Grocery_Brands": {
                    "US": ["Dave's Killer Bread for whole-grain toast.", "Sabra for hummus.", "Amy's Kitchen for lentil soup."],
                    "IN": ["The Health Factory or La Americana for whole-grain bread.", "Wingreens Farms for hummus.", "Tata Sampann for lentils."]
                }
            },
            "Weight Gain": {
                "description": "A nutrient-dense Mediterranean plan to support healthy weight gain.",
                "Breakfast": "Shakshuka (eggs poached in tomato sauce) with feta and crusty bread.",
                "Lunch": "Moussaka (eggplant and minced meat casserole) with a side salad.",
                "Dinner": "Whole-wheat pasta with seafood (shrimp, mussels) in a garlic and tomato sauce.",
                "Snack": "A handful of dates and almonds.",
                "Grocery_Brands": {
                    "US": ["Barilla for whole-wheat pasta.", "Cento for canned tomatoes.", "Kar's Nuts for nut mixes."],
                    "IN": ["Borges for whole-wheat pasta.", "Happilo or Nutraj for dates and almonds.", "Keya for herbs and spices."]
                }
            }
        },
        "Vegetarian": {
            "Weight Loss": {
                "description": "A vegetarian Mediterranean plan for weight loss, emphasizing legumes and fresh produce.",
                "Breakfast": "Greek yogurt with fresh figs and a drizzle of honey.",
                "Lunch": "Large chickpea salad with tomatoes, cucumbers, bell peppers, and a lemon-tahini dressing.",
                "Dinner": "Stuffed bell peppers with rice, herbs, and lentils.",
                "Snack": "A peach or a pear.",
                "Grocery_Brands": {
                    "US": ["365 by Whole Foods Market for organic produce.", "Eden Organic for canned chickpeas.", "Lundberg Family Farms for rice."],
                    "IN": ["24 Mantra Organic for produce and staples.", "Organic Tattva for chickpeas and lentils.", "Daawat for rice."]
                }
            },
            "Maintenance": {
                "description": "A balanced vegetarian Mediterranean diet for overall wellness.",
                "Breakfast": "Oatmeal with dates, almonds, and a sprinkle of cinnamon.",
                "Lunch": "Spanakopita (spinach pie) with a side salad.",
                "Dinner": "Grilled halloumi cheese with roasted vegetables (zucchini, eggplant) and couscous.",
                "Snack": "A small bowl of olives and feta cheese.",
                "Grocery_Brands": {
                    "US": ["Bob's Red Mill for oatmeal.", "Near East for couscous.", "Athenos for feta and olives."],
                    "IN": ["Saffola for oats.", "Amul or Gowardhan for halloumi (paneer).", "Urban Platter for couscous."]
                }
            },
            "Weight Gain": {
                "description": "A calorie-rich vegetarian Mediterranean plan for gaining weight.",
                "Breakfast": "Smoothie with Greek yogurt, banana, honey, oats, and almond butter.",
                "Lunch": "Vegetarian moussaka using lentils and eggplant.",
                "Dinner": "Falafel in pita bread with hummus, tahini sauce, and a large salad.",
                "Snack": "Whole-grain bread dipped in extra virgin olive oil.",
                "Grocery_Brands": {
                    "US": ["Cedar's for hummus and tahini.", "Oikos for Greek yogurt.", "Bertolli for olive oil."],
                    "IN": ["Veeba or Wingreens for hummus and tahini.", "Dabur for honey.", "Pintola for almond butter."]
                }
            }
        },
        "Vegan": {
            "Weight Loss": {
                "description": "A light, plant-based Mediterranean plan for weight loss.",
                "Breakfast": "A bowl of fresh berries with a few almonds.",
                "Lunch": "Tabbouleh salad (parsley, mint, bulgur, tomato, lemon juice).",
                "Dinner": "Roasted vegetable platter (zucchini, eggplant, tomatoes) with a side of hummus.",
                "Snack": "An apple.",
                "Grocery_Brands": {
                    "US": ["Bob's Red Mill for bulgur wheat.", "Sabra for hummus.", "Driscoll's for berries."],
                    "IN": ["Urban Platter for bulgur wheat.", "Wingreens Farms for hummus.", "Local vendors for fresh produce."]
                }
            },
            "Maintenance": {
                "description": "A balanced vegan Mediterranean diet for sustained health.",
                "Breakfast": "Whole-grain toast with mashed avocado and a sprinkle of za'atar.",
                "Lunch": "Mujadara (lentils and rice with caramelized onions).",
                "Dinner": "Gigantes Plaki (giant beans baked in a tomato sauce).",
                "Snack": "A handful of walnuts and a pear.",
                "Grocery_Brands": {
                    "US": ["Ezekiel 4:9 for sprouted grain bread.", "Goya for beans and lentils.", "Spice Islands for za'atar."],
                    "IN": ["The Health Factory for bread.", "Tata Sampann for lentils.", "Keya for spices."]
                }
            },
            "Weight Gain": {
                "description": "A nutrient-dense vegan Mediterranean plan for weight gain.",
                "Breakfast": "Oatmeal with tahini, dates, and pistachios.",
                "Lunch": "Large falafel wrap with extra hummus and vegetables in a whole-wheat pita.",
                "Dinner": "Vegan paella with artichoke hearts, bell peppers, and chickpeas.",
                "Snack": "A handful of dried figs and nuts.",
                "Grocery_Brands": {
                    "US": ["Mighty Sesame Co. for tahini.", "Simple Truth (Kroger) for organic canned goods.", "Sun-Maid for dried figs."],
                    "IN": ["Urban Platter for tahini and vegan products.", "Happilo for dried fruits and nuts.", "So Good for plant-based milk."]
                }
            }
        }
    }
}

def get_user_input(prompt):
    """A robust function to get a positive number from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.", file=sys.stderr)
        except ValueError:
            print("Invalid input. Please enter a number.", file=sys.stderr)

def _get_choice_from_list(prompt_text, options, description_map=None):
    """Generic function to display a list of options and get a validated user choice."""
    print(prompt_text)
    for i, option in enumerate(options):
        description = f" ({description_map[option]})" if description_map and option in description_map else ""
        print(f"  {i+1}. {option}{description}")

    while True:
        try:
            choice = int(input(f"Your choice (1-{len(options)}): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(options)}.", file=sys.stderr)
        except ValueError:
            print("Invalid input. Please enter a number.", file=sys.stderr)

def get_market_preference():
    """Gets the user's market preference for brand recommendations."""
    markets = ["US", "IN"]
    market_descriptions = {"US": "Western", "IN": "Indian"}
    return _get_choice_from_list("\nSelect your market for brand recommendations:", markets, market_descriptions)

def get_user_preferences():
    """Gets the user's region, diet, and market preferences."""
    print("\n--- Personal Preferences ---")

    # --- Region Selection ---
    regions = list(MEAL_PLANS.keys())
    selected_region = _get_choice_from_list("Select your geological region:", regions)

    # --- Diet Selection ---
    diets = list(MEAL_PLANS[selected_region].keys())
    selected_diet = _get_choice_from_list("\nSelect your dietary preference:", diets)

    selected_market = get_market_preference()
    
    return selected_region, selected_diet, selected_market

def health_checkup():
    """
    Conducts a simple health check-up by calculating BMI.
    Returns the BMI and a corresponding health category.
    """
    print("\n--- Health Check-up ---")
    print("Let's start with a few basic measurements.")

    weight_kg = get_user_input("Enter your weight in kilograms (kg): ")
    height_cm = get_user_input("Enter your height in centimeters (cm): ")

    # Convert height from cm to meters for BMI calculation
    height_m = height_cm / 100
    
    # Calculate BMI: weight (kg) / (height (m))^2
    bmi = weight_kg / (height_m ** 2)

    print(f"\nYour Body Mass Index (BMI) is: {bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
        plan_key = "Weight Gain"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        plan_key = "Maintenance"
    elif 25 <= bmi < 30:
        category = "Overweight"
        plan_key = "Weight Loss"
    else: # bmi >= 30
        category = "Obese"
        plan_key = "Weight Loss"

    print(f"Based on your BMI, you are in the '{category}' category.")
    return plan_key

def display_food_plan(region, diet_type, plan_key, market, is_recommendation=True):
    """Displays a food plan based on the provided key."""
    try:
        plan = MEAL_PLANS[region][diet_type][plan_key]
    except KeyError:
        print(f"\nCould not find a suitable meal plan for {region}/{diet_type}/{plan_key}.", file=sys.stderr)
        return

    title_prefix = "Recommended" if is_recommendation else "Details for"

    print("\n" + "="*50)
    print(f"  {title_prefix} Food Plan: {plan_key} ({diet_type})")
    print(f"  Region: {region}")
    print("="*50)
    print(f"\nDescription: {plan['description']}\n")

    print(f"  - Breakfast: {plan['Breakfast']}")
    print(f"  - Lunch:     {plan['Lunch']}")
    print(f"  - Dinner:    {plan['Dinner']}")
    print(f"  - Snack:     {plan['Snack']}")

    if "Grocery_Brands" in plan and market in plan["Grocery_Brands"]:
        brands = plan["Grocery_Brands"][market]
        if brands:
            print(f"\n  --- Recommended Grocery Brands ({market}) ---")
            for brand in brands:
                print(f"  - {brand}")

    print("\n" + "="*50)
    if is_recommendation:
        print("\nDisclaimer: This is a sample plan. Consult a nutritionist for personalized advice.")

def browse_all_plans():
    """Allows the user to browse all available meal plans."""
    print("\n--- Browse All Meal Plans ---")
    print("Here you can see all the meal plans available in the app.")
    print("\nDisclaimer: These are sample plans. Consult a nutritionist for personalized advice.")
    
    market = get_market_preference()

    for region, diets in MEAL_PLANS.items():
        for diet_type, plans in diets.items():
            for plan_key in plans:
                display_food_plan(region, diet_type, plan_key, market, is_recommendation=False)
                input("\nPress Enter to see the next plan...")
    
    print("\n--- End of All Meal Plans ---")

def main():
    """Main function to run the health planner app."""
    while True:
        print("\nWelcome to the Health & Food Planner App!")
        print("1. Start Health Check-up & Get Food Plan")
        print("2. Browse All Meal Plans")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Get user preferences first
            region, diet_type, market = get_user_preferences()

            # Run the check-up to get the recommended health goal
            health_goal = health_checkup()
            
            # Display the corresponding food plan
            display_food_plan(region, diet_type, health_goal, market)

            input("\nPress Enter to return to the main menu...")
        
        elif choice == '2':
            browse_all_plans()
            input("\nPress Enter to return to the main menu...")

        elif choice == '3':
            print("Thank you for using the app. Stay healthy!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.", file=sys.stderr)

if __name__ == "__main__":
    main()