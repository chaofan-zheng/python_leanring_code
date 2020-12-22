import requests
response = requests.get('https://gitlab.com/digitalhumanitiesatberkeley/computational-literary-analysis-readings/-/raw/master/content/texts/moonstone.md')
moonstone2 = response.text
print(moonstone2[:1000])
