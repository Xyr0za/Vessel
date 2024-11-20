# dCEL

Distributed Computation Execution Library


## 1. Initialise a Server

```python
from dCEL.master import MasterNode
from dCEL.coordinator import Coordinator

if __name__ == '__main__':
    coordinator = Coordinator(current_iter=0, batch_size=1000, nodes={*()})
    master = MasterNode(
        coordinator=coordinator,
    )

    master.api_construct()
    master.initate()
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
    return True
```

## 3. On the nodes; intiatite the worker scripts

```py
from dCEL.worker import Worker

worker1 = Worker()
worker1.request_node()

while Working:
    worker1.request_rights()
    worker1.work(is_prime)
```

# Features to implement
* Result Consolidation - Returning of the calculation results
* Documentation inside functions
* Improved Security
