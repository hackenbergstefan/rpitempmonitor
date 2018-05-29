#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os


class DataLogger(object):

    def __init__(self, logger_file, write_interval=10):
        self.logger_file = logger_file
        self.write_interval = write_interval
        self.data = []

    def add_data(self, point):
        """
        Add point to data.
        """
        self.data.append(point)
        if len(self.data) % self.write_interval:
            self.save()

    def read(self):
        """
        Read data from file.
        """
        return getattr(self, 'read_%s' % os.path.splitext(self.logger_file)[1][1:])()

    def save(self):
        """
        Save data to file.
        """
        getattr(self, 'save_%s' % os.path.splitext(self.logger_file)[1][1:])()

    def save_csv(self):
        """
        Save data to csv file.
        """
        with open(self.logger_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data)

    def read_csv(self):
        """
        Read data from csv file.
        """
        with open(self.logger_file) as csvfile:
            reader = csv.reader(csvfile)
            self.data = list(reader)
        return self.data
