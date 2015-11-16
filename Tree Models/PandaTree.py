# for pandas
import pandas as pd

# Open method, query demonstration

def OpenCSV2DF(file):
    '''opens a csv file
       returns it as a dataframe'''
    df = pd.read_csv(file)
    return df


# structure is:
# Dataframe[Dataframe[column] == condition]
# casting this as a string returns it as a string
# normally it is a dataframe object

def randomQuery(df, myClass, mySeason):
    ''' Test querying from class and season with .sample()'''
    #this returns a dataframe cast to a string
    out = str(df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)])
    #print(out)
    # if empty
    if df.empty:
        return "COURSE NOT FOUND, SEE ADVISOR"

    return out


# test open
myDF = OpenCSV2DF('Catalog.csv')

randomQuery(myDF, 'ANI 423', 'Fall 2012-2013')

# may need a dict instantiator helper function

def toMap(classes):
    '''maps an array of classnames to dictionary'''

    return dict.fromkeys(classes, None)

def majorAnimation(df):
    ''' defines animation major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # Focus Area Electives
    FAE = ['ANI 430', 'ANI 431', 'ANI 432', 'ANI 433',
            'ANI 435', 'ANI 436', 'ANI 438', 'ANI 439',
            'ANI 445', 'ANI 450', 'ANI 451', 'ANI 452',
            'ANI 453', 'ANI 478', 'ANI 420', 'ANI 427',
            'ANI 455', 'ANI 456', 'ANI 457','ANI 470', 'ANI 490']

    # general elective choices
    E = ['ANI', 'DC', 'GAM', 'GD', 'GPH', 'HCI', 'VFX']

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['ANI 423','ANI 460','ANI 421']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # animation focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['ANI 425','ANI 422','FAE']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # 466 can be 444
    # animation focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['ANI 440','ANI 466','FAE']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # animation elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['ANI 540','FAE','E']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # animation focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['ANI 541','FAE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # 466 can be 444
    # animation focus areaelective is FAE
    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['FAE','FAE','FAE']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo



    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'FAE':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorAnimation(myDF)

def majorProduction(df):
    ''' defines production major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # Focus Area Electives. Need 7 of these
    FAE = ['ANI', 'DC', 'VFX']

    # Exclude these classes for FAE
    Exclude = ['DC 401', 'DC 423', 'DC 476', 'DC 495',
                'DC 565', 'DC 566', 'DC 567', 'DC 568']

    # general elective choices
    E = []

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['DC 409']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # major focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['DC 461','DC 420']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # major focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['DC 462','DC 475']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # major elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['FAE','FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # major focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['FAE','FAE','FAE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # major focus areaelective is FAE
    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['FAE','FAE']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo



    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'FAE':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorProduction(myDF)

def majorPostProduction(df):
    ''' defines post production major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # Focus Area Electives. Need 3 of these
    FAE = ['ANI', 'DC', 'VFX']

    # Exclude these classes for FAE
    Exclude = ['DC 401', 'DC 423', 'DC 476', 'DC 495',
                'DC 565', 'DC 566', 'DC 567', 'DC 568']

    # general elective choices
    E = []

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['DC 409']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # major focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['DC 461','DC 420']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # major focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['DC 462','DC 475']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # major elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['DC 415','DC 422','FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # major focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['DC 425','FAE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # major focus areaelective is FAE
    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['DC 440','FAE']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo



    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'FAE':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorPostProduction(myDF)

def majorSound(df):
    ''' defines sound major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # Focus Area Electives. Need 2 of these
    FAE = ['ANI', 'DC', 'VFX']

    # Exclude these classes for FAE
    Exclude = ['DC 401', 'DC 423', 'DC 476', 'DC 495',
                'DC 565', 'DC 566', 'DC 567', 'DC 568']

    # general elective choices
    E = []

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['DC 409']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # major focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['DC 461','DC 420']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # major focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['DC 415','DC 491']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # major elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['DC 412','DC 419','FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # major focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['DC 417','FAE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # major focus areaelective is FAE
    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['DC 413','DC 418']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo



    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'FAE':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorSound(myDF)
