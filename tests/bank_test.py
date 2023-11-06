import bank

def test_BankAccount():
    ba = bank.BankAccount('Iris Green', 1000.0)
    assert ba.get_name() == 'Iris Green'
    assert ba.get_balance() == 1000.0
    assert ba.get_frozen() == False
    assert ba.deposit(5) == True
    assert ba.get_balance() == 1005.0
    assert ba.withdraw(250) == True
    assert ba.get_balance() == 755.0
    ba.freeze()
    assert ba.get_frozen() == True
    ba.unfreeze()
    assert ba.get_frozen() == False

def test_withdraw(capsys):
    ba = bank.BankAccount('Ups Brown', 800)
    ba.freeze()
    assert ba.withdraw(1) == False
    captured = capsys.readouterr()
    assert len(captured.out) > 0
    ba.unfreeze()
    assert ba.withdraw(1001) == False
    assert ba.get_frozen() == True
    ba.unfreeze()
    assert ba.withdraw(801) == False
    if ba.get_frozen():
        ba.unfreeze()
    assert ba.withdraw(50) == True
    assert ba.get_balance() == 750.0