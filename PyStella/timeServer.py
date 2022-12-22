from datetime import datetime
from math import floor

class pyStellaMasterTime:

    def __init__(self,request_server=None):
        self.requestServer = request_server
        self.master_time = 0

    def getMasterTime(self):
        return self.master_time

    def gregorian_to_julian(self,year, month, day,hour = 12,minute = 0,second= 0):
        aa,mm = (year,month) if (month>2) else (year-1,month+12)
        s = floor(aa/100)
        b = 2 - s+floor(s/4)
        q = day+(((hour*3600)+(minute*60)+second)/86400)
        return floor(365.25*aa) + floor(30.6001*(mm+1)) + q + b + 1720994.5
    
    def setTimeUtc(self,year,month,day,hour=0,minute=0,second=0):
        self.master_time = self.gregorian_to_julian(year,month,day,hour,minute,second)
        r = self.requestServer.post('main/time',{'time': str(self.master_time)})
        return self.master_time

    def setTimeNow(self):
        d = datetime.utcnow()
        self.master_time = self.gregorian_to_julian(d.year,d.month,d.day,d.hour,d.minute,d.second)
        r = self.requestServer.post('main/time',{'time': str(self.master_time)})
        return self.master_time
    
    def setTimeRate(self,timerate):
        t = timerate/86400.0
        r = self.requestServer.post('main/time',{'timerate': str(t)})


    def getStellariumTime(self):
        r = self.requestServer.get('main/status')
        self.master_time = r['time']['jday'] if (r is not None) else None
        return self.master_time

    def getStellariumTimerate(self):
        r = self.requestServer.get('main/status')
        return r['time']['timerate'] if (r is not None) else None
        
