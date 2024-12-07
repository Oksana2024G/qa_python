import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def populated_collector(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.add_new_book('Мисс Марпл')
    collector.set_book_genre('Мисс Марпл', 'Детективы')
    collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    return collector
