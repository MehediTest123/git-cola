import os

from qtpy import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


def assert_pyside():
    import PySide
    assert QtCore.QEvent is PySide.QtCore.QEvent
    assert QtGui.QPainter is PySide.QtGui.QPainter
    assert QtWidgets.QWidget is PySide.QtGui.QWidget
    assert QtWebEngineWidgets.QWebEnginePage is PySide.QtWebKit.QWebPage


def assert_pyqt4():
    import PyQt4
    assert QtCore.QEvent is PyQt4.QtCore.QEvent
    assert QtGui.QPainter is PyQt4.QtGui.QPainter
    assert QtWidgets.QWidget is PyQt4.QtGui.QWidget
    assert QtWebEngineWidgets.QWebEnginePage is PyQt4.QtWebKit.QWebPage


def assert_pyqt5():
    import PyQt5
    assert QtCore.QEvent is PyQt5.QtCore.QEvent
    assert QtGui.QPainter is PyQt5.QtGui.QPainter
    assert QtWidgets.QWidget is PyQt5.QtWidgets.QWidget
    assert QtWebEngineWidgets.QWebEnginePage is PyQt5.QtWebKitWidgets.QWebPage


def test_qt_api():
    """
    If QT_API is specified, we check that the correct Qt wrapper was used
    """

    QT_API = os.environ.get('QT_API', None)

    if QT_API == 'pyside':
        assert_pyside()
    elif QT_API in ('pyqt', 'pyqt4'):
        assert_pyqt4()
    elif QT_API == 'pyqt5':
        assert_pyqt5()
    else:
        # If the tests are run locally, USE_QT_API and QT_API may not be
        # defined, but we still want to make sure qtpy is behaving sensibly.
        # We should then be loading, in order of decreasing preference, PyQt5,
        # PyQt4, and PySide.
        try:
            import PyQt5
        except ImportError:
            try:
                import PyQt4
            except ImportError:
                import PySide
                assert_pyside()
            else:
                assert_pyqt4()
        else:
            assert_pyqt5()
