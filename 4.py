def calculate_sum_and_average() -> None:
    numbers = []

    # Step 1: เก็บ input 5 ค่า
    for i in range(1, 6):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a real number.")

    # Step 2: คำนวณผลรวม
    total = sum(numbers)

    # Step 3: คำนวณค่าเฉลี่ย
    average = total / len(numbers)

    # Step 4: แสดงผลลัพธ์ด้วยทศนิยม 2 ตำแหน่ง
    print(f"Sum: {total:.2f}")
    print(f"Average: {average:.2f}")
