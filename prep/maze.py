"""
Generate a maze then make turtle navigate it.

@author: ChatGPT on 1/28/2024 after several prompts
@author: Amin G. Alhashim (aalhashi@macalester.edu)

Prompts Used -------------------------------------------------------------------
Take the role of Python expert

Can you generate a Python turtle code that first randomly generate a maze of
size n by n where n is read from the user then place a turtle randomly inside
the maze and make it solve the maze

can you ensure the maze have a path

The maze is still does not have a path

The turtle is not finding the path

The turtle is jumping over the wall!!!

The turtle is still jump over the wall!!!
"""

import turtle
import random

def generate_maze_with_path(n):
    maze = [['WALL' for _ in range(n)] for _ in range(n)]
    stack = [(0, 0)]
    visited = set([(0, 0)])

    while stack:
        x, y = stack[-1]

        neighbors = [(x, y - 2), (x, y + 2), (x - 2, y), (x + 2, y)]
        unvisited_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited]

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            maze[(x + nx) // 2][(y + ny) // 2] = 'EMPTY'
            maze[nx][ny] = 'EMPTY'
            visited.add((nx, ny))
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

def display_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'WALL':
                turtle.penup()
                turtle.goto(j * 20 - n * 10, n * 10 - i * 20)
                turtle.pendown()
                turtle.setheading(0)
                turtle.forward(20)
                turtle.right(90)
                turtle.forward(20)
                turtle.right(90)
                turtle.forward(20)
                turtle.right(90)
                turtle.forward(20)
                turtle.right(90)

def place_turtle(maze):
    while True:
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        if maze[x][y] == 'EMPTY':
            return x, y

def solve_maze(maze, start_x, start_y):
    turtle.penup()
    turtle.goto(start_y * 20 - n * 10 + 10, n * 10 - start_x * 20 - 10)
    turtle.pendown()
    turtle.shape("turtle")
    turtle.color("red")

    turtle.speed(1)
    turtle.pendown()

    stack = [(start_x, start_y)]

    while stack:
        x, y = stack[-1]

        if x == n - 1 and y == n - 1:
            break

        neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 'EMPTY']

        if valid_neighbors:
            nx, ny = valid_neighbors[0]
            stack.append((nx, ny))
            maze[nx][ny] = 'VISITED'  # Mark the visited cell to ensure the turtle doesn't revisit it
            turtle.setheading(turtle.towards(ny * 20 - n * 10 + 10, n * 10 - nx * 20 - 10))
            turtle.goto(ny * 20 - n * 10 + 10, n * 10 - nx * 20 - 10)
            turtle.stamp()
        else:
            stack.pop()

n = 10
turtle.speed(0)
maze = generate_maze_with_path(n)
display_maze(maze)
start_x, start_y = place_turtle(maze)
solve_maze(maze, start_x, start_y)
turtle.done()
