from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = (today.year - birthDate.year - 
           ((today.month, today.day) < (birthDate.month, birthDate.day)))
 
    return age

def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # 👇️ preserve calendar day (if Feb 29th doesn't exist, set to 28th)
        return start_date.replace(year=start_date.year + years, day=28)

def generatePESEL(id):
    return id + 10**11