import re
import puzzles

test_puzzles = [(25, 'Winnie the Pooh', 'no clue'),
    (100, 'Leaves')]

def test_puzzle_class():
    p = puzzles.Puzzle(test_puzzles[0][0], test_puzzles[0][1], test_puzzles[0][2])
    assert p.pieces == test_puzzles[0][0]
    assert p.title == test_puzzles[0][1]
    assert p.company == test_puzzles[0][2]
    p2 = puzzles.Puzzle(test_puzzles[1][0], test_puzzles[1][1])
    assert p2.pieces == test_puzzles[1][0]
    assert p2.title == test_puzzles[1][1]
    assert p.company
    assert re.search(test_puzzles[0][1], str(p))

def test_puzzle_sort():
    l = []
    test_puzzles.reverse()
    for p in test_puzzles:
        l.append(puzzles.Puzzle(p[0], p[1]))
    l.sort(key=puzzles.Puzzle.sort_priority)
    assert l[0].title == 'Winnie the Pooh'
    varnames = puzzles.main.__code__.co_varnames
    assert 'sorted_puzzles' in varnames

