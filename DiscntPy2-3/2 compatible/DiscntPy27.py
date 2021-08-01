# -*- coding: utf-8 -*-
'''
Note The scope of this Function: ONLY FOR SIMPLE DISCOUNT 
Author - Catacutan Z.J., Pascual S., Veneracion J.E., Cabuhat L. 
Date - DS: 0CTOBER 23, 2019 DF: 0CTOBER 30,2019
Professor - MARIA LORENA S.P. VILLENA'''
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''

class Simple_Discount():
##======================================================================================================== INITIALIZATION
    def __init__(self):
        '''This part takes no arguments it is only for the initializations of variables or values to be returned after calculation. The default values are:

            --> Amount of Face Value or Maturity Value is Zero  = 0
            --> Discount Rate is Zero = 0
            --> Time is Zero = 0
            --> Proceed is Zero = 0
            --> Discount or Bank Discount or Interest is Zero = 0

           To call each values use the syntax of:
           
                         object_name.values_name
               
               NOTE:
                   --> 'object_name' must be an object of the class 'Simple_Discount()'
                   --> acceptable 'values_name' are [ Amount, Proceed, Discount, dis_rate, ty, tm, td ]
                   --> 'td' will only return approximated number of days if your input is in months.
               
                    --> HOW TO USE:
                           a = Simple_Discount() --> setting 'a' as an object of the class Simple_Discount()
                           print a.Amount        --> printing out the value for the Amount or Face Value
                           x = a.Proceed         --> You can also assign it to a variable. Here x is equal to the amount of 'Proceed' for object 'a'
---------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        self.Amount = 0
        self.dis_rate = 0
        self.ty = 0
        self.tm = 0
        self.td = 0
        self.Proceed = 0
        self.Discount = 0
        self.accepted_var=['A','d','td_o_actual','td_e_actual','td_o_approx','td_e_approx','ty','tm','P','D','B','I','MV','FV']
        self.decimal=0
        '''------------------------------------- INACCESIBLE INSTANCES -------------------------------------------------------- '''
        self.__time = 0
        self.__run = 0
        self.__main_inputs = {}
        self.__copy_inputs = {}
        self.__main_sol = {}

##============================================================================================================= EXCEPTION FINDER FUNCTION
    def __err_list(self,err_num=None,err_in='',err_sample=''):
        '''hidden --> list of exceptions'''
        if err_num == 0:
            raise TypeError('Expected type of inputs in values are [ int, float ]. But \'{}\' of {} given.'.format(err_sample,err_in))
        elif err_num == 1:
            raise TypeError('Expected type of inputs in variables are [ str ]. But \'{}\' of {} given.'.format(err_sample,err_in))
        elif err_num == 2:
            def err_with_suggest():
                raise Exception('Unacceptable variable \'{}\' given. Do you mean \'{}\' ?'.format(err_in.strip(),suggest))
            def err_only():
                raise Exception('Unacceptable variable \'{}\' given.'.format(err_in))
            if err_in[0] == 'A' or err_in[0] == 'a':
                suggest = 'A'
                err_with_suggest()
            elif err_in[0] == 'D' or err_in[0] == 'd':
                suggest = 'D'
                err_with_suggest()
            elif err_in[0] == 'P' or err_in[0] == 'p':
                suggest = 'P'
                err_with_suggest()
            elif err_in[0] == 'd' or err_in[0] == 'a':
                suggest = 'd'
                err_with_suggest()
            elif err_in[0] == 't' or err_in[0] == 'T':
                suggest = [ 'ty', 'tm', 'td_o_actual','td_e_actual','td_o_approx','td_e_approx' ]
                err_with_suggest()
            elif err_in[0] == 'B' or err_in[0] == 'b':
                suggest = 'B'
                err_with_suggest()
            elif err_in[0] == 'M' or err_in[0] == 'm':
                suggest = 'MV'
                err_with_suggest()
            elif err_in[0] == 'F' or err_in[0] == 'f':
                suggest = 'FV'
                err_with_suggest()
            elif err_in[0] == 'I' or err_in[0] == 'i':
                suggest = 'I'
                err_with_suggest()
            else:
                err_only()   
        elif err_num == 3:
            raise Exception('Expected inputs on values must be greather than Zero (0). But \'{}\' given.'.format(err_in))
        elif err_num == 4:
            raise Exception('Expected number of arguments for inputs in values is 5. But \'{}\' given.'.format(err_in))
        elif err_num == 5:
            raise Exception('Expected number of arguments for inputs in variables is 5. But \'{}\' given.'.format(err_in))
        elif err_num == 6:
            raise Exception('Multiple use of variables with the same definition \'{}\'.'.format(err_in))
        elif err_num == 7:
            raise Exception('Something went wrong. Please check your inputs on variables. Empty input identified.')

##===================================================================================================== THE ANALYZER FUNCTION NOTE: PLEASE DONT MESS WITH IT      
    def __input_analyzer(self,testval=[], testvar=[]):
        '''hidden--> analyze the inputs'''
        '''checking the length of inputs per list'''
        if len(testval) != 5:
            self.__err_list(4,len(testval))
        else: pass
        if len(testvar) != 5:
            self.__err_list(5,len(testvar))
        else: pass
        for samples in testval:
            '''checking the input type for values'''
            if type(samples) == int or type(samples) == float: pass
            else: self.__err_list(0,str(type(samples)),samples)
        for samples2 in testvar:
            '''checking the input type for variables'''
            if type(samples2) != str:
                self.__err_list(1,str(type(samples2)),samples2)
        else:
            '''checking the values if not less than zero'''
            for sample in testval:
                if sample<0:
                    self.__err_list(3,sample)
            '''checking the variables if accepted'''
            for sample2 in testvar:
                if sample2 not in self.accepted_var:
                    self.__err_list(2,sample2)
                    
        temp_list_for_A_MV_FV = []
        temp_list_for_d = []
        temp_list_for_td = []
        temp_list_for_ty = []
        temp_list_for_tm = []
        temp_list_for_D = []
        temp_list_for_P = []
        for sample in testvar:
            if sample[0] == 'A' or sample[0] == 'M' or sample[0] == 'F':
                temp_list_for_A_MV_FV.append(sample)
            elif sample[0] == 'd':
                temp_list_for_d.append(sample)
            elif sample[0] == 't' and sample[1] == 'd':
                temp_list_for_td.append(sample)
            elif sample[0] == 't' and sample[1] == 'y':
                temp_list_for_ty.append(sample)
            elif sample[0] == 't' and sample[1] == 'm':
                temp_list_for_tm.append(sample)
            elif sample[0] == 'D' or sample[0] == 'B' or sample[0] == 'I':
                temp_list_for_D.append(sample)
            elif sample[0] == 'P':
                temp_list_for_P.append(sample)
        '''checking fo multiple use of variables with same definition'''
        if len(temp_list_for_A_MV_FV)>1:
            self.__err_list(6,temp_list_for_A_MV_FV)
        if len(temp_list_for_d)>1:
            self.__err_list(6,temp_list_for_d)
        if len(temp_list_for_td + temp_list_for_ty + temp_list_for_tm)>1:
            self.__err_list(6,temp_list_for_td + temp_list_for_ty + temp_list_for_tm)
        if len(temp_list_for_D)>1:
            self.__err_list(6,temp_list_for_D)
        if len(temp_list_for_P)>1:
            self.__err_list(6,temp_list_for_P)
            
##========================================================================================================== THE SORTER FUNCTION NOTE: PLEASE DONT MESS WITH IT
    def __sorter(self):
        '''hidden --> sorts the given inputs for preparation in calculation.'''
        for key in self.__main_inputs.keys():
            if key == 'A' or key == 'MV' or key == 'FV':
                self.Amount = self.__main_inputs[key]
            elif key =='d':
                self.dis_rate = float(self.__main_inputs[key])/100.00              
            elif key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx':
                if key == 'td_o_actual' or key == 'td_o_approx':
                    self.__time = float(self.__main_inputs[key])/360.00
                    self.td = self.__main_inputs[key]
                    self.ty = self.__time
                elif key == 'td_e_actual' or key == 'td_e_approx':
                    self.__time = float(self.__main_inputs[key])/365.00
                    self.td = self.__main_inputs[key]
                    self.ty = self.__time
                self.tm = self.__time * 12
            elif key == 'tm':
                self.__time = float(self.__main_inputs[key])/12.0
                self.tm = self.__main_inputs[key]
                self.ty = self.__time
                self.td = self.__main_inputs[key] * 30; '''approximate no of days'''
            elif key == 'ty':
                self.__time = self.__main_inputs[key]
                self.ty = self.__main_inputs[key]
                self.td = self.__main_inputs[key] * 365; '''actual no of days in a year'''
                self.tm = self.__time * 12
            elif key == 'P':
                self.Proceed = self.__main_inputs[key]
            elif key == 'D' or key == 'B' or key =='I':
                self.Discount = self.__main_inputs[key]
                
##=============================================================================================== THE ALGORITHM TO COMPUTE THE UNKOWNS NOTE: PLEASE DONT MESS WITH IT
    def __compute(self):
        '''hidden --> think for itself to calculate missing values'''
        def __checker():
            temp_list_of_val = [self.Amount, self.Discount, self.Proceed, self.dis_rate, self.__time]
            '''hidden --> check for certain parameters'''
            '''all is zero'''
            if temp_list_of_val.count(0) == 5:
                raise Exception('We don\'t how to solve this problem if all are unknowns. Please check your inputs.')
                '''if all have values'''
            elif temp_list_of_val.count(0) == 0:
                '''if all have values a new dictionary with computed values will be created'''
                temp_sol_var = ['A','D','P','d','ty']
                temp_sol_val = [self.Amount,self.Discount,self.Proceed,self.dis_rate,self.__time]
                self.__main_sol = dict(zip(temp_sol_var,temp_sol_val))
                '''if more than 2 is unknown'''
            elif temp_list_of_val.count(0)> 2:
                raise Exception('We don\'t know how to solve this problem. You have too many unknowns.')
                '''A and D'''
            elif self.Amount != 0 and self.Discount != 0 and self.Proceed == 0:
                self.Proceed = self.Amount - self.Discount
                __checker()
                '''A ands P'''
            elif self.Amount != 0 and self.Proceed != 0 and self.Discount == 0:
                self.Discount = self.Amount - self.Proceed
                __checker()
                '''P and D'''
            elif self.Proceed != 0 and self.Discount != 0 and self.Amount == 0:
                self.Amount = self.Discount + self.Proceed
                __checker()
                '''A and D and P and d'''
            elif self.Amount != 0 and self.Discount != 0 and self.Proceed != 0 and self.dis_rate != 0:
                if 'td_e_actual' in self.__main_inputs.keys() or 'td_e_approx' in self.__main_inputs.keys():
                    self.__time = float(self.Discount)/(self.Amount * self.dis_rate)
                    self.td = float(365 * self.Discount)/(self.Amount*self.dis_rate)
                    self.ty = self.__time
                    self.tm = self.__time * 12
                elif 'td_o_actual' in self.__main_inputs.keys() or 'td_o_approx'in self.__main_inputs.keys():
                    self.__time = float(self.Discount)/(self.Amount * self.dis_rate)
                    self.td = float(360 * self.Discount)/(self.Amount*self.dis_rate)
                    self.ty = self.__time
                    self.tm = self.__time * 12
                elif 'tm' in self.__main_inputs.keys():
                    self.__time = float(self.Discount)/(self.Amount * self.dis_rate)
                    self.tm = self.__time * 12
                    self.td = self.__time * 365
                    self.ty = self.__time
                elif 'ty' in self.__main_inputs.keys():
                    self.__time = float(self.Discount)/(self.Amount * self.dis_rate)
                    self.ty = self.__time
                    self.tm = self.__time * 12
                    self.td = self.__time * 365
                __checker()
                '''A and D and P and t'''
            elif self.Amount != 0 and self.Discount != 0 and self.Proceed != 0 and self.__time != 0:
                self.dis_rate = float(self.Discount)/(self.Amount * self.__time)
                __checker()
                '''A and d and t'''
            elif self.Amount != 0 and self.dis_rate != 0 and self.__time != 0:
                self.Discount = self.Amount * self.dis_rate * self.__time
                __checker()
                '''D and d and t'''
            elif self.Discount != 0 and self.dis_rate != 0 and self.__time != 0:
                self.Amount = float(self.Discount)/(self.dis_rate * self.__time)
                __checker()
                '''P and d and t'''
            elif self.Proceed != 0 and self.dis_rate != 0 and self.__time != 0:
                self.Amount = float(self.Proceed)/(1-(self.dis_rate * self.__time))
                __checker()
                '''A and d and t'''
            elif self.Amount != 0 and self.dis_rate != 0 and self.__time != 0:
                self.Proceed = float(self.Amount)/(1-(self.dis_rate * self.__time))
                __checker()
        __checker()

##----------------------------------------------------------------------------------------------------------------- USEABLE FUNCTION ARE DEFINED UNDER THIS LINE        
        
    def show_inputs(self,border=''):
        '''This method will show the inputs in a more arranged and organized way
            --> It only takes one argument 'border' which in default was set to empty character.
            --> By placing any character in 'border' it will be printed as the border for the output.
            --> If you want a new line to be printed out at the top and bottom of the showned inputs just make the border equal to space ' '.
                The number of space will be treated as the number of new lines to be printed.

                --> HOW TO USE:
                                    object_name.show_inputs('-')
---------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        if self.__run == 0: pass
        else:
            if border == '': pass
            else:print (str(border)*70)
            for key in self.__copy_inputs.keys():
                if key == 'A' or  key == 'MV' or key == 'FV':
                    print ('Amount or Maturity Value or Face Value = {}'.format(round(self.__copy_inputs[key],self.decimal)))
                elif key == 'P':
                    print ('Proceed = {}'.format(round(self.__copy_inputs[key],self.decimal)))
                elif key == 'D' or key == 'B' or key == 'I':
                    print ('Discount or Bank Discount or Interest = {}'.format(round(self.__copy_inputs[key],self.decimal)))
                elif key == 'd':
                    print ('Discount Rate = {}'.format(round(self.__copy_inputs[key],self.decimal)))
                elif key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx' or key == 'tm' or key == 'ty':
                    if key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx':
                        placeholder = 'Time in Days'
                    elif key == 'tm':
                        placeholder = 'Time in Months'
                    else: placeholder = 'Time in Years'
                    print ('{} = {}'.format(placeholder,round(self.__copy_inputs[key],self.decimal)))
            if border == '': pass
            else:print (str(border)*70)

    def show_computed(self,border=''):
        '''This method will show the calculated unknowns in a more arranged and organized way
            --> It only takes one argument 'border' which in default was set to empty character.
            --> By placing any character in 'border' it will be printed as the border for the output.
            --> If you want a new line to be printed out at the top and bottom of the showned computed output just make the border equal to space ' '.
                The number of space will be treated as the number of new lines to be printed.

                --> HOW TO USE:
                                     object_name.show_computed('-')
---------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        if self.__run == 0: pass
        else:
            if border == '': pass
            else:print (str(border)*70)
            for key in self.__copy_inputs.keys():
                if key == 'A' or  key == 'MV' or key == 'FV':
                    print ('Amount or Maturity Value or Face Value = {}'.format(round(self.Amount,self.decimal)))
                elif key == 'P':
                    print ('Proceed = {}'.format(round(self.Proceed,self.decimal)))
                elif key == 'D' or key == 'B' or key == 'I':
                    print ('Discount or Bank Discount or Interest = {}'.format(round(self.Discount,self.decimal)))
                elif key == 'd':
                    print ('Discount Rate = {}'.format(round(self.dis_rate,self.decimal)))
                elif key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx' or key == 'tm' or key == 'ty':
                    print ('Time in years = {}'.format(round(self.__time,self.decimal)))
            if border == '': pass
            else:print (str(border)*70)

    def discnt_inputs(self,val = [0,0,0,0,0], var = [],decimal=4):
        '''This method is use to input all the 'values' and 'variables' that you have based on the problem you are trying to solve.

           NOTE:
           --> Values --> 'val':
                   acceptable values are of type --> [ int, float ]
                   only place 5 values as minimum and max if you dont have that 'value' for a certain 'variable' place 0 or 0.0.
           --> Variable --> 'var':
                   acceptable variables are -- > ['A','d','td_o_actual','td_e_actual','td_o_approx','td_e_approx','ty','tm','P','D','B','I','MV','FV']
                   --> You can show all the accepted variables by using the method '.accepted_var':
                                   syntax:
                                               print object_name.accepted_var
                       USE:
                           'A' or 'MV' or 'FV' --> for Amount, Maturity Value, or Future Value
                           'd' --> lower case 'd' is for discount rate
                           'td_(...)' --> Time in DAYS. It contains four types:
                                    Approximated number of days in one year is 360 days, 30 days per month
                                       --> use 'td_o_actual' for Actual number of days in an Ordinary Interest
                                       --> use 'td_e_actual' for Actual number of days in an Exact Interest
                                       --> use 'td_o_approx' for Approximated number of days in an Ordinary Interest
                                       --> use 'td_e_approx' for Approximated number of days in an Exact Interest
                           'tm' --> Time in MONTHS
                           'ty' --> Time in YEAR
                           'P' --> upper case 'P' is for Proceed
                           'D' or 'B' or 'I' --> is for Discount or Bank Discount or Interest
           --> decimal:
                   --> The decimal is replaceable by any desired value not less than zero.
                   --> This only sets the decimal number of the returned outputs.
                   --> By default 4 is set.
                   
            --> HOW TO USE:
            
                            object_name.discnt_inputs([0,0,0,0,0],['A','d','ty','D','P'],4)

                NOTE:
                    --> The 'values' are assigned based on its arrangement with respect to 'variables' arrangement.
                    --> Use only one variable to represent a value to avoid multiple use of variables.
---------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        '''this will let the function know that this was firstly initialize'''
        self.__run = 0 
        self.__run += 1
        self.decimal=decimal
        for index in range(len(var)):
            x = var[index] 
            if type(var[index]) == str:
                if var[index].strip() == '': self.__err_list(7)
                var.remove(var[index])
                var.insert(index,x.strip())
            else: self.__err_list(1,str(type(var[index])),var[index])
        '''passing the input to method __input_analyzer()'''
        self.__input_analyzer(val,var)
        '''building up the main dictionary if no error occur'''
        self.__main_inputs=dict(zip(var,val))
        self.__copy_inputs = self.__main_inputs
        '''sort the inputs for preparation in calculation'''
        self.__sorter()
        '''analyze and solve the unknowns if possible or not'''
        self.__compute()


    def formula_for(self,discount_var_name='',title=''):
        '''This method returns all possible formulas for a certain unknown in relation to DISCOUNTING.
           It takes one argument 'dicount_var_name'.

            --> HOW TO USE:

                            object_name.formula_for(discount_var_name, title = '')

                NOTE:
                    --> 'discount_var_name' can be of the following:

                            [ 'LEGEND', 'ALL', 'AMOUNT', 'MATURITY VALUE', 'FACE VALUE', DISCOUNT', 'BANK DISCOUNT', 'INTEREST', 'DISCOUNT RATE', 'TIME' ]

                    --> Not case sensitive

                         --> 'LEGEND' = returns the variable definition. It is suggested to call it first before calling other parameters.
                         --> 'ALL' = returns all the formula for Simple Discount.
                         --> 'AMOUNT' or 'MATURITY VALUE' or 'FACE VALUE' = returns all the formula for Amount.
                         --> 'DISCOUNT' or 'BANK DISCOUNT' or 'INTEREST' = returns all the formula for Discount.
                         --> 'DISCOUNT RATE' = returns all the formula for Discount rate.
                         --> 'TIME' = returns all the formula for Time.

                    --> 'title' can be changed based on desired title for each table of formula.
---------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        title = str(title).strip()
        def __LEGEND():
            print ('''
            LEGEND:
                A = Amount or Maturity Value or Face Value          d = discount rate
                D = Discount or Bank Discount or Interest           t = time in years
                P = Proceed
            ''')
            
        '''FORMULA TABLE NOTE: PLEASE DONT MESS WITH SPACS OF THE FORMAT MAY CHANGED'''
        self.__table_A = [['USING','FORMULA       '],['D,d,t','A = D/(d x t) '],['D,P  ','A = D + P     '],['P,d,t','A = P/(1 - dt)']]
        self.__table_D = [['USING','FORMULA       '],['A,d,t','D = A x d x t '],['A,P  ','D = A - P     ']]
        self.__table_P = [['USING','FORMULA         '],['A,D  ','P = A - D       '],['A,d,t','P = A x (1 - dt)']]
        self.__table_DR = [['USING','FORMULA           '],['D,A,t','d = D/(A x t)     '],['A,P,t','d =(A - P)/(A x t)']]
        self.__table_T = [['USING','FORMULA           '],['D,A,d','t = D/(A x d)     '],['A,P,d','t =(A - P)/(A x d)']]

        '''AMOUNT'''
        def __AMOUNT():
            if title == '':
                print (' ALL THE FORMULA TO SOLVE FOR THE VALUE OF \'AMOUNT\' OR \'MATURITY VALUE\' OR \'FACE VALUE\':')
            else: print ' '+str(title)
            c = 0
            for item in range(len(self.__table_A)):
                if c == 0: print ' '+'='*23
                if c == 2 or c==4 or c == 6: print '|'
                for item2 in range(len(self.__table_A)-2):
                    print " |" + self.__table_A[item][item2],
                    c+=1
                    if c==8:
                        print '|'
                        print ' '+'='*23
        '''DISCOUNT'''
        def __DISCOUNT():
            if title == '':
                print (' ALL THE FORMULA TO SOLVE FOR THE VALUE OF \'DISCOUNT\' OR \'BANK DISCOUNT\' OR \'INTEREST\':')
            else: print ' '+str(title)
            c = 0
            for item in range(len(self.__table_D)):
                if c == 0: print ' '+'='*23
                if c == 2 or c==4: print '|'
                for item2 in range(len(self.__table_D)-1):
                    print " |" + self.__table_D[item][item2],
                    c+=1
                    if c==6:
                        print '|'
                        print ' '+'='*23

        '''PROCEED'''
        def __PROCEED():
            if title == '':
                print (' ALL THE FORMULA TO SOLVE FOR THE VALUE OF \'PROCEED\':')
            else: print ' '+str(title)
            c = 0
            for item in range(len(self.__table_P)):
                if c == 0: print ' '+'='*25
                if c == 2 or c==4: print '|'
                for item2 in range(len(self.__table_P)-1):
                    print " |" + self.__table_P[item][item2],
                    c+=1
                    if c==6:
                        print '|'
                        print ' '+'='*25
                        
        '''DISCOUNT RATE'''
        def __DISCOUNT_RATE():
            if title == '':
                print (' ALL THE FORMULA TO SOLVE FOR THE VALUE OF \'DISCOUNT RATE\':')
            else: print ' '+str(title)
            c = 0
            for item in range(len(self.__table_DR)):
                if c == 0: print ' '+'='*27
                if c == 2 or c==4: print '|'
                for item2 in range(len(self.__table_DR)-1):
                    print " |" + self.__table_DR[item][item2],
                    c+=1
                    if c==6:
                        print '|'
                        print ' '+'='*27

        '''TIME'''
        def __TIME():
            if title == '':
                print (' ALL THE FORMULA TO SOLVE FOR THE VALUE OF \'TIME IN YEARS\':')
            else: print ' '+str(title)
            c = 0
            for item in range(len(self.__table_T)):
                if c == 0: print ' '+'='*27
                if c == 2 or c==4: print '|'
                for item2 in range(len(self.__table_T)-1):
                    print " |" + self.__table_T[item][item2],
                    c+=1
                    if c==6:
                        print '|'
                        print ' '+'='*27
            print ' OTHER FORMULA FOR TIME:\n '+'='*119
            print ''' 1) To convert 'time in years' to 'time in months'.
     	 MULTIPLY the 'time in years' by '12'.
                 TIME_IN_MONTHS = time_in_years * 12
                 
 2) To convert 'time in months' to 'time in years':
     	 DIVIDE the 'time in months' by '12'.
                 TIME_IN_YEARS = time_in_months / 12
                 
 3) To convert 'time in days' to 'time in months':
     	 If you want to find the 'APPROXIMATED VALUE' of that 'number of DAYS' in 'MONTHS' you must divide it by '30'.
                 APPROXIMATED_NUMBER_OF_MONTHS = time_in_days / 30
                 
 4) To convert 'time in months' to 'time in days':
                 ACTUAL_NUMBER_OF_DAYS = (time_in_months(365))/12
                 APPROXIMATED_NUMBER_OF_DAYS = (time_in_months(360))/12
                 
 5) To convert 'time in days' to 'time in years':
     	 If you want to find the 'ACTUAL VALUE IN YEARS' of that 'number of DAYS' you should divide it by '365'.
                 ACTUAL_TIME_IN_YEARS = time_in_days / 365
    
     	 If you want to find the 'APPROXIMATED VALUE IN YEARS' of that 'number of DAYS' you should divide it by '360'.
                 APPROXIMATED_TIME_IN_YEARS = time_in_days / 360'''
            print (' '+'='*119)
        discount_var_name = str(discount_var_name).strip()
        if discount_var_name.upper().strip() == "LEGEND":
            __LEGEND()
        elif discount_var_name.upper().strip() == "ALL":
            if title != '': title = ''
            __LEGEND()
            __AMOUNT()
            __DISCOUNT()
            __PROCEED()
            __DISCOUNT_RATE()
            __TIME()
        elif discount_var_name.upper().strip() == "AMOUNT" or discount_var_name.upper() == "MATURITY VALUE" or discount_var_name.upper() == "FACE VALUE":
            __AMOUNT()
        elif discount_var_name.upper().strip() == "DISCOUNT" or discount_var_name.upper() == "BANK DISCOUNT" or discount_var_name.upper() == "INTEREST":
            __DISCOUNT()
        elif discount_var_name.upper().strip() == "DISCOUNT RATE":
            __DISCOUNT_RATE()
        elif discount_var_name.upper().strip() == "TIME":
            __TIME()
        elif discount_var_name.upper().strip() == "PROCEED":
            __PROCEED()
        else:
            if discount_var_name[0].upper() == 'A':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'AMOUNT\' or \'ALL\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'M':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'MATURITY VALUE\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper().strip() == 'P':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'PROCEED\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'F':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'FACE VALUE\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'D':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'DISCOUNT\' or \'DISCOUNT RATE\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'B':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'BANK DISCOUNT\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'I':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'INTEREST\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'T':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'TIME\' ?'.format(discount_var_name))
            elif discount_var_name[0].upper() == 'L':
                raise Exception('Unknown variable name: \'{}\'. Do you mean \'LEGEND\' ?'.format(discount_var_name))
            else:
                raise Exception('Unknown variable name: {}'.format(discount_var_name))

    def save(self,border = '',title = '',smode = ''):
        '''This method will allow you to save your INPUTS and RESULTS in a text document named 'RESULTS_Discount.txt'
           It takes three arguments 'border' and 'title' and 'smode'.
                   --> 'border' = let you change the boundary decorators for inputs and results.
                   --> 'title' = set a title for each results.
                   --> 'smode' = will allow you to choose if you want to append current computation on the file or replace all saved computation in the file.
                               = if you leave it empty by, default the saving mode is set to 'append'.
                               = it is CASE SENSITIVE.
                               = it only accept:
                                   'a' to append.
                                   'w' to write or replace.

                --> HOW TO USE:
                                object_name.save('-','COMPUTATION NUMBER 1','a')
---------------------------------------------------------------------------------------------------------------------------------------------------------------'''
        if self.__run == 0: pass
        else:
            if str(smode).strip() == 'a' or str(smode).strip() == 'w' or str(smode).strip() == '': pass
            else: raise Exception('Invalid key for saving mode: \'{}\'. Use \'a\' or \'w\'.'.format(smode))
            if smode == '': smode = 'a'
            border = str(border)
            with open('RESULTS_Discount.txt',smode) as temp_f:
                temp_f.write(str(title))
                '''WRITING OUT THE INPUTS TO FILE'''
                if border == '':
                    temp_f.write('\n'+'-'*70)
                    temp_f.write('\n> INPUTS\n'+'-'*70+'\n')
                else:
                    temp_f.write('\n'+border*70)
                    temp_f.write('\n> INPUTS\n'+border*70+'\n')
                for key in self.__copy_inputs.keys():
                    if key == 'A' or  key == 'MV' or key == 'FV':
                        temp_f.write(('Amount or Maturity Value or Face Value = {}'.format(round(self.__copy_inputs[key],self.decimal))))
                    elif key == 'P':
                        temp_f.write(('Proceed = {}'.format(round(self.__copy_inputs[key],self.decimal))))
                    elif key == 'D' or key == 'B' or key == 'I':
                        temp_f.write(('Discount or Bank Discount or Interest = {}'.format(round(self.__copy_inputs[key],self.decimal))))
                    elif key == 'd':
                        temp_f.write(('Discount Rate = {}'.format(round(self.__copy_inputs[key],self.decimal))))
                    elif key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx' or key == 'tm' or key == 'ty':
                        if key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx':
                            placeholder = 'Time in Days'
                        elif key == 'tm':
                            placeholder = 'Time in Months'
                        else: placeholder = 'Time in Years'
                        temp_f.write(('{} = {}'.format(placeholder,round(self.__copy_inputs[key],self.decimal))))
                    temp_f.write('\n')
                '''WRITING OUT THE RESULTS TO FILE'''
                if border == '':
                    temp_f.write('-'*70)
                    temp_f.write('\n> RESULTS\n'+'-'*70+'\n')
                else:
                    temp_f.write(border*70)
                    temp_f.write('\n> RESULTS\n'+border*70+'\n')
                for key in self.__copy_inputs.keys():
                    if key == 'A' or  key == 'MV' or key == 'FV':
                        temp_f.write(('Amount or Maturity Value or Face Value = {}'.format(round(self.Amount,self.decimal))))
                    elif key == 'P':
                        temp_f.write(('Proceed = {}'.format(round(self.Proceed,self.decimal))))
                    elif key == 'D' or key == 'B' or key == 'I':
                        temp_f.write(('Discount or Bank Discount or Interest = {}'.format(round(self.Discount,self.decimal))))
                    elif key == 'd':
                        temp_f.write(('Discount Rate = {}'.format(round(self.dis_rate,self.decimal))))
                    elif key == 'td_o_actual' or key == 'td_e_actual' or key == 'td_o_approx' or key == 'td_e_approx' or key == 'tm' or key == 'ty':
                        temp_f.write(('Time in years = {}'.format(round(self.__time,self.decimal))))
                    temp_f.write('\n')
                if border == '':
                    temp_f.write('-'*70)
                else: temp_f.write(border*70)
                temp_f.write('\n\n')


        
        
