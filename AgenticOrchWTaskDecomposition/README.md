This project explores Langgraph based Agentic Orchestration with Task Decomposition

Agent Orchestrator with Task Decomposition
This project combines task decomposition capabilities with agent selection to create a powerful workflow that:

Decomposes complex tasks into smaller, manageable steps
Selects the most appropriate agent for each step based on embeddings similarity
Executes each step with the selected agent
Reflects on the results and adjusts as needed
Features
Task Decomposition: Breaks down complex queries into manageable steps
Dynamic Agent Selection: Uses embeddings to select the most appropriate agent for each step
Reflection and Replanning: Evaluates results and replans if necessary
Local Execution: Uses Ollama models for privacy and no API costs
Comprehensive Summary: Generates a detailed summary of the workflow execution

Available Agents
General Conversation Agent: For casual conversations and general questions
Technical Support Agent: For programming and technical questions
Creative Writing Agent: For storytelling and creative content
Business Consultant Agent: For business strategy and professional advice
Health & Wellness Agent: For health, fitness, and wellness guidance
How It Works
Planning Phase: The LLM creates a detailed plan to solve the problem
Agent Selection Phase: For each step, the most appropriate agent is selected using embedding similarity
Execution Phase: The selected agent executes the current step
Reflection Phase: Results are evaluated to determine if they meet requirements
Decision Phase: Either continue with next steps or replan if results are not satisfactory
Summary Phase: A comprehensive summary of the workflow is generated
Example
Input:

I want to create a personal finance tracking app. Help me understand what features it should have, how to implement it, and what technologies to use.
The system will:

Break this down into steps (feature planning, technology selection, implementation strategy, etc.)
Select appropriate agents for each step (business consultant for features, technical support for technologies, etc.)
Execute each step with the selected agent
Generate a comprehensive summary of the plan
