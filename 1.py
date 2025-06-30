def find_multiples_of_three(start: int, end: int) -> list:
   
    if start > end:
        return []
    result = []
    # วนลูป start ถึง end 
    for number in range(start, end + 1):
        if number % 3 == 0:
            result.append(number)
    return result
# ตัวอย่าง
start = 10
end = 25
print("Multiples of 3:", find_multiples_of_three(start, end))
