import re
import movies

def test_movie_class():
    m = movies.Movie('The Lion, the Witch, and the Wardrobe', '2005')
    assert m.title == 'The Lion, the Witch, and the Wardrobe'
    assert m.year == '2005'
    assert m.cast == list()
    assert m.genres == list()
    assert m.description == None

def test_set_methods():
    c = ['Hugo Weaving', 'Natalie Portman']
    g = ['dystopian']
    d = 'Man in Guy Fawkes mask fights the establishment in fascist Britain.'
    m = movies.Movie('V for Vendetta', '2005')
    m.set_cast(c)
    assert m.cast == c
    m.set_genres(g)
    assert m.genres == g
    m.set_description(d)
    assert m.description == d

def test_loading_data(capsys):
    movies.main()
    captured = capsys.readouterr()
    assert re.search(r"36273", captured.out)
    
