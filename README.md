1. test_add_new_book_add_new_books: Проверяем добавление книг в разном количестве
2. test_add_new_book_long_name_book_not_added: Проверяем, что книга с недопустимой длиной названия более 41 символа не добавится в список
3. test_add_new_book_the_same_book_added_once: Проверяем, что одна и та же книга не добавляется повторно
4. test_set_book_genre_set_genre_from_genre_list: Проверяем, что жанр из списка жанров присваивается книге
5. test_set_book_genre_for_not_added_book_is_impossible: Проверяем, что жанр не присваивается не добавленной в список книге
6. test_set_book_genre_out_of_the_list_is_empty: Проверяем, что при попытке присвоить жанр не из списка, значение останется пустым
7. test_get_book_genre_get_correct_genre: Проверяем, что присвоенный жанр возвращается правильно
8. test_get_books_with_specific_genre_gets_proper_book_list: Проверяем, что по запросу жанра возвращается список соответствующих книг
9. test_get_books_with_specific_genre_returns_empty_list_for_not_added_genre: Проверяем, что при попытке получения жанра не из списка жанров вернется пустой список
10. test_get_books_with_specific_genre_returns_empty_list_for_genre_with_no_books: Проверяем, что если в списке нет книг запрашиваемого жанра, вернется пустой список
11. test_get_books_genre_returns_proper_dictionary: Проверяем, что при запросе книги по жанру вернется ожидаемый словарь
12. test_get_books_for_children_returns_proper_books: Проверяем возврат списка книг, подходящих для детей
13. test_add_book_in_favorites_add_book_to_favorites: Проверяем добавление книги в избранное
14. test_add_book_in_favorites_double_adding_is_not_possible: Проверяем, что повторное добавление книги в избранное не происходит
15. test_delete_book_from_favorites_delete_book: Проверяем удаление книги из избранного
16. test_delete_book_from_favorites_for_not_added_book: Проверяем удаление из избранного книги, которую туда не добавляли
17. test_get_list_of_favorites_books_returns_correct_list: Проверяем что возвращается ожидаемый список избранного при пустом списке, одной и двух книгах

