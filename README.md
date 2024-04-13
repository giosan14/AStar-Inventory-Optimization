## Summary

This project implements the A* heuristic search algorithm to optimize the sorting of inventory items in Amazon warehouses. The algorithm considers the locations of the robot, each inventory item, and the target destination to evaluate travel costs and find the optimal path.

## Problem Statement

Amazon aims to utilize a robot to sort inventory items within its warehouse. With three inventories located at specific positions in the warehouse, the robot's task is to move these inventories to a target position while avoiding collisions with defined obstacles (walls) along the way.

## Objective

The objective of this project is to implement the A* heuristic search function to solve a real-world problem involving robot navigation and inventory sorting. The model takes into account the robot's location, the location of each inventory item, and the final destination, evaluating travel costs to find the best path.

## Algorithm Overview

A* is a complete and optimal heuristic search algorithm that finds the shortest path between a starting point and a destination. The algorithm requires an initial state, a description of the goal states, and an admissible heuristic to measure progress towards the goal state.

## Solution Proposal

The project implements the A* algorithm by calculating the Manhattan heuristic function. The algorithm determines the optimal route from the robot's initial position to each inventory item's final position, considering obstacles and minimizing travel costs.

## Results

The initial implementation faced challenges regarding obstacle handling and coordinate input. However, after resolving these issues, the algorithm successfully generated optimal paths for inventory organization, respecting obstacles and item coordinates. Visual evidence, including GIFs and diagrams, demonstrates the algorithm's effectiveness in optimizing inventory sorting.

**Inventory Items:**

- Three inventory items are located at specific positions within the warehouse.
- Each inventory item must be moved to a designated target position.
- The robot navigates the warehouse environment, avoiding obstacles and efficiently transporting inventory items to their target locations.

**Visualization:**

To provide insight into the algorithm's functionality, the project includes a GIF demonstrating how the robot navigates the warehouse environment, picks up inventory items, and places them at their designated locations. This visualization showcases the algorithm's ability to optimize inventory sorting while avoiding obstacles and minimizing travel costs.
