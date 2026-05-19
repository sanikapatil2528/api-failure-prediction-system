from scenarios import traffic_overload


def run_simulation(steps=20):
    state={
        "requests":100,
        "cpu":30,
        "memory":50,
        "latency":80,
        "errors":0
    }

    for step in range(steps):
        state=traffic_overload(state)
        print(f"Step {step}: {state}")


if __name__=="__main__":
    run_simulation()