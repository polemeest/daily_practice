class Employee():
    def __init__(self, name: str, salary: int) -> None:
        self.__name = name
        self.__salary = salary

    def __get_name(self) -> None:
        return self.__name
    
    def __get_salary(self) -> None:
        return self.__salary
    
    def __set_salary(self, new_salary: (int, float)) -> None:
        if not isinstance(new_salary, (int, float)) or new_salary < 0:
            print(f'ErrorValue:{new_salary}')
            return
        self.__salary = new_salary

    title = property(__get_name)
    reward = property(__get_salary, __set_salary)
            