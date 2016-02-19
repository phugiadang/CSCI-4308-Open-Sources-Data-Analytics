import glob
import pandas as pd
import os.path, requests
import urllib
import zipfile
import operator
import lxml.html as lh

local_path = '/home/dano8957/panda/GDELT2/'

fips_country_code = 'US'

df = pd.read_pickle(local_path+'backup'+fips_country_code+'.pickle');
