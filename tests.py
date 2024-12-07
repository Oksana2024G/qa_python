from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_books_genre_empty_true(self, collector):
        assert collector.books_genre == {}

    # напиши свои тесты ниже
    def test_add_new_book_correct_book_in_collector(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.books_genre

    def test_set_book_genre_existent_book_add_genre(self, collector):
        collector.add_new_book('Мисс Марпл')
        collector.set_book_genre('Мисс Марпл', 'Детективы')
        assert collector.books_genre['Мисс Марпл'] == 'Детективы'

    def test_get_book_genre_existent_book_with_existent_genre_true(self, populated_collector):
        assert populated_collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_existent_genre_without_books_empty_list(self, populated_collector):
        assert populated_collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_genre_existent_book_expected_genre(self, populated_collector):
        expected_genre = {'Гордость и предубеждение и зомби': 'Ужасы', 'Мисс Марпл': 'Детективы'}
        assert populated_collector.get_books_genre() == expected_genre

    def test_get_books_for_children_when_genre_not_age_rating_add_children_book(self, populated_collector):
        populated_collector.add_new_book('Три поросенка')
        populated_collector.set_book_genre('Три поросенка', 'Мультфильмы')
        assert populated_collector.get_books_for_children() == ['Три поросенка']

    def test_add_book_in_favorites_necessary_book_in_favorites(self, populated_collector):
        favorites = populated_collector.get_list_of_favorites_books()
        assert 'Гордость и предубеждение и зомби' in favorites

    def test_delete_book_from_favorites_unnecessary_book_not_in_list(self, populated_collector):
        populated_collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        favorites = populated_collector.get_list_of_favorites_books()
        assert favorites == []

    def test_get_list_of_favorites_books_necessary_book_in_favorites(self, populated_collector):
        favorites = populated_collector.get_list_of_favorites_books()
        assert favorites == ['Гордость и предубеждение и зомби']
