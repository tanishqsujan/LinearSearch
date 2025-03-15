tour_locations= ["New York", "Los Angeles", "London", "Bankok", "Istanbul", "Toronto"]
target_city= "New York"

def linear_search(search_list, target_value):
    matches= []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
            
            
    if not matches:
        ValueError("{0} is not in the list".format(target_value))
        
    else:
        return matches
    
tour_stops= linear_search(tour_locations, target_city)

print("{} is present in the following locations in the list: {}".format(target_city, tour_stops))