# from PyQt5 import *
from interface.main_ui import *
from classes.database import *
from classes.riot.login import *
import classes.riot.get_account_data as get_account_data
from classes.social_links import SocialLinks
from psutil import process_iter
from os import system
from os.path import isfile
import sys
system('cls')



class MainWindow(QMainWindow):
    def __init__(self):
        self.version = "0.0.1"
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_9.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">League Account Manager</span></p><p align=\"center\"><span style=\" font-size:14pt;\">v{}</span></p><p align=\"center\"><span style=\" font-size:20pt;\">Developed by: Gabriel Viana</span></p></body></html>".format(self.version))
        if isfile("./data.db") == False:
            self.ui.tabWidget.setCurrentIndex(2)
        self.db = Database()

        self.temp_username = ""
        self.temp_summoner_data = {
            "accountId": 0,
            "summonerId": 0,
            "puuid": "",
            "profileIconId": 0
        }

        self.ui.login_input.setText("")
        self.ui.password_input.setText("")

        self.ui.acc_list.setColumnCount(7)
        self.ui.acc_list.setHorizontalHeaderLabels(["Server", "Username", "Summoner Name", "BE", "RP", "SoloQ", "FlexQ"])
        self.ui.acc_list.setColumnWidth(0, 43)
        self.ui.acc_list.setColumnWidth(1, 120)
        self.ui.acc_list.setColumnWidth(2, 120)
        self.ui.acc_list.setColumnWidth(3, 70)
        self.ui.acc_list.setColumnWidth(4, 70)
        self.ui.acc_list.setColumnWidth(5, 220)
        self.ui.acc_list.setColumnWidth(6, 220)
        
        self.list_accounts("ALL", "All")
        self.ui.add_account_btn.clicked.connect(self.add_account)
        self.ui.manage_btn.clicked.connect(self.manage_account)
        self.ui.save_changes_btn.clicked.connect(self.save_changes)
        self.ui.login_btn.clicked.connect(self.login_account)
        self.ui.dele_account_btn.clicked.connect(self.delete_account)
        self.ui.get_data_btn.clicked.connect(self.get_summoner_data)
        self.ui.copy_username.clicked.connect(lambda: self.copy_to_clipboard("username"))
        self.ui.copy_password.clicked.connect(lambda: self.copy_to_clipboard("password"))
        self.ui.copy_summoner.clicked.connect(lambda: self.copy_to_clipboard("summoner"))
        self.ui.select_server.activated[str].connect(self.list_accounts_server)
        self.ui.select_elo.activated[str].connect(self.list_accounts_elo)
        self.ui.disc_btn.clicked.connect(lambda: self.copy_to_clipboard("discord"))
        self.ui.tt_btn.clicked.connect(lambda: SocialLinks("twitter").openLink())
        self.ui.insta_btn.clicked.connect(lambda: SocialLinks("instagram").openLink())
        self.ui.git_btn.clicked.connect(lambda: SocialLinks("github").openLink())
        self.ui.pp_btn.clicked.connect(lambda: SocialLinks("paypal").openLink())
        self.ui.acc_list.itemDoubleClicked.connect(self.login_account)

        self.ui.statusBar.showMessage("...")
    
    def copy_to_clipboard(self, input):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        if input == "username":
            cb.setText(self.ui.m_login_input.text(), mode=cb.Clipboard)
        elif input == "password":
            cb.setText(self.ui.m_password_input.text(), mode=cb.Clipboard)
        elif input == "summoner":
            cb.setText(self.ui.m_summoner_input.text(), mode=cb.Clipboard)
        elif input == "discord":
            cb.setText("Sirius Beck#4365", mode=cb.Clipboard)
            self.ui.statusBar.showMessage("Username copied to clipboard!", 2000)
            return None
        self.ui.statusBar.showMessage("Text copied to clipboard!", 2000)
    
    def msg(self, type, title, msg):
        if type == "information":
            box = QMessageBox.information(self, title, msg, buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
        elif type == "question":
            box = QMessageBox.question(self, title, msg, defaultButton=QMessageBox.Yes)
        elif type == "warning":
            box = QMessageBox.warning(self, title, msg, buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
        elif type == "critical":
            box = QMessageBox.critical(self, title, msg, buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok)
        else:
            print("Wrong QMessageBox type!")
    
    def add_account(self):
        server = self.ui.select_server.currentText()
        elo = self.ui.select_elo.currentText()
        username = self.ui.login_input.text()
        password = self.ui.password_input.text()
        if username != "" and password != "":
            rows = self.db.search_account(username)
            if len(rows) > 0:
                self.msg("warning", "Error adding account", "This account has already been added!")
            else:
                self.db.add_account(username, password)
                self.ui.login_input.setText("")
                self.ui.password_input.setText("")
                rows = self.db.search_account(username)
                if len(rows) > 0:
                    self.ui.statusBar.showMessage("Account successfully added!", 2000)
                else:
                    self.msg("critical", "Error adding account", "Account not added!")
                self.list_accounts(server, elo)
        else:
            self.msg("warning", "Error adding account", "Please fill in all fields first!")
    
    def list_accounts(self, server, elo):
        rows = self.db.list_accounts(server, elo)
        self.ui.acc_list.setRowCount(self.db.rows_count)

        row_count = 0
        for row in rows:
            self.ui.acc_list.setItem(row_count, 0, QTableWidgetItem(row[0]))
            self.ui.acc_list.setItem(row_count, 1, QTableWidgetItem(row[6]))
            self.ui.acc_list.setItem(row_count, 2, QTableWidgetItem(row[1]))
            self.ui.acc_list.setItem(row_count, 3, QTableWidgetItem(str(row[2])))
            self.ui.acc_list.setItem(row_count, 4, QTableWidgetItem(str(row[3])))
            self.ui.acc_list.setItem(row_count, 5, QTableWidgetItem(row[4]))
            self.ui.acc_list.setItem(row_count, 6, QTableWidgetItem(row[5]))
            row_count += 1

    def list_accounts_server(self, server):
        elo = self.ui.select_elo.currentText()
        self.list_accounts(server, elo)
    
    def list_accounts_elo(self, elo):
        server = self.ui.select_server.currentText()
        self.list_accounts(server, elo)
    
    def manage_account(self):
        print('current username key: ' + self.temp_username)
        selected_account = self.ui.acc_list.selectedItems()
        if len(selected_account) == 7:
            self.temp_username = selected_account[1].text()
            print('username key changed to: ' + self.temp_username)
            rows = self.db.search_account(self.temp_username)
            for row in rows:
                self.ui.m_server_input.setText(row[0])
                self.ui.m_summoner_input.setText(row[1])
                self.ui.m_be_input.setText(str(row[2]))
                self.ui.m_rp_input.setText(str(row[3]))
                self.ui.m_soloq_input.setText(row[4])
                self.ui.m_flexq_input.setText(row[5])
                self.ui.m_login_input.setText(row[6])
                self.ui.m_password_input.setText(row[7])
                self.ui.tabWidget.setCurrentIndex(1)
                self.temp_summoner_data = {
                    "accountId": row[8],
                    "summonerId": row[9],
                    "puuid": row[10],
                    "profileIconId": row[11]
                }
        else:
            self.msg("warning", "No account selected", "Please select an account first!")
    
    def get_summoner_data(self):
        get_account_data.check_lol(False)
        if get_account_data.is_logged:
            if self.temp_summoner_data['accountId'] == get_account_data.summoner_data['accountId']:
                # Get summoner region
                self.ui.m_server_input.setText(get_account_data.region_data['Server'])
                self.ui.m_summoner_input.setText(get_account_data.summoner_data['displayName'])
                self.ui.m_be_input.setText(str(get_account_data.wallet_data['ip']))
                self.ui.m_rp_input.setText(str(get_account_data.wallet_data['rp']))
                self.ui.m_soloq_input.setText(get_account_data.soloq)
                self.ui.m_flexq_input.setText(get_account_data.flexq)
                self.temp_summoner_data = {
                    "accountId": get_account_data.summoner_data['accountId'],
                    "summonerId": get_account_data.summoner_data['summonerId'],
                    "puuid": get_account_data.summoner_data['puuid'],
                    "profileIconId": get_account_data.summoner_data['profileIconId']
                }
            else:
                self.msg("warning", "Account not connected", "The selected account is not logged in.")
        else:
             self.msg("warning", "Account not connected", "The selected account is not logged in.")
    
    def save_changes(self):
        server = self.ui.select_server.currentText()
        elo = self.ui.select_elo.currentText()
        self.db.save_changes(
            self.ui.m_server_input.text(),
            self.ui.m_summoner_input.text(),
            self.ui.m_be_input.text(),
            self.ui.m_rp_input.text(),
            self.ui.m_soloq_input.text(),
            self.ui.m_flexq_input.text(),
            self.ui.m_login_input.text(),
            self.ui.m_password_input.text(),
            self.temp_summoner_data['accountId'],
            self.temp_summoner_data['summonerId'],
            self.temp_summoner_data['puuid'],
            self.temp_summoner_data['profileIconId'],
            self.temp_username
        )
        self.list_accounts(server, elo)
        self.msg("information", "Success", "Successfully changed data!")
        self.ui.tabWidget.setCurrentIndex(0)

    def delete_account(self):
        server = self.ui.select_server.currentText()
        elo = self.ui.select_elo.currentText()
        username = self.ui.m_login_input.text()
        self.db.delete_account(username)
        rows = self.db.search_account(username)
        if len(rows) > 0:
            self.msg("critical", "Error deleting", "Error deleting account, just click the \"Manage Selected Account\" button again.")
        else:
            self.ui.statusBar.showMessage("Account has been successfully deleted!", 2000)
        self.list_accounts(server, elo)
        self.ui.tabWidget.setCurrentIndex(0)

    def login_account(self):
        server = self.ui.select_server.currentText()
        elo = self.ui.select_elo.currentText()
        get_account_data.check_lol(True)
        if get_account_data.is_logged == False:
            if "RiotClientUx.exe" in (proc.name() for proc in process_iter()):
                selected_account = self.ui.acc_list.selectedItems()
                rows = self.db.search_account(selected_account[1].text())
                for row in rows:
                    summoner = row[1]
                    username = row[6]
                    password = row[7]
                self.ui.statusBar.showMessage(f"Trying to log into the account (Username: {username})")
                login = Login(username, password)
                if login.check_error() == "connection":
                    self.msg("critical", "Connection error", "Please reopen the Riot Client!")
                    self.ui.statusBar.showMessage("...")
                elif login.check_error() == 'auth_failure':
                    self.msg("critical", "Authentication error", "Incorrect username or password")
                    self.ui.statusBar.showMessage("...")
                elif login.check_error() == "":
                    if summoner == "?????":
                        self.ui.statusBar.showMessage("Getting first access data...")
                        get_account_data.is_login = False
                        get_account_data.first_login()
                        self.db.first_login_update(
                            get_account_data.region_data['Server'],
                            get_account_data.summoner_data['displayName'],
                            get_account_data.wallet_data['ip'],
                            get_account_data.wallet_data['rp'],
                            get_account_data.soloq,
                            get_account_data.flexq,
                            get_account_data.summoner_data['accountId'],
                            get_account_data.summoner_data['summonerId'],
                            get_account_data.summoner_data['puuid'],
                            get_account_data.summoner_data['profileIconId'],
                            username
                        )
                        self.ui.statusBar.showMessage("Data successfully updated!", 2000)
                        self.list_accounts(server, elo)
                    self.ui.statusBar.showMessage("Account successfully logged in!", 2000)
            else:
                self.msg("warning", "Riot client is closed", "Open the Riot client first!")
        else:
            self.ui.statusBar.showMessage("Log out of current account first!", 2000)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()