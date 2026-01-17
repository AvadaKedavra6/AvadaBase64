#
#               AvadaKedavra6 - Base64
#               I made it for roblox and then I wanted to do it in python x)
#               Its also for train me on PyQt6 bc i'm a beginner in ^^
#

import sys
import base64
from typing import Optional, Tuple
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QComboBox, QCheckBox, QGroupBox, QTabWidget, QStatusBar, QMessageBox
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QFont, QDesktopServices, QCursor

# Base64 Engine
class Base64Engine:
    def __init__(self):
        self.StandardAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        self.UrlSafeAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    
    # Encode funcs
    def encode_standard(self, input_text: str, use_padding: bool = True) -> Tuple[Optional[str], Optional[str]]:
        try:
            if not input_text:
                return None, "Input cannot be empty"
            
            encoded = base64.b64encode(input_text.encode('utf-8')).decode('ascii')

            if not use_padding:
                encoded = encoded.rstrip('=')
            
            return encoded, None
        except Exception as e:
            return None, f"Encoding error: {str(e)}"
        
    def encode_urlsafe(self, input_text: str, use_padding: bool = True) -> Tuple[Optional[str], Optional[str]]:
        try:
            if not input_text:
                return None, "Input cannot be empty"
            
            encoded = base64.urlsafe_b64encode(input_text.encode('utf-8')).decode('ascii')
            
            if not use_padding:
                encoded = encoded.rstrip('=')
            
            return encoded, None
        except Exception as e:
            return None, f"Encoding error: {str(e)}"
    
    # Decode funcs
    def decode_standard(self, input_text: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            if not input_text:
                return None, "Input cannot be empty"
            
            padding = 4 - (len(input_text) % 4)
            if padding != 4:
                input_text += '=' * padding
            
            decoded = base64.b64decode(input_text).decode('utf-8')
            return decoded, None
        except Exception as e:
            return None, f"Decoding error: {str(e)}"
    
    def decode_urlsafe(self, input_text: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            if not input_text:
                return None, "Input cannot be empty"
            
            padding = 4 - (len(input_text) % 4)
            if padding != 4:
                input_text += '=' * padding
            
            decoded = base64.urlsafe_b64decode(input_text).decode('utf-8')
            return decoded, None
        except Exception as e:
            return None, f"Decoding error: {str(e)}"
    
    def decode_auto(self, input_text: str) -> Tuple[Optional[str], Optional[str]]:
        if not input_text:
            return None, "Input cannot be empty"
        
        if '-' in input_text or '_' in input_text:
            return self.decode_urlsafe(input_text)
        else:
            return self.decode_standard(input_text)
        
    def is_valid(self, input_text: str, urlsafe: bool = False) -> bool:
        if not input_text or len(input_text) % 4 != 0:
            if not input_text:
                return False
        
        alphabet = self.urlsafe_alphabet if urlsafe else self.standard_alphabet
        valid_chars = set(alphabet + '=')
        
        return all(c in valid_chars for c in input_text)
    
# Class Btn
class Button(QPushButton):
    def __init__(self, text: str, primary: bool = False):
        super().__init__(text)
        self.setMinimumHeight(40)
        self.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        
        if primary:
            self.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #667eea, stop:1 #764ba2);
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #5568d3, stop:1 #6941a0);
                }
                QPushButton:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                        stop:0 #4a5bc4, stop:1 #5c3890);
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    color: #333;
                    border: 2px solid #ddd;
                    border-radius: 8px;
                    padding: 10px 20px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                    border-color: #ccc;
                }
                QPushButton:pressed {
                    background-color: #d0d0d0;
                }
            """)

# Class UI
class Base64GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.engine = Base64Engine()
        self.github_url = "https://github.com/AvadaKedavra6/AvadaBase64"
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("AvadaKedavra Base64 - Encoder/Decoder")
        self.setMinimumSize(900, 700)
        self.apply_dark_theme()
        
        # Central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        top_bar = QHBoxLayout()
        
        # GitHub
        github_btn = QPushButton("⭐")
        github_btn.setFont(QFont("Segoe UI", 10))
        github_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        github_btn.setFixedSize(50, 35)
        github_btn.clicked.connect(self.open_github)
        github_btn.setStyleSheet("""
            QPushButton {
                background-color: #24292e;
                color: white;
                border: 2px solid #444;
                border-radius: 6px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #2f363d;
                border-color: #667eea;
            }
            QPushButton:pressed {
                background-color: #1c2127;
            }
        """)
        
        top_bar.addWidget(github_btn)
        top_bar.addStretch()
        main_layout.addLayout(top_bar)
        
        # Header
        header = QLabel("AvadaKedavra - Base64")
        header.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet("color: #667eea; margin: 10px 0;")
        main_layout.addWidget(header)

        # Subtitle
        subtitle = QLabel("Simple Base64 Encoding aand Decoding !")
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #888; margin-bottom: 20px;")
        main_layout.addWidget(subtitle)
        
        # Tab
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #444;
                border-radius: 8px;
                background-color: #2b2b2b;
            }
            QTabBar::tab {
                background: #333;
                color: #ccc;
                padding: 10px 20px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
            }
        """)
        
        # Encode tab
        encode_tab = self.create_encode_tab()
        tabs.addTab(encode_tab, "✏️ Encode")
        
        # Decode tab
        decode_tab = self.create_decode_tab()
        tabs.addTab(decode_tab, "🔓 Decode")
        main_layout.addWidget(tabs)
        
        # Status bar (the litle text on the bottom of the page)
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.setStyleSheet("background-color: #222; color: #aaa;")
        self.status_bar.showMessage("Ready")
    
    def create_encode_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # Options group
        options_group = QGroupBox("Encoding Options")
        options_layout = QHBoxLayout()
        
        self.encode_mode = QComboBox()
        self.encode_mode.addItems(["Standard", "URL-Safe"])
        self.encode_mode.setMinimumHeight(35)
        
        self.encode_padding = QCheckBox("Use Padding")
        self.encode_padding.setChecked(True)
        
        options_layout.addWidget(QLabel("Mode:"))
        options_layout.addWidget(self.encode_mode)
        options_layout.addWidget(self.encode_padding)
        options_layout.addStretch()
        
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        
        # Input
        layout.addWidget(QLabel("Input Text:"))
        self.encode_input = QTextEdit()
        self.encode_input.setPlaceholderText("Enter text to encode...")
        self.encode_input.setMinimumHeight(150)
        self.style_text_edit(self.encode_input)
        layout.addWidget(self.encode_input)
        
        # Btns
        btn_layout = QHBoxLayout()
        encode_btn = Button("🔒 Encode", primary=True)
        encode_btn.clicked.connect(self.perform_encode)
        clear_btn = Button("🗑️ Clear")
        clear_btn.clicked.connect(lambda: self.encode_input.clear())
        
        btn_layout.addWidget(encode_btn)
        btn_layout.addWidget(clear_btn)
        layout.addLayout(btn_layout)
        
        # Output
        layout.addWidget(QLabel("Encoded Output:"))
        self.encode_output = QTextEdit()
        self.encode_output.setPlaceholderText("Encoded text will appear here...")
        self.encode_output.setReadOnly(True)
        self.encode_output.setMinimumHeight(150)
        self.style_text_edit(self.encode_output)
        layout.addWidget(self.encode_output)
        
        # Copy btn
        copy_btn = Button("📋 Copy to Clipboard")
        copy_btn.clicked.connect(lambda: self.copy_to_clipboard(self.encode_output))
        layout.addWidget(copy_btn)
        
        return widget
    
    def create_decode_tab(self) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # Options group
        options_group = QGroupBox("Decoding Options")
        options_layout = QHBoxLayout()
        
        self.decode_mode = QComboBox()
        self.decode_mode.addItems(["Auto-Detect", "Standard", "URL-Safe"])
        self.decode_mode.setMinimumHeight(35)
        
        options_layout.addWidget(QLabel("Mode:"))
        options_layout.addWidget(self.decode_mode)
        options_layout.addStretch()
        
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        
        # Input
        layout.addWidget(QLabel("Encoded Text:"))
        self.decode_input = QTextEdit()
        self.decode_input.setPlaceholderText("Enter Base64 encoded text...")
        self.decode_input.setMinimumHeight(150)
        self.style_text_edit(self.decode_input)
        layout.addWidget(self.decode_input)
        
        # Btns
        btn_layout = QHBoxLayout()
        decode_btn = Button("🔓 Decode", primary=True)
        decode_btn.clicked.connect(self.perform_decode)
        clear_btn = Button("🗑️ Clear")
        clear_btn.clicked.connect(lambda: self.decode_input.clear())
        
        btn_layout.addWidget(decode_btn)
        btn_layout.addWidget(clear_btn)
        layout.addLayout(btn_layout)
        
        # Output
        layout.addWidget(QLabel("Decoded Output:"))
        self.decode_output = QTextEdit()
        self.decode_output.setPlaceholderText("Decoded text will appear here...")
        self.decode_output.setReadOnly(True)
        self.decode_output.setMinimumHeight(150)
        self.style_text_edit(self.decode_output)
        layout.addWidget(self.decode_output)
        
        # Copy btn
        copy_btn = Button("📋 Copy to Clipboard")
        copy_btn.clicked.connect(lambda: self.copy_to_clipboard(self.decode_output))
        layout.addWidget(copy_btn)
        
        return widget
    
    def style_text_edit(self, text_edit: QTextEdit):
        text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 2px solid #444;
                border-radius: 8px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 11pt;
            }
            QTextEdit:focus {
                border-color: #667eea;
            }
        """)
    
    # Encode/Decode funcs
    def perform_encode(self):
        input_text = self.encode_input.toPlainText()
        
        if not input_text:
            self.show_error("Please enter text to encode")
            return
        
        mode = self.encode_mode.currentText()
        use_padding = self.encode_padding.isChecked()
        
        if mode == "Standard":
            result, error = self.engine.encode_standard(input_text, use_padding)
        else:
            result, error = self.engine.encode_urlsafe(input_text, use_padding)
        
        if error:
            self.show_error(error)
        else:
            self.encode_output.setPlainText(result)
            self.status_bar.showMessage(f"Encoded successfully ({len(result)} characters)", 3000)
    
    def perform_decode(self):
        input_text = self.decode_input.toPlainText().strip()
        
        if not input_text:
            self.show_error("Please enter text to decode")
            return
        
        mode = self.decode_mode.currentText()
        
        if mode == "Auto-Detect":
            result, error = self.engine.decode_auto(input_text)
        elif mode == "Standard":
            result, error = self.engine.decode_standard(input_text)
        else:
            result, error = self.engine.decode_urlsafe(input_text)
        
        if error:
            self.show_error(error)
        else:
            self.decode_output.setPlainText(result)
            self.status_bar.showMessage(f"Decoded successfully ({len(result)} characters)", 3000)

    # All the secondary funcs
    def copy_to_clipboard(self, text_edit: QTextEdit):
        text = text_edit.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self.status_bar.showMessage("Copied to clipboard !", 2000)
        else:
            self.show_error("No text to copy")
    
    def show_error(self, message: str):
        QMessageBox.critical(self, "Error", message)
        self.status_bar.showMessage(f"{message}", 5000)

    def open_github(self):
        QDesktopServices.openUrl(QUrl(self.github_url))
        self.status_bar.showMessage("🌐 Opening GitHub profile...", 2000)
    
    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
            QWidget {
                background-color: #1a1a1a;
                color: #e0e0e0;
            }
            QGroupBox {
                border: 2px solid #444;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
                font-weight: bold;
                color: #aaa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QLabel {
                color: #ccc;
                font-size: 10pt;
            }
            QComboBox {
                background-color: #2b2b2b;
                color: #e0e0e0;
                border: 2px solid #444;
                border-radius: 6px;
                padding: 5px 10px;
                min-width: 150px;
            }
            QComboBox:hover {
                border-color: #667eea;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: #2b2b2b;
                color: #e0e0e0;
                selection-background-color: #667eea;
            }
            QCheckBox {
                color: #ccc;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border: 2px solid #444;
                border-radius: 4px;
                background-color: #2b2b2b;
            }
            QCheckBox::indicator:checked {
                background-color: #667eea;
                border-color: #667eea;
            }
        """)

# Main
def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = Base64GUI()
    window.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()