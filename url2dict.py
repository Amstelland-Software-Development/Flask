# https://www.w3schools.com/python/python_ref_string.asp

url = "https://stagemarkt.nl/vacatures/?Termen=Software+developer+(25604)&PlaatsPostcode=amsterdam&Straal=0&Land=e883076c-11d5-11d4-90d3-009027dcddb5&ZoekenIn=A&Page=1&Longitude=&Latitude=&Regio=&Plaats=&Niveau=&SBI=&Kwalificatie=&Sector=&RandomSeed=743&Leerweg=&Internationaal=&Beschikbaarheid=&AlleWerkprocessenUitvoerbaar=&LeerplaatsGewijzigd=&Sortering=0&Bron=STA&Focus=&LeerplaatsKenmerk=&OrganisatieKenmerk="

def url2dict(url):
    baseURL = "https://stagemarkt.nl/vacatures/"
    urlPropertyDictionary = {};
    baseURL =  url[:url.find("?")];
    remainderString = url[url.find("?")+1:]
    listOfProperties = remainderString.split("&")
    for item in listOfProperties: #voorbeeld van property: &PlaatsPostcode=amsterdam
        # print(item)
        listPropValue = item.split("=")
        # print(listPropValue[0] + " => " + listPropValue[1])
        urlPropertyDictionary[listPropValue[0]] = listPropValue[1]
    return urlPropertyDictionary

def dict2url(dict):
    url = "https://stagemarkt.nl/vacatures/?"
    for key, value in dict.items():
        url += key + "=" + value + "&"
    return url


# dict = url2dict(url)
# print(dict)
# dict['Page'] = "2"
# url = dict2url(dict)
# print(url)
# print(dict)