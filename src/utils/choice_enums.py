from enum import Enum

class CountryChoice(Enum):   # A subclass of Enum
    EN = "ENGLAND"
    SP = "SPAIN"
    IT = "ITALY"


class DivisionChoice(Enum):
    ENGLISH_PREMERE = "E1"
    # ENGLISH_CUP= "E2"
    # E1 = "E3"

    



 


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     language = models.CharField(
#       max_length=5,
#       choices=[(tag, tag.value) for tag in LanguageChoice]  # Choices is a list of Tuple
#     )

# b = Book(title='Deutsch Für Ausländer', language=LanguageChoice.DE)
# b.save()
