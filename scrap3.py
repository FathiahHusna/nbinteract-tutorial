#from scrap1 (grab; price, condition, link)
#drpd link(grab; general, transmission, engine, dimension&weight, brake, susp, steering, tyres&wheel)

#calling package URL lib
from urllib.request import urlopen as uReq
#pase HTML text
from bs4 import BeautifulSoup as soup

my_url = 'https://www.mudah.my/malaysia/cars-for-sale'

#opening up the connnection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing  
page_soup = soup(page_html, "html.parser")

#filename = "cars3.csv"
#filename = "cars3_.csv"
filename = "cars3__.csv"
f = open(filename, "w")

headers = "Name, Price, Condition, Link, Mileage, NewMil, Brand, Model, Seat, Variant, Type, Series, Manufactured_Yr, Country, Transmission, EngineCC, Eng_Compression, Eng_PeakPower, Eng_PeakTorque, Eng_Type, Eng_Fuel, Length, Width, height, WheelBase, KerbWeight, FuelTank, FrontBrake, RearBrake, FrontSusp, RearSusp, Steering, FrontTyres, RearTyres, FrontRim, RearRim"

f.write(headers)
f.write("\n")

containers = page_soup.findAll("div", {"class":"listing_params_container"})

#substituting avg of mileage
def subs (gMileage):
    if gMileage == "0 - 4 999":
        return gMileage.replace("0 - 4 999", "2500", 1)
    elif gMileage == "5 000 - 9 999":
        return gMileage.replace("5 000 - 9 999", "52500", 1)
    elif gMileage == "10 000 - 14 999":
        return gMileage.replace("10 000 - 14 999", "12500", 1)
    elif gMileage == "15 000 - 19 999":
        return gMileage.replace("15 000 - 19 999", "17500", 1)
    elif gMileage == "20 000 - 24 999":
        return gMileage.replace("20 000 - 24 999", "22500", 1)
    elif gMileage == "25 000 - 29 999":
        return gMileage.replace("25 000 - 29 999", "27500", 1)
    elif gMileage == "30 000 - 34 999":
        return gMileage.replace("30 000 - 34 999", "32500", 1)
    elif gMileage == "35 000 - 39 999":
        return gMileage.replace("35 000 - 39 999", "37500", 1)
    elif gMileage == "40 000 - 44 999":
        return gMileage.replace("40 000 - 44 999", "42500", 1)
    elif gMileage == "45 000 - 49 999":
        return gMileage.replace("45 000 - 49 999", "47500", 1)
    elif gMileage == "50 000 - 54 999":
        return gMileage.replace("50 000 - 54 999", "52500", 1)
    elif gMileage == "55 000 - 59 999":
        return gMileage.replace("55 000 - 59 999", "57500", 1)
    elif gMileage == "60 000 - 64 999":
        return gMileage.replace("60 000 - 64 999", "62500", 1)
    elif gMileage == "65 000 - 69 999":
        return gMileage.replace("65 000 - 69 999", "67500", 1)
    elif gMileage == "70 000 - 74 999":
        return gMileage.replace("70 000 - 74 999", "72500", 1)
    elif gMileage == "75 000 - 79 999":
        return gMileage.replace("75 000 - 79 999", "77500", 1)
    elif gMileage == "80 000 - 84 999":
        return gMileage.replace("80 000 - 84 999", "82500", 1)
    elif gMileage == "85 000 - 89 999":
        return gMileage.replace("85 000 - 89 999", "87500", 1)
    elif gMileage == "90 000 - 94 999":
        return gMileage.replace("90 000 - 94 999", "92500", 1)
    elif gMileage == "95 000 - 99 999":
        return gMileage.replace("95 000 - 99 999", "97500", 1)
    elif gMileage == "100 000 - 109 999":
        return gMileage.replace("100 000 - 109 999", "105000", 1)
    elif gMileage == "110 000 - 119 999":
        return gMileage.replace("110 000 - 119 999", "115000", 1)
    elif gMileage == "120 000 - 129 999":
        return gMileage.replace("120 000 - 129 999", "125000", 1)
    elif gMileage == "130 000 - 139 999":
        return gMileage.replace("130 000 - 139 999", "135000", 1)
    elif gMileage == "140 000 - 149 999":
        return gMileage.replace("140 000 - 149 999", "145000", 1)
    elif gMileage == "150 000 - 159 999":
        return gMileage.replace("150 000 - 159 999", "155000", 1)
    elif gMileage == "160 000 - 169 999":
        return gMileage.replace("160 000 - 169 999", "165000", 1)
    elif gMileage == "170 000 - 179 999":
        return gMileage.replace("170 000 - 179 999", "175000", 1)
    elif gMileage == "180 000 - 189 999":
        return gMileage.replace("180 000 - 189 999", "185000", 1)
    elif gMileage == "190 000 - 199 999":
        return gMileage.replace("190 000 - 199 999", "195000", 1)
    elif gMileage == "200 000 - 249 999":
        return gMileage.replace("200 000 - 249 999", "225000", 1)
    elif gMileage == "250 000 - 299 999":
        return gMileage.replace("250 000 - 299 999", "275000", 1)
    elif gMileage == "300 000 - 349 999":
        return gMileage.replace("300 000 - 349 999", "325000", 1)
    elif gMileagee == "350 000 - 399 999":
        return gMileage.replace("350 000 - 399 999", "375000", 1)
    elif gMileage == "400 000 - 449 999":
        return gMileage.replace("400 000 - 449 999", "425000", 1)
    elif gMileage == "450 000 - 499 999":
        return gMileage.replace("450 000 - 499 999", "475000", 1)
    else:
        return gMileage

#substituting (-) data (quantitative variable) with certain value   
def dash (a):
    if a == '-':
        return a.replace("-", "-1", 1)
    else:
        return a
    
    
for fathiah in containers:
    name = fathiah.div.div.a["title"].strip()
    price = fathiah.findAll("div", {"class":"ads_price"})
    Price = price[0].text.strip()
    year = fathiah.findAll("font", {"class":"icon_label"})
    Condition = year[0].text.strip()
    clink = fathiah.div.div.a["href"].strip()
    gMileage = year[2].text.strip()
    
    print("Name: " + name)
    print("Price: " + Price)
    print("Condition: " + Condition)
    print("Link: " + clink)
    print("Mileage: " + gMileage)
    Mil = subs(gMileage)
    f.write(name + "," + Price.replace("RM", "", 1) + "," + Condition + "," + clink + "," + gMileage + "," + Mil.strip() + ",")
    #from urllib.request import urlopen as uReq1

    #from bs4 import BeautifulSoup as soup1
    my_url1 = clink
    uClient1 = uReq(my_url1)
    page_html1 = uClient1.read()
    uClient1.close()
    #html parsing  
    page_soup1 = soup(page_html1, "html.parser")

    panel1 = page_soup1.findAll("div", {"class":"general_section"})

    #GENERAL
    for pop in panel1:
        brand = pop.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
        gBrand = brand[0].text.strip()
        #gMileage = brand[1].text.strip()
        gModel = brand[2].text.strip()
        gSeat = brand[3].text.strip()
        gVariant = brand[4].text.strip()
        gType = brand[5].text.strip()
        gSeries = brand[6].text.strip()
        gYear = brand[7].text.strip()
        gCountry = brand[8].text.strip()
        
       
        #Mil = subs(gMileage)
        print("Brand: " + gBrand)
        #print("Mileage: " + gMileage)
        print("Model: " + gModel)
        print("Seat: " + gSeat)
        print("Variant: " + gVariant)
        print("Type: " + gType)
        print("Series: " + gSeries)
        print("Manufactured Yr: " + gYear)
        print("Country: " + gCountry)
        print("newMil: " + Mil.strip())
        
        f.write(gBrand + "," + gModel + "," + gSeat + "," + gVariant + "," + gType + "," + gSeries + "," + gYear + "," + gCountry + ",")

    #TRANSMISSION
    panel2 = page_soup1.findAll("div", {"class":"transmission_section"})
    for pop2 in panel2:
        trans= pop2.findAll("div", {"class":"col-xs-9 mcd_record_adview"})
        Ttrans = trans[0].text.strip()

        print("Transmission: " + Ttrans)
        f.write(Ttrans+ ",")

    
    #ENGINE
    panel3 = page_soup1.findAll("div", {"class":"engine_section"})
    for pop3 in panel3:
        eng = pop3.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
        engCC = eng[0].text.strip()
        engCompr = eng[1].text.strip()
        engPeakPwr = eng[2].text.strip()
        engPeakTorque = eng[3].text.strip()
        engType = eng[4].text.strip()
        engFuel = eng[5].text.strip()

        print("EngineCC: " + engCC)
        print("Engine Compression: " + engCompr)
        print("Engine Peak Power: " + engPeakPwr)
        print("Engine Peak Torque: " + engPeakTorque)
        print("Engine Type: " + engType)
        print("Engine Fuel: " + engFuel)
        f.write(dash(engCC).strip() + "," + dash(engCompr).strip() + "," + dash(engPeakPwr).strip() + "," + dash(engPeakTorque).strip() + "," + engType + "," + engFuel + ",")
        

    #DIMENSION
    panel4 = page_soup1.findAll("div", {"class":"dimension_section"})
    for pop4 in panel4:
        dim = pop4.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
        dLength = dim[0].text.strip()
        dWidth = dim[1].text.strip()
        dHeight = dim[2].text.strip()
        dWheelBase = dim[3].text.strip()
        dKerbWeight = dim[4].text.strip()
        dFuelTank = dim[5].text.strip()

        print("Length: " + dLength)
        print("Width: " + dWidth)
        print("Height: " + dHeight)
        print("Wheel Base: " + dWheelBase)
        print("Kerb Weight: " + dKerbWeight)
        print("Fuel tank: " + dFuelTank)
        f.write(dash(dLength).strip() + "," + dash(dWidth).strip() + "," + dash(dHeight).strip() + "," + dash(dWheelBase).strip() + "," + dash(dKerbWeight).strip() + "," + dash(dFuelTank).strip() + ",")
        
    
    #BRAKES
    panel5 = page_soup1.findAll("div", {"class":"brakes_section"})
    for pop5 in panel5:
        b = pop5.findAll("div", {"class": "col-xs-3 mcd_record_adview"})
        bFront = b[0].text.strip()
        bRear = b[1].text.strip()

        print("Front Brake: " + bFront)
        print("Rear Brake: " + bRear)
        f.write (bFront + "," + bRear + ",")

        
    #SUSPENSIONS
    panel6 = page_soup1.findAll("div", {"class":"suspensions_section"})
    for pop6 in panel6:
        s = pop6.findAll("div", {"class": "col-xs-3 mcd_record_adview"})
        sFront = s[0].text.strip()
        sRear =  s[1].text.strip()

        print("Front Suspension: " + sFront)
        print("Rear Suspension: " + sRear)
        f.write(sFront + "," + sRear + ",")
        
        
    #STEERING
    panel7 = page_soup1.findAll("div", {"class":"steering_section"})
    for pop7 in panel7:
        st = pop7.findAll("div", {"class":"col-xs-9 mcd_record_adview"})
        sSteering = st[0].text.strip()

        print("Steering: " + sSteering)
        f.write(sSteering + ",")
        
    #TYRES
    panel8 = page_soup1.findAll("div", {"class":"tyres_section"})
    for pop8 in panel8:
        t = pop8.findAll("div", {"class":"col-xs-3 mcd_record_adview"})
        tFront = t[0].text.strip()
        tRear = t[1].text.strip()
        tFRim = t[2].text.strip()
        tRRim = t[3].text.strip()

        print("Front Tyres: " + tFront)
        print("Rear Tyres: " + tRear)
        print("Front Rim: " +tFRim)
        print("Rear rim: " +tRRim)
        f.write(tFront + "," + tRear + "," + tFRim + "," + tRRim + "\n")

    
f.close()