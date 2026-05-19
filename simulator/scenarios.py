import random


def traffic_overload(state):
    state["requests"]+=random.randint(0,8)
    state["cpu"]+=(state["requests"]*0.01)+random.uniform(-2,2) ## dependency + noise
    ## keep cpu within realistic bounds (0%-100%)
    state["cpu"]=max(0,min(state["cpu"],100))
    return state