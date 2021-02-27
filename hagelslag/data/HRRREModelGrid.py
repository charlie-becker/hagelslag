#!/usr/bin/env python
import numpy as np
from os.path import exists, join
from .GribModelGrid import GribModelGrid


class HRRREModelGrid(GribModelGrid):
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
        self.run_date = run_date
        self.start_date = start_date
        self.end_date = end_date
        self.variable = variable
        filenames = []
        self.forecast_hours = np.arange((self.start_date - self.run_date).total_seconds() / 3600,
                                        (self.end_date - self.run_date).total_seconds() / 3600 + 1, dtype=int)
        
       # for forecast_hr in self.forecast_hours:
       #     file_name=self.path+'{1}00/{0}_{1}00f0{2:02}.grib2'.format(
       #                                                 self.member,
       #                                                 run_date.strftime("%Y%m%d"),
       #                                                 forecast_hr)
       #     if not exists(file_name):
       #         member_number=self.member.split("0")[-1]
       #         file_name=self.path+'{0}00/wrftwo_hrrre_clue_mem000{1}_{2}.grib2'.format(
       #                                                         run_date.strftime("%Y%m%d"),
       #                                                         member_number,
       #                                                        forecast_hr)
       #         if not exists(file_name):
       #             file_name = self.path+'{0}00/wrftwo_conus_mem000{1}_{2}.grib2'.format(
       #                                                         run_date.strftime("%Y%m%d"),
       #                                                         member_number,
       #                                                         forecast_hr)
       #      
       #     filenames.append(file_name)
        for forecast_hour in self.forecast_hours:
            filenames.append(join(self.path, f"{self.run_date.strftime('%Y%m%d')}12",
                                   f"hrrr.t12z.wrfsfcf{forecast_hour:02d}.grib2"))

        super(HRRREModelGrid, self).__init__(filenames,run_date,start_date,end_date,variable,member)
        
        return 
