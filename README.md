# qa_python
1. test_books_genre_empty_true
Проверяем, что словарь books_genre пустой.

2. test_add_new_book_correct_book_in_collector
Проверяем, что книга добавилась в словарь books_genre

3. test_set_book_genre_existent_book_add_genre
Проверяем, что существующей книге присвоен жанр

4. test_get_book_genre_existent_book_with_existent_genre_true
Проверяем, что для существующей книге выводится присвоенный жанр

5. test_get_books_with_specific_genre_existent_genre_without_books_empty_list
Проверяем, что если нет книг определенного жанра, то список книг будет пустой

6. test_get_books_genre_existent_book_expected_genre
Проверяем, что существующие книги с ожидаемым жанром находятся в словаре

7. test_get_books_for_children_when_genre_not_age_rating_add_children_book
Проверяем, что когда жанр книги не из взрослого рейтинга, то книга подходит для детей

8. test_add_book_in_favorites_necessary_book_in_favorites
Проверяем, что нужная книга добавлена в Избранное

9. test_delete_book_from_favorites_unnecessary_book_not_in_list
Проверяем, ненужная книга из списка Избранное удалена

10. test_get_list_of_favorites_books_necessary_book_in_favorites
Проверяем, что нужная книга в списке Избранное 
