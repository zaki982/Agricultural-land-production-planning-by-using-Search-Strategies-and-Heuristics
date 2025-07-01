import numpy as np
import pandas as pd
import zipfile
import csv
import os
from filelock import FileLock

product_names = [
    "aubergine",
    "corn",
    "date",
    "greenpepper",
    "potatoe",
    "tomatoe",
    "wheat"
]
strategic_products=[
    "date",
    "potatoe",
    "tomatoe",
    "wheat"
]
seasons = ["winter","spring","summer","autumn"]
years = [2016,2017,2018,2019]
#class year implementation
class Year:
    def __init__(self):
        self.yearly_production_data = {year: [0, 1, 0] for year in years}
        self.yearly_prices_data = {year: {season: 0 for season in seasons} for year in years}
        self.country_yearly_consumption_data = {year: 0 for year in years}
        self.country_yearly_production_data={year: 0 for year in years}
    #function to adding a year in the system
    def add_year(self, year_num):
        self.yearly_production_data[year_num] = [0, 0, 0]
        self.yearly_prices_data[year_num] = {season: 0 for season in ["winter", "spring", "summer", "autumn"]}
        self.country_yearly_consumption_data[year_num] = 0
        self.country_yearly_production_data[year_num]=0    
    def set_yearly_production(self, year, ld_size, prod,productivity):
        if year in years and ld_size >= 0 and prod >= 1 and productivity >=0:
            self.yearly_production_data[year] = [ld_size, prod, productivity]
        elif year in years and prod == 0:
            self.yearly_production_data[year][1] =1
        else:
            print("Invalid year, size, production or productivity.")

    def get_yearly_production(self, year):
        if year in years:
            return self.yearly_production_data[year]
        else:
            print("No production data available for the specified year.")

    def set_prices_per_season(self, year, price, season):
        if year in years and season in seasons and price >= 0:
            self.yearly_prices_data[year][season] = price
        else:
            print("Invalid year, season, or price.")

    def get_prices_per_season(self, year, season):
        if year in years and season in seasons:
            return self.yearly_prices_data[year][season]
        else:
            print("No price data available for the specified year or season.")
    def set_country_yearly_consumption(self, year, consumption):
        if year in years and consumption >= 0:
            self.country_yearly_consumption_data[year] = consumption
        else:
            print("Invalid year or consumption value.")

    def get_country_yearly_consumption(self, year):
        if year in years:
            return self.country_yearly_consumption_data[year]
        else:
            print("No consumption data available for the specified year.")
    def set_country_yearly_production(self, year, p):
        if year in years and p >= 0:
            self.country_yearly_production_data[year] = p
        else:
            print("Invalid year or production value.")

    def get_country_yearly_production(self, y):
        if y in years:
            return self.country_yearly_production_data[y]
        else:
            print("No production data available for the specified year.")
#class product implementation
class product:
    def __init__(self, name=''):
        self.set_name(name)
        self.yearly_info = Year()

    def set_name(self, name):
        if name in product_names:
            self.name = name
        else:
            print('Product does not exist.')

    def get_name(self):
        return self.name

    def self_sufficiency(self, year):
        n = self.get_name()
        p = self.yearly_info.get_country_yearly_production(year)
        c = self.yearly_info.get_country_yearly_consumption(year)
        if p > c:
            return print(f"For product: {n} in {year}, Algeria has achieved self-sufficiency.")
        else:
            return print(f"For product: {n} in {year}, Algeria did not achieve self-sufficiency.")

#class wilaya implementation
class Wilaya:
    def __init__(self, num):
        if 1 <= num <= 48:
            self.wilaya_number = num
        else:
            print("Error: Wilaya number must be between 1 and 48.")
            return 
        self.name =""
        self.wilaya_products = {product_name: product(product_name) for product_name in product_names}
        self.wilaya_size = 0 

 
       #setters
    def set_wilaya_name(self,name):
        self.name = name 
    
    #Getters
    def get_wilaya_number(self):
        return self.wilaya_number

    def get_products(self):
        return list(self.wilaya_products.values())

    def get_wilaya_size(self):
        return self.wilaya_size

    def get_wilaya_name(self):
        return self.name
        
           
    def wilaya_specialty(self, year):
        best_product = None
        max_production = 0
    
        for product in self.wilaya_products.values():
            yearly_production = product.yearly_info.get_yearly_production(year)
            production = yearly_production[2]  
            if production > max_production:
                max_production = production
                best_product = product.get_name()
    
        return {
            "wilaya_number": self.get_wilaya_number(),
            "wilaya_specialty": best_product
        }
