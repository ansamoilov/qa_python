import pytest

from main import BooksCollector


class TestBooksCollector:

    #фикстура для создания экземпляра класса не в теле теста
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    @pytest.mark.parametrize('books, expected_count', [
        ([], 0),
        (['Дракула'], 1),
        (['Дракула', 'Этюд в багровых тонах'], 2),
    ])
    def test_add_new_book_add_new_books(self, collector, books, expected_count):
        """Проверяем добавление книг в разном количестве"""
        for book in books:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == expected_count

    def test_add_new_book_long_name_book_not_added(self, collector):
        """Проверяем, что книга с недопустимой длиной названия более 41 символа не добавится в список"""
        long_name = ('Сказка о Тройке. История непримиримой борьбы за повышение трудовой дисциплины, против '
                     'бюрократизма, за высокий моральный уровень, против обезлички, за здоровую критику и здоровую '
                     'самокритику, за личную ответственность каждого, за образцовое содержание отчетности и против '
                     'недооценки собственных сил')
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_the_same_book_added_once(self, collector):
        """Проверяем, что одна и та же книга не добавляется повторно"""
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre, expected_genre', [
        ('Дракула', 'Ужасы', 'Ужасы'),
        ('Война миров', 'Фантастика', 'Фантастика'),
        ('Этюд в багровых тонах', 'Детективы', 'Детективы'),
        ('Трое в лодке, не считая собаки', 'Комедии', 'Комедии'),
    ])
    def test_set_book_genre_set_genre_from_genre_list(self, collector, name, genre, expected_genre):
        """Проверяем, что жанр из списка жанров присваивается книге"""
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == expected_genre

    def test_set_book_genre_for_not_added_book_is_impossible(self, collector):
        """Проверяем, что жанр не присваивается не добавленной в список книге"""
        collector.set_book_genre('Война миров', 'Фантастика')
        assert collector.get_book_genre('Война миров') is None

    def test_set_book_genre_out_of_the_list_is_empty(self, collector):
        """Проверяем, что при попытке присвоить жанр не из списка, значение останется пустым"""
        name = '1984'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Антиутопия')
        assert collector.get_book_genre(name) is ''

    def test_get_book_genre_get_correct_genre(self, collector):
        """Проверяем, что присвоенный жанр возвращается правильно"""
        name = 'Дракула'
        genre = 'Ужасы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [
        ('Черепашки-ниндзя и космический охотник', 'Мультфильмы'),
        ('Дракула', 'Ужасы')
    ])
    def test_get_books_with_specific_genre_gets_proper_book_list(self, collector, name, genre):
        """Прверяем, что по запросу жанра возвращается список соответствующих книг"""
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_with_specific_genre_returns_empty_list_for_not_added_genre(self, collector):
        """Проверяем, что при попытке получения жанра не из списка жанров вернется пустой список"""
        assert collector.get_books_with_specific_genre('Антиутопия') == []

    def test_get_books_with_specific_genre_returns_empty_list_for_genre_with_no_books(self, collector):
        """Проверяем, что если в списке нет книг запрашиваемого жанра, вернется пустой список"""
        assert collector.get_books_with_specific_genre('Комедии') == []

    @pytest.mark.parametrize(
        'book_info, expected_genre_dict',
        [
            (
                    [('Война миров', 'Фантастика'), ('Дракула', 'Ужасы')],
                    {
                        'Война миров': 'Фантастика',
                        'Дракула': 'Ужасы'
                    }
            ),
            (
                    [('Этюд в багровых тонах', 'Детективы'), ('Трое в лодке, не считая собаки', 'Комедии')],
                    {
                        'Этюд в багровых тонах': 'Детективы',
                        'Трое в лодке, не считая собаки': 'Комедии'
                    }
            )
        ]
    )
    def test_get_books_genre_returns_proper_dictionary(self, collector, book_info, expected_genre_dict):
        """Проверяем, что при запросе книги по жанру вернется ожидаемый словарь"""
        for name, genre in book_info:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == expected_genre_dict

    @pytest.mark.parametrize(
        'books_data, expected_children_books',
        [
            (
                    [
                        ('Война миров', 'Фантастика'),
                        ('Дракула', 'Ужасы'),
                        ('Этюд в багровых тонах', 'Детективы'),
                        ('Трое в лодке, не считая собаки', 'Комедии'),
                        ('Черепашки-ниндзя и космический охотник', 'Мультфильмы')
                    ],
                    ['Война миров', 'Трое в лодке, не считая собаки', 'Черепашки-ниндзя и космический охотник']
            ),
            (
                    [
                        ('Черепашки-ниндзя и космический охотник', 'Мультфильмы'),
                        ('Этюд в багровых тонах', 'Детективы')
                    ],
                    ['Черепашки-ниндзя и космический охотник']
            )
        ]
    )
    def test_get_books_for_children_returns_proper_books(self, collector, books_data, expected_children_books):
        """Проверяем возврат списка книг, подходящих для детей"""
        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == expected_children_books

    def test_add_book_in_favorites_add_book_to_favorites(self, collector):
        """Проверяем добавление книги в избранное"""
        name = 'Этюд в багровых тонах'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    def test_add_book_in_favorites_double_adding_is_not_possible(self, collector):
        """Проверяем, что повторное добавление книги в избранное не происходит"""
        name = 'Этюд в багровых тонах'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_book(self, collector):
        """Проверяем удаление книги из избранного"""
        name = 'Дракула'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_for_not_added_book(self, collector):
        """Проверяем удаление из избранного книги, котрую туда не добавляли"""
        name = 'Дракула'
        collector.delete_book_from_favorites(name)
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize("books, favorites", [
        ([], []),
        (['Этюд в багровых тонах'], ['Этюд в багровых тонах']),
        (['Дракула', 'Война миров'], ['Дракула', 'Война миров']),
    ])
    def test_get_list_of_favorites_books_returns_correct_list(self, collector, books, favorites):
        """Проверяем что возвращается ожидаемый список избранного при пустом списке, одной и двух книгах"""
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert collector.get_list_of_favorites_books() == favorites
