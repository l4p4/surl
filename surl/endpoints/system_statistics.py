# -*- encoding: utf-8 -*-
'''
__author__ = "Larry_Pavanery
'''

import falcon
from base_response import BaseResponse


class SystemStatistics(BaseResponse):

    def on_get(self, req, resp):
        """ GET /stats """
        print ('SystemStatistics')
