def find_multiples_of_three_and_four(start: int, end: int) -> list:
    # ตรวจสอบว่า start ไม่มากกว่า end
    if start > end:
        return []

    # ใช้ LCM ของ 3 และ 4 คือ 12
    result = []
    for number in range(start, end + 1):
        if number % 12 == 0:
            result.append(number)

    return result

# ตัวอย่างการเรียกใช้
print(find_multiples_of_three_and_four(10, 50))  # Output: [12, 24, 36, 48]
