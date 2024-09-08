# SeqRAG: A Practical Agent Architecture for Sequential Planning with Retrieval-Augmented Generation
## Overview
SeqRAG (Sequential Retrieval-Augmented Generation) is a robust agent architecture designed to simplify multistep AI problem-solving through a structured, sequential approach. This repository provides an implementation of SeqRAG, demonstrating its capabilities through a trip-planning example. By leveraging OpenAI's GPT models, SeqRAG transforms complex planning tasks into manageable, step-by-step processes, enabling more effective problem-solving.


## Context
Generative AI models and Retrieval-Augmented Generation (RAG) have significantly advanced AI capabilities, enabling more autonomous systems. Despite this, many frameworks—such as Microsoft's AutoGen, ReAct, and PlanRAG—struggle with multistep task execution in production settings. Through extensive experimentation, we identified challenges in building reliable, production-ready AI agents.

SeqRAG addresses these challenges by breaking down tasks into clearly defined, sequential steps, each optimized for a specific function. Designed for simplicity, reliability, and ease of implementation, SeqRAG is a practical solution for deploying AI agents in real-world scenarios that require structured problem-solving.

## Key Components
The code implements the following agents to form a coherent architecture for task execution:

1. **High-Level Planning Agent (HLPA)**: Generates a broad, step-by-step plan for a task using OpenAI's GPT models.
2. **Detailed Planning Agent (DPA)**: Breaks down each high-level step into detailed actions, specifying tools and parameters.
3. **Action Agent (AA)**: Executes the detailed actions using predefined APIs and mock data.
4. **Writing Agent (WA)**: Combines the results into a final, coherent output.

### Trip Planning Example
In this demonstration, SeqRAG is applied to trip planning:

1. **Query Input**: The user provides a query such as “Plan a 3-day trip to Paris next month from New York.”
2. **High-Level Plan**: The HLPA outlines key steps like booking flights, accommodation, creating a daily itinerary, and arranging local transportation.
3. **Detailed Plan**: The DPA specifies exact tools and services (e.g., FlightSearchAPI for flights, HotelBookingAPI for accommodations).
4. **Execution**: The AA retrieves the relevant data using mock APIs, executing each step in sequence.
5. **Final Output**: The WA synthesizes the gathered information into a complete travel itinerary.

## How to Run the Code

### 1. Install Dependencies
Ensure the required dependencies are installed. Run the following command:
```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
Add your OpenAI API key in the `.env` file:
```
OPENAI_API_KEY=<your-api-key-here>
```

### 3. Run the Application
To generate a plan based on a sample query, execute the following command:
```bash
python app.py
```

### Optional: Create a Local Environment
For better isolation, you can create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

## Advantages of SeqRAG
1. **Efficiency**: Sequential planning allows faster execution in time-critical environments by minimizing reprocessing.
2. **Consistency**: The step-by-step approach provides consistent outputs across multiple runs.
3. **Reduced Overhead**: By avoiding constant replanning, SeqRAG lowers computational costs.
4. **Easier Debugging**: The modular structure helps isolate issues, simplifying debugging.
5. **Tailored for Complex Queries**: Optimized for multistep planning, especially in tasks requiring detailed decision-making.

## Limitations of SeqRAG
1. **Limited Adaptability**: It may struggle with dynamically changing or unanticipated information.
2. **Dependency on Initial Planning**: The quality of the output heavily relies on the initial plan's effectiveness.
3. **Overspecialization**: While great for specific tasks, SeqRAG may not be as versatile for general-purpose problem-solving.

## Why Use SeqRAG?
SeqRAG streamlines multistep AI problem-solving by organizing tasks into methodical steps, increasing clarity, predictability, and overall efficiency. The trip-planning example highlights its ability to handle complex, context-dependent tasks while delivering reliable results.

By focusing on structured problem-solving, SeqRAG offers a practical solution for developers looking to deploy AI agents in real-world, production-ready scenarios.
