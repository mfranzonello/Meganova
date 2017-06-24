'''Calculate bills'''
import datetime,pandas
from typing import List
from app.stella import physical,rates,times

class TimePeriod:
    '''Period with start and end date'''
    def __init__(self,start:datetime.date,days:int=None,end:datetime.date=None,prorate:int=1):
        self.start = start
        if days is not None:
            self.end = self.start + datetime.timedelta(days=days)
        else:
            self.end = end
        self.prorate = prorate

class BillPeriod(TimePeriod):
    '''Period after which a customer is billed by meter'''
    def __init__(self,start:datetime.date,days:int=None,end:datetime.date=None):
        TimePeriod.__init__(self,start,days,end)

    def get_spans(self,service_agreement:rates.ServiceAgreement,tou:times.TOU) -> List[TimePeriod]:
        # dates of change in rate effective date or TOU season
        timespans = []
        for x in []:
            start = None
            end = None
            prorate = None
            timespans.append(TimePeriod(start,end),prorate)
        return timespans

class BillSchedule:
    '''List of periods over which a customer is billed by meter'''
    def __init__(self,meter:physical.Meter):
        self.id = meter.id
        self.schedule = []
    def add_period(self,billperiod:BillPeriod):
        self.extend(billperiod)

class MonthlyBill:
    '''Quantities and payments for one bill period per meter'''
    def __init__(self,interval:physical.Interval,rate_list:List[rates.RateSchedule],
                 service_agreement:rates.ServiceAgreement,timespan:TimePeriod):
        return None
    def prorate(self):
        self.something = None
    def add_costs(cost_type,data,params):
        if cost_type == 'fixed':
            something
        elif cost_type == 'demand':
            something
        elif cost_type == 'energy':
            something
    def summarize(self):
        return None

class AnnualBill:
    '''Total collection of bills for multiple periods'''
    def __init__(self):
        return None

class Payment:
    '''Total amount spent by customer for all meters on an annual basis'''
    def __init__(self):
        return None