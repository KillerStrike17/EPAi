from faker import Faker
from collections import namedtuple
import functools
from datetime import date,datetime
from decimal import Decimal
from statistics import mode
import string
import random
fake = Faker()

## Task 1

def init_task1()->namedtuple:
  """
  This is the init function, this is to initialize and create a profile named tuple containing each profile information
  and all profile named tuple containing all the profiles.
  """
  profile = namedtuple('profile',fake.profile().keys())
  allprofiles = namedtuple('allprofile',['profile'])

  p1 = profile(**fake.profile())
  all_profile_nt = allprofiles(p1)

  for _ in range(19_999):
    p1 = profile(**fake.profile())
    all_profile_nt += allprofiles(p1)
  # all_profile_nt.__doc__ = """
  # This is a named tuple storing all the profiles. Each Profile has 
  # address, birthdate, Blood_group, company, current_location, job, 
  # mail, name, residence, sex, ssn, username and website. 
  # """
  return all_profile_nt

def oldest_person_nt(all_profile_nt:namedtuple)->tuple:
  """
  This function finds the oldest person from the slot, calculates the duration. The minimum birthdate and
  time is returned.

  # Param:
    all_profile_nt: Named tuple containing all  profiles

  """
  start = datetime.now()
  value = min(all_profile_nt, key=lambda v : v[-1])
  end = datetime.now()
  return end-start, value

def average_age_nt(all_profile_nt: namedtuple)->tuple:
  """
  This function finds the average age of the person from the slot, calculates the duration to perform that operation. 
  The average age and time is returned.

  # Param:
    all_profile_nt: Named tuple containing all  profiles

  """
  today = date.today()
  start = datetime.now()
  value = sum(map(lambda v : today.year - v[-1].year -((today.month, today.day) < (v[-1].month, v[-1].day)),all_profile_nt))/len(all_profile_nt)
  end = datetime.now()
  return end-start, value

def average_coords_nt(all_profile_nt:namedtuple)->tuple:
  """
  This function finds the average coordinates  from the slot, calculates the duration to perform that operation. 
  The average coordinates and time is returned.

  # Param:
    all_profile_nt: Named tuple containing all  profiles

  """
  start = datetime.now()
  x, y = sum(map(lambda t: t[0],map(lambda v : v[4],all_profile_nt)))/len(all_profile_nt),sum(map(lambda t: t[1],map(lambda v : v[4],all_profile_nt)))/len(all_profile_nt)
  end = datetime.now()
  return end-start, x, y

def average_bloodgroup_nt(all_profile_nt:namedtuple)->tuple:
  """
  This function uses the mode function defined in statisics library to find the most occured blood group from the list. The list is generated
  using the lambda function and returned to the mode function as a parameters. The code is then timed and the result and time is sent back.

  # Param:
    all_profile_nt: Named tuple containing all  profiles
  """
  start = datetime.now()
  blood_group = mode(list(map(lambda v: v[5],all_profile_nt)))
  end = datetime.now()
  return end-start, blood_group

## Task 2

def init_task2()->namedtuple:
  """
  This is the init function, this is to initialize and create a profile dictionary containing each profile information
  and all profile dictionary containing all the profiles.\
  """
  all_profile_dict = {}
  for _ in range(20_000):
    all_profile_dict[_+1] = fake.profile()
  return all_profile_dict

def oldest_person_dc(all_profile_dict:dict)->tuple:
  """
  This function finds the oldest person from the slot, calculates the duration. The minimum birthdate and
  time is returned.

  # Param:
    all_profile_dc: dictionary containing all  profiles
  """
  start = datetime.now()
  value = min(all_profile_dict.values(),key = lambda v : v['birthdate'])
  end = datetime.now()
  return end-start, value

def average_age_dc(all_profile_dict:dict)->tuple:
  """
  This function finds the average age of the person from the slot, calculates the duration to perform that operation. 
  The average age and time is returned.

  # Param:
    all_profile_dc: Dictionary containing all  profiles

  """
  today = date.today()
  start = datetime.now()
  value = sum(map(lambda v : today.year - v['birthdate'].year -((today.month, today.day) < (v['birthdate'].month, v['birthdate'].day)),all_profile_dict.values()))/len(all_profile_dict)
  end = datetime.now()
  return end-start, value

def average_coords_dc(all_profile_dict:dict)->tuple:
  """
  This function finds the average coordinates  from the slot, calculates the duration to perform that operation. 
  The average coordinates and time is returned.

  # Param:
    all_profile_dc: dictionary containing all profiles

  """
  start = datetime.now()
  x,y = sum(map(lambda t: t[0],map(lambda v : v['current_location'],all_profile_dict.values())))/len(all_profile_dict.values()),sum(map(lambda t: t[1],map(lambda v : v['current_location'],all_profile_dict.values())))/len(all_profile_dict.values())
  end = datetime.now()
  return end-start, x, y

def average_bloodgroup_dc(all_profile_dict:dict)->tuple:
  """
  This function uses the mode function defined in statisics library to find the most occured blood group from the list. The list is generated
  using the lambda function and returned to the mode function as a parameters. The code is then timed and the result and time is sent back.

  # Param:
    all_profile_dc: dictionary containing all profiles
  """
  start = datetime.now()
  value = mode(list(map(lambda v: v['blood_group'],all_profile_dict.values())))
  end = datetime.now()
  return end-start, value

## Task 3
Company = namedtuple('Company', 'name symbol open high low close')
allcompany = namedtuple('allcompany',['Company'])
random_weight  =  namedtuple('random_weight','weight')
def init_task3()->tuple:
  """
  This function is used to initilize the all company named tuple( where data 
  of all the companies will be stored) and the normalized weights. 

  # Returns:

    It returns the Tuple containing the initailized All Company Named
    tuple and Normalized weights.
  """

  weight = random.uniform(0,1)
  r1  = random_weight(weight)

  for _ in range(99):
    weight = random.uniform(0,1)
    r1 += weight,

  sum_value = sum(r1)
  r2 = tuple(map(lambda x: x/sum_value,r1))

  open_ = random.randint(1000,50000) * weight
  close = open_ * random.uniform(0.7,1.15)
  high = open_ * random.uniform(0.85,1.15)
  low = open_ * random.uniform(0.7,1)
  if high < open_:
    high = open_
  if high < close:
    high = close
  if low > high:
    if high>open_:
      low = open_
    else:
      low = close
  c1 = Company(fake.company(),''.join(random.sample(string.ascii_uppercase, 3)),open_, high, low, close)
  c2 = allcompany(c1)
  # c2.__doc__= """
  # This is a named tuple storing all the Company stock market. Each Company has 
  # name, open, close, high and Low. 
  # """
  return c2, r2

def stock_market(comp_stock:namedtuple ,norm_weights: namedtuple)->namedtuple:
  """
  This function is used to generate the stock market data for 99 Companies
  
  # Param:
    Comp_stock: Named tuple containing the initialized all Company named tuple
    
    norm_weights: Tuple containing the normalized weights used to generated the 
                  which will be used to calculate the high, open, close and low.
  
  # Returns:
    It returns a Named tuple containing the stocks value of all 100 companies.
  """
  for _ in range(99):
    weight = norm_weights[_+1]
    open_ = random.randint(1000,50000) * weight
    close = open_ * random.uniform(0.7,1.15)
    high = open_ * random.uniform(0.85,1.15)
    low = open_ * random.uniform(0.7,1)
    if high < open_:
      high = open_
    if high < close:
      high = close
    if low > high:
      if high>open_:
        low = open_
      else:
        low = close
    c1 = Company(fake.company(),''.join(random.sample(string.ascii_uppercase, 3)),open_, high, low, close)
    comp_stock += allcompany(c1)

  return comp_stock

