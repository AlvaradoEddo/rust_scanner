from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from lexer import *
from sintactico import *


class RustEditor(QPlainTextEdit):
    '''
    References: 
    * https://nachtimwald.com/2009/08/19/better-qplaintextedit-with-line-numbers/
    * https://play.rust-lang.org/  

    @Todo:
    * Add Rust Syntax Highlighter 
    '''

    class NumberBar(QWidget):
        '''numbar for the code editor'''

        def __init__(self, editor):
            QWidget.__init__(self, editor)

            self.editor = editor
            self.editor.blockCountChanged.connect(self.updateWidth)
            self.editor.updateRequest.connect(self.updateContents)
            self.font = QFont()
            self.numberBarColor = QColor("#e8e8e8")

        def paintEvent(self, event):

            painter = QPainter(self)
            painter.fillRect(event.rect(), self.numberBarColor)

            block = self.editor.firstVisibleBlock()

            while block.isValid():
                blockNumber = block.blockNumber()
                block_top = self.editor.blockBoundingGeometry(
                    block).translated(self.editor.contentOffset()).top()

                if not block.isVisible() or block_top >= event.rect().bottom():
                    break

                if blockNumber == self.editor.textCursor().blockNumber():
                    self.font.setBold(True)
                    painter.setPen(QColor("#2F2F36"))
                else:
                    self.font.setBold(False)
                    painter.setPen(QColor("#2F2F36"))
                painter.setFont(self.font)

                paint_rect = QRect(0, block_top, self.width(),
                                   self.editor.fontMetrics().height())
                painter.drawText(paint_rect, Qt.AlignRight, str(blockNumber+1))

                block = block.next()

            painter.end()

            QWidget.paintEvent(self, event)

        def getWidth(self):
            count = self.editor.blockCount()
            width = self.fontMetrics().width(str(count)) + 10
            return width

        def updateWidth(self):
            width = self.getWidth()
            if self.width() != width:
                self.setFixedWidth(width)
                self.editor.setViewportMargins(width, 0, 0, 0)

        def updateContents(self, rect, scroll):
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update(0, rect.y(), self.width(), rect.height())

            if rect.contains(self.editor.viewport().rect()):
                fontSize = self.editor.currentCharFormat().font().pointSize()
                self.font.setPointSize(fontSize)
                self.font.setStyle(QFont.StyleNormal)
                self.updateWidth()

    def __init__(self, DISPLAY_LINE_NUMBERS=True, HIGHLIGHT_CURRENT_LINE=True,
                 SyntaxHighlighter=None):

        super(RustEditor, self).__init__()

        self.setFont(QFont("Ubuntu Mono", 11))
        self.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.DISPLAY_LINE_NUMBERS = DISPLAY_LINE_NUMBERS

        if DISPLAY_LINE_NUMBERS:
            self.number_bar = self.NumberBar(self)

        if HIGHLIGHT_CURRENT_LINE:
            self.currentLineNumber = None
            self.currentLineColor = QColor("#FFE2B6")
            self.cursorPositionChanged.connect(self.highligtCurrentLine)

    def resizeEvent(self, *e):

        if self.DISPLAY_LINE_NUMBERS:
            cr = self.contentsRect()
            rec = QRect(cr.left(), cr.top(),
                        self.number_bar.getWidth(), cr.height())
            self.number_bar.setGeometry(rec)

        QPlainTextEdit.resizeEvent(self, *e)

    def highligtCurrentLine(self):
        newCurrentLineNumber = self.textCursor().blockNumber()
        if newCurrentLineNumber != self.currentLineNumber:
            self.currentLineNumber = newCurrentLineNumber
            hi_selection = QTextEdit.ExtraSelection()
            hi_selection.format.setBackground(self.currentLineColor)
            hi_selection.format.setProperty(
                QTextFormat.FullWidthSelection, True)
            hi_selection.cursor = self.textCursor()
            hi_selection.cursor.clearSelection()
            self.setExtraSelections([hi_selection])


class LabelCode(QWidget):
    def __init__(self):
        super(LabelCode, self).__init__()
        layout = QHBoxLayout()
        label_text = QLabel()
        label_text.setText("<h4>Start coding (having fun) here!</h4>")
        label_text.setStyleSheet("color: #2D2D2D;")
        label_code = QLabel()
        pixmap_code = QPixmap("./images/GUI/code.png")
        pixmap_code = pixmap_code.scaled(20, 20, Qt.KeepAspectRatio)
        label_code.setPixmap(pixmap_code)

        layout.addWidget(label_code)
        layout.addWidget(label_text)
        layout.addStretch(1)
        self.setLayout(layout)


class LabelExecution(QWidget):
    vb = QVBoxLayout()
    hb_layout = QHBoxLayout()
    label_text = None
    plain_text = None
    def __init__(self):
        super(LabelExecution, self).__init__()
        self.label_text = QLabel()
        self.label_text.setText("<h4>Execution</h4>")
        self.label_text.setStyleSheet("color: #2D2D2D;")
        self.label_code = QLabel()
        pixmap_code = QPixmap("./images/GUI/rs-exec.png")
        pixmap_code = pixmap_code.scaled(50, 100, Qt.KeepAspectRatio)
        self.label_code.setPixmap(pixmap_code)

        self.plain_text = QPlainTextEdit()
        self.plain_text.setReadOnly(True)
        self.plain_text.setStyleSheet("background-color: #E5E8ED;")
        
        self.hb_layout.addWidget(self.label_code)
        self.hb_layout.addWidget(self.label_text)
        self.hb_layout.addStretch(1)

        self.vb.addLayout(self.hb_layout)
        self.vb.addWidget(self.plain_text)
        self.setLayout(self.vb)


class Buttons(QWidget):
    def __init__(self, editor, execution_label):
        super(Buttons, self).__init__()
        layout = QVBoxLayout()
        button_lexer = QPushButton("Run Lexer")
        button_lexer.setIcon(QIcon("./images/GUI/play.png"))
        button_lexer.setFixedSize(100, 40)
        button_lexer.setCursor(QCursor(Qt.PointingHandCursor))
        button_lexer.clicked.connect(lambda: self.onClickedLexer(editor, execution_label))

        layout = QVBoxLayout()
        button_parser = QPushButton("Run Parser")
        button_parser.setIcon(QIcon("./images/GUI/play.png"))
        button_parser.setFixedSize(100, 40)
        button_parser.setCursor(QCursor(Qt.PointingHandCursor))
        button_parser.clicked.connect(lambda: self.onClickedParser(editor, execution_label))

        button_open = QPushButton("Open File")
        button_open.setIcon(QIcon("./images/GUI/open.png"))
        button_open.setFixedSize(100, 40)
        button_open.setCursor(QCursor(Qt.PointingHandCursor))

        layout.addWidget(button_lexer)
        layout.addWidget(button_parser)
        layout.addWidget(button_open)
        self.setLayout(layout)

    def onClickedLexer(self,editor,execution_label):
        print("Clicked")
        print(editor.toPlainText())
        tp = execution_label.plain_text
        tp.insertPlainText("")
        l_token = run_lexer(editor.toPlainText())
        for tok in l_token:
            tp.insertPlainText("{:5} : {:5}".format(tok.value,tok.type))
            tp.insertPlainText("\n")
        tp.insertPlainText("\n")
        tp.insertPlainText("\n")

    def onClickedParser(self,editor,execution_label):
        tp = execution_label.plain_text
        try:
            p_tree = run_parser(editor.toPlainText())
            print(f'Este es el ptree: {p_tree}')
            tp.insertPlainText(str(p_tree))
            tp.insertPlainText("\n")
        except Exception as e:
            tp.insertPlainText(str(e))
            tp.insertPlainText("\n")
            tp.insertPlainText("\n")
        

class SyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super(SyntaxHighlighter, self).__init__(parent)
        self._lines = {}


class MainApp(QMainWindow):
    def __init__(self, parent=None, *args):
        super().__init__()
        self.title = 'Proyecto Lenguajes'
        self.setGeometry(100, 100, 900, 600)
        self.setWindowIcon(QIcon("./images/GUI/ico.png"))
        self.setStyleSheet("background-color: #E5E8ED;")

        self.UIComponents()

    def UIComponents(self):

        self.setStyleSheet("""
        QPushButton {
            background-color: #CD5C1C;
            color: #FFFFFF;
            border-color: #f44336;
            border-radius: 5px;
         }
        
        QPushButton:hover {
            background-color: #EF671B;
            color: #FFFFFF;
        }

        QPlainTextEdit {
            background-color: #FFFFFF;
            font: 10pt Monospace;
            color: #2D2D2D;
            border-radius: 5px;
            border: 1.5px solid;
            border-color: #C4C4C4;             
        }

        QLabel{
            font: 12pt Ubuntu;
        }
        """)
        self.setWindowTitle(self.title)

        # Labels declarations
        label_img = QLabel(self)
        label_code = LabelCode()
        label_exec = LabelExecution()

        editor = RustEditor(DISPLAY_LINE_NUMBERS=True,
                            HIGHLIGHT_CURRENT_LINE=True)

        buttons = Buttons(editor,label_exec)

        splitter = QFrame()
        splitter.setObjectName("splitter")
        splitter.setFrameShape(QFrame.HLine)
        splitter.setLineWidth(1)
        splitter.setStyleSheet("#splitter{ color: #C4C4C4; }")

        # adding layouts
        layout_v = QVBoxLayout()
        widget = QWidget(self)
        widget_2 = QWidget(self)

        hbox = QHBoxLayout()
        hbox.addWidget(editor)
        hbox.addWidget(buttons)
        widget_2.setLayout(hbox)

        # Adding widgets to layouts
        layout_v.addWidget(label_img)
        layout_v.addWidget(label_code)
        layout_v.addWidget(widget_2)
        layout_v.addWidget(splitter)
        layout_v.addWidget(label_exec)

        layout_v.addStretch(1)

        widget.setLayout(layout_v)
        self.setCentralWidget(widget)

        # Rust scanner logo
        pixmap_rust = QPixmap("./images/GUI/rust.png")
        label_img.setPixmap(pixmap_rust)
        label_img.resize(pixmap_rust.width(), pixmap_rust.height())
        label_img.setAlignment(Qt.AlignHCenter)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()
