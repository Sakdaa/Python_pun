import heapq

def load_map(map_fname):
    with open(map_fname, 'r') as file:
        map_data = file.readlines()
    
    roads = {}
    
    for line in map_data:
        town_info, road_info = line.strip().split(';')
        
        town_name, location = town_info.split(':')
        town_name = town_name.strip()
        
        road_list = road_info.split(',')
        roads[town_name] = {}
        for road in road_list:
            dest_town, distance = road.split(':')
            roads[town_name][dest_town.strip()] = int(distance.strip())
    
    return roads

def P3_route(map_fname, start, goal):
    map_data = load_map(map_fname)
    
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        cost, town, path = heapq.heappop(pq)
        
        if town == goal:
            return ' - '.join(path)
        
        if town not in visited:
            visited.add(town)
            
            for neighbor, distance in map_data[town].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + distance, neighbor, path + [neighbor]))
    
    return "No route found"

