class Diabetes:
    def __init__(self, blood_pressure, cholesterol, BMI, level_health,
                 smoker, mind, exercise, sex, age,
                 education, income, eat_fruits, eat_veggies):
        self.blood_pressure = blood_pressure  # Huyết áp cao 
        self.cholesterol = cholesterol        # Cholesterol
        self.BMI = BMI                        # Chỉ số cơ thể
        self.level_health = level_health      # Sức khỏe tổng quát 
        self.smoker = smoker                  # Hút thuốc 
        self.mind = mind                      # Số ngày tinh thần kém trong tháng
        self.exercise = exercise              # Tham gia hoạt động trong tháng 
        self.sex = sex                        # Giới tính 
        self.age = age                        # Độ tuổi
        self.education = education            # Học vấn 
        self.income = income                  # Thu nhập
        self.eat_fruits = eat_fruits          # Tiêu thụ trái cây trong ngày 
        self.eat_veggies = eat_veggies        # Tiêu thụ rau trong ngày 

    # Phương thức to_string để debug
    def __str__(self):
        return (f"Diabetes(blood_pressure={self.blood_pressure}, cholesterol={self.cholesterol}, "
                f"BMI={self.BMI}, level_health={self.level_health}, smoker={self.smoker}, "
                f"mind={self.mind}, exercise={self.exercise}, sex={self.sex}, "
                f"age={self.age}, education={self.education}, income={self.income}, "
                f"eat_fruits={self.eat_fruits}, eat_veggies={self.eat_veggies})")
