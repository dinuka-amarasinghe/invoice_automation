import os
import subprocess
import datetime as dt
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import docx


class InvoiceAutomation:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Invoice Automation")
        self.root.geometry("500x600")

        self.partner_label = tk.Label(self.root, text="Partner")
        self.partner_street_label = tk.Label(self.root, text="Partner Street")
        self.partner_zip_city_country_label = tk.Label(self.root, text="Partner ZIP Country")
        self.invoice_number_label = tk.Label(self.root, text="Invoice Number")
        self.service_description_label = tk.Label(self.root, text="Service Description")
        self.service_amount_label = tk.Label(self.root, text="Service Amount")
        self.service_single_price_label = tk.Label(self.root, text="Service Single Price")
        self.payment_method_label = tk.Label(self.root, text="Payment Method")
