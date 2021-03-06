# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# lat_lon_obj = LatLon(10, 22)
# print(lat_lon_obj.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`,
# and `lon` to the constructor. It should inherit from LatLon. Look
# up the `super` method.

# YOUR CODE HERE


class Waypoint (LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return (f"Waypoint {self.name} is at {self.lat} {self.lon}")


wp_obj = Waypoint('space', 20, 20)
print(wp_obj.name, wp_obj.lat, wp_obj.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache (Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        result_string = (
            f"Geocache {self.name} is at {self.lat} {self.lon} "
            f"and is rated {self.difficulty}.")
        return result_string

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint('Catacombs', 41.70505, -121.51521)
# print(waypoint.name, waypoint.lat, waypoint.lon)
geo_cata = Geocache('Catacombs', 'superhard',
                    '4 sq. miles', 41.70505, -121.51521)
# print(geo_cata.name, geo_cata.difficulty,
#       geo_cata.size, geo_cata.lat, geo_cata.lon)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache('Newberry Views', 'diff 1.5',
                    'size 2', 44.052137, -121.41556)
# print(geo_berry.name, geo_berry.difficulty,
#       geo_berry.size, geo_berry.lat, geo_berry.lon)

# Print it--also make this print more nicely
print(geocache)
