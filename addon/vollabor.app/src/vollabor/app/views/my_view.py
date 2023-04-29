# -*- coding: utf-8 -*-

# from vollabor.app import _
from Products.Five.browser import BrowserView
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IMyView(Interface):
    """ Marker Interface for IMyView"""


class MyView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('my_view.pt')

     def __init__(self, context, request):
        self.context = context
        self.request = request

     def __call__(self):

        num1=self.request["num1"]
        num2=self.request["num2"]
        #return "Hello world. You are rendering this view at the context of %s" % self.context
        return int(num1)+int(num2)

    #def __call__(self):
        # Implement your own actions:
       # return self.index()
