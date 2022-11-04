from dateutil.relativedelta import relativedelta
import datetime
import re

class CheckStruct():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    @classmethod
    def check_data(cls, data):
        if re.fullmatch(r'\d{4}-\d{2}-\d{2}', data):
            A,M,D = data.split("-")
            data = datetime.date(int(A),int(M),int(D))
            if relativedelta(datetime.date.today(),data).years >= 18:
                return data # maior de idade
            else:
                return False # menor de idade
        else:
            return True # data invalid

    @classmethod
    def check(cls,email):
        if(re.fullmatch(cls.regex, email)):
            return True
        return False