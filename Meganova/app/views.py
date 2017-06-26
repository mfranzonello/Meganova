"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from . import models
session = models.Session()

from app.stella import *

def home(request):
    """Renders the home page."""
    #request.session['first'] = billing.test
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Meganova Home',
            'year':datetime.now().year,
        }
    )

def showutilities(request):
    '''Creat new utility'''
    assert isinstance(request,HttpRequest)
    utilities = session.query(models.IOU).all()
    return render(
        request,
        'app/showutilities.html',
        {
            'title':'Utilities',
            'year':datetime.now().year,
            'utilities':utilities,
        }
    )


def newproject(request):
    '''Create a new project'''
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/newproject.html',
        {
            'title':'Create a new project',
            'year':datetime.now().year,
            'utilities':references.utilities,
        }
    )

#def waiting(request,nextview,variables):
#    if nextview=='showproject':
#        message = 'something'
#        redirect = 'showproject/{}'.format(request.session['utility'])
#    else:
#        message = 'oops'
#        redirect = ''
#    return render(
#        request,
#        'app/waiting.html',
#        {
#            'title':'Please wait',
#            'message':'Please wait while the system {}.'.format(message),
#            'year':datetime.now().year,
#            'redirect':redirect,
#            'variables':variables,
#        }
#    )

def showproject(request,utility_name):
    '''Show project'''
    assert isinstance(request,HttpRequest)
    # set up rate database
    print('defining utility')
    utility = org.IOU(utility_name,1.0)
    request.session['utility'] = utility
    print('getting excel file')
    rates_raw = xltable.RawXL(references.rates)
    print('creating db')
    rates_db = rates.RatesDB(rates_raw,utility)
    utility_rates = RateTable(rates.UtilityRates(rates_db))
    standby_rates = RateTable(rates.StandbyRates(rates_db))
    crs_rates = RateTable(rates.CRSRates(rates_db))
    cca_rates = RateTable(rates.CCARates(rates_db))
    pkp_rates = RateTable(rates.PKPRates(rates_db))
    interrupt_rates = RateTable(rates.InterruptRates(rates_db))
    shift_rates = RateTable(rates.ShiftRates(rates_db))

    request.session['rate db'] = rates_db
    request.session['utility rates'] = utility_rates
    return render(
        request,
        'app/showproject.html',
        {
            'title':'My new project',
            'message':'This is the rate database of {}.'.format(utility),
            'year':datetime.now().year,
            'to_show':utility_rates.to_html(),
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
