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
    if "Empty DataFrame" in out:
        return "COURSE NOT FOUND, SEE ADVISOR"

    return out


# test open
myDF = OpenCSV2DF('Catalog.csv')

randomQuery(myDF, 'ANI 423', 'Fall 2012-2013')

# may need a dict instantiator helper function

def toMap(classes):
    '''maps an array of classnames to dictionary'''

    return dict.fromkeys(classes, None)

# Major: Animation; Concentration: Animator
def majorAnimator(df):
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

#majorAnimator(myDF)

# Major: Animation; Concentration: Technical Artist
def majorTechnicalArtist(df):
    ''' defines animation major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # Focus Area Electives - 4 courses; (recommended one of the areas of focus)
    FAE = ['RFA','AFA','MFA','EFA']
    RFA = ['ANI 430', 'ANI 432', 'ANI 433', 'ANI 435', 'ANI 450']
    AFA = ['ANI 450', 'ANI 451', 'ANI 430', 'ANI 431', 'ANI 432']
    MFA = ['ANI 435', 'ANI 436', 'ANI 437', 'ANI 438', 'ANI 439']
    EFA = ['ANI 478', 'ANI 479', 'VFX 478', 'DC 430']
    Other = ['GAM 690', 'GAM 691']

    # General Electives - GRAD COURSES (400+)
    GE = ['ANI', 'CNS', 'CSC', 'DC', 'DMA', 'ECT', 'EXP',
          'GAM', 'GD', 'GPH', 'HCD', 'HCI', 'HIT', 'ILL',
          'IM', 'IS', 'ISM', 'IT', 'LSP', 'PM', 'SAP',
          'SE', 'TDC', 'TV','VFX']

    # Core requirements
    # take either GAM 690+GAM 691 OR take just ANI 440
    C = ['ANI 423', 'ANI 446', 'ANI 452', 'ANI 453',
         'ANI 444', 'GAM 690', 'GAM 691', 'ANI 440']
    #FALL -423*,[452*: prereq = ANI 405]

    #WINTER - [690*: prereq = GAM 475]

    #SPRING - [446*: prereq = ANI 405], 444*,
    #[691*: prereq = GAM 474 or SE 456], 440

    #NOT OFFERED - 453

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne = ['ANI 423', 'FAE', 'GE']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # technical animator focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['GAM 690', 'FAE','FAE']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # technical animator focus area elective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['ANI 446', 'GAM 691']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # technical animator elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['ANI 452', 'GE', 'FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # technical animator focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['GE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # technical animator focus areaelective is FAE
    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['ANI 444']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo



    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'GE' and course != 'FAE':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'GE':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

#majorTechnicalArtist(myDF)

# Major: Business Information Technology
def majorBusinessIT(df):
    ''' defines animation major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # 2 Open Electives, range 421-699
    E = ['CNS', 'CSC', 'ECT', 'GAM', 'GPH', 'HCI',
           'HIT', 'IPD', 'IS', 'IT', 'PM', 'SE', 'TDC']

    # capstone, one of the three choices
    #IS - winter, PM - Spring, ECT - Fall
    CAP = ['IS 577', 'PM 577', 'ECT 589']

    # CDM required courses
    #AVAILABLE ALL QUARTERS - IS 421, PM 430, CNS 440, ECT 424, HCI 440

    #Kellstadt Required
    #AVAILABLE ALL QUARTERS - ACC 500, MKT 555, MGT 500, MGT 504*, MGT 554*, MGT 573
    # (*) denotes 2 credit hour class
    # Prereqs - MGT 504: GSB 420; MGT 554: MGT 500

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['IS 421', 'ACC 500', 'MGT 555']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # animation focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['PM 430', 'CNS 440', 'MGT 500']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # animation focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['ECT 424', 'MGT 504', 'MGT 554']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # animation elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['HCI 440', 'MGT 573', 'E']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # animation focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['E', 'CAP']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # animation focus areaelective is FAE
    #springYearTwo = 'Spring 2014-2015'
    #springTwo =  []
    #springTwo = toMap(springTwo)
    #courseTrack[springYearTwo] = springTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'CAP':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'CAP':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorBusinessIT(myDF)

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

#majorProduction(myDF)

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

#majorPostProduction(myDF)

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

#majorSound(myDF)
