from csv import DictReader

from django.core.management import BaseCommand

from adoptions.models import ArrestData
from pytz import UTC

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from ArrestData.csv into our ArrestData model"

    def handle(self, *args, **options):
        if ArrestData.objects.exists():
            print('Arrest data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading arrest data")
        for row in DictReader(open('./ArrestData.csv')):
            data = ArrestData()
            data._id = row['_id']
            data.PK = row['PK']
            data.CCR = row['CCR']
            data.AGE = row['AGE']
            data.GENDER = row['GENDER']
            data.RACE = row['RACE']
            data.ARRESTTIME = row['ARRESTTIME']
            data.ARRESTLOCATION = row['ARRESTLOCATION']
            data.OFFENSES = row['OFFENSES']
            data.INCIDENTLOCATION = row['INCIDENTLOCATION']
            data.INCIDENTNEIGHBORHOOD = row['INCIDENTNEIGHBORHOOD']
            data.INCIDENTZONE = row['INCIDENTZONE']
            data.INCIDENTTRACT = row['INCIDENTTRACT']
            data.COUNCIL_DISTRICT = row['COUNCIL_DISTRICT']
            data.PUBLIC_WORKS_DIVISION = row['PUBLIC_WORKS_DIVISION']
            data.X = row['X']
            data.Y = row['Y']
            data.save()
           
