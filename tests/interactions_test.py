import allure
from conftest import driver
from pages.interactions_page import (SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage)


@allure.suite("Interactions")
class TestInteractions:
    @allure.feature('Sortable')
    class TestSortable:

        @allure.title('Check sortable')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            assert order_before != order_after

        @allure.title('Check grid sortable')
        def test_grid_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_order()
            assert order_before != order_after

    @allure.feature('Selectable')
    class TestSelectable:

        @allure.title('Check selectable')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_items()
            item_grid = selectable_page.select_grid_items()
            assert len(item_list) > 0, 'no elements were selected'
            assert len(item_grid) > 0, 'no elements were selected'

    @allure.feature('Resizable')
    class TestResizable:

        @allure.title('Check resizable')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box, 'max size not equal to "500px" "300px"'
            assert ('150px', '150px') == min_box, 'min size not equal to  "150px", "150px"'
            assert min_resize != max_resize, 'resizable has not change'

    @allure.feature('Droppable')
    class TestDroppable:

        @allure.title('Check simple droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'the elements has not been dropped'

        @allure.title('Check accept droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here', 'the dropped element has been accepted'
            assert accept == 'Dropped!', 'the dropped element has not been dropped'

        @allure.title('Check prevent propogination droppable')
        def test_prevent_propogination_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'the element text has not been changed'
            assert not_greedy_inner == 'Dropped!', 'the element text has not been changed'
            assert greedy == 'Outer droppable', 'the element text has been changed'
            assert greedy_inner == 'Dropped!', 'the element text has not been changed'

        @allure.title('Check revert draggable droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, 'the element has not reverted'
            assert not_will_after_move == not_will_after_revert, 'the element has reverted'

    @allure.feature('Draggable')
    class TestDraggable:

        @allure.title('Check simple draggable')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, 'the position of the box has not been changed'

        @allure.title('Check axis restricted draggable')
        def test_axis_restricted_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, \
                'box position has not changed or there has been a shift in the y-axis'
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, \
                'box position has not changed or there has been a shift in the y-axis'
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, \
                'box position has not changed or there has been a shift in the x-axis'
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, \
                'box position has not changed or there has been a shift in the x-axis'
