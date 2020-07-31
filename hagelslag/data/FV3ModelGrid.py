#!/usr/bin/env python
import pygrib
import numpy as np
from os.path import exists
from pandas import DatetimeIndex
from .Grib_ModelGrid import Grib_ModelGrid

class FV3ModelGrid(Grib_ModelGrid):
    """
    Extension of the ModelGrid class for interfacing with the HREFv2  ensemble.
    Args:
        member (str): Name of the ensemble member
        run_date (datetime.datetime object): Date of the initial step of the ensemble run
        variable(int or str): name of grib2 variable(str) or grib2 message number(int) being loaded
        start_date (datetime.datetime object): First time step extracted.
        end_date (datetime.datetime object): Last time step extracted.
        path (str): Path to model output files
        single_step (boolean (default=True): Whether variable information is stored with each time step in a separate
                file (True) or one file containing all timesteps (False).
    """

    def __init__(self, member, run_date, variable, start_date, 
                end_date, path,single_step=True):
        self.path = path
        self.member = member
        filenames = []
        self.forecast_hours = np.arange((start_date - run_date).total_seconds() / 3600,
                                        (end_date - run_date).total_seconds() / 3600 + 1, dtype=int)
        
        for forecast_hr in self.forecast_hours:
            file_name=self.path+'{0}/{1}*{0}*f{2:02}.grib2'.format(
                                                        run_date.strftime("%Y%m%d"),
                                                        self.member,
                                                        forecast_hr)
            filenames.append(file_name)
        
        super(FV3ModelGrid, self).__init__(filenames,run_date,start_date,end_date,variable,member)
        
        return 