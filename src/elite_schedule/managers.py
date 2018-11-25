
from django.db import models


class MatchManager(models.Manager):
    # Add query by divisions ie EPL,Laliga etc
    def e_1_division(self):
        return self.filter(division='E1')
    def e_2_division(self):
        return  self.filter(division='E2')
    def e_3_division(self):
        return  self.filter(division='E3')

    def e_1_division(self):
        return self.filter(division='S1')
    def e_2_division(self):
        return  self.filter(division='S2')
    def e_3_division(self):
        return  self.filter(division='S3')

    def I_1_division(self):
        return self.filter(division='I1')
    def I_2_division(self):
        return  self.filter(division='I2')
    def I_3_division(self):
        return  self.filter(division='I3')

    def g_1_division(self):
        return self.filter(division='G1')
    def g_2_division(self):
        return  self.filter(division='G2')
    def g_3_division(self):
        return  self.filter(division='G3')