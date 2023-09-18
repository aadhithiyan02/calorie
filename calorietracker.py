# import streamlit as st
# import numpy as np
# import plotly.express as px
# import pandas as pd

# # Initialize variables
# calorie_goal_limit = 2500
# protein_goal = 180
# fat_goal = 80
# carbs_goal = 250

# # Initialize session state to store data persistently
# if 'today' not in st.session_state:
#     st.session_state.today = []

# class Food:
#     def __init__(self, name, calories, proteins, fats, carbs):
#         self.name = name
#         self.calories = calories
#         self.proteins = proteins
#         self.fats = fats
#         self.carbs = carbs

# # Streamlit app
# st.title("Food Intake Tracker")

# # Sidebar for changing goal intake values
# st.sidebar.subheader("Set Goal Intake Values")
# calorie_goal_limit = st.sidebar.number_input("Calorie Goal", min_value=0)
# protein_goal = st.sidebar.number_input("Protein Goal (grams)", min_value=0)
# fat_goal = st.sidebar.number_input("Fat Goal (grams)", min_value=0)
# carbs_goal = st.sidebar.number_input("Carbs Goal (grams)", min_value=0)

# menu_choice = st.sidebar.selectbox("Select an option", ["Add Food Intake", "Visualize Progress", "View Food Intake", "Quit"])

# if menu_choice == "Add Food Intake":
#     st.header("Add New Food Intake")
#     name = st.text_input("Enter food name")
#     calories = st.number_input("Enter calories", min_value=0)
#     proteins = st.number_input("Enter protein (grams)", min_value=0)
#     fats = st.number_input("Enter fat (grams)", min_value=0)
#     carbs = st.number_input("Enter carbs (grams)", min_value=0)

#     if st.button("Add Food"):
#         food = Food(name, calories, proteins, fats, carbs)
#         st.session_state.today.append(food)
#         st.success("Food added successfully!")

# if menu_choice == "Visualize Progress":
#     st.header("Visualize Progress")
    
#     # Initialize with 0 to avoid NaN errors
#     calories_sum = 0
#     proteins_sum = 0
#     fats_sum = 0
#     carbs_sum = 0
    
#     if st.session_state.today:
#         calories_sum = sum(food.calories for food in st.session_state.today)
#         proteins_sum = sum(food.proteins for food in st.session_state.today)
#         fats_sum = sum(food.fats for food in st.session_state.today)
#         carbs_sum = sum(food.carbs for food in st.session_state.today)

#     st.subheader("Macro Nutrients Distribution")

#     # Create a Plotly pie chart
#     fig1 = px.pie(names=["Proteins", "Fats", "Carbs"], values=[proteins_sum, fats_sum, carbs_sum], title="Macro Nutrients Distribution")
#     st.plotly_chart(fig1)

#     st.subheader("Macro Nutrients Progress")
    
#     # Create a DataFrame for progress
#     progress_data = {
#         'Nutrient': ["Proteins", "Fats", "Carbs", "Calories"],
#         'Intake': [proteins_sum, fats_sum, carbs_sum, calories_sum],
#         'Goal': [protein_goal, fat_goal, carbs_goal, calorie_goal_limit]
#     }
#     df_progress = pd.DataFrame(progress_data)
    
#     # Create a Plotly bar chart for progress
#     fig2 = px.bar(df_progress, x='Nutrient', y=['Intake', 'Goal'], title="Macro Nutrients Progress")
#     st.plotly_chart(fig2)

#     st.subheader("Calories Goal vs Calories Taken")
    
#     # Create a Plotly line chart for calories goal vs. taken
#     fig3 = px.line(df_progress, x='Nutrient', y=['Intake', 'Goal'], title="Calories Goal vs Calories Taken")
#     st.plotly_chart(fig3)

#     # Additional Charts
#     st.subheader("Nutrient Distribution Bar Chart")
#     nutrient_values = [proteins_sum, fats_sum, carbs_sum]
#     fig4 = px.bar(x=["Proteins", "Fats", "Carbs"], y=nutrient_values, labels={'x':'Nutrient', 'y':'Intake (grams)'}, title="Nutrient Distribution")
#     st.plotly_chart(fig4)

#     st.subheader("Calories vs. Time Line Chart")
#     calories_per_meal = [food.calories for food in st.session_state.today]
#     meal_times = [f"Meal {i+1}" for i in range(len(calories_per_meal))]
#     fig5 = px.line(x=meal_times, y=calories_per_meal, labels={'x':'Meal Time', 'y':'Calories'}, title="Calories vs. Time")
#     st.plotly_chart(fig5)

#     st.subheader("Nutrient Ratio Pie Chart")
#     nutrient_ratios = [proteins_sum / protein_goal, fats_sum / fat_goal, carbs_sum / carbs_goal]
#     fig6 = px.pie(names=["Proteins", "Fats", "Carbs"], values=nutrient_ratios, title="Nutrient Ratio")
#     st.plotly_chart(fig6)

#     st.subheader("Calories vs. Nutrients Scatter Plot")
#     fig7 = px.scatter(df_progress, x='Calories', y='Intake', color='Nutrient', labels={'x':'Calories', 'y':'Nutrient Intake'}, title="Calories vs. Nutrients")
#     st.plotly_chart(fig7)

# if menu_choice == "View Food Intake":
#     st.header("View Food Intake")
#     st.subheader("List of Foods Eaten Today")
    
#     # Display the list of foods eaten
#     if st.session_state.today:
#         for i, food in enumerate(st.session_state.today):
#             st.write(f"{i + 1}. Food: {food.name}, Calories: {food.calories}, Proteins: {food.proteins}, Fats: {food.fats}, Carbs: {food.carbs}")
        
#         # Provide the option to delete a food intake
#         delete_food = st.selectbox("Select a food to delete:", [food.name for food in st.session_state.today])
        
#         if st.button("Delete Food"):
#             # Find and remove the selected food from the list
#             for food in st.session_state.today:
#                 if food.name == delete_food:
#                     st.session_state.today.remove(food)
#             st.success(f"{delete_food} has been removed from your food intake.")
#     else:
#         st.write("No food intake recorded yet.")

# if menu_choice == "Quit":
#     st.text("Thank you for using the Food Intake Tracker!")


# import streamlit as st
# import numpy as np
# import plotly.express as px
# import pandas as pd

# # Initialize variables
# calorie_goal_limit = 2500
# protein_goal = 180
# fat_goal = 80
# carbs_goal = 250

# # Initialize session state to store data persistently
# if 'today' not in st.session_state:
#     st.session_state.today = []

# class Food:
#     def __init__(self, name, calories, proteins, fats, carbs):
#         self.name = name
#         self.calories = calories
#         self.proteins = proteins
#         self.fats = fats
#         self.carbs = carbs

# # Streamlit app
# st.title("Food Intake Tracker")

# # Sidebar for changing goal intake values
# st.sidebar.subheader("Set Goal Intake Values")
# calorie_goal_limit = st.sidebar.number_input("Calorie Goal", min_value=0)
# protein_goal = st.sidebar.number_input("Protein Goal (grams)", min_value=0)
# fat_goal = st.sidebar.number_input("Fat Goal (grams)", min_value=0)
# carbs_goal = st.sidebar.number_input("Carbs Goal (grams)", min_value=0)

# menu_choice = st.sidebar.selectbox("Select an option", ["Add Food Intake", "Visualize Progress", "View Food Intake", "Quit"])

# if menu_choice == "Add Food Intake":
#     st.header("Add New Food Intake")
#     name = st.text_input("Enter food name")
#     calories = st.number_input("Enter calories", min_value=0)
#     proteins = st.number_input("Enter protein (grams)", min_value=0)
#     fats = st.number_input("Enter fat (grams)", min_value=0)
#     carbs = st.number_input("Enter carbs (grams)", min_value=0)

#     if st.button("Add Food"):
#         food = Food(name, calories, proteins, fats, carbs)
#         st.session_state.today.append(food)
#         st.success("Food added successfully!")

# if menu_choice == "Visualize Progress":
#     st.header("Visualize Progress")
    
#     # Initialize with 0 to avoid NaN errors
#     calories_sum = 0
#     proteins_sum = 0
#     fats_sum = 0
#     carbs_sum = 0
    
#     if st.session_state.today:
#         calories_sum = sum(food.calories for food in st.session_state.today)
#         proteins_sum = sum(food.proteins for food in st.session_state.today)
#         fats_sum = sum(food.fats for food in st.session_state.today)
#         carbs_sum = sum(food.carbs for food in st.session_state.today)

#     st.subheader("Macro Nutrients Distribution")

#     # Create a Plotly pie chart
#     fig1 = px.pie(names=["Proteins", "Fats", "Carbs"], values=[proteins_sum, fats_sum, carbs_sum], title="Macro Nutrients Distribution")
#     st.plotly_chart(fig1)

#     st.subheader("Macro Nutrients Progress")
    
#     # Create a DataFrame for progress
#     progress_data = {
#         'Nutrient': ["Proteins", "Fats", "Carbs", "Calories"],
#         'Intake': [proteins_sum, fats_sum, carbs_sum, calories_sum],
#         'Goal': [protein_goal, fat_goal, carbs_goal, calorie_goal_limit]
#     }
#     df_progress = pd.DataFrame(progress_data)
    
#     # Create a Plotly bar chart for progress
#     fig2 = px.bar(df_progress, x='Nutrient', y=['Intake', 'Goal'], title="Macro Nutrients Progress")
#     st.plotly_chart(fig2)

#     st.subheader("Calories Goal vs Calories Taken")
    
#     # Create a Plotly line chart for calories goal vs. taken
#     fig3 = px.line(df_progress, x='Nutrient', y=['Intake', 'Goal'], title="Calories Goal vs Calories Taken")
#     st.plotly_chart(fig3)

#     # Additional Charts
#     st.subheader("Nutrient Distribution Bar Chart")
#     nutrient_values = [proteins_sum, fats_sum, carbs_sum]
#     fig4 = px.bar(x=["Proteins", "Fats", "Carbs"], y=nutrient_values, labels={'x':'Nutrient', 'y':'Intake (grams)'}, title="Nutrient Distribution")
#     st.plotly_chart(fig4)

#     st.subheader("Calories vs. Time Line Chart")
#     calories_per_meal = [food.calories for food in st.session_state.today]
#     meal_times = [f"Meal {i+1}" for i in range(len(calories_per_meal))]
#     fig5 = px.line(x=meal_times, y=calories_per_meal, labels={'x':'Meal Time', 'y':'Calories'}, title="Calories vs. Time")
#     st.plotly_chart(fig5)

#     st.subheader("Nutrient Ratio Pie Chart")
#     nutrient_ratios = [proteins_sum / protein_goal, fats_sum / fat_goal, carbs_sum / carbs_goal]
#     fig6 = px.pie(names=["Proteins", "Fats", "Carbs"], values=nutrient_ratios, title="Nutrient Ratio")
#     st.plotly_chart(fig6)

#     st.subheader("Calories vs. Nutrients Scatter Plot")
#     fig7 = px.scatter(df_progress, x='Calories', y='Intake', color='Nutrient', labels={'x':'Calories', 'y':'Nutrient Intake'}, title="Calories vs. Nutrients")
#     st.plotly_chart(fig7)

#     st.subheader("Calories Taken vs Calories Remaining")
#     calories_remaining = max(calorie_goal_limit - calories_sum, 0)
#     calories_data = [calories_sum, calories_remaining]
#     fig8 = px.bar(x=["Calories Taken", "Calories Remaining"], y=calories_data, labels={'x':'', 'y':'Calories'}, title="Calories Taken vs Calories Remaining")
#     st.plotly_chart(fig8)

# if menu_choice == "View Food Intake":
#     st.header("View Food Intake")
#     st.subheader("List of Foods Eaten Today")
    
#     # Display the list of foods eaten
#     if st.session_state.today:
#         for i, food in enumerate(st.session_state.today):
#             st.write(f"{i + 1}. Food: {food.name}, Calories: {food.calories}, Proteins: {food.proteins}, Fats: {food.fats}, Carbs: {food.carbs}")
        
#         # Provide the option to delete a food intake
#         delete_food = st.selectbox("Select a food to delete:", [food.name for food in st.session_state.today])
        
#         if st.button("Delete Food"):
#             # Find and remove the selected food from the list
#             for food in st.session_state.today:
#                 if food.name == delete_food:
#                     st.session_state.today.remove(food)
#             st.success(f"{delete_food} has been removed from your food intake.")
#     else:
#         st.write("No food intake recorded yet.")

# if menu_choice == "Quit":
#     st.text("Thank you for using the Food Intake Tracker!")

import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

# Initialize variables
calorie_goal_limit = 2500
protein_goal = 180
fat_goal = 80
carbs_goal = 250

# Initialize session state to store data persistently
if 'today' not in st.session_state:
    st.session_state.today = []

class Food:
    def __init__(self, name, calories, proteins, fats, carbs):
        self.name = name
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs

# Streamlit app
st.title("Food Intake Tracker")

# Sidebar for changing goal intake values
st.sidebar.subheader("Set Goal Intake Values")
calorie_goal_limit = st.sidebar.number_input("Calorie Goal", min_value=0)
protein_goal = st.sidebar.number_input("Protein Goal (grams)", min_value=0)
fat_goal = st.sidebar.number_input("Fat Goal (grams)", min_value=0)
carbs_goal = st.sidebar.number_input("Carbs Goal (grams)", min_value=0)

menu_choice = st.sidebar.selectbox("Select an option", ["Add Food Intake", "Visualize Progress", "View Food Intake", "Quit"])

if menu_choice == "Add Food Intake":
    st.header("Add New Food Intake")
    name = st.text_input("Enter food name")
    calories = st.number_input("Enter calories", min_value=0)
    proteins = st.number_input("Enter protein (grams)", min_value=0)
    fats = st.number_input("Enter fat (grams)", min_value=0)
    carbs = st.number_input("Enter carbs (grams)", min_value=0)

    if st.button("Add Food"):
        food = Food(name, calories, proteins, fats, carbs)
        st.session_state.today.append(food)
        st.success("Food added successfully!")

if menu_choice == "Visualize Progress":
    st.header("Visualize Progress")
    
    # Initialize with 0 to avoid NaN errors
    calories_sum = 0
    proteins_sum = 0
    fats_sum = 0
    carbs_sum = 0
    
    if st.session_state.today:
        calories_sum = sum(food.calories for food in st.session_state.today)
        proteins_sum = sum(food.proteins for food in st.session_state.today)
        fats_sum = sum(food.fats for food in st.session_state.today)
        carbs_sum = sum(food.carbs for food in st.session_state.today)

    st.subheader("Macro Nutrients Distribution")

    # Create a Plotly pie chart
    fig1 = px.pie(names=["Proteins", "Fats", "Carbs"], values=[proteins_sum, fats_sum, carbs_sum], title="Macro Nutrients Distribution")
    st.plotly_chart(fig1)

    st.subheader("Macro Nutrients Progress")
    
    # Create a DataFrame for progress
    progress_data = {
         'Nutrient': ["Proteins", "Fats", "Carbs", "Calories"],
         'Intake': [proteins_sum, fats_sum, carbs_sum, calories_sum],
         'Goal': [protein_goal, fat_goal, carbs_goal, calorie_goal_limit]
     }
    df_progress = pd.DataFrame(progress_data)
    
     # Create a Plotly bar chart for progress
    fig2 = px.bar(df_progress, x='Nutrient', y=['Intake', 'Goal'], title="Macro Nutrients Progress")
    st.plotly_chart(fig2)

    st.subheader("Calories Goal vs Calories Taken")
    
    # Create a Plotly line chart for calories goal vs. taken
    fig3 = px.line(df_progress, x='Nutrient', y=['Intake', 'Goal'], title="Calories Goal vs Calories Taken")
    st.plotly_chart(fig3)

    # Additional Charts
    st.subheader("Nutrient Distribution Bar Chart")
    nutrient_values = [proteins_sum, fats_sum, carbs_sum]
    fig4 = px.bar(x=["Proteins", "Fats", "Carbs"], y=nutrient_values, labels={'x':'Nutrient', 'y':'Intake (grams)'}, title="Nutrient Distribution")
    st.plotly_chart(fig4)

    st.subheader("Calories vs. Time Line Chart")
    calories_per_meal = [food.calories for food in st.session_state.today]
    meal_times = [f"Meal {i+1}" for i in range(len(calories_per_meal))]
    fig5 = px.line(x=meal_times, y=calories_per_meal, labels={'x':'Meal Time', 'y':'Calories'}, title="Calories vs. Time")
    st.plotly_chart(fig5)

    st.subheader("Nutrient Ratio Pie Chart")
    nutrient_ratios = [proteins_sum / protein_goal, fats_sum / fat_goal, carbs_sum / carbs_goal]
    fig6 = px.pie(names=["Proteins", "Fats", "Carbs"], values=nutrient_ratios, title="Nutrient Ratio")
    st.plotly_chart(fig6)

    st.subheader("Calories Taken vs Calories Remaining")
    calories_remaining = max(calorie_goal_limit - calories_sum, 0)
    calories_data = [calories_sum, calories_remaining]
    fig8 = px.pie(names=['Calories intaken','Calories Remaining'],values=calories_data, title="Calories Taken vs Calories Remaining")
    st.plotly_chart(fig8)

if menu_choice == "View Food Intake":
    st.header("View Food Intake")
    st.subheader("List of Foods Eaten Today")
    
    # Display the list of foods eaten
    if st.session_state.today:
        for i, food in enumerate(st.session_state.today):
            st.write(f"{i + 1}. Food: {food.name}, Calories: {food.calories}, Proteins: {food.proteins}, Fats: {food.fats}, Carbs: {food.carbs}")
        
        # Provide the option to delete a food intake
        delete_food = st.selectbox("Select a food to delete:", [food.name for food in st.session_state.today])
        
        if st.button("Delete Food"):
            # Find and remove the selected food from the list
            for food in st.session_state.today:
                if food.name == delete_food:
                    st.session_state.today.remove(food)
            st.success(f"{delete_food} has been removed from your food intake.")
    else:
        st.write("No food intake recorded yet.")

if menu_choice == "Quit":
    st.text("Thank you for using the Food Intake Tracker!")
