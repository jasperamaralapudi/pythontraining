boat_capacity=int(input())
adults=int(input())
children=int(input())
weight=adults*75+children*30
if boat_capacity<weight:
    print('Boat will drown')
else:
    print('Boat is stable')