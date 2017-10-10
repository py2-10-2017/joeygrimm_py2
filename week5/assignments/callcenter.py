from datetime import datetime
import operator

class Call(object):
    totalcalls = 0
    Call_List = []
    Call_Dict = {}
    def __init__(self, name, phone_number,reason):
        Call.totalcalls += 1
        self.id = Call.totalcalls
        self.name=name
        self.phone_number=phone_number
        self.time_of_call=datetime.now()
        self.reason=reason
        Call_Dict = {
            "ID":self.id,
            "Name":self.name,
            "Phone#":self.phone_number,
            "Call Time":self.time_of_call,
            "Reason for Call":self.reason
            }
        Call.Call_List.append(dict(Call_Dict))
    def display(self):
        print "\nID: {}".format(self.id)
        print "Name: {}".format(self.name)
        print "Phone #: {}".format(self.phone_number)
        print "Call Time: {}".format(self.time_of_call)
        print "Reason for the Call: {}\n".format(self.reason)
        return self

class CallCenter(Call):
    def __init__(self, name, phone_number,reason):
        super(CallCenter, self).__init__(name, phone_number,reason)
        self.calls=Call.Call_List
        Call.Call_List.sort()
        self.queue=len(self.calls)
    def Call_Center_Info(self):
        for i in self.calls:
            print i['ID'],i['Name'],i['Phone#']
        print "{}\n".format(self.queue)
        return self
    def Add_Call(self):
        print "Please Fill out Your Information."
        Form_Name = raw_input('Name: ')
        Form_Phone = raw_input('Phone#: ')
        Form_Reason = raw_input('Reason for Call: ')
        new_caller = Call(str(Form_Name),Form_Phone,str(Form_Reason))
        return self
    def Delete_Caller(self):
        for i in self.calls:
            print i['ID'],i['Name'],i['Phone#']
        Form_ID = input('ID# to Delete: ')

        for i in self.calls:
            if i['ID'] == Form_ID:
                self.calls.remove(i)
                print "Removed Dictionary Item."
        return self
            

        
        

        

a = CallCenter("Dave Evans",9131234567,"Broken Computer.")
b = CallCenter("Joe Evans",9131235267,"Broken Tooth.")

a.Call_Center_Info().Add_Call().Call_Center_Info()
b.Call_Center_Info().Delete_Caller()