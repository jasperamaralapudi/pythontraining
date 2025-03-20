def ASP(acitivities):
    activities.sort(key=lambda x:x[1])
    selectedactivity=[activities[0]]
    for activity in activities[1:]:
        if activity[0]>=selectedactivity[-1][1]:
           selectedactivity.append(activity) 
    return selectedactivity
def optimized_ASP(activities):
    activities.sort(key=lambda x:x[1])
    selectedactivity=[activities[0]]
    for activity in activities[1:]:
        lastselectedactivity=selectedactivity[-1]
        if activity[0]>=lastselectedactivity[1]:
            selectedactivity.append(activity)
    return selectedactivity
activities=[[2, 4], [1, 3], [5, 7], [3, 6], [8, 10], [4, 9]]
print('Naive Greedy Approach:',ASP(activities))
print('Optimized Greedy Approach:',optimized_ASP(activities))