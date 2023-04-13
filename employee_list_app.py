import tkinter as tk
from tkinter import ttk, filedialog

import pdfplumber
# from pypdf import PdfReader   # anothe more accurate library

import os


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("PDF Filter")
        self.geometry("420x200")
        self.resizable(False, False)
        self.iconbitmap('filter_list_21446.ico')
        
        # Create a notebook with tabs for each window
        self.notebook = ttk.Notebook(self)
        
        # Create the Upload Data window
        self.upload_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.upload_frame, text='Upload Data')
        
        self.filepath_var = tk.StringVar()
        self.filepath_label = ttk.Label(self.upload_frame, text="PDF Filepath:", style='TLabel')
        self.filepath_label.grid(column=0, row=0, padx=10, pady=10)
        
        self.filepath_entry = ttk.Entry(self.upload_frame, textvariable=self.filepath_var, width=30)
        self.filepath_entry.grid(column=1, row=0, padx=10, pady=10)
        
        self.browse_button = ttk.Button(self.upload_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(column=2, row=0, padx=10, pady=10)
        
        self.upload_button = ttk.Button(self.upload_frame, text="Upload", command=self.upload, style='TButton')
        self.upload_button.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
        
        # Create the Filter Data window
        self.filter_frame = ttk.Frame(self.notebook, style='TFrame')
        self.notebook.add(self.filter_frame, text='Filter Data')
        
        self.filter_label = ttk.Label(self.filter_frame, text="Filter:", style='TLabel')
        self.filter_label.grid(column=1, row=0, padx=10, pady=10)
        
        self.filter_entry = ttk.Entry(self.filter_frame, width=30)
        self.filter_entry.grid(column=2, row=0, padx=10, pady=10)
        
        self.filter_button = ttk.Button(self.filter_frame, text="Filter", command=self.filter, style='TButton')
        self.filter_button.grid(column=2, row=1, columnspan=2, padx=10, pady=10)
        
        self.style = ttk.Style()
        # self.style.configure('TFrame', background='#E5E5E5')
        self.style.configure('TFrame', background='#91F9FE')
        # self.style.configure('TLabel', background='#E5E5E5', font=('Arial', 10))
        self.style.configure('TLabel', background='#91F9FE', font=('Arial', 10))
        self.style.configure('TButton', background='#0041BB', foreground='black', font=('Arial', 10))
        self.style.map('TButton', background=[('active', '#2C6EEA')])
        
        self.notebook.pack(expand=True, fill='both')
        
    def browse_file(self):
        filepath = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
        self.filepath_var.set(filepath)
        
    def upload(self):
        last_update = ''
        plant = ''
        department = ''
        section = ''

        filepath = self.filepath_entry.get()

        if '.pdf' in filepath:

            #________________Open the PDF file in read-binary mode_________________________________
            with pdfplumber.open(filepath) as pdf_file:
                # Extract the text from each page of the PDF
                page_text = [page.extract_text() for page in pdf_file.pages]
                
                # Join the text from each page into a single string
                text = ''.join(page_text)
                
                # _________________________________Open a text file in write mode_________________________________
                with open('raw_text.txt', 'w+') as txt_file:
                    # Write the text to the file
                    txt_file.write(text)

            # _________________________________read raw_text file_________________________________
            with open('raw_text.txt', 'r') as f:
                raw_lines = f.readlines()

            # _________________________________Get last update date of dataset_________________________________
            for line_no in range(len(raw_lines)):    
                # check last update date for one time
                if not last_update:
                    if 'Month End Summary' in raw_lines[line_no]:
                        last_update = raw_lines[line_no+1][22:32]
                        break

            # _________________________________Remove 'Noratel International (Pvt) Ltd.'- part_________________________________ 
            lines_without_noratel = []
            for line in raw_lines:
                if 'Noratel International (Pvt) Ltd.' in line:
                    if line == 'Noratel International (Pvt) Ltd.\n':
                        lines_without_noratel.append(line.replace("Noratel International (Pvt) Ltd.\n", ""))
                    else:
                        lines_without_noratel.append(line.replace("Noratel International (Pvt) Ltd.", ""))
                else:
                    lines_without_noratel.append(line)

            # with open('raw_text_without_Noratel.txt', 'w+') as f:
            #     f.writelines(lines_without_noratel)

            # _________________________________remove page and table header lines_________________________________
            lines_without_header = []
            avoid_line_number = -1
            for i in range(len(lines_without_noratel)):
                if 'Month End Summary' in lines_without_noratel[i]:
                    avoid_line_number = i
                if i >= avoid_line_number and i <= avoid_line_number+4:
                    continue    
                lines_without_header.append(lines_without_noratel[i])

            # with open('raw_text_without_header.txt', 'w+') as f:
            #     f.writelines(lines_without_header)


            # _________________________________Get employee details fromnoratel and header filtered data_________________________________
            final_lines = []
            avoid_employee_count_line = -1
            for line_no in range(len(lines_without_header)):
                # check plant
                if lines_without_header[line_no] == 'P1\n' or lines_without_header[line_no] == 'P3\n':
                    department = ''
                    section = ''
                    try:
                        if not (' L0' in lines_without_header[line_no + 1]) and not (' T0' in lines_without_header[line_no + 1]) and not (len([char for char in lines_without_header[line_no + 1] if char.isdigit()]) >= 5):
                            department = lines_without_header[line_no + 1][:-1]
                        if not (' L0' in lines_without_header[line_no + 2]) and not (' T0' in lines_without_header[line_no + 2]) and not (len([char for char in lines_without_header[line_no + 2] if char.isdigit()]) >= 5):
                            section = lines_without_header[line_no + 2][:-1]
                    except:
                        pass

                    if lines_without_header[line_no] == 'P1\n':
                        plant = 'P01'
                    if lines_without_header[line_no] == 'P3\n':
                        plant = 'P03'

                elif 'Employee Count :' in lines_without_header[line_no]:
                    avoid_employee_count_line = line_no
                    department = ''
                    section = ''
                    try:
                        if not (' L0' in lines_without_header[line_no + 2]) and not (' T0' in lines_without_header[line_no + 2]) and not (len([char for char in lines_without_header[line_no + 2] if char.isdigit()]) >= 5):
                            department = lines_without_header[line_no + 2][:-1]
                        if not (' L0' in lines_without_header[line_no + 3]) and not (' T0' in lines_without_header[line_no + 3]) and not (len([char for char in lines_without_header[line_no + 3] if char.isdigit()]) >= 5):
                            section = lines_without_header[line_no + 3][:-1]
                    except:
                        pass
                if line_no == avoid_employee_count_line or line_no == avoid_employee_count_line+1:
                    continue
                else:
                    try:
                        for i in range(len(lines_without_header[line_no])):
                            if (lines_without_header[line_no][i] == 'T' or lines_without_header[line_no][i] == 'L') and lines_without_header[line_no][i+1].isdigit() and lines_without_header[line_no][i-1] == " ":
                                name = lines_without_header[line_no][:i-2]
                                id = lines_without_header[line_no][i:i+7]
                                final_lines.append(name + '\t\t\t' + id + '\t\t\t' + plant + '\t\t\t' + department + '\t\t\t' + section + '\n')
                    except:
                        pass

            with open('final_employee_list.txt', 'w+') as f:
                f.writelines(final_lines)

            # Open file in editor
            os.startfile('final_employee_list.txt')
        
        else:
            with open('final_employee_list.txt', 'w+') as f:
                f.writelines("Invalid File Selected - The file you have selected is incorrect. Please select the correct file and try again.")
            
            # Open file in editor
            os.startfile('final_employee_list.txt')
        
    def filter(self):
        filter_text = self.filter_entry.get().lower()

        with open('final_employee_list.txt', 'r') as f:
            raw_lines = f.readlines()   

        filtered_lines = []
        for line in raw_lines:
            line_lower = line.lower()    
            if filter_text in line_lower:
                filtered_lines.append(line)

        with open('filtered_data.txt', 'w+') as f:
            f.writelines(filtered_lines)

        os.startfile('filtered_data.txt')
                    
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()
