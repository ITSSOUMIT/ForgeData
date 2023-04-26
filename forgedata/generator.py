import random
import pandas as pd
from importlib import resources
import io
import string

def name(type, quantity, gender='all'):
    allowedTypes = ['firstname', 'lastname', 'fullname']
    allowedGender = ['male', 'female', 'all']
    if type not in allowedTypes:
        raise ValueError("Invalid type. Allowed types are: firstname, lastname, fullname")
    elif gender not in allowedGender:
        raise ValueError("Invalid gender. Allowed types are: male, female, all")
    else:
        
        # first name
        if type=='firstname':
            
            # male
            if gender=='male':
                if quantity>100:
                    raise ValueError("Quantity cannot be greater than 100")
                else:
                    with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
                        df = pd.read_csv(io.BytesIO(fp.read()), header=None)
                        fp.close()
                    sollist = df[df.columns[0]].tolist()
                    return random.sample(sollist, quantity)
            
            # female
            elif gender=='female':
                if quantity>100:
                    raise ValueError("Quantity cannot be greater than 100")
                else:
                    with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
                        df = pd.read_csv(io.BytesIO(fp.read()), header=None)
                        fp.close()
                    sollist = df[df.columns[0]].tolist()
                    return random.sample(sollist, quantity)
            
            # all
            else:
                if quantity>200:
                    raise ValueError("Quantity cannot be greater than 200")
                else:
                    with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
                        dfmale = pd.read_csv(io.BytesIO(fp.read()), header=None)
                        fp.close()
                    with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
                        dffemale = pd.read_csv(io.BytesIO(fp.read()), header=None)
                        fp.close()
                    dfall = pd.concat([dfmale, dffemale])
                    sollist = dfall[dfall.columns[0]].tolist()
                    return random.sample(sollist, quantity)
                
        # last name                
        elif type=='lastname':
            if quantity>150:
                raise ValueError("Quantity cannot be greater than 150")
            else:
                with resources.open_binary('forgedata', 'lastname.csv') as fp:
                    df = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                sollist = df[df.columns[0]].tolist()
                return random.sample(sollist, quantity)
        
        # full name
        else:

            # male
            if gender=='male':
                with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
                    dfmale = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                with resources.open_binary('forgedata', 'lastname.csv') as fp:
                    dflast = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                dfmerge = dfmale.merge(dflast, how='cross')
                sollist = random.sample(dfmerge.values.tolist(), quantity)
                for i in range(len(sollist)):
                    sollist[i] = ' '.join(sollist[i])
                return sollist
            
            # female
            elif gender=='female':
                with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
                    dffemale = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                with resources.open_binary('forgedata', 'lastname.csv') as fp:
                    dflast = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                dfmerge = dffemale.merge(dflast, how='cross')
                sollist = random.sample(dfmerge.values.tolist(), quantity)
                for i in range(len(sollist)):
                    sollist[i] = ' '.join(sollist[i])
                return sollist
            
            # all
            else:
                with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
                    dfmale = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
                    dffemale = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                dfall = pd.concat([dfmale, dffemale])
                with resources.open_binary('forgedata', 'lastname.csv') as fp:
                    dflast = pd.read_csv(io.BytesIO(fp.read()), header=None)
                    fp.close()
                dfmerge = dfall.merge(dflast, how='cross')
                sollist = random.sample(dfmerge.values.tolist(), quantity)
                for i in range(len(sollist)):
                    sollist[i] = ' '.join(sollist[i])
                return sollist
            

def email(quantity, domain=None):
    # no specific domains
    if domain==None:
        with resources.open_binary('forgedata', 'domains.csv') as fp:
            dfdomain = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
            dfmale = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
            dffemale = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        dfall = pd.concat([dfmale, dffemale])
        dfmerge = dfall.merge(dfdomain, how='cross')
        sollist = random.sample(dfmerge.values.tolist(), quantity)
        for i in range(len(sollist)):
            sollist[i] = '@'.join(sollist[i])
            sollist[i] = sollist[i].lower()
        return sollist
    
    # only common domains
    elif domain=='common':
        domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        dfdomain = pd.DataFrame(domain)
        with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
            dfmale = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
            dffemale = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        dfall = pd.concat([dfmale, dffemale])
        dfmerge = dfall.merge(dfdomain, how='cross')
        sollist = random.sample(dfmerge.values.tolist(), quantity)
        for i in range(len(sollist)):
            sollist[i] = '@'.join(sollist[i])
            sollist[i] = sollist[i].lower()
        return sollist
    
    # specific domain list
    elif type(domain)==list:
        dfdomain = pd.DataFrame(domain)
        with resources.open_binary('forgedata', 'firstname-male.csv') as fp:
            dfmale = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        with resources.open_binary('forgedata', 'firstname-female.csv') as fp:
            dffemale = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        dfall = pd.concat([dfmale, dffemale])
        dfmerge = dfall.merge(dfdomain, how='cross')
        sollist = random.sample(dfmerge.values.tolist(), quantity)
        for i in range(len(sollist)):
            sollist[i] = '@'.join(sollist[i])
            sollist[i] = sollist[i].lower()
        return sollist
    
    # everything else
    else:
        raise ValueError("Invalid domain. Allowed types are: None, common, list")

    
def website(quantity, domain=None, www=False):
    # no specific domains
    if domain==None:
        with resources.open_binary('forgedata', 'domains.csv') as fp:
            dfdomain = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        with resources.open_binary('forgedata', 'domains-common.csv') as fp:
            dfdomaincommons = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        dfall = pd.concat([dfdomain, dfdomaincommons])
        sollist = dfall[dfall.columns[0]].tolist()
        if www==True:
            toappend = 'www.'
            return random.sample([toappend + s for s in sollist], quantity)
        else:
            return random.sample(sollist, quantity)
    
    # only common domains
    elif domain=='common':
        with resources.open_binary('forgedata', 'domains-common.csv') as fp:
            dfdomain = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        sollist = dfdomain[dfdomain.columns[0]].tolist()
        if www==True:
            toappend = 'www.'
            return random.sample([toappend + s for s in sollist], quantity)
        else:
            return random.sample(sollist, quantity)
    
    # throw exception
    else:
        raise ValueError("Invalid domain. Allowed types are: None, common")
    

def phone(quantity):
    sol = []
    for i in range(quantity):
        first = str(random.randint(100,999))
        second = str(random.randint(1,888)).zfill(3)

        last = (str(random.randint(1,9998)).zfill(4))
        while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
            last = (str(random.randint(1,9998)).zfill(4))
        num = f'{first}{second}{last}'
        sol.append(int(num))
    return sol


def country(quantity='all', countrycode=False):
    # all countries
    if quantity=='all':
        with resources.open_binary('forgedata', 'countries.csv') as fp:
            dfcountry = pd.read_csv(io.BytesIO(fp.read()), header=None)
            fp.close()
        templist = dfcountry[dfcountry.columns[0]].tolist()
        if countrycode==False:
            sollist = [i[3:] for i in templist]
            return sollist
        else:
            soldict = {}
            for i in range(len(templist)):
                code = templist[i][0:2]
                countryname = templist[i][3:]
                soldict[code] = countryname
            return list(soldict.items())
        
    # fixed quantity
    else:
        if quantity>241:
            raise ValueError("Quantity cannot be greater than 241.")
        else:
            with resources.open_binary('forgedata', 'countries.csv') as fp:
                dfcountry = pd.read_csv(io.BytesIO(fp.read()), header=None)
                fp.close()
            templist = dfcountry[dfcountry.columns[0]].tolist()
            if countrycode==False:
                sollist = [i[3:] for i in templist]
                return random.sample(sollist, quantity)
            else:
                soldict = {}
                for i in range(len(templist)):
                    code = templist[i][0:2]
                    countryname = templist[i][3:]
                    soldict[code] = countryname
                return random.sample(list(soldict.items()), quantity)


def password(quantity, length, difficulty="hard"):
    allowedDifficulty = ['easy', 'medium', 'hard']
    if difficulty not in allowedDifficulty:
        raise ValueError("Difficulty must be 'easy', 'medium', or 'hard'.")
    else:
        if difficulty == "easy":
            password_characters = string.ascii_letters
        elif difficulty == "medium":
            password_characters = string.ascii_letters + string.digits
        elif difficulty == "hard":
            password_characters = string.ascii_letters + string.digits + string.punctuation
        
        if quantity==1:
            return "".join(random.choice(password_characters) for _ in range(length))
        else:
            sollist = []
            for i in range(quantity):
                sollist.append("".join(random.choice(password_characters) for _ in range(length)))
            return sollist