
class SalaryCalculator:
    def calculate_average_salary(self, salaries):
        if len(salaries)<=2:
            print("The tuple must have 3 values atlest")
        min_salary=min(salaries)
        max_salary=max(salaries)
        sum_salary= sum(salaries)-min_salary-max_salary
        average_salary=sum_salary/(len(salaries)-2)
        return round(average_salary)
    
calc=SalaryCalculator()
salaries=(4000,3000,1000,2000)
average_salary=calc.calculate_average_salary (salaries)
print(average_salary)