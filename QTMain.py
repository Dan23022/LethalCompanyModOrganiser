import os
import shutil
import sys
import configparser
from PyQt5.QtCore import QMetaObject, QCoreApplication, QRect, QStringListModel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QSizePolicy,
    QMainWindow,
    QWidget,
    QMenuBar,
    QStatusBar,
    QPushButton,
    QListView,
    QLabel,
    QComboBox,
    QGridLayout,
    QApplication, QFileDialog, QMenu, QAction, QVBoxLayout, QProgressBar,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(633, 516)
        try:
            self.verticalLayoutWidget = QWidget(Form)
            self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
            self.verticalLayoutWidget.setGeometry(QRect(10, 90, 611, 411))
            self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout.setObjectName(u"verticalLayout")
            self.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.modsList = QListView(self.verticalLayoutWidget)
            self.modsList.setObjectName(u"modsList")

            self.verticalLayout.addWidget(self.modsList)

            self.progressBar = QProgressBar(self.verticalLayoutWidget)
            self.progressBar.setObjectName(u"progressBar")
            self.progressBar.setValue(0)

            self.verticalLayout.addWidget(self.progressBar)

            self.downloadButton = QPushButton(self.verticalLayoutWidget)
            self.downloadButton.setObjectName(u"downloadButton")

            self.verticalLayout.addWidget(self.downloadButton)

            self.verticalLayoutWidget_2 = QWidget(Form)
            self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
            self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 611, 51))
            self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
            self.verticalLayout_2.setObjectName(u"verticalLayout_2")
            self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.headingLabel = QLabel(self.verticalLayoutWidget_2)
            self.headingLabel.setObjectName(u"headingLabel")
            font = QFont()
            font.setPointSize(24)
            self.headingLabel.setFont(font)

            self.verticalLayout_2.addWidget(self.headingLabel)#

            self.retranslateUi(Form)

            QMetaObject.connectSlotsByName(Form)

        except Exception as e:
            print(f"Error in setupUi: {e}")

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Download more mods", u"Download more mods", None))
        self.downloadButton.setText(QCoreApplication.translate("Form", u"Download", None))
        self.headingLabel.setText(QCoreApplication.translate("Form", u"Download more mods", None))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(698, 569)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionDownload_Mods = QAction(MainWindow)
        self.actionDownload_Mods.setObjectName(u"actionDownload_Mods")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.gridLayout.addWidget(self.loadButton, 4, 1, 1, 1)

        self.unloadedModsList = QListView(self.centralwidget)
        self.unloadedModsList.setObjectName(u"unloadedModsList")
        self.gridLayout.addWidget(self.unloadedModsList, 4, 0, 1, 1)

        self.loadedModsList = QListView(self.centralwidget)
        self.loadedModsList.setObjectName(u"loadedModsList")
        self.gridLayout.addWidget(self.loadedModsList, 4, 3, 1, 1)

        self.unloadBuon = QPushButton(self.centralwidget)
        self.unloadBuon.setObjectName(u"unloadBuon")
        self.gridLayout.addWidget(self.unloadBuon, 4, 1, 9, 1)

        self.unloadedModsLabel = QLabel(self.centralwidget)
        self.unloadedModsLabel.setObjectName(u"unloadedModsLabel")
        font = QFont()
        font.setPointSize(16)
        self.unloadedModsLabel.setFont(font)
        self.gridLayout.addWidget(self.unloadedModsLabel, 3, 0, 1, 2)

        self.loadAllBuon = QPushButton(self.centralwidget)
        self.loadAllBuon.setObjectName(u"loadAllBuon")
        self.gridLayout.addWidget(self.loadAllBuon, 7, 0, 1, 1)

        self.headingLabel = QLabel(self.centralwidget)
        self.headingLabel.setObjectName(u"headingLabel")
        font1 = QFont()
        font1.setPointSize(24)
        self.headingLabel.setFont(font1)
        self.gridLayout.addWidget(self.headingLabel, 0, 0, 1, 4)

        self.unloadAllBuon = QPushButton(self.centralwidget)
        self.unloadAllBuon.setObjectName(u"unloadAllBuon")
        self.gridLayout.addWidget(self.unloadAllBuon, 7, 3, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.loadedModsLabel = QLabel(self.centralwidget)
        self.loadedModsLabel.setObjectName(u"loadedModsLabel")
        self.loadedModsLabel.setFont(font)
        self.gridLayout.addWidget(self.loadedModsLabel, 3, 3, 1, 1)

        self.progilesDropDown = QComboBox(self.centralwidget)
        self.progilesDropDown.setObjectName(u"progilesDropDown")
        self.gridLayout.addWidget(self.progilesDropDown, 2, 0, 1, 1)

        self.saveProfileButton = QPushButton(self.centralwidget)
        self.saveProfileButton.setObjectName(u"saveProfileButton")
        self.gridLayout.addWidget(self.saveProfileButton, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 698, 21))
        self.menuMore = QMenu(self.menubar)
        self.menuMore.setObjectName(u"menuMore")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMore.menuAction())
        self.menuMore.addAction(self.actionDownload_Mods)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LCMDT", None))
        self.actionDownload_Mods.setText(QCoreApplication.translate("MainWindow", u"Download Mods", None))
        self.saveProfileButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.unloadAllBuon.setText(QCoreApplication.translate("MainWindow", u"Unload All", None))
        self.headingLabel.setText(QCoreApplication.translate("MainWindow", u"Lethal Comapny Mod Deployment Tool", None))
        self.loadedModsLabel.setText(QCoreApplication.translate("MainWindow", u"Loaded Mods", None))
        self.loadAllBuon.setText(QCoreApplication.translate("MainWindow", u"Load All", None))
        self.unloadedModsLabel.setText(QCoreApplication.translate("MainWindow", u"Unloaded Mods", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Profile:", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.unloadBuon.setText(QCoreApplication.translate("MainWindow", u"Unload", None))
        self.menuMore.setTitle(QCoreApplication.translate("MainWindow", u"More", None))


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.mods_window = Ui_Form()

        self.loadButton.clicked.connect(self.loadMod)
        self.unloadBuon.clicked.connect(self.unloadMod)
        self.loadAllBuon.clicked.connect(self.loadAllMods)
        self.unloadAllBuon.clicked.connect(self.unloadAllMods)

        self.unloaded_mods_model = QStringListModel()
        self.loaded_mods_model = QStringListModel()

        self.unloadedModsList.setModel(self.unloaded_mods_model)
        self.loadedModsList.setModel(self.loaded_mods_model)

        self.actionDownload_Mods.triggered.connect(self.open_new_window)

    def open_new_window(self):
        try:
            self.mods_window = QWidget()
            ui_form = Ui_Form()
            ui_form.setupUi(self.mods_window)
            self.mods_window.show()
        except Exception as e:
            import traceback
            traceback.print_exc()

    def populateLoaded(self):
        folders = []
        files = []
        scriptDirectory = os.getcwd()

        if "plugins" not in pluginsPath:
            folder_path, _ = QFileDialog.getExistingDirectory(self, "Select Plugins Directory")
            config["PATH"]["path"] = folder_path
            print(str(folder_path))
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            folder_path = pluginsPath

        for entry in os.listdir(f"{scriptDirectory}/mods"):
            full_path = os.path.join(f"{scriptDirectory}/mods", entry)
            if os.path.isdir(full_path):
                folders.append(entry)
            else:
                files.append(entry)

        unloaded_mods = folders + files
        self.unloaded_mods_model.setStringList(unloaded_mods)

        loaded_folders = []
        loaded_files = []
        for entry in os.listdir(pluginsPath):
            full_path = os.path.join(pluginsPath, entry)
            if os.path.isdir(full_path):
                loaded_folders.append(entry)
            else:
                loaded_files.append(entry)

        loaded_mods = loaded_folders + loaded_files
        self.loaded_mods_model.setStringList(loaded_mods)

    def showEvent(self, event):
        super(MyMainWindow, self).showEvent(event)
        self.populateLoaded()

    def loadAllMods(self):
        script_directory = os.getcwd()
        global pluginsPath

        if "SteamLibrary" not in pluginsPath:
            folder_path, _ = QFileDialog.getExistingDirectory(self, "Select Directory")
            config["PATH"]["path"] = folder_path
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            folder_path = pluginsPath

        folders = []
        files = []
        for entry in os.listdir(os.path.join(script_directory, "mods")):
            full_path = os.path.join(os.path.join(script_directory, "mods"), entry)
            if os.path.isdir(full_path):
                folders.append(entry)
            else:
                files.append(entry)

        for mod in folders + files:
            target_path = os.path.join(folder_path, mod)
            shutil.move(os.path.join(script_directory, "mods", mod), target_path)
            print(f"{mod} - has been Loaded")

        self.unloaded_mods_model.setStringList([])

        loaded_folders = []
        loaded_files = []
        for entry in os.listdir(folder_path):
            full_path = os.path.join(folder_path, entry)
            if os.path.isdir(full_path):
                loaded_folders.append(entry)
            else:
                loaded_files.append(entry)

        loaded_mods = loaded_folders + loaded_files
        self.loaded_mods_model.setStringList(loaded_mods)

    def unloadAllMods(self):
        script_directory = os.getcwd()
        global pluginsPath

        if "SteamLibrary" not in pluginsPath:
            folder_path, _ = QFileDialog.getExistingDirectory(self, "Select Directory")
            config["PATH"]["path"] = folder_path
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        else:
            folder_path = pluginsPath

        folders = []
        files = []
        for entry in os.listdir(folder_path):
            full_path = os.path.join(folder_path, entry)
            if os.path.isdir(full_path):
                folders.append(entry)
            else:
                files.append(entry)

        for mod in folders + files:
            shutil.move(os.path.join(folder_path, mod), os.path.join(script_directory, "mods", mod))
            print(f"{mod} - has been Unloaded")

        self.loaded_mods_model.setStringList([])

        unloaded_folders = []
        unloaded_files = []
        for entry in os.listdir(os.path.join(script_directory, "mods")):
            full_path = os.path.join(os.path.join(script_directory, "mods"), entry)
            if os.path.isdir(full_path):
                unloaded_folders.append(entry)
            else:
                unloaded_files.append(entry)

        unloaded_mods = unloaded_folders + unloaded_files
        self.unloaded_mods_model.setStringList(unloaded_mods)

        self.unloadedModsList.setModel(self.unloaded_mods_model)

    def loadMod(self):
        selected_index = self.unloadedModsList.currentIndex()
        if selected_index.isValid():
            selected_mod = selected_index.data()
            script_directory = os.getcwd()
            global pluginsPath

            if "SteamLibrary" not in pluginsPath:
                folder_path, _ = QFileDialog.getExistingDirectory(self, "Select Directory")
                config["PATH"]["path"] = folder_path
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                folder_path = pluginsPath

            unloaded_mods = [item for item in self.unloaded_mods_model.stringList() if item != selected_mod]
            self.unloaded_mods_model.setStringList(unloaded_mods)

            target_path = os.path.join(folder_path, selected_mod)
            shutil.move(os.path.join(script_directory, "mods", selected_mod), target_path)
            print(f"{selected_mod} - has been Loaded")

            loaded_folders = []
            loaded_files = []
            for entry in os.listdir(folder_path):
                full_path = os.path.join(folder_path, entry)
                if os.path.isdir(full_path):
                    loaded_folders.append(entry)
                else:
                    loaded_files.append(entry)

            loaded_mods = loaded_folders + loaded_files
            self.loaded_mods_model.setStringList(loaded_mods)

    def unloadMod(self):
        selected_index = self.loadedModsList.currentIndex()
        if selected_index.isValid():
            selected_mod = selected_index.data()
            script_directory = os.getcwd()
            global pluginsPath

            if "SteamLibrary" not in pluginsPath:
                folder_path, _ = QFileDialog.getExistingDirectory(self, "Select Directory")
                config["PATH"]["path"] = folder_path
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
            else:
                folder_path = pluginsPath

            shutil.move(os.path.join(folder_path, selected_mod), os.path.join(script_directory, "mods", selected_mod))
            print(f"{selected_mod} - has been Unloaded")

            loaded_folders = []
            loaded_files = []
            for entry in os.listdir(folder_path):
                full_path = os.path.join(folder_path, entry)
                if os.path.isdir(full_path):
                    loaded_folders.append(entry)
                else:
                    loaded_files.append(entry)

            loaded_mods = loaded_folders + loaded_files
            self.loaded_mods_model.setStringList(loaded_mods)

            self.loadedModsList.setModel(self.loaded_mods_model)

            unloaded_folders = []
            unloaded_files = []
            for entry in os.listdir(os.path.join(script_directory, "mods")):
                full_path = os.path.join(os.path.join(script_directory, "mods"), entry)
                if os.path.isdir(full_path):
                    unloaded_folders.append(entry)
                else:
                    unloaded_files.append(entry)

            unloaded_mods = unloaded_folders + unloaded_files
            self.unloaded_mods_model.setStringList(unloaded_mods)

            self.unloadedModsList.setModel(self.unloaded_mods_model)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    pluginsPath = config["PATH"]["path"]

    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
