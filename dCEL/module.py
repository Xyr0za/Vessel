from dCEL.master import MasterNode
from dCEL.coordinator import Coordinator

import hashlib
import datetime


if __name__ == '__main__':
    coordinator = Coordinator(current_iter=0, batch_size=1000, nodes={*()})
    master = MasterNode(
        coordinator=coordinator,
    )

    master.api_construct()
    master.initate()
