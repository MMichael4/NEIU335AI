## Zero-Shot Prompting Example

You are a CS 335 teaching assistant. Write a Python function that implements breadth-first search (BFS) on a 
graph represented as an adjacency list, and briefly explain its time and space complexity."


## Few-Shot Prompting Example
I love CS 335! // Positive
Professor Omeed talks to much // Negative
Summer in Chicago is awesome // Positive
Class is usually boring //


## Chain-of-Thought Prompting Example
You are a teaching assistant for CS 335. Solve the following search problem step-by-step:
Graph:
  • A–B has weight 2
  • B–C has weight 3
  • A–C has weight 10
Question: What is the shortest path from A to C? Explain each step of your reasoning.

--
Expected Outline:
1. List possible paths and calculate weights
2. Compare totals
3. Select the minimum and state conclusion