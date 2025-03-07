import sys  # 导入 sys 模块，用于与 Python 解释器交互
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow  # 从 PyQt5 中导入所需的类


# 创建一个主窗口类，继承自 QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类 QMainWindow 的初始化方法
        self.setWindowTitle("PyQt5 第一个窗口")  # 设置窗口标题

        # 创建一个 QLabel 标签，并将其作为主窗口的中央控件
        label = QLabel("Hello, World!", self)
        self.setCentralWidget(label)  # 将标签作为窗口的中央控件


# 创建一个 PyQt5 应用程序对象
app = QApplication(sys.argv)

# 创建主窗口实例
window = MainWindow()
window.show()  # 显示窗口

# 进入应用程序的事件循环，保持应用程序运行，直到关闭窗口
sys.exit(app.exec_())
