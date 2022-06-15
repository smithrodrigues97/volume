a = float(input(" If tank has slope input 1 "))
if a== 1
   A_xaea12= float(input("Please enter height : "))
   a_variable_1=A_xaea12/1000
   E_xaea12= float (input("please enter height 2 : "))
   e_variable_2= E_xaea12/1000
   B_xaea12= float(input("please enter width : "))
   b_variable_3=B_xaea12/1000
   C_xaea12= float(input("please enter length : "))
   c_variable_4=C_xaea12/1000
   a_1_c_variable_1=e_variable_2-a_variable_1
   a_2_c_variable_2=b_variable_3
   Volume_1 = a_variable_1*b_variable_3*c_variable_4
   volume_2 = 1/2*a_1_c_variable_1*a_2_c_variable_2*c_variable_4
   Volume = Volume_1 +volume_2
   print("Volume","=",Volume,"Cubic meters: ")
   D= Volume*1000
   def new_func(D):
   print (D,"liters : ")
   new_func(D)
else
    A= float(input("Please enter height : "))
    a=A/1000
    B= float(input("please enter width : "))
    b=B/1000
    C= float(input("please enter length : "))
    c=C/1000
    Volume = a*b*c
    print("Volume","=",Volume,"Cubic meters: ")
    D= Volume*1000
    print(D,"liters : ")


