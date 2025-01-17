import requests
from PyQt5.QtCore import QThread, pyqtSignal

class ConnectionCheckThread(QThread):
    github_status_checked = pyqtSignal(bool)
    server_status_checked = pyqtSignal(bool)

    def run(self):
        try:
            response = requests.get('https://github.com', timeout=10)
            if response.status_code == 200:
                self.github_status_checked.emit(True)
            else:
                raise Exception("GitHub no response")
        except:
            self.github_status_checked.emit(False)

        try:
            response = requests.get('https://stlunlocker.pro', timeout=10)
            if response.status_code == 200:
                self.server_status_checked.emit(True)
            else:
                raise Exception("Server no response")
        except:
            self.server_status_checked.emit(False)