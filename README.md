First, create a virtualenv:  virtualenv venv --distribute; source venv/bin/activate

Next, install sqlalchemy




Notes:
each time you add a new table or whatever, you have to reinitialize the database.  Which is BAD!  This means that we can't change our database or add new models because then all of the old data will get erased.  This is a major problem that needs to be addressed.