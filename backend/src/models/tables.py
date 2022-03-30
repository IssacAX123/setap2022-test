from sqlalchemy.ext.automap import automap_base

from src.models import db

Base = automap_base()
Base.prepare(db.engine, reflect=True)

x = Base.classes
User = Base.classes.registereduser
Friend = Base.classes.friend
Journey = Base.classes.journey
Trip = Base.classes.trip
BookedTrip = Base.classes.bookedtrip