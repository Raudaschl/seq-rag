# SeqRAG: A Practical Agent Architecture for Sequential Planning with Retrieval-Augmented Generation
## Overview
The code accompanying this README is an implementation of SeqRAG (Sequential Retrieval-Augmented Generation), a robust agent architecture designed to simplify multistep plan based AI problem-solving. This project demonstrates SeqRAG through a trip planning example, showcasing how this architecture can generate detailed travel itineraries. By leveraging OpenAI's GPT models, SeqRAG streamlines complex planning processes into a series of manageable, sequential steps.

## Context
The rise of generative AI models and Retrieval-Augmented Generation (RAG) has transformed the AI landscape, enabling more sophisticated and autonomous capabilities. However, while there is significant excitement around AI agents, existing frameworks often fall short in handling the intricacies of multistep tasks in production environments. After extensive experimentation with promising frameworks like Microsoft's AutoGen, ReAct, and PlanRAG, we've discovered that creating truly effective, production-ready AI agents remains a significant challenge.

SeqRAG (Sequential Retrieval-Augmented Generation) aims to bridge this gap by structuring problem-solving into a sequence of clearly defined steps, each optimized for specific tasks. This agent architecture is designed with simplicity and reliability in mind, ensuring that each component of the problem is tackled methodically. By focusing on ease of implementation and robust performance, SeqRAG offers a practical solution for deploying AI agents in real-world scenarios.

SeqRAG is detailed in the [article](), "Sequential Retrieval-Augmented Generation: A Modular Approach to AI Problem-Solving," which explores how this methodology can enhance various applications, including search technologies and task automation.

## What The Code Does
1. **High-Level Planning Agent (HLPA)**: Generates a broad, step-by-step plan for a given task using OpenAI's GPT models.
2. **Detailed Planning Agent (DPA)**: Expands the high-level plan with specific tools and parameters for each step.
3. **Action Agent (AA)**: Executes each step sequentially, utilizing predefined APIs and mock data.
4. **Writing Agent (WA)**: Compiles the results of each step into a coherent final output.

### Trip Planning Example
In this example, the SeqRAG agent architecture is used to create a detailed travel itinerary:

- **Query Input**: The user provides details about the trip (e.g., "Plan a 3-day trip to Paris for next month from New York").
- **High-Level Plan**: HLPA outlines necessary steps such as flight booking, accommodation, itinerary planning, and local transportation.
- **Detailed Plan**: DPA specifies exact tools and parameters for each step (e.g., FlightSearchAPI for flights, HotelBookingAPI for accommodations).
- **Execution**: AA sequentially executes each step using mock APIs to retrieve relevant data.
- **Final Output**: WA synthesizes the results into a comprehensive trip plan.

## How to Run the Code
1. **Install Dependencies**: Ensure you have the required dependencies installed.
   ```sh
   pip install openai
   ```
2. **Set Up API Key**: Place your OpenAI API key in the appropriate spot in the .env file.
3. **Run the Script**: Execute the script with a sample query.
   ```sh
   python app.py
   ```

## Advantages of SeqRAG
1. **Efficiency in Time-Critical Environments**: The predetermined plan allows for faster execution, crucial in production environments.
2. **Consistency**: The structured approach leads to more consistent results across multiple runs.
3. **Reduced Computational Overhead**: By avoiding continuous replanning, SeqRAG potentially reduces computational requirements.
4. **Simplified Debugging**: The clear, step-by-step plan makes it easier to identify and fix issues in the process.
5. **Specialization for Planning Queries**: Tailored for complex, multistep planning queries, addressing a specific niche effectively.

## Limitations of SeqRAG
1. **Limited Adaptability**: May not handle unexpected information or changes as flexibly as more adaptive approaches.
2. **Dependency on Initial Planning Quality**: The effectiveness heavily relies on the quality of the initial plan.
3. **Potential Overspecialization**: Might be less versatile for general-purpose problem-solving compared to more flexible approaches.

## Why SeqRAG?

SeqRAG is an agent architecture designed to make multistep AI problem-solving more accessible and reliable by structuring tasks into a series of well-defined steps. This approach not only enhances the clarity and predictability of the process but also improves overall efficiency and performance. By demonstrating SeqRAG through the trip planning example, we showcase its potential to simplify and enhance complex, context-dependent tasks, ensuring each step is handled methodically by specialized agents.