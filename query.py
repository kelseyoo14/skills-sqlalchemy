"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

brand = Brand.query.get(8)


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

chev_corvette = Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()


# Get all models that are older than 1960.

older_mods = Model.query.filter(Model.year < 1960).all()


# Get all brands that were founded after 1920.

newer_brands = Brand.query.filter(Brand.founded > 1920).all()


# Get all models with names that begin with "Cor".

cor_models = Model.query.filter(Model.name.like('Cor%')).all()


# Get all brands that were founded in 1903 and that are not yet discontinued.

brands_1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()


# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

old_brands = Brand.query.filter((Brand.discontinued != None)|(Brand.founded < 1950)).all()


# Get any model whose brand_name is not Chevrolet.

not_chevrolet = Model.query.filter(Model.brand_name != 'Chevrolet').all()


# # Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    # FIX ME When testing, if i print out model.brand.headquarters for 1 model object
    # it works, but using it in the for loop isn't working. Why?
    # Fixed! 'Fillmore' does not exist in the 'brands' table,
    # which explains the "'NoneType' object has no attribute 'headquarters'" AttributeError
    # Added if statement to only print if brand_name exists in brands table
    for model in models:
        if model.brand:
            print model.name, model.brand_name, model.brand.headquarters
        else:
            headquarters = None
            print model.name, model.brand_name, headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_and_models = Model.query.order_by(Model.brand_name).all()

    for model in brands_and_models:
        print model.brand_name, model.name


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# This returns a query. Without .all(), .get(), .one(), or .first(), we are not actually querying
# the database for a result (which would be records from our tables). If I print this query, here
# is the output:

# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded AS brands_founded, 
# brands.headquarters AS brands_headquarters, brands.discontinued AS brands_discontinued
# FROM brands
# WHERE brands.name = :name_1



# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# As association table is a table that is created to manage two tables that have a 
# 'many to many' relationship. The association table has a many to one relationship
# to each of the original tables, and doesn't have any other columns than the ones 
# needed to manage the relationship between the two original tables.



# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()


def get_models_between(start_year, end_year):
    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
