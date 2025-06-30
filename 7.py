def prime_numbers_in_range(start: int, end: int) -> tuple:
    # ฟังก์ชันตรวจสอบจำนวนเฉพาะ
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # สร้างลิสต์จำนวนเฉพาะในช่วง start ถึง end
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    
    # คืนผลลัพธ์เป็น tuple: (ลิสต์จำนวนเฉพาะ, ผลรวม)
    return (primes, sum(primes))


# ตัวอย่างการใช้งาน
result = prime_numbers_in_range(10, 20)
print(result)  # Output: ([11, 13, 17, 19], 60)
