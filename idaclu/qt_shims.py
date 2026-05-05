# Shim file to support PySide6 (IDA >= 9.0), PyQt5 (IDA 7.x-8.x), and PySide v1.x (IDA <= 6.8).
# Documentation provided by Qt and Riverbank Computing Ltd.:
#  - https://doc.qt.io/qtforpython-6/
#  - https://doc.qt.io/qtforpython-5/
#  - https://srinikom.github.io/pyside-docs/
# Inspired by the gist of Willi Ballenthin:
#  - https://gist.github.com/williballenthin/277eedca569043ef0984


is_ida = True
try:
    import idaapi
except ImportError:
    is_ida = False


_binding = None
QtCore = None
QtGui = None
QtWidgets = None
Signal = None

if is_ida and idaapi.IDA_SDK_VERSION <= 680:
    import PySide.QtCore as QtCore
    import PySide.QtGui as QtGui
    QtWidgets = None
    Signal = QtCore.Signal
    _binding = 'PySide'
else:
    try:
        import PySide6.QtCore as QtCore
        import PySide6.QtGui as QtGui
        import PySide6.QtWidgets as QtWidgets
        Signal = QtCore.Signal
        _binding = 'PySide6'
    except ImportError:
        try:
            import PySide2.QtCore as QtCore
            import PySide2.QtGui as QtGui
            import PySide2.QtWidgets as QtWidgets
            Signal = QtCore.Signal
            _binding = 'PySide2'
        except ImportError:
            import PyQt5.QtCore as QtCore
            import PyQt5.QtGui as QtGui
            import PyQt5.QtWidgets as QtWidgets
            Signal = QtCore.pyqtSignal
            _binding = 'PyQt5'


def _resolve(name, modules):
    for mod in modules:
        if mod is not None and hasattr(mod, name):
            return getattr(mod, name)
    raise AttributeError("Qt class {!r} not found in {}".format(name, _binding))


# In Qt6, QAction moved from QtWidgets to QtGui. In PySide v1, everything is in QtGui.
# _resolve searches in priority order; first match wins.
_GUI_FIRST = (QtGui, QtWidgets, QtCore)
_WIDGETS_FIRST = (QtWidgets, QtGui, QtCore)
_CORE_FIRST = (QtCore, QtGui, QtWidgets)


# QtCore
QAbstractItemModel = _resolve('QAbstractItemModel', _CORE_FIRST)
QByteArray = _resolve('QByteArray', _CORE_FIRST)
QCoreApplication = _resolve('QCoreApplication', _CORE_FIRST)
QEvent = _resolve('QEvent', _CORE_FIRST)
QMetaObject = _resolve('QMetaObject', _CORE_FIRST)
QModelIndex = _resolve('QModelIndex', _CORE_FIRST)
QPoint = _resolve('QPoint', _CORE_FIRST)
QPointF = _resolve('QPointF', _CORE_FIRST)
QRect = _resolve('QRect', _CORE_FIRST)
QSize = _resolve('QSize', _CORE_FIRST)
QSortFilterProxyModel = _resolve('QSortFilterProxyModel', _CORE_FIRST)
QStringListModel = _resolve('QStringListModel', _CORE_FIRST)
Qt = _resolve('Qt', _CORE_FIRST)
QThread = _resolve('QThread', _CORE_FIRST)
QTranslator = _resolve('QTranslator', _CORE_FIRST)

# QtGui
QBrush = _resolve('QBrush', _GUI_FIRST)
QColor = _resolve('QColor', _GUI_FIRST)
QCursor = _resolve('QCursor', _GUI_FIRST)
QFont = _resolve('QFont', _GUI_FIRST)
QIcon = _resolve('QIcon', _GUI_FIRST)
QImage = _resolve('QImage', _GUI_FIRST)
QPainter = _resolve('QPainter', _GUI_FIRST)
QPixmap = _resolve('QPixmap', _GUI_FIRST)
QStandardItem = _resolve('QStandardItem', _GUI_FIRST)
QStandardItemModel = _resolve('QStandardItemModel', _GUI_FIRST)
# QAction lives in QtGui under Qt6, in QtWidgets under Qt5, in QtGui under PySide v1.
QAction = _resolve('QAction', _GUI_FIRST)

# QtWidgets (Qt5/6) / QtGui (PySide v1)
QAbstractItemView = _resolve('QAbstractItemView', _WIDGETS_FIRST)
QApplication = _resolve('QApplication', _WIDGETS_FIRST)
QCheckBox = _resolve('QCheckBox', _WIDGETS_FIRST)
QComboBox = _resolve('QComboBox', _WIDGETS_FIRST)
QCompleter = _resolve('QCompleter', _WIDGETS_FIRST)
QDialog = _resolve('QDialog', _WIDGETS_FIRST)
QFrame = _resolve('QFrame', _WIDGETS_FIRST)
QGroupBox = _resolve('QGroupBox', _WIDGETS_FIRST)
QHeaderView = _resolve('QHeaderView', _WIDGETS_FIRST)
QHBoxLayout = _resolve('QHBoxLayout', _WIDGETS_FIRST)
QLabel = _resolve('QLabel', _WIDGETS_FIRST)
QLineEdit = _resolve('QLineEdit', _WIDGETS_FIRST)
QListView = _resolve('QListView', _WIDGETS_FIRST)
QMainWindow = _resolve('QMainWindow', _WIDGETS_FIRST)
QMenu = _resolve('QMenu', _WIDGETS_FIRST)
QMessageBox = _resolve('QMessageBox', _WIDGETS_FIRST)
QProgressBar = _resolve('QProgressBar', _WIDGETS_FIRST)
QPushButton = _resolve('QPushButton', _WIDGETS_FIRST)
QRadioButton = _resolve('QRadioButton', _WIDGETS_FIRST)
QScrollArea = _resolve('QScrollArea', _WIDGETS_FIRST)
QSizePolicy = _resolve('QSizePolicy', _WIDGETS_FIRST)
QSlider = _resolve('QSlider', _WIDGETS_FIRST)
QSpacerItem = _resolve('QSpacerItem', _WIDGETS_FIRST)
QSplitter = _resolve('QSplitter', _WIDGETS_FIRST)
QStyle = _resolve('QStyle', _WIDGETS_FIRST)
QStyledItemDelegate = _resolve('QStyledItemDelegate', _WIDGETS_FIRST)
QStyleFactory = _resolve('QStyleFactory', _WIDGETS_FIRST)
QStyleOptionComboBox = _resolve('QStyleOptionComboBox', _WIDGETS_FIRST)
QStyleOptionSlider = _resolve('QStyleOptionSlider', _WIDGETS_FIRST)
QTableWidget = _resolve('QTableWidget', _WIDGETS_FIRST)
QTableWidgetItem = _resolve('QTableWidgetItem', _WIDGETS_FIRST)
QTabWidget = _resolve('QTabWidget', _WIDGETS_FIRST)
QTextBrowser = _resolve('QTextBrowser', _WIDGETS_FIRST)
QTextEdit = _resolve('QTextEdit', _WIDGETS_FIRST)
QTreeView = _resolve('QTreeView', _WIDGETS_FIRST)
QTreeWidget = _resolve('QTreeWidget', _WIDGETS_FIRST)
QTreeWidgetItem = _resolve('QTreeWidgetItem', _WIDGETS_FIRST)
QVBoxLayout = _resolve('QVBoxLayout', _WIDGETS_FIRST)
QWidget = _resolve('QWidget', _WIDGETS_FIRST)


# Qt5 exposes Qt.DescendingOrder directly; Qt6 / PySide v1 expose it under Qt.SortOrder.
DescendingOrder = getattr(Qt, 'DescendingOrder', None)
if DescendingOrder is None:
    DescendingOrder = Qt.SortOrder.DescendingOrder
