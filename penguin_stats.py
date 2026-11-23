# penguin_stats.py
# Jayden Reutzel
# 11/15/2026
# Functions for calculating and classifying penguin statistics

# returns the count as a percentage of the total
def calculate_percentage(count, total):
    return count / total * 100

# returns whether a percentage is "small", "medium", or "large"
def classify_species(percent):
    if percent < 25:
        return "small"
    elif (percent >= 25) and (percent < 40):
        return "medium"
    else:
        return "large"

# returns whether a species is the "largest", "smallest", or "middle-sized"
def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"
