

def minimum_flights_needed(airports):
    n = len(airports) # Tumber of airports present in the given array

    if n == 0:  # This is an edge case to check if there is zero ariports present then the function will return -1
        return -1

    
    flight_taken = 0  # This variable is used to keep the count of the flight taken to reach the end
    farthest_reachable_airport = 0 # This variable is used to keep the maximum distance we can travel from a particular airport.
    current_reachable_airport = 0 # This variable is used to keep the airport that we can reach from the current airport that we are on.

    # The loop runs from 0 to n-1 and checks for the farthest airport we can reach from the index i.
    # Then it checks if the index is equal to the current_reachable airport. If true it indicates that we have exhausted the fuel and need to take another flight. But before taking the flight we check wether
    # here was a flight that can reach more than the current airport. if yes then we change the current to the farthest and increase the count of the flight.
    # If at any point the current_reachable_airport is more than the last ariport then we return the number of flights taken else it will return -1.


    for i in range(n):
        farthest_reachable_airport = max(farthest_reachable_airport, i + airports[i])

        if i == current_reachable_airport:
            if farthest_reachable_airport <= i:
                return -1

            current_reachable_airport = farthest_reachable_airport
            flight_taken += 1

            if current_reachable_airport >= n-1:
                return flight_taken
    return -1

print(minimum_flights_needed([1,6,3,4,5,0,0,0,6]))
    # Time complexity is O(n) and where n is the length of the array and space complexity is O(1).
