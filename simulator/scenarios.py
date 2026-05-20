import random


def traffic_overload(state):
    state["requests"]+=random.randint(0,8)

    state["cpu"]+=(state["requests"]*0.01)+random.uniform(-2,2) ## dependency + noise
    ## keep cpu within realistic bounds (0%-100%)
    state["cpu"]=max(0,min(state["cpu"],100))

    state["latency"]+=(state["cpu"]*0.05)+random.uniform(-5,5)
    state["latency"]=max(10,state["latency"])

    # errors
    if state["cpu"]>75 or state["latency"]>120:
        state["errors"]+=random.uniform(0,3)
    else:
        state["errors"]=max(0,state["errors"]-0.5)

    # system crash
    if state["cpu"]>85 and state["latency"]>150 and state["errors"]>10:
        state["failed"]=1
    else :
        state["failed"]=0

    return state