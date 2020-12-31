from datetime import datetime


class Demand:
    def __init__(self, first_name, last_name,
                 tracking_code, ssn, phone_number,
                 status='Sent'):
        self.first_name = first_name
        self.last_name = last_name
        self.tracking_code = tracking_code
        self.ssn = ssn
        self.phone_number = phone_number
        self.status = status
        self.registratoin_date = datetime.now()

    def __repr__(self):
        return "<Demand name:{},status{}".format(self.first_name +
                                                 ' ' +
                                                 self.last_name,
                                                 self.status)
