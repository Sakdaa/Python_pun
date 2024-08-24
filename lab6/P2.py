from collections import deque

def load_map(map_fname):
    with open(map_fname, 'r') as file:
        map_data = file.readlines()
    
    locations = {}
    roads = {}
    
    for line in map_data:
        town_info, road_info = line.strip().split(';')
        
        town_name, location = town_info.split(':')
        town_name = town_name.strip()
        x, y = map(int, location.split(','))
        locations[town_name] = (x, y)
        
        road_list = road_info.split(',')
        roads[town_name] = {}
        for road in road_list:
            dest_town, distance = road.split(':')
            roads[town_name][dest_town.strip()] = int(distance.strip())
    
    return roads

def P2_route(map_fname, start, goal):
    map_data = load_map(map_fname)
    
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        town = path[-1]
        
        if town == goal:
            return ' - '.join(path)
        
        if town not in visited:
            visited.add(town)
            
            for neighbor in map_data[town]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return "No route found"

