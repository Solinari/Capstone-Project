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
                #print(course)
                out = randomQuery(df, course, season)
                #print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(str(courseTrack))

majorAnimator(myDF)

# Major: Animation; Concentration: Technical Artist
def majorTechnicalArtist(df):
    ''' defines technical artist major requirements'''

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
    springOne =  ['ANI 446', 'GAM 691', 'ANI 444']
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
    winterTwo =  ['ANI 453', 'ANI 440', 'GE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # technical animator focus areaelective is FAE
    springYearTwo = 'Spring 2014-2015'
    springTwo =  []
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
    ''' defines Business Information Technology major requirements'''

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

#majorBusinessIT(myDF)

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

# Major: Computational Finance
def majorComputationalFinance(df):
    ''' defines Computational Finance major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #CSC 401, all quarters, none
    #CSC 404, all quarters, none
    #IT 403, all quarters, none
    #CSC 412, Fall/Winter, none
    
    #CDM foundation courses
    # CSC 423, all quarters, IT 403
    # CSC 425, Fall/Winter, CSC423 or MAT 456
    # CSC 431, Winter, CSC402 and 2 course calculus sequence
    # CSC 485, no information, MAT 220
    # NOTE: Students can take either CSC 431 or CSC 485
    # CSC 521, Spring, (CSC402 or CSC404) and CSC 423

    # Kellstadt Foundation Courses
    # ACC 500, all quarters, none
    # ECO 555, all quarters, GSB 420
    # FIN 555; all quarters; ACC 500, ECO 555, and GSB 420
    # FIN 523, all quarters, FIN 555 and GSB 420
    # FIN 525, all quarters, FIN 523
    # FIN 562, all quarters, FIN 555 and GSB 420
    # FIN 662; all quarters; FIN 523, FIN 555, and (GSB 400 or GSB 420)

    #Advanced courses, one of the three
    # CSC 695, all quarters, all foundation courses (CDM and Kellstadt)
    # CSC 697, all quarters, none
    # CSC 599, Spring, CSC 404 and (CSC 431 or CSC 521 or CSC 425)
    AC = ['CSC 695', 'CSC 697', 'CSC 599']

    #Major Elective - 1 500 lvl course at CDM, Kellstadt, or Department of math
    E = ['E']

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['ACC 500', 'ECO 555', 'IT 403']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 423', 'CSC 401', 'CSC 404']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['FIN 555', 'CSC 521', 'E']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['CSC 425', 'CSC 412', 'FIN 523']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['CSC 431', 'FIN 525', 'FIN 562']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['FIN 562', 'AC']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'AC':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'AC':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorComputationalFinance(myDF)

# Major: Computer Game Development
def majorComputerGameDev(df):
    ''' defines Computer Game Development major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #CSC 400, all quarters, none
    #CSC 401, all quarters, none
    #CSC 402, all quarters, CSC401
    #CSC 403, all quarters, CSC402
    #CSC 406, all quarters, CSC401
    #CSC 407, all quarters, CSC406 and CSC402
    
    #foundation courses
    # GAM 425, Fall, CSC 461 and CSC 403
    # CSC 461; Fall; CSC 400, CSC 403, CSC 407
    # SE 456, Winter, CSC 403
    # GPH 469; Winter; CSC 461 and GAM 425

    # Advanced Courses
    # GAM 490; Spring; CSC 461, CSC 407, (SE 456 or SE 450)
    # GAM 475, Fall, GPH 469 and (SE 456 or SE 450)
    # GAM 575, Winter, GAM 475
    # *GAM 476; Winter; CSC 461, GAM 424, (SE 456 or SE 450)
    # *GAM 450, Fall, GAM 425 and (SE 456 or SE 450)
    # *NOTE: students can take either GAM 476 or GAM 450

    #Major Elective - take 3 GAM courses 421-699
    E = ['GAM']

    #Capstone - take either 690 and 691 OR just 695
    #GAM 690, winter, GAM 475
    #GAM 691, spring, GAM 474 or SE 456
    #GAM 695, all quarters, GAM 575 and consent of teacher
    Cap = ['GAM 690', 'GAM 691', 'GAM 695']

##    # dictionaries are class names to panda queries
##    fallYearOne = 'Fall 2012-2013'
##    fallOne =  ['CSC 400', 'CSC 401', 'E']
##    fallOne = toMap(fallOne)
##    courseTrack[fallYearOne] = fallOne
##    # works
##    #print(fallOne)
##
##    winterYearOne = 'Winter 2013-2014'
##    winterOne =  ['CSC 402', 'CSC 406', 'E']
##    winterOne = toMap(winterOne)
##    courseTrack[winterYearOne] = winterOne
##
##    springYearOne = 'Spring 2013-2014'
##    springOne =  ['CSC 403', 'CSC 407', 'E']
##    springOne = toMap(springOne)
##    courseTrack[springYearOne] = springOne
##
##    fallYearTwo = 'Fall 2013-2014'
##    fallTwo =  ['GAM 425', 'CSC 461']
##    fallTwo = toMap(fallTwo)
##    courseTrack[fallYearTwo] = fallTwo
##
##    # works
##    #print(fallTwo)
##
##    winterYearTwo = 'Winter 2014-2015'
##    winterTwo =  ['SE 456', 'GPH 469']
##    winterTwo = toMap(winterTwo)
##    courseTrack[winterYearTwo] = winterTwo
##
##    springYearTwo = 'Spring 2014-2015'
##    springTwo =  ['GAM 490']
##    springTwo = toMap(springTwo)
##    courseTrack[springYearTwo] = springTwo

##    fallYearThree = 'Fall 2014-2015'
##    fallThree =  ['GAM 475', 'GAM 450']
##    fallThree = toMap(fallThree)
##    courseTrack[fallYearThree] = fallThree
##    # works
##    #print(fallThree)
##
##    winterYearThree = 'Winter 2015-2016'
##    winterThree =  ['GAM 575', 'Cap']
##    winterThreee = toMap(winterThree)
##    courseTrack[winterYearThree] = winterThree
##
##    springYearThree = 'Spring 2015-2016'
##    springThree =  ['Cap']
##    springThree = toMap(springThree)
##    courseTrack[springYearThree] = springThree

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['GAM 425', 'CSC 461', 'E']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['SE 456', 'GPH 469', 'E']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['GAM 490', 'E']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['GAM 475', 'GAM 450']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    #Note: if 'Cap' is taken (GAM 695) then GAM 690 will be dropped
    #along with GAM 691. The latter means the student won't be enrolled
    #in school in spring
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['GAM 575', 'GAM 690', 'Cap']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['GAM 691']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo

    #foundation courses

    # Advanced Courses
    # GAM 475, Fall, GPH 469 and (SE 456 or SE 450)
    # GAM 575, Winter, GAM 475
    # *GAM 476; Winter; CSC 461, GAM 424, (SE 456 or SE 450)
    # *GAM 450, Fall, GAM 425 and (SE 456 or SE 450)
    # *NOTE: students can take either GAM 476 or GAM 450

    #Capstone - take either 690 and 691 OR just 695
    #GAM 690, winter, GAM 475
    #GAM 691, spring, GAM 474 or SE 456
    #GAM 695, all quarters, GAM 575 and consent of teacher
    

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'Cap':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'Cap':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorComputerGameDev(myDF)

# Major: Computer Science
def majorComputerScience(df):
    ''' defines Computer Science major requirements'''

    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #CSC 400, all quarters, none
    #CSC 401, all quarters, none
    #CSC 402, all quarters, CSC401
    #CSC 403, all quarters, CSC402
    #CSC 406, all quarters, CSC401
    #CSC 407, all quarters, CSC406 and CSC402
    
    #foundation courses
    # CSC 421, all quarters, CSC 400 and CSC 403
    # CSC 435, all quarters, CSC 403 and CSC 407
    # CSC 447, all quarters, CSC 403 and CSC 406
    # CSC 453, all quarters, CSC 403
    # SE 450, all quarters, CSC 403

    # Major Elective Courses
    # 4 courses from one area
    # 4 courses from any area
    FAE = ['SSD', 'T', 'DS', 'DBS', 'AI', 'SoEn', 'MM']

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['CSC 400', 'CSC 401', 'E']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 402', 'CSC 406', 'E']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['CSC 403', 'CSC 407', 'E']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['GAM 425', 'CSC 461']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['SE 456', 'GPH 469']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    springYearTwo = 'Spring 2014-2015'
    springTwo =  ['GAM 490']
    springTwo = toMap(springTwo)
    courseTrack[springYearTwo] = springTwo

    fallYearThree = 'Fall 2014-2015'
    fallThree =  ['GAM 475', 'GAM 450']
    fallThree = toMap(fallThree)
    courseTrack[fallYearThree] = fallThree
    # works
    #print(fallThree)

    winterYearThree = 'Winter 2015-2016'
    winterThree =  ['GAM 575', 'Cap']
    winterThreee = toMap(winterThree)
    courseTrack[winterYearThree] = winterThree

    springYearThree = 'Spring 2015-2016'
    springThree =  ['Cap']
    springThree = toMap(springThree)
    courseTrack[springYearThree] = springThree

                
    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'Cap':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'Cap':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)

majorComputerScience(myDF)
