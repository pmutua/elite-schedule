
from django.db import models
from django.db.models import Q


class EnglishPremierLeagueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='E0')

class EnglishChampionShipManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='E1')

class EnglishLeague1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='E2')

class EnglishLeague2Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='E3')

class EnglishConference(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='EC')


class ScotLandPremierLeageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='SC0')

class ScotLandDivision1Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='SC1')

class ScotLandDivision2Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='SC2')

class ScotLandDivision3Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='SC3')

class Bundesliga1Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='D1')

class Bundesliga2Manger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='D2')

class SerieAManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='I1')

class SerieBManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='I2')

class LaligaPrimieraManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='SP1')

class LaligaSegundaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='SP2')

class FranceLeChampionnatManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='F1')

class FranceDivision2Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='F2')

class NetherlandsEredivisieManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='N1')

class BelgiumJupilerLeagueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='B1')

class PortugalLigaIManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='P1')

class TurkeyFutbolLigi1Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='T1')

class GreeceEthnikiKatigoriaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(division__code='G1')
        

class EnglandMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="E0") &
                Q(division__code__iexact="E1") &
                Q(division__code__iexact="E2") &
                Q(division__code__iexact="E3") &
                Q(division__code__iexact="EC")
        )

class ScotLandMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="SC0") &
                Q(division__code__iexact="SC1") &
                Q(division__code__iexact="SC2") &
                Q(division__code__iexact="SC3") 
        )


class GermanMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="D1") &
                Q(division__code__iexact="D2")
        )


class ItalianMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="I1") &
                Q(division__code__iexact="I2")
        )


class SpanishMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="SP1") &
                Q(division__code__iexact="SP2")
        )

class FranceMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="F1")
        )

class NetherlandsMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="N1")
        )

class BelgiumMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="B1")
        )

class PortugalMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="P1")
        )

class TurkeyMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="T1")
        )

class GreeceMatchesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
                Q(division__code__iexact="G1")
        )