from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR,
                 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR,
                        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR,
                        'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR,
                        'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')


class DroppablePageLocators:
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    SIMPLE_DRAG_ME = (By.CSS_SELECTOR, 'div[id="draggable"]')
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    ACCEPT_DROP_HERE = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    PREVENT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_DROP_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    PREVENT_DRAG_ME = (By.CSS_SELECTOR, '#ppDropContainer #dragBox')

    REVERT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    REVERT_DROP_HERE = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')


class DraggablePageLocators:
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    SIMPLE_DRAG_BOX = (By.CSS_SELECTOR, 'div[id="dragBox"]')

    AXIS_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')
