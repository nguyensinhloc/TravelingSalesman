# Ask the user to input the number of cities
n = int(input("Enter the number of cities: "))

# Initialize an empty distance matrix
dist = []

# Ask the user to input the distance matrix row by row
for i in range(n):
    # Split the input by spaces and convert each element to an integer
    row = list(map(int, input(f"Enter the distances from city {i}: ").split()))
    # Check if the input is valid
    if len(row) != n or row[i] != -1:
        print("Invalid input. Please enter a valid distance matrix.")
        break
    # Append the row to the distance matrix
    dist.append(row)
else:
    # The rest of the code is unchanged from the previous script
    # Choose a starting city
    start = 0

    # Initialize the tour and the cost
    tour = [start]
    cost = 0

    # Mark the starting city as visited
    visited = [False] * n
    visited[start] = True

    # Repeat until all cities are visited
    while len(tour) < n:
        # Find the nearest unvisited city from the current city
        min_dist = float('inf')
        next_city = -1
        for i in range(n):
            if not visited[i] and dist[tour[-1]][i] != -1 and dist[tour[-1]][i] < min_dist:
                min_dist = dist[tour[-1]][i]
                next_city = i

        # Add the next city to the tour and update the cost
        tour.append(next_city)
        cost += min_dist

        # Mark the next city as visited
        visited[next_city] = True

    # Add the starting city to the tour and update the cost
    tour.append(start)
    cost += dist[tour[-1]][start]

    # Print the tour and the cost
    print("The tour is:", tour)
    print("The cost is:", cost)
