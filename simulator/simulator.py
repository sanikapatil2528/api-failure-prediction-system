from simulator.scenarios import traffic_overload
from dashboard.visualize import plot_metrics
from preprocessing.preprocess import create_future_failure_label
import pandas as pd

history=[]
def run_simulation(steps=50):
    state={
        "requests":100,
        "cpu":30,
        "memory":50,
        "latency":80,
        "errors":0
    }

    for step in range(steps):
        state=traffic_overload(state)
        history.append(state.copy())
        print(f"Step {step}: {state}")
        if state["failed"]==1:
            print("\nSYSTEM FAILURE DETECTED")
            print(f"System crashed at step {step}")
            break
    
    return history


if __name__=="__main__":
    history=run_simulation()
    df=pd.DataFrame(history)
    df=create_future_failure_label(df)
    print(df[["failed","future_failure"]].tail(10))
    # print(df.head())
    # plot_metrics(df)