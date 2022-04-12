#!/usr/bin/env python
# coding: utf-8

# In[85]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 
         'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol',
         'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David',
         'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina',
         'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']


# In[3]:


# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 
          'September', 'September', 'September', 'September', 'September',
          'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September',
          'September', 'July', 'August', 'September', 'October', 'August', 'September',
          'October', 'September', 'September', 'October']


# In[4]:


# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955,
         1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989,
         1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007,
         2016, 2017, 2017, 2018]


# In[5]:


# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160,
                       160, 175, 175, 160, 160, 175, 160, 175, 175, 190,
                       185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 
                       175, 175, 165, 180, 175, 160]


# In[6]:


# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'],
                  ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], 
                  ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], 
                  ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], 
                  ['Cuba', 'United States Gulf Coast'], 
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
                  ['Mexico'], ['The Caribbean', 'United States East coast'], 
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
                  ['The Caribbean', 'United States East Coast'], 
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
                  ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
                  ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


# In[86]:


# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M',
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', 
           '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', 
           '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', 
           '91.6B', '25.1B']


# In[87]:


# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,
          37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# In[88]:


# write your update damages function here:
def str_to_float(string):
    newfloat = string
    if string[-1] == "M": 
        newfloat = float(string[:-1])*1000000
    elif string[-1] == "B": 
        newfloat = float(string[:-1])*1000000000                     
    return newfloat


# In[89]:


for i in range(len(damages)):
    damages[i] = str_to_float(damages[i])


# In[113]:


print(damages)


# In[18]:


def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane = {}
    for i in range(len(names)):
        hurricane.update({names[i]: {"Name": names[i], "Month": months[i], 
                                     "Year": years[i], "Max Sustained Wind": max_sustained_winds[i],
                                     "Areas affected": areas_affected[i], "Damage": damages[i], 
                                     "Deaths": deaths[i]}})
    return hurricane


# In[136]:


hurricane_names = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(hurricane_names)


# In[66]:


def hurricane_by_year(h_by_name):
    h_by_year = {}
    for info in h_by_name.values():
        if info["Year"] not in h_by_year:
            h_by_year.update({info["Year"]: {"Name": info["Name"], 
                                             "Month": info["Month"], "Year": info["Year"], 
                                             "Max Sustained Wind": info["Max Sustained Wind"], 
                                             "Areas affected": info["Areas affected"], 
                                             "Damage": info["Damage"], "Deaths": info["Deaths"]}})
        else:
            h_by_year.update({info["Year"]: [h_by_year[info["Year"]], 
                                             {info["Year"]: {"Name": info["Name"], 
                                                             "Month": info["Month"], 
                                                             "Year": info["Year"], 
                                                             "Max Sustained Wind": info["Max Sustained Wind"],
                                                             "Areas affected": info["Areas affected"],
                                                             "Damage": info["Damage"], "Deaths": info["Deaths"]}}]})
    return h_by_year


# In[137]:


hurricane_years = hurricane_by_year(hurricane_names)
print(hurricane_years)


# In[74]:


def hurricane_area_count(hurricanes):
    counts = {}
    for info in hurricanes.values():
        for location in info["Areas affected"]:
            if location not in counts:
                counts.update({location: 1})
            else:
                counts.update({location: counts[location] + 1})
    return counts
        


# In[75]:


area_counts = hurricane_area_count(hurricane_names)
print(area_counts)


# In[76]:


def hurricane_central(hurricanes):
    max_value = 0
    hardest_hit = ""
    for area in hurricanes:
        if hurricanes[area] > max_value:
            max_value = hurricanes[area]
            hardest_hit = area
    return (hardest_hit, max_value)


# In[77]:


print(hurricane_central(area_counts))


# In[110]:


def most_fatal(hurricanes):
    max_deaths = 0
    worst_hurricane = ""
    for hurricane in hurricanes.values():
        if hurricane["Deaths"] > max_deaths:
            max_deaths = hurricane["Deaths"]
            worst_hurricane = hurricane
    return (worst_hurricane["Name"], max_deaths)
        


# In[140]:


print(most_fatal(hurricane_names))


# In[118]:


def mortality_index(hurricanes):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    scaled_hurricanes = {1: [], 2: [], 3: [], 4:[], 5:[]}
    
    for hurricane in hurricanes.values():
        for i in range(1,5):
            if hurricane["Deaths"] < mortality_scale[i]:
                index = i
                break
            else:
                index = 5
        scaled_hurricanes[index].append(hurricane["Name"])
    return(scaled_hurricanes)
        
    


# In[119]:


#print(list(zip(names, deaths)))
print(mortality_index(hurricane_names))


# In[116]:


def greatest_damage(hurricanes):
    worst_hurricane = ""
    max_cost = 0
    
    for hurricane in hurricanes.values():
        if type(hurricane["Damage"]) == float:
            if hurricane["Damage"] > max_cost:
                max_cost = hurricane["Damage"]
                worst_hurricane = hurricane["Name"]
    return (worst_hurricane, max_cost)


# In[158]:


print(greatest_damage(hurricane_names))
#print(hurricane_names)
for hurricane in hurricane_names.values():
    print (hurricane["Damage"])


# In[165]:


def damage_index(hurricanes):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    scaled_hurricanes = {1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes.values():
        if type(hurricane["Damage"]) != float:
            continue
        for i in range(1,5):
            if hurricane["Damage"] < damage_scale[i]:
                index = i
                break
            else:
                index = 5
        scaled_hurricanes[index].append(hurricane["Name"])
    return(scaled_hurricanes)
    
    


# In[167]:


print(list(zip(names, damages)))
print(damage_index(hurricane_names))

