import analyze_employees

def test_employee_class():
    jill = analyze_employees.Employee('Jill', 90000, 6)
    assert jill.name == 'Jill'
    assert jill.get_salary() == 90000
    assert jill.get_years_of_service() == 6

def test_department_class():
    dept = analyze_employees.Department('Seidenberg')
    assert dept.name == 'Seidenberg'
    assert dept.employees == list()
    dept.add_employee(analyze_employees.Employee('Jill', 90000, 6))
    dept.add_employee(analyze_employees.Employee('Katie', 80000, 2))
    assert type(dept.get_employees()) == list
    assert len(dept.get_employees()) == 2
    assert dept.department_size() == 2
    assert dept.average_salary() == 85000
    assert dept.average_years_of_service() == 4