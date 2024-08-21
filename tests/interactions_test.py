from conftest import driver
from pages.interactions_page import (SortablePage, SelectablePage, ResizablePage)


class TestInteractions:
    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            assert order_before != order_after

        def test_grid_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_order()
            assert order_before != order_after

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_items()
            item_grid = selectable_page.select_grid_items()
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, 'no elements were selected'

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, 'max size not equal to "500px" "300px"'
            assert ('150px', '150px') == min_box, 'min size not equal to  "150px", "150px"'
            assert min_resize != max_resize, 'resizable has not change'


