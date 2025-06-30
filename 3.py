def find_non_multiples(start: int, end: int) -> list:
    # ตรวจสอบว่า start ไม่มากกว่า end
    if start > end:
        return []

    result = []
    for number in range(start, end + 1):
        if number % 3 != 0 and number % 4 != 0 and number % 5 != 0:
            result.append(number)

    return result

# ตัวอย่างการใช้งาน
print(find_non_multiples(10, 25))  # Output: [11, 13, 17, 19, 23]
