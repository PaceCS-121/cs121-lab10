# write classes

def main():
    alice = Employee("Alice", 100000, 12)
    bob = Employee("Bob", 45000, 2)
    carol = Employee("Carol", 50000, 5)
    bryan = Employee("Bryan", 85000, 8)
    dan = Employee("Dan", 70000, 8)
    erin = Employee("Erin", 65000, 8)
    frank = Employee("Frank", 99000, 10)
    grace = Employee("Grace", 550000, 3)

    sales = Department("Sales")
    sales.add_employee(alice)
    sales.add_employee(bob)
    marketing = Department("Marketing")
    marketing.add_employee(carol)
    marketing.add_employee(bryan)
    it = Department("IT")
    it.add_employee(dan)
    engineering = Department("Engineering")
    engineering.add_employee(erin)
    product_development = Department("Product Development")
    product_development.add_employee(frank)
    executive_office = Department("Executive Office")
    executive_office.add_employee(grace)

    departments = [sales, marketing, it, engineering, product_development, executive_office]
    employees = [alice, bob, carol, bryan, dan, erin, frank, grace]

    # print top 3 earners

    # analyse departments

    # largest departments

if __name__ == "__main__":
    main()
