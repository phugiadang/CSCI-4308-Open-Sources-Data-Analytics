import os.path, requests
import urllib
import zipfile
import glob
import operator
import lxml.html as lh
gdelt_base_url = 'http://data.gdeltproject.org/events/'

# get the list of all the links on the gdelt file page
page = requests.get(gdelt_base_url+'index.html')
doc = lh.fromstring(page.content)
link_list = doc.xpath("//*/ul/li/a/@href")

# separate out those links that begin with four digits 
file_list = [x for x in link_list if str.isdigit(x[0:4])]

infilecounter = 0
outfilecounter = 0

local_path = '/home/dano8957/panda/GDELT2/'

fips_country_code = 'US'

for compressed_file in file_list[infilecounter:]:
    print compressed_file,
    
    # if we dont have the compressed file stored locally, go get it. Keep trying if necessary.
    while not os.path.isfile(local_path+compressed_file): 
        print 'downloading,',
        urllib.urlretrieve(url=gdelt_base_url+compressed_file, 
                           filename=local_path+compressed_file)
        
    # extract the contents of the compressed file to a temporary directory    
    print 'extracting,',
    z = zipfile.ZipFile(file=local_path+compressed_file, mode='r')    
    z.extractall(path=local_path+'tmp/')
    
    # parse each of the csv files in the working directory, 
    print 'parsing,',
    for infile_name in glob.glob(local_path+'tmp/*'):
        outfile_name = local_path+'country/'+fips_country_code+'%04i.tsv'%outfilecounter
        
        # open the infile and outfile
        with open(infile_name, mode='r') as infile, open(outfile_name, mode='w') as outfile:
            for line in infile:
                # extract lines with our interest country code
                if fips_country_code in operator.itemgetter(51, 37, 44)(line.split('\t')):    
                    outfile.write(line)
            outfilecounter +=1
            
        # delete the temporary file
        os.remove(infile_name)
    infilecounter +=1
    print 'done'
