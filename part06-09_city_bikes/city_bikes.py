# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    station_data = {}

    with open(filename) as new_file:

        for line in new_file:
            line = line.strip()
            parts = line.split(";")

            if parts[0] == "Longitude":
                continue
            station_data[parts[3]] = (float(parts[0]), float(parts[1]))
    return station_data


def distance(stations: dict, station1: str, station2: str):
    x1_long, y1_lat = stations[station1]
    x2_long, y2_lat = stations[station2]

    x_km = (x1_long - x2_long) * 55.26
    y_km = (y1_lat - y2_lat) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict):
    max_distance = 0
    sta1 = sta2 = "" 
    stations_list = []

    for station in stations:
        lat, long = stations[station]
        stations_list.append((station, lat, long))

    
    for i in range(len(stations_list)):
        for j in range(i + 1, len(stations_list)):
            cur_distance = distance(stations, stations_list[i][0], stations_list[j][0])
            if cur_distance > max_distance:
                sta1, sta2 = stations_list[i][0], stations_list[j][0]
                max_distance = max(max_distance, cur_distance)

    return (sta1, sta2, max_distance)



if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
