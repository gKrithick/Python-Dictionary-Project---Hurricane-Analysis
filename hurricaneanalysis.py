# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def updated_damages_fn(damages):
  updated_damages = []
  for damage in damages:
    if 'Damages not recorded' in damage:
      updated_damages.append(damage)
    if 'M' in damage:
      updated_damages.append(float(damage.strip('M'))*conversion['M'])
    if 'B' in damage:
      updated_damages.append(float(damage.strip('B'))*conversion['B'])
  return updated_damages                    

# test function by updating damages
updated_damages = updated_damages_fn(damages)
#print(updated_damages)

# 2 
# Create a Table
def dict_fn(names, months, years, max_sustained_winds,updated_damages, areas_affected, deaths):
  dict = {}
  for i in range(len(names)):
    dict[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
  return dict

dict = dict_fn(names, months, years, max_sustained_winds,updated_damages, areas_affected, deaths)

print(dict)   

#print(dict_fn(names, months, years, max_sustained_winds,updated_damages, areas_affected, deaths))


# Create and view the hurricanes dictionary

# 3
# Organizing by Year
def year_dict(dict):
    hurricane_years = {}
#for loop that checks if year in hurricane_years, and adds data 
    for data in dict.values():
      for year, lst in hurricane_years.items():
        if data['Year'] == year:
          lst.append(data)
      hurricane_years.update({data['Year']: [data]})
    return hurricane_years
 
# create a new dictionary of hurricanes with year and key
year_dict = year_dict(dict)
#print(year_dict)   

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in

def areas_affecteddict(dict):
  total_areas_affected = []
  total_areas_affected_dict = {}
  #areas_affected_dict = defaultdict(total_areas_affected)
  for hurricanes in dict.values():
    for key,values in hurricanes.items():
      if key == 'Areas Affected':
        total_areas_affected += values
  for i in total_areas_affected:
      if i not in total_areas_affected_dict:
        total_areas_affected_dict[i] = 1
      if i in total_areas_affected_dict:
        total_areas_affected_dict[i] += 1
  return total_areas_affected_dict      

dict_areas_affected = areas_affecteddict(dict)
#print(dict_areas_affected)    

    
# 5 
# Calculating Maximum Hurricane Count
def max_hurricane_count(dict_areas_affected):
  max = 0
  max_affected = ''
  for key, value in dict_areas_affected.items():
    if value > max:
      max = value
      max_affected = key
  return max_affected, max        
max_hurricane = max_hurricane_count(dict_areas_affected)  
#print(max_hurricane)

# find most frequently affected area and the number of hurricanes involved in


# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(dict):
  max_value = 0
  max = ''
  for i in dict.values():
    for key, value in i.items():
      if key == 'Deaths':
        if value > max_value:
          max_value = value
          max = i['Name']
  return max, max_value

deadliest_hurricane =  deadliest_hurricane(dict)
#print(deadliest_hurricane)


# find highest mortality hurricane and the number of deaths
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# 7
# Rating Hurricanes by Mortality
def hurricanes_by_mortality(dict):
  hurricanes_by_mortalitydict = {0: '',1: '', 2: '', 3: '',4:''}
  for i in dict.values():
    for key, value in i.items():
      if key == 'Deaths':
        if value == 0:
          hurricanes_by_mortalitydict[0] +=  ',' + i['Name'] 
        if value > 0 and value >= 100:
          hurricanes_by_mortalitydict[1] += ',' + i['Name'] 
        if value > 100 and value >= 500:
          hurricanes_by_mortalitydict[2] += ',' + i['Name'] 
        if value > 500 and value >= 1000:
          hurricanes_by_mortalitydict[3] += ',' + i['Name'] 
        if value > 1000 and value >= 10000:
          hurricanes_by_mortalitydict[4] += ',' + i['Name'] 
  return hurricanes_by_mortalitydict 
hurricanes_by_mortalitydict = hurricanes_by_mortality(dict)
#print(hurricanes_by_mortalitydict)         
        




# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def max_damage(dict):
  max_damage = ''
  cost = 0
  for i in dict.values():
    for key, value in i.items():
      if key == "Damage":
        if value == "Damages not recorded":
          continue
        if int(value) > cost:
          cost = value
          max_damage = i['Name']
  return max_damage, cost
max_damages = max_damage(dict)
#print(max_damages)          

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_scale(dict):
  damage_scale_dict = {0: '',
                1: '',
                2: '',
                3: '',
                4: ''}
  for i in dict.values():
    for key, value in i.items():
      if key == "Damage":
        if value == "Damages not recorded":
          continue
        if value == 0:
          damage_scale_dict[0] +=  i['Name']  
        if value > 100000000:
          damage_scale_dict[1] +=  i['Name'] + ', '
        if value > 1000000000:
          damage_scale_dict[2] +=  i['Name'] + ', ' 
        if value > 10000000000:
          damage_scale_dict[3] +=  i['Name'] + ', '
        if value > 5000000000:
          damage_scale_dict[4] +=  i['Name']  + ', '  
  return damage_scale_dict  
damage_scale = damage_scale(dict)
print(damage_scale)  
