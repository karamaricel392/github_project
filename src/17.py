import math

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    
    # Distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    return distance

def main():
    city1 = (34.0522, 118.2437)  # Paris, France
    city2 = (51.5074, 0.1273)     # New York City, USA
    
    print(f"Distance between {city1} and {city2}: {distance(city1, city2)} units")

if __name__ == "__main__":
    main()
