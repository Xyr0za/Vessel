# dCEL

# Distributed Computation Execution Library


Allows a server node to host a FLASK server that external and internal worker nodes can request work from. The work is transffered through the POST protocol over https:// returning a JSON object with the necessary information. In order to contact the Master Node for work; nodes muust first be registered with the coordinator where a UUID is granted. 

Requests WILL be rejected if an invalid UUID is detected; in future pushes this UUID will have a life time before being retired. 


FLOW CHART WILL BE ADDED HERE

----------


## 1. Initialise a Server

```python
from dCEL.master import MasterNode
from dCEL.coordinator import Coordinator
from dCEL.dump import Dump

if __name__ == '__main__':
    coordinator = Coordinator(current_iter=0, batch_size=1000, nodes={*()})
    dump = Dump("C:\Path\To\Dump\text.txt")
    master = MasterNode(
        coordinator=coordinator,
        dump=dump
    )

    master.api_construct()
    master.initate(debug=True)
```

## 2. Write the distributed function

```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n, True # Function returns a tuple in the form (ELEMENT TO STORE: any, STORE: boolean)
```

## 3. On the nodes; intiatite the worker scripts

```py
worker1 = Worker()
worker1.request_node()

while True:
    worker1.request_rights()
    info = worker1.work(function_to_work)
    worker1.post_return(info)
```

# Planned Features
* Result Consolidation - Returning of the calculation results - COMPLETED
* Documentation inside functions
* Improved Security
* Modularising the function definition
* Fallbacks
* Prevention of malicious injection
