from openai import OpenAI
import json
import random

client = OpenAI()

# Mock APIs
def weather_api(city, date):
    conditions = ["Sunny", "Partly Cloudy", "Overcast", "Light Rain", "Thunderstorms"]
    temp = random.randint(15, 30)
    condition = random.choice(conditions)
    humidity = random.randint(40, 80)
    return f"{condition}, {temp}°C, Humidity: {humidity}%"

def available_activities_api(city):
    activities = {
        "Paris": ["Sightseeing", "Museum Visits", "Cruise", "Shopping", "Food Tour"],
        "New York": ["Sightseeing", "Broadway Show", "Museum Visits", "Shopping", "Food Tour"],
        "Tokyo": ["Sightseeing", "Temple Visits", "Shopping", "Food Tour", "Anime Tour"]
    }
    return activities.get(city, ["Local Tour", "City Exploration", "Cultural Experience"])

def activity_details_api(city, activity):

    city = city.lower()
    activity = activity.lower()

    details = {
        "paris": {
            "eiffel tower": {
                "description": "The Eiffel Tower is an iconic symbol of Paris, offering panoramic views of the city from its observation decks.",
                "opening_hours": "9:00 AM - 12:45 AM",
                "ticket_price": "$25",
                "location": "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France"
            },
            "seine river cruise": {
                "description": "A Seine River Cruise provides a relaxing way to see the landmarks of Paris from the water.",
                "duration": "1 hour",
                "ticket_price": "$20",
                "departure_point": "Port de la Bourdonnais, 75007 Paris, France"
            },
            "louvre museum": {
                "description": "The Louvre Museum is the world's largest art museum, home to thousands of works including the Mona Lisa.",
                "opening_hours": "9:00 AM - 6:00 PM",
                "ticket_price": "$17",
                "location": "Rue de Rivoli, 75001 Paris, France"
            },
            "shopping": {
                "description": "Paris is a shopper's paradise, with famous shopping districts like Le Marais and the Champs-Élysées.",
                "famous_spots": ["Le Marais", "Champs-Élysées"],
                "average_cost": "Varies"
            }
        }
    }
    return details.get(city.lower(), {}).get(activity.lower(), {"description": "Activity details not found."})

def travel_api(origin, destination, date):
    airlines = ["AirFrance", "Delta", "JAL", "Lufthansa", "Emirates"]
    return f"{random.choice(airlines)} flight at {random.randint(0, 23):02d}:00, ${random.randint(500, 1500)}"

def restaurant_api(city):
    restaurants = {
        "Paris": ["Le Chateaubriand", "L'Ami Louis", "Septime", "Bistrot Paul Bert", "Clown Bar"]
    }
    return random.sample(restaurants.get(city, ["Local Cafe", "City Bistro"]), 2)

def city_transport_api(city):
    options = {
        "Paris": ["Metro", "Bus", "RER", "Taxi", "Bike rental"]
    }
    return random.sample(options.get(city, ["Bus", "Taxi"]), 2)

def high_level_planning_agent(query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a high-level planning agent. Generate a broad plan for the given trip query in JSON format."},
            {"role": "user", "content": f"""
## You have access to the following types of tools:
- Weather API: Get the weather for a city on a specific date
- Available Activities API: Get a list of available activities in a city
- Activity Details API: Get more details about a specific activity in a city
- Travel API: Get flight information from one city to another
- Restaurant API: Get popular restaurants in a city
- City Transport API: Get transportation options in a city
             
## Example Query:
- Plan a 3-day trip to Venice for next month
Output: {{
    "days": 3,
    "origin": "London",
    "destination": "Venice",
    "dates": ["2023-12-12", "2023-12-13", "2023-12-14"],
    "budget": 1000,
    "plan": [
        "Day 1: Travel plan from London to Venice", 
        "Day 2: Visit St. Mark's Basilica", 
        "Day 3: Gondola ride in Venice",
        "Day 4: Return to London"
    ]
}}

## Your task:
Create a high-level plan for: {query}
"""}
        ]
    )
    return json.loads(response.choices[0].message.content)

def detailed_planning_agent(high_level_plan):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a detailed planning agent. Expand the high-level plan with specific API calls and parameters in JSON format."},
            {"role": "user", "content": f"""
## You have access to the following APIs:
- Weather API: Get the weather for a city on a specific date
Parameters: city, date
- Available Activities API: Get a list of available activities in a city
Parameters: city
- Activity Details API: Get more details about a specific activity in a city
Parameters: city, activity
- Travel API: Get flight information from one city to another
Parameters: origin, destination, date
- Restaurant API: Get restaurant recommendations in a city
Parameters: city
- City Transport API: Get transportation options within a city
Parameters: city

## Instructions:
- Use the high-level plan to generate a detailed plan with specific API calls and parameters.
- Ensure that the plan stays within the specified budget.
- Write the detailed plan in JSON format than lists the steps with API calls and parameters.

## Example Output:
{{
    "steps": [
        {{
            "description": "Check weather in Venice",
            "api": "weather_api",
            "parameters": {{
                "city": "Venice",
                "date": "2023-12-15"
            }}
        }},
        {{
            "description": "Book flight to Venice",
            "api": "travel_api",
            "parameters": {{
                "origin": "London",
                "destination": "Venice",
                "date": "2023-12-15"
            }}
        }}
    ]
}}

## Your task:
Create a detailed plan for: {json.dumps(high_level_plan)}
Ensure that the plan stays within the specified budget.
"""
            }
        ]
    )
    return json.loads(response.choices[0].message.content)

def action_agent(detailed_plan):
    results = []
    for step in detailed_plan['steps']:
        if step['api'] == 'weather_api':
            result = weather_api(step['parameters']['city'], step['parameters']['date'])
        elif step['api'] == 'available_activities_api':
            result = available_activities_api(step['parameters']['city'])
        elif step['api'] == 'activity_details_api':
            result = activity_details_api(step['parameters']['city'], step['parameters']['activity'])
        elif step['api'] == 'travel_api':
            result = travel_api(step['parameters']['origin'], step['parameters']['destination'], step['parameters']['date'])
        elif step['api'] == 'restaurant_api':
            result = restaurant_api(step['parameters']['city'])
        elif step['api'] == 'city_transport_api':
            result = city_transport_api(step['parameters']['city'])
        else:
            result = f"Unknown API: {step['api']}"
        results.append({"step": step['description'], "result": result})
    return results

def writing_agent(query, action_results):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are an expert trip planning writing agent. Synthesize the given results into a coherent trip plan with detailed information."},
            {"role": "user", "content": f"Query: {query}\n\nResults: {json.dumps(action_results)}"}
        ]
    )
    return response.choices[0].message.content

def seqrag(query):
    print(f"Query: {query}")
    
    high_level_plan = high_level_planning_agent(query)
    print(f"\nHigh-Level Plan: {json.dumps(high_level_plan, indent=2)}")
    
    detailed_plan = detailed_planning_agent(high_level_plan)
    print(f"\nDetailed Plan: {json.dumps(detailed_plan, indent=2)}")
    
    action_results = action_agent(detailed_plan)
    print(f"\nAction Results: {json.dumps(action_results, indent=2)}")
    
    final_response = writing_agent(query, action_results)
    print(f"\nFinal Trip Plan:\n{final_response}")

if __name__ == "__main__":
    query = "Plan a 3-day trip to Paris for next month from New York"
    seqrag(query)
