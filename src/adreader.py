#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
# Import compiled GUI
from mainwindowUi import Ui_MainWindow
# Import parsers
import feedparser
from articleparser import *


class Main(QMainWindow):
    """Main Window Class
    Define
    """

    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        # Setup pyuic generated code
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Parse RSS feed
        ad = feedparser.parse("http://www.appuntidigitali.it/feed")
        #Create article parser
        self.ap = ArticleParser()
        #Populate TreeWiget with feed elements
        for entry in ad.entries:
            item = QTreeWidgetItem([
                entry.title,
                entry.author,
                entry.slash_comments,
                entry.link,
                ])
            self.ui.treeWidget.addTopLevelItem(item)

    def on_treeWidget_itemDoubleClicked(self):
        """ Load feed item URL in the webview on doubleclick
        Show article's title in a text label
        """
        url = str(self.ui.treeWidget.currentItem().text(3))
        self.ui.webView.setHtml(self.ap.get_article(url))
        self.ui.title.setText(self.ui.treeWidget.currentItem().text(0))

    def on_actionQuit_triggered(self):
        """Exit from main window when actionQuit is triggered"""
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Set application proxy
    #proxy = QNetworkProxy(
    #    QNetworkProxy.HttpProxy,
    #    "proxy.stud.univpm.it",
    #    3128
    #    )
    #QNetworkProxy.setApplicationProxy(proxy)
    #Create and show main window
    window = Main()
    window.show()
    sys.exit(app.exec_())
