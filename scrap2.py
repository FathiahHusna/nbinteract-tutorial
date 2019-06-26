#calling package URL lib
from urllib.request import urlopen as uReq
#pase HTML text
from bs4 import BeautifulSoup as soup

#my_url = 'https://www.mudah.my/2014+Mercedes+Benz+CLA180+AMG+UNREG-71580492.htm'

my_url = 'https://www.mudah.my/2018+Toyota+HARRIER+2+0+PROGRESS+FULL+SPEC+UNREG-68253250.htm'

#opening up the connnection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing  
page_soup = soup(page_html, "html.parser")

#filename = "cars1.csv"
filename = "cars1_.csv"
f = open(filename, "w")

headers = "Brand, Mileage, Model, Seat, Variant, Type, Series, Manufactured_Yr, Country, Transmission, EngineCC, Eng_Compression, Eng_PeakPower, Eng_PeakTorque, Eng_Type, Eng_Fuel, Length, Width, height, WheelBase, KerbWeight, FuelTank, FrontBrake, RearBrake, FrontSusp, RearSusp, Steering, FrontTyres, RearTyres, FrontRim, RearRim"

f.write(headers)
f.write("\n")

#GENERAL
panel1 = page_soup.findAll("div", {"class":"general_section"})

for pop in panel1:
    brand = pop.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
    gBrand = brand[0].text
    gMileage = brand[1].text
    gModel = brand[2].text
    gSeat = brand[3].text
    gVariant = brand[4].text
    gType = brand[5].text
    gSeries = brand[6].text
    gYear = brand[7].text
    gCountry = brand[8].text

    print("Brand: " + gBrand)
    print("Mileage: " + gMileage)
    print("Model: " + gModel)
    print("Seat: " + gSeat)
    print("Variant: " + gVariant)
    print("Type: " + gType)
    print("Series: " + gSeries)
    print("Manufactured Yr: " + gYear)
    print("Country: " + gCountry)


    f.write(gBrand + "," + gMileage + "," + gModel + "," + gSeat + "," + gVariant + "," + gType + "," + gSeries + "," + gYear + "," + gCountry + ",")
    
#TRANSMISSION
panel2 = page_soup.findAll("div", {"class":"transmission_section"})

for pop2 in panel2:
    trans= pop2.findAll("div", {"class":"col-xs-9 mcd_record_adview"})
    Ttrans = trans[0].text

    print("Transmission: " + Ttrans)
    f.write(Ttrans+ ",")


#ENGINE
panel3 = page_soup.findAll("div", {"class":"engine_section"})

#ENGINE
for pop3 in panel3:
    eng = pop3.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
    engCC = eng[0].text
    engCompr = eng[1].text
    engPeakPwr = eng[2].text
    engPeakTorque = eng[3].text
    engType = eng[4].text
    engFuel = eng[5].text

    print("EngineCC: " + engCC)
    print("Engine Compression: " + engCompr)
    print("Engine Peak Power: " + engPeakPwr)
    print("Engine Peak Torque: " + engPeakTorque)
    print("Engine Type: " + engType)
    print("Engine Fuel: " + engFuel)
    f.write(engCC + "," + engCompr + "," + engPeakPwr + "," + engPeakTorque + "," + engType + "," + engFuel + ",")
    

#DIMENSION
panel4 = page_soup.findAll("div", {"class":"dimension_section"})

for pop4 in panel4:
    dim = pop4.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
    dLength = dim[0].text
    dWidth = dim[1].text
    dHeight = dim[2].text
    dWheelBase = dim[3].text
    dKerbWeight = dim[4].text
    dFuelTank = dim[5].text

    print("Length: " + dLength)
    print("Width: " + dWidth)
    print("Height: " + dHeight)
    print("Wheel Base: " + dWheelBase)
    print("Kerb Weight: " + dKerbWeight)
    print("Fuel tank: " + dFuelTank)
    f.write(dLength + "," + dWidth + "," + dHeight + "," + dWheelBase + "," + dKerbWeight + "," + dFuelTank + ",")


#BRAKES
panel5 = page_soup.findAll("div", {"class":"brakes_section"})

for pop5 in panel5:
    b = pop5.findAll("div", {"class": "col-xs-3 mcd_record_adview"})
    bFront = b[0].text
    bRear = b[1].text

    print("Front Brake: " + bFront)
    print("Rear Brake: " + bRear)
    f.write (bFront + "," + bRear + ",")

#SUSPENSION
panel6 = page_soup.findAll("div", {"class":"suspensions_section"})

for pop6 in panel6:
    s = pop6.findAll("div", {"class": "col-xs-3 mcd_record_adview"})
    sFront = s[0].text
    sRear =  s[1].text

    print("Front Suspension: " + sFront)
    print("Rear Suspension: " + sRear)
    f.write(sFront + "," + sRear + ",")
    
#STEERING
panel7 = page_soup.findAll("div", {"class":"steering_section"})

for pop7 in panel7:
    st = pop7.findAll("div", {"class":"col-xs-9 mcd_record_adview"})
    sSteering = st[0].text

    print("Steering: " + sSteering)
    f.write(sSteering + ",")

#TYRES
panel8 = page_soup.findAll("div", {"class":"tyres_section"})

for pop8 in panel8:
    t = pop8.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
    tFront = t[0].text
    tRear = t[1].text
    tFRim = t[2].text
    tRRim = t[3].text

    print("Front Tyres: " + tFront)
    print("Rear Tyres: " + tRear)
    print("Front Rim: " +tFRim)
    print("Rear rim: " +tRRim)
    f.write(tFront + "," + tRear + "," + tFRim + "," + tRRim + ",")

f.close()


