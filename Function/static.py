import socket, os, json
from PySide6.QtWidgets import QMessageBox
from pathvalidate import sanitize_filename, sanitize_filepath


""" 检测端口是否被占用 """
def is_port_in_use(port):
    try:
        # 创建一个套接字并尝试绑定到指定端口
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return False  # 端口未被占用
    except OSError:
        return True  # 端口已被占用
    
""" 查找可用端口 """
def find_available_port(start_port, max_attempts=1000):
    for port in range(start_port, start_port + max_attempts):
        if not is_port_in_use(port):
            return port
    return None  # 未找到可用端口

""" 弹窗 """
def message_box(title, text, icon=QMessageBox.Warning):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setIcon(icon)
    msg.exec()

""" 创建文件夹 """
def mkdir(dirpath, replace="_"):
    dirpath = sanitize_filepath(dirpath , replace)
    # 检查目录路径是否存在
    if not os.path.exists(dirpath):
        # 如果路径不存在，创建路径
        os.makedirs(dirpath)

def load_config():
    """ 加载json文件 """
    with open('config.json', 'r') as file:
        return json.load(file)
    
def save_config(config):
    """ 保存config文件 """
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)

def is_debug():
    """ 是否是调试模式 """
    return "DEBUG" if load_config()["debug"] else "INFO"
