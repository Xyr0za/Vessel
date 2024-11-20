from dCEL.worker import Worker


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


worker1 = Worker()
worker1.request_node()

print("Iden: ", worker1.identity)

for i in range(3):
    worker1.request_rights()

    print(worker1.rights)

    worker1.work(is_prime)


