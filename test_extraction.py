
import employee_list_app

expected_raw_text = """Noratel International (Pvt) Ltd.
Month End Summary for January
From : 2023-01-02 To :2023-01-08
1.5 1.75 2.0 2.5 3.0 3.5 Late Night Wr Wrk Days
kHrs Hrs Attended
Inc Brk Exc Brk
Noratel International (Pvt) Ltd.
P1
Administration
Administration
Nimal bandara L00125 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
Xys nfjlda T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd T01113 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
Drivers
dkash djkas T01111 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
sbvajhf dnkja T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd L05636 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
Administration
Administration
Nimal bandara L00125 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
Xys nfjlda T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd T01113 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
Drivers
dkash djkas T01111 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
sbvajhf dnkja T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd L05636 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3Noratel International (Pvt) Ltd.
Month End Summary for January
From : 2023-01-02 To :2023-01-08
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
P3
Administration
Administration
Nimal bandara L00125 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
Xys nfjlda T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd T01113 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
Drivers
dkash djkas T01111 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
sbvajhf dnkja T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd L05636 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
Administration
Administration
Nimal bandara L00125 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
Xys nfjlda T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1
s.a.A. abcd T01113 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2
Kamal X.Y.Z T01114 0.00 0.00 0.00 0.00 0.00 0.00 - 4.55 0.03 3
Gyan J T01115 0.00 0.00 0.00 0.00 0.00 0.00 - 4.1 0.04 4
Employee Count : 5 1.00 1.01 1.02 1.01 1.02
2.00 2.01 2.02 2.01 2.02
Drivers
dkash djkas T01111 0.00 0.00 0.00 0.00 0.00 0.00 - - 0.00 0
sbvajhf dnkja T01112 0.00 0.00 0.00 0.00 0.00 0.00 - 35.94 0.01 1Noratel International (Pvt) Ltd.
Month End Summary for January
From : 2023-01-02 To :2023-01-08
s.a.A. abcd L05636 0.00 0.00 0.00 0.00 0.00 0.00 - 78.5 0.02 2"""

expected_employee_list = """Data up to 2023-01-08
Nimal bandar			L00125 			P01			Administration			Administration
Xys nfjld			T01112 			P01			Administration			Administration
s.a.A. abc			T01113 			P01			Administration			Administration
Kamal X.Y.			T01114 			P01			Administration			Administration
Gyan 			T01115 			P01			Administration			Administration
dkash djka			T01111 			P01			Drivers			
sbvajhf dnkj			T01112 			P01			Drivers			
s.a.A. abc			L05636 			P01			Drivers			
Kamal X.Y.			T01114 			P01			Drivers			
Gyan 			T01115 			P01			Drivers			
Nimal bandar			L00125 			P01			Administration			Administration
Xys nfjld			T01112 			P01			Administration			Administration
s.a.A. abc			T01113 			P01			Administration			Administration
Kamal X.Y.			T01114 			P01			Administration			Administration
Gyan 			T01115 			P01			Administration			Administration
dkash djka			T01111 			P01			Drivers			
sbvajhf dnkj			T01112 			P01			Drivers			
s.a.A. abc			L05636 			P01			Drivers			
Kamal X.Y.			T01114 			P01			Drivers			
Nimal bandar			L00125 			P03			Administration			Administration
Xys nfjld			T01112 			P03			Administration			Administration
s.a.A. abc			T01113 			P03			Administration			Administration
Kamal X.Y.			T01114 			P03			Administration			Administration
Gyan 			T01115 			P03			Administration			Administration
dkash djka			T01111 			P03			Drivers			
sbvajhf dnkj			T01112 			P03			Drivers			
s.a.A. abc			L05636 			P03			Drivers			
Kamal X.Y.			T01114 			P03			Drivers			
Gyan 			T01115 			P03			Drivers			
Nimal bandar			L00125 			P03			Administration			Administration
Xys nfjld			T01112 			P03			Administration			Administration
s.a.A. abc			T01113 			P03			Administration			Administration
Kamal X.Y.			T01114 			P03			Administration			Administration
Gyan 			T01115 			P03			Administration			Administration
dkash djka			T01111 			P03			Drivers			
sbvajhf dnkj			T01112 			P03			Drivers			
"""



def test_upload():
    app = employee_list_app.Application()
    app.upload("test_input.pdf")
    with open("final_employee_list.txt", "r") as f:
        employee_list = f.read()
        assert employee_list == expected_employee_list
    
    with open("raw_text.txt", "r") as f:
        raw_text = f.read()
        assert raw_text == expected_raw_text
