#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    flight_table = {}
    starting_source = "NONE"
    route = []    
    i = 0
    
    while i < length:
        flight_table[tickets[i].source] = tickets[i].destination
        i+=1
    
    j = 0
    
    while j < length:
        route.append(flight_table[starting_source])
        starting_source = route[j]
        j+=1
        
    return route