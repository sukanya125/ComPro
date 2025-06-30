from typing import List

def find_divisors(n: int) -> List[int]:
    # Step 1: ตรวจสอบว่าเป็นจำนวนเต็มบวกมากกว่า 0
    if n <= 0:
        return []

    # Step 2: หาตัวหารทั้งหมดของ n
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # เพิ่มตัวประกอบคู่ เช่น 2 และ 10 ถ้า n = 20
                divisors.append(n // i)

    # Step 3: คืนค่าลิสต์เรียงจากน้อยไปมาก
    return sorted(divisors)

# ตัวอย่างการใช้งาน
print(find_divisors(20))  # Output: [1, 2, 4, 5, 10, 20]
