import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# إنشاء أو الاتصال بقاعدة البيانات محلياً وتوليد الجداول تلقائياً
def init_db():
    conn = sqlite3.connect('agro_management.db')
    cursor = conn.cursor()
    
    # جدول المزارعين
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS farmers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            details TEXT
        )
    ''')
    
    # جدول العملاء
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            details TEXT
        )
    ''')
    
    # جدول الحركات المالية والصندوق
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            notes TEXT,
            date TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

class AgroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نظام الإدارة الزراعية")
        self.root.geometry("400x700")
        
        init_db()
        
        # تصميم الواجهة متعددة التبويبات لتتناسب مع الشاشات
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        self.tab_cash = ttk.Frame(self.notebook)
        self.tab_farmers = ttk.Frame(self.notebook)
        self.tab_customers = ttk.Frame(self.notebook)
        self.tab_debts = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_cash, text='الصندوق')
        self.notebook.add(self.tab_farmers, text='المزارعون')
        self.notebook.add(self.tab_customers, text='العملاء')
        self.notebook.add(self.tab_debts, text='الديون')
        
        self.setup_cash_tab()
        self.setup_farmers_tab()
        self.setup_customers_tab()
        self.setup_debts_tab()

    def setup_cash_tab(self):
        lbl = tk.Label(self.tab_cash, text="إدارة الصندوق والحركات المالية", font=("Arial", 14, "bold"))
        lbl.pack(pady=20)
        
        tk.Button(self.tab_cash, text="عرض رصيد الصندوق", width=20, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

    def setup_farmers_tab(self):
        lbl = tk.Label(self.tab_farmers, text="حسابات المزارعين", font=("Arial", 14, "bold"))
        lbl.pack(pady=20)

    def setup_customers_tab(self):
        lbl = tk.Label(self.tab_customers, text="حسابات العملاء", font=("Arial", 14, "bold"))
        lbl.pack(pady=20)

    def setup_debts_tab(self):
        lbl = tk.Label(self.tab_debts, text="تجميع الديون والملخصات", font=("Arial", 14, "bold"))
        lbl.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgroApp(root)
    root.mainloop()
