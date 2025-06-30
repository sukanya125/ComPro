def check_prime(n: int) -> str:
    # Step 1: ตรวจสอบ input ต้องมากกว่า 1
    if n <= 1:
        return "is not prime"

    # Step 2: ตรวจสอบว่าเป็นจำนวนเฉพาะหรือไม่
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "is not prime"

    return "is prime"
