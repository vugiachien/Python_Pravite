class Job:
    def __init__(self, job_code, job_name, job_field, salary):
        self.job_code = job_code
        self.job_name = job_name
        self.job_field = job_field
        self.salary = salary

    def evaluate(self):
        print("Đánh giá cơ bản cho công việc: ")
        print("Mã công việc:", self.job_code)
        print("Tên công việc:", self.job_name)
        print("Lĩnh vực công việc:", self.job_field)
        print("Mức lương:", self.salary)


class AI(Job):
    def __init__(self, job_code, job_name, job_field, salary, python_skill, ml_skill, deep_skill, math_skill):
        super().__init__(job_code, job_name, job_field, salary)
        self.python_skill = python_skill
        self.ml_skill = ml_skill
        self.deep_skill = deep_skill
        self.math_skill = math_skill

    def evaluate(self):
        super().evaluate()
        average_skill = (self.python_skill + self.ml_skill + self.deep_skill + self.math_skill) / 4
        print("Đánh giá cho công việc liên quan đến Trí tuệ nhân tạo:")
        print("Kỹ năng Python:", self.python_skill)
        print("Kỹ năng Machine Learning:", self.ml_skill)
        print("Kỹ năng Deep Learning:", self.deep_skill)
        print("Kỹ năng Toán học:", self.math_skill)
        print("Đánh giá tổng thể:", self.get_evaluation(average_skill))

    @staticmethod
    def get_evaluation(average_skill):
        if average_skill > 9.0:
            return "Rất phù hợp"
        elif average_skill > 7.0:
            return "Phù hợp"
        elif average_skill > 5.0:
            return "Tạm được"
        elif average_skill > 3.0:
            return "Cần bổ sung thêm kiến thức"
        else:
            return "Cần học lại kiến thức base"


class Backend(Job):
    def __init__(self, job_code, job_name, job_field, salary, sql_skill, oop_skill, api_skill, java_skill):
        super().__init__(job_code, job_name, job_field, salary)
        self.sql_skill = sql_skill
        self.oop_skill = oop_skill
        self.api_skill = api_skill
        self.java_skill = java_skill

    def evaluate(self):
        super().evaluate()
        average_skill = (self.sql_skill + self.oop_skill + self.api_skill + self.java_skill) / 4
        print("Đánh giá cho công việc phát triển Backend:")
        print("Kỹ năng SQL:", self.sql_skill)
        print("Kỹ năng OOP:", self.oop_skill)
        print("Kỹ năng phát triển API:", self.api_skill)
        print("Kỹ năng Java:", self.java_skill)
        print("Đánh giá tổng thể:", self.get_evaluation(average_skill))

    @staticmethod
    def get_evaluation(average_skill):
        if average_skill > 9.0:
            return "Rất phù hợp"
        elif average_skill > 7.0:
            return "Phù hợp"
        elif average_skill > 5.0:
            return "Tạm được"
        elif average_skill > 3.0:
            return "Cần bổ sung thêm kiến thức"
        else:
            return "Cần học lại kiến thức base"


class Frontend(Job):
    def __init__(self, job_code, job_name, job_field, salary, html_skill, css_skill, nodejs_skill, ux_skill, ui_skill):
        super().__init__(job_code, job_name, job_field, salary)
        self.html_skill = html_skill
        self.css_skill = css_skill
        self.nodejs_skill = nodejs_skill
        self.ux_skill = ux_skill
        self.ui_skill = ui_skill

    def evaluate(self):
        super().evaluate()
        average_skill = (self.html_skill + self.css_skill + self.nodejs_skill + self.ux_skill + self.ui_skill) / 5
        print("Đánh giá cho công việc phát triển Frontend:")
        print("Kỹ năng HTML:", self.html_skill)
        print("Kỹ năng CSS:", self.css_skill)
        print("Kỹ năng Node.js:", self.nodejs_skill)
        print("Kỹ năng UX:", self.ux_skill)
        print("Kỹ năng UI:", self.ui_skill)
        print("Đánh giá tổng thể:", self.get_evaluation(average_skill))

    @staticmethod
    def get_evaluation(average_skill):
        if average_skill > 9.0:
            return "Rất phù hợp"
        elif average_skill > 7.0:
            return "Phù hợp"
        elif average_skill > 5.0:
            return "Tạm được"
        elif average_skill > 3.0:
            return "Cần bổ sung thêm kiến thức"
        else:
            return "Cần học lại kiến thức base"


class Fullstack(Backend, Frontend):
    def __init__(self, job_code, job_name, job_field, salary, sql_skill, oop_skill, api_skill, java_skill,
                 html_skill, css_skill, nodejs_skill, ux_skill, ui_skill):
        Backend.__init__(self, job_code, job_name, job_field, salary, sql_skill, oop_skill, api_skill, java_skill)
        Frontend.__init__(self, job_code, job_name, job_field, salary, html_skill, css_skill, nodejs_skill,
                          ux_skill, ui_skill)

    def evaluate(self):
        print("Đánh giá cho công việc phát triển FullStack:")
        print("Công việc liên quan đến phát triển Backend:")
        Backend.evaluate(self)
        print("Công việc liên quan đến phát triển Frontend:")
        Frontend.evaluate(self)


# Tạo đối tượng tương ứng với AI
ai_job = AI("AI001", "AI Engineer", "Artificial Intelligence", 10000, 9.5, 8.5, 9.0, 9.0)
ai_job.evaluate()

print("-----------------------------------")

# Tạo đối tượng tương ứng với Frontend
frontend_job = Frontend("FE001", "Frontend Developer", "Web Development", 8000, 8.0, 9.0, 7.5, 8.5, 9.0)
frontend_job.evaluate()

print("-----------------------------------")

# Tạo đối tượng tương ứng với Backend
backend_job = Backend("BE001", "Backend Developer", "Web Development", 9000, 8.5, 9.0, 8.0, 8.5)
backend_job.evaluate()

print("-----------------------------------")

# Tạo đối tượng tương ứng với Fullstack
fullstack_job = Fullstack("FS001", "Fullstack Developer", "Web Development", 12000, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5, 8.5)
fullstack_job.evaluate()