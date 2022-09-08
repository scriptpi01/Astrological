birthday = int(input("Input birthday :"))
month = str(input("Input month of birth (e.g. march, july etc) :"))
astrological = ''
if (month == 'january' and (birthday >= 20 and birthday <= 31)) or (month == 'february' and (birthday >= 1 and birthday <= 18)):
  astrological = "Aquarius"
elif (month == 'february' and (birthday >= 19 and birthday <= 29)) or (month == 'march' and (birthday >= 1 and birthday <= 20)):
  astrological = "Pisces"
elif (month == 'march' and (birthday >= 21 and birthday <= 31)) or (month == 'april' and (birthday >= 1 and birthday <= 19)):
  astrological = "Aires"
elif (month == 'april' and (birthday >= 20 and birthday <= 30)) or (month == 'may' and (birthday >= 1 and birthday <= 20)):
  astrological = "Taurus"
elif (month == 'may' and (birthday >= 21 and birthday <= 31)) or (month == 'june' and (birthday >= 1 and birthday <= 21)):
  astrological = "Gemini"
elif (month == 'june' and (birthday >= 22 and birthday <= 30)) or (month == 'july' and (birthday >= 1 and birthday <= 22)):
  astrological = "Cancer"
elif (month == 'july' and (birthday >= 23 and birthday <= 31)) or (month == 'august' and (birthday >= 1 and birthday <= 22)):
  astrological = "Leo"
elif (month == 'august' and (birthday >= 23 and birthday <= 31)) or (month == 'september' and (birthday >= 1 and birthday <= 22)):
  astrological = "Virgo"
elif (month == 'september' and (birthday >= 23 and birthday <= 30)) or (month == 'october' and (birthday >= 1 and birthday <= 23)):
  astrological = "Libra"
elif (month == 'october' and (birthday >= 24 and birthday <= 31)) or (month == 'november' and (birthday >= 1 and birthday <= 21)):
  astrological = "Scorpius"
elif (month == 'november' and (birthday >= 22 and birthday <= 30)) or (month == 'december' and (birthday >= 1 and birthday <= 21)):
  astrological = "Sagittarius"
elif (month == 'december' and (birthday >= 22 and birthday <= 31)) or (month == 'january' and (birthday >= 1 and birthday <= 19)):
  astrological = "Capricornus"
else:
  print("Please try again")
  astrological = "Error"
print("%s %s"%("Your Astrological sign is :", astrological))