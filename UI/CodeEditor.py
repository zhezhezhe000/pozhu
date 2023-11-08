from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtGui import QTextFormat, QPainter, QColor
from PySide6.QtWidgets import QApplication, QPlainTextEdit, QWidget, QTextEdit
"""
chatgpt生成的可以显示行号的plainTextEdit组件
称为代码编辑器 CodeEditor.py
"""
class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)

    # 会话事件
    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)

# 创建一个自定义 QWidget 用于显示行号
class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineNumberArea = LineNumberArea(self)

        # 监听文本内容的变化以更新行号区域
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)

    # 计算行号区域的宽度
    def lineNumberAreaWidth(self):
        digits = 1
        max_count = max(1, self.blockCount())
        while max_count >= 10:
            max_count /= 10
            digits += 1

        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits

        return space

    # 更新行号区域的宽度
    def updateLineNumberAreaWidth(self, newBlockCount):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    # 更新行号区域的显示
    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    # 处理窗口的大小变化事件
    def resizeEvent(self, event):
        super().resizeEvent(event)

        cr = self.contentsRect()
        width = self.lineNumberAreaWidth()
        rect = QRect(cr.left(), cr.top(), width, cr.height())
        self.lineNumberArea.setGeometry(rect)

    # 处理行号区域的绘制事件
    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            block_number += 1

    # 高亮当前行的函数
    def highlightCurrentLine(self):
        extra_selections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()

            line_color = QColor(Qt.yellow).lighter(160)

            selection.format.setBackground(line_color)
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)



if __name__ == "__main__":

    app = QApplication([])

    editor = CodeEditor()
    editor.show()

    app.exec()
