"""
    A group of people are walking in the area as shown in the illustration
    The red line is the row of red flags
    The yellow line is the row of yellow flags
    The green line is the row of green flags
    The blue line is the row of blue flags
    The person walking can tell how far away his
        or her position is from the two nearest rows of flags on either side
    Write a program to find the 10% of people who are furthest away from other people
"""

import numpy as np

SIZE_PEOPLE = 100
def calculate_distance(person_a, person_b):
    """Calculate distance between two people."""
    return np.sqrt((person_a[0] - person_b[0])**2 + (person_a[1] - person_b[1])**2)

# Example usage
people_positions = [
                    (np.random.randint(1, 100), np.random.randint(1, 100))
                    for _ in range(SIZE_PEOPLE)
                    ]

distances = []
for person1 in people_positions:
    min_distance = np.inf
    for person2 in people_positions:
        if person1 != person2:
            distance = calculate_distance(person1, person2)
            min_distance = min(distance, min_distance)
    distances.append((person1, min_distance))

# Sort distances
distances.sort(key=lambda x: x[1], reverse=True)
lst_long_distances = [person for person, _ in distances[:int(len(distances)*0.1)]]

print(lst_long_distances)