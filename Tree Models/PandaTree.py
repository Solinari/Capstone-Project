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
    pd.set_option('expand_frame_repr', False)
    out = str(df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)])
    #print(out)
    # if empty
    if "Empty DataFrame" not in out:
        out = df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)].sample()
        # stillis dataframe. converty to list
        out = out.values.T.tolist()
        #print(out)
        return out

    if "Empty DataFrame" in out:
        return "COURSE NOT FOUND, SEE ADVISOR"

def faeQuery(df, myClass, mySeason):
    '''Test querying for the focus area electives'''
    pd.set_option('expand_frame_repr', False)
    output = str(df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)])
    #print(output)
    if "Empty DataFrame" not in output:
         output = df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)].sample()
         output = output.values.T.tolist()
         return output

    if "Empty DataFrame" in output:
         return "COURSE NOT FOUND, SEE ADVISOR"
    #return output

def eQuery(df, myClass, mySeason):
    '''Test querying for the general electives'''
    pd.set_option('expand_frame_repr', False)
    outputE = str(df[(df['Class Name'].str.contains(myClass)) & (df['Season'] == mySeason)])
    #print(outputE)
    # if "Empty DataFrame" not in outputE:
    #      outputE = df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)].sample()
    #      outputE = outputE.values.T.tolist()
    #      return outputE

    if "Empty DataFrame" in outputE:
         return "COURSE NOT FOUND, SEE ADVISOR"
    return outputE
# one dataframe that all majors can read from
myDF = OpenCSV2DF('Catalog.csv')

def returnDataFrame():
    '''returns global view of dataframe'''

    global myDF
    return myDF

#randomQuery(myDF, 'ANI 423', 'Fall 2012-2013')

# may need a dict instantiator helper function

def toMap(classes):
    '''maps an array of classnames to dictionary'''

    return dict.fromkeys(classes, None)

# Major: Animation; Concentration: Animator
def majorAnimator():
    ''' defines animation major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    usedFAE = []
    usedClasses = []
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
        #print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'FAE':
                #print(course)
                out = randomQuery(df, course, season)
                #print(out)
                courseTrack[season][course] = out
                usedClasses.append(course)

            if course == 'E':
                for short in E:
                    outputE = eQuery(df, short, season)
                    print(outputE)
                    if "COURSE NOT FOUND, SEE ADVISOR" not in outputE:
                        break
                courseTrack[season][course] = outputE
                usedClasses.append(short)

            if course == 'FAE':
                for item in FAE:
                    if item not in usedFAE:
                        output = faeQuery(df, item, season)
                        if "COURSE NOT FOUND, SEE ADVISOR" not in output:
                            usedFAE.append(item)
                            break
                #print(output)
                courseTrack[season][course] = output
                usedClasses.append(item)


    # works
    return str(courseTrack)



# Major: Animation; Concentration: Technical Artist
def majorTechnicalArtist():
    ''' defines technical artist major requirements'''

    df = returnDataFrame()
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
    return str(courseTrack)



# Major: Business Information Technology
def majorBusinessIT():
    ''' defines Business Information Technology major requirements'''

    df = returnDataFrame()
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
    return str(courseTrack)



def majorProduction():
    ''' defines production major requirements'''

    df = returnDataFrame()
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
    return str(courseTrack)



def majorPostProduction():
    ''' defines post production major requirements'''

    df = returnDataFrame()
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
    return str(courseTrack)



def majorSound():
    ''' defines sound major requirements'''

    df = returnDataFrame()
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
    return str(courseTrack)



# Major: Computational Finance
def majorComputationalFinance():
    ''' defines Computational Finance major requirements'''

    df = returnDataFrame()
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
    return str(courseTrack)



# Major: Computer Game Development
def majorComputerGameDev():
    ''' defines Computer Game Development major requirements'''

    df = returnDataFrame()
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
##    winterThree = toMap(winterThree)
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
    return str(courseTrack)



# Major: Computer Science
def majorComputerScience():
    ''' defines Computer Science major requirements'''

    df = returnDataFrame()
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
    SSD = ['CSC 436', 'CSC 438', 'CSC 439', 'CSC 443', 'CSC 448',
           'CSC 461', 'CSC 462', 'CSC 471', 'CSC 472', 'CSC 475',
           'CSC 548', 'CSC 549', 'CSC 551', 'CSC 553', 'CSC 536',
           'CSC 540', 'CSC 534', 'CSC 552', 'HCI 441', 'SE 560',
           'SE 452', 'SE 459', 'SE 525', 'SE 526', 'SE 554',
           'CNS 450', 'SE 491', 'SE 591', 'GAM 690', 'GAM 691',
           'TDC 478', 'TDC 484', 'TDC 568']
    T = ['CSC 431', 'CSC 440', 'CSC 444', 'CSC 489', 'CSC 503',
         'CSC 521', 'CSC 525', 'CSC 531', 'CSCS 535', 'CSC 557',
         'CSC 547', 'CSC 580', 'CSC 591', 'SE 533']
    DS = ['CSC 423', 'CSC 424', 'CSC 425', 'CSC 428', 'CSC 433',
          'CSCS 465', 'CSC 478', 'CSC 481', 'CSC 482', 'CSC 495',
          'CSC 529', 'CSC 555', 'CSC 575', 'CSC 578', 'ECT 584', 'IS 467']
    DBS = ['CSC 433', 'CSC 452', 'CSC 454', 'CSC 478', 'CSC 529', 'CSC 543',
           'CSC 549', 'CSC 551', 'CSC 553', 'CSC 554', 'CSC 555', 'CSC 575', 'CSC 589']
    AI = ['CSC 457', 'CSC 458', 'CSC 478', 'CSC 480', 'CSC 583', 'CSC 495',
          'CSC 575', 'CSC 528', 'CSC 578', 'CSC 582', 'CSC 587', 'CSC 594',
          'CSC 481', 'CSC 538', 'CSC 482', 'CSC 529', 'CSC 576', 'CSC 592',
          'ECT 584', 'GEO 441', 'GEO 442', 'IS 467']
    SoEn = ['SE 430', 'SE 433', 'SE 453', 'SE 459', 'SE 457', 'SE 475',
            'SE 477', 'SE 480', 'SE 482', 'SE 525', 'SE 526', 'SE 533',
            'SE 529', 'SE 546', 'SE 549', 'SE 579', 'SE 581', 'SE 582']
    MM = ['GAM 450', 'CSC 461', 'GAM 453', 'GAM 474', 'GAM 475', 'GAM 476',
          'GAM 477', 'GAM 486', 'GAM 490', 'GAM 575', 'GAM 690', 'GAM 691',
          'GPH 436', 'GPH 469', 'GPH 570', 'GPH 572', ]

    # dictionaries are class names to panda queries
##    fallYearOne = 'Fall 2012-2013'
##    fallOne =  ['CSC 400', 'CSC 401', 'FAE']
##    fallOne = toMap(fallOne)
##    courseTrack[fallYearOne] = fallOne
##    # works
##    #print(fallOne)
##
##    winterYearOne = 'Winter 2013-2014'
##    winterOne =  ['CSC 402', 'CSC 406', 'FAE']
##    winterOne = toMap(winterOne)
##    courseTrack[winterYearOne] = winterOne
##
##    springYearOne = 'Spring 2013-2014'
##    springOne =  ['CSC 403', 'CSC 407', 'FAE']
##    springOne = toMap(springOne)
##    courseTrack[springYearOne] = springOne
##
##    fallYearTwo = 'Fall 2013-2014'
##    fallTwo =  ['CSC 421', 'CSC 435', 'CSC 447']
##    fallTwo = toMap(fallTwo)
##    courseTrack[fallYearTwo] = fallTwo
##
##    # works
##    #print(fallTwo)
##
##    winterYearTwo = 'Winter 2014-2015'
##    winterTwo =  ['CSC 453', 'SE 450', 'FAE']
##    winterTwo = toMap(winterTwo)
##    courseTrack[winterYearTwo] = winterTwo
##
##    springYearTwo = 'Spring 2014-2015'
##    springTwo =  ['FAE', 'FAE', 'FAE']
##    springTwo = toMap(springTwo)
##    courseTrack[springYearTwo] = springTwo
##
##    fallYearThree = 'Fall 2014-2015'
##    fallThree =  ['FAE']
##    fallThree = toMap(fallThree)
##    courseTrack[fallYearThree] = fallThree
##    # works
##    #print(fallThree)
##
##    winterYearThree = 'Winter 2015-2016'
##    winterThree =  ['', '', '']
##    winterThree = toMap(winterThree)
##    courseTrack[winterYearThree] = winterThree
##
##    springYearThree = 'Spring 2015-2016'
##    springThree =  ['', '', '']
##    springThree = toMap(springThree)
##    courseTrack[springYearThree] = springThree

    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['CSC 421', 'FAE', 'FAE']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne

    # works
    #print(fallTwo)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 453', 'FAE', 'FAE']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['CSC 447', 'FAE', 'FAE']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['SE 450', 'FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo
    # works
    #print(fallThree)

    winterYearTwo = 'Winter 2014-20155'
    winterTwo =  ['FAE', 'CSC 435']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo


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
    return str(courseTrack)



# Major: Computer, Information and Network Security
# Concentration: Computer Security
def majorComputerSecurity():
    ''' defines Computer Security major requirements'''

    df = returnDataFrame()
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
    # CSC 435, all quarters, CSC 403 and CSC 407
    # SE 450, all quarters, CSC 403
    # TDC 477, all quarters, TDC 463 or CSC 435
    # CNS 440, all quarters, none
    # CNS 450, fall, CSC 403 and CSC 406

    # Advanced Courses
    # CSC 439, all quarters, CSC 407

    # complete 2 of the 4
    # CSC 440, winter, CSC 403
    # SE 525, winter, CSC 435 and SE 450
    # SE 526, winter, CSC 435
    # TDC 577, fall/spring, TDC 477 or TDC 572
    take2 = ['CSC 440', 'SE 525', 'SE 526', 'TDC 577']

    # complete 1 of the following (not counting courses taken to satisfy
    # requirements above)
    take1 = ['CNS 477', 'CSC 440', 'SE 482', 'SE 525', 'SE 526',
             'SE 529', 'CSC 536', 'CSC 557', 'TDC 577']

    #Major Elective Courses
    # Complete 1 CINS course 421+ OR a course from list
    ME = ['ACC 500', 'ACC 541', 'ACC 547', 'CSC 439', 'CSC 440', 'CSC 536',
         'CSC 557', 'ECT 582', 'IS 421', 'IS 444', 'IS 505', 'IS 506', 'SE 430',
         'SE 482', 'SE 525', 'SE 526', 'SE 529', 'TDC 468', 'TDC 511', 'TDC 560',
         'TDC 562', 'TDC 563', 'TDC 567', 'TDC 568', 'TDC 577']

    # 2 open electives in the range 421-699
    OE = [ 'CSC', 'CNS', 'TDC', 'SE', 'IS', 'ECT',
           'IT', 'PM', 'IPD', 'HIT', 'HCI', 'GAM']

    #capstone, 1 of the following
    # CNS 594, winter/spring, TDC 477 or CNS 533
    # CSC 695, winter/spring, all foundation courses
    # CSC 698, fall/spring, successful defense of a thesis
    CAP = ['CNS 594', 'CSC 695', 'CSC 698']

    #list of all elective courses required
    #ME, TAKE1 - take 1 course
    #OE, TAKE2 - take 2 courses
    #TOTAL OF 6
    FAE = ['take1', 'take2', 'ME', 'OE']

    # dictionaries are class names to panda queries
##    fallYearOne = 'Fall 2012-2013'
##    fallOne =  ['CSC 400', 'CSC 401', 'FAE']
##    fallOne = toMap(fallOne)
##    courseTrack[fallYearOne] = fallOne
##    # works
##    #print(fallOne)
##
##    winterYearOne = 'Winter 2013-2014'
##    winterOne =  ['CSC 402', 'CSC 406', 'FAE']
##    winterOne = toMap(winterOne)
##    courseTrack[winterYearOne] = winterOne
##
##    springYearOne = 'Spring 2013-2014'
##    springOne =  ['CSC 403', 'CSC 407', 'FAE']
##    springOne = toMap(springOne)
##    courseTrack[springYearOne] = springOne
##
##    fallYearTwo = 'Fall 2013-2014'
##    fallTwo =  ['CSS 435', 'SE 450', 'CNS 450']
##    fallTwo = toMap(fallTwo)
##    courseTrack[fallYearTwo] = fallTwo
##
##    # works
##    #print(fallTwo)
##
##    winterYearTwo = 'Winter 2014-2015'
##    winterTwo =  ['CSC 439', 'TDC 477', 'FAE']
##    winterTwo = toMap(winterTwo)
##    courseTrack[winterYearTwo] = winterTwo
##
##    springYearTwo = 'Spring 2014-2015'
##    springTwo =  ['CNS 440', 'FAE', 'FAE']
##    springTwo = toMap(springTwo)
##    courseTrack[springYearTwo] = springTwo
##
##    fallYearThree = 'Fall 2014-2015'
##    fallThree =  ['FAE', 'FAE', 'FAE']
##    fallThree = toMap(fallThree)
##    courseTrack[fallYearThree] = fallThree
##    # works
##    #print(fallThree)
##
##    winterYearThree = 'Winter 2015-2016'
##    winterThree =  ['CAP']
##    winterThree = toMap(winterThree)
##    courseTrack[winterYearThree] = winterThree

    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['CSS 435', 'SE 450', 'CNS 450']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne

    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 439', 'TDC 477', 'FAE']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['CNS 440', 'FAE', 'FAE']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['FAE', 'FAE',]
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['FAE', 'CAP']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'CAP' and course != 'FAE':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'CAP':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    return str(courseTrack)



# Major: Computer, Information and Network Security
# Concentration: Governance, Risk Management and Compliance
def majorGovtRiskMgmtCompl():
    ''' defines Governance, Risk Management
    and Compliance major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #IT 403, all quarters, none
    #TDC 411, fall/winter, none
    #CNS 418, winter, TDC 411

    #foundation courses
    # CSC 451, all quarters, none
    # CNS 477, fall/winter, CNS 440 or IS 433
    # CNS 440, all quarters, none
    # IS 444, fall/spring, none
    # IS 505, all quarters, none

    # Advanced Courses - 3 ACs
    AC = ['CSC 487', 'CNS 533', 'IS 560']

    # complete 1 of the folowing
    # CNS 490, spring, CNS 440
    # IS 430, all quarters, none
    # IS 483, winter, completion of 5+ SoC MS lvl courses
    take1 = ['CNS 490', 'IS 430', 'IS 483']

    #Major Elective Courses
    # Complete 2 CINS courses 421+ OR 2 courses from list
    ME = ['ACC 500', 'ACC 541', 'ACC 547', 'CSC 439', 'CSC 440', 'CSC 536',
         'CSC 557', 'ECT 582', 'IS 421', 'IS 444', 'IS 505', 'IS 506', 'SE 430',
         'SE 482', 'SE 525', 'SE 526', 'SE 529', 'TDC 468', 'TDC 511', 'TDC 560',
         'TDC 562', 'TDC 563', 'TDC 567', 'TDC 568', 'TDC 577']

    # 1 open elective in the range 421-699
    OE = [ 'CSC', 'CNS', 'TDC', 'SE', 'IS', 'ECT',
           'IT', 'PM', 'IPD', 'HIT', 'HCI', 'GAM']

    #capstone, 1 of the following
    # CNS 594, winter/spring, TDC 477 or CNS 533
    # CSC 695, winter/spring, all foundation courses
    # CSC 698, fall/spring, successful defense of a thesis
    CAP = ['CNS 594', 'CSC 695', 'CSC 698']

    #list of all elective courses required
    #ME - take 2 courses
    #OE, take1 - take 1
    #TOTAL 4 FAEs
    FAE = ['take1', 'ME', 'OE']

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['CSC 451', 'CNS 440', 'IS 444']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 477', 'IS 505', 'AC']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['AC', 'FAE', 'FAE']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['AC', 'FAE', 'FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['CAP']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'CAP' and course != 'FAE' and course != 'AC':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'CAP':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'AC':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    return str(courseTrack)


# Major: Computer, Information and Network Security
# Concentration: Network Security
def majorNetworkSecurity():
    ''' defines Network Security major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #TDC 411, fall/winter, none
    #TDC 413, all quarters, none
    #TDC 405, all quarters, none
    #CNS 418, winter, TDC 411

    #foundation courses
    # TDC 460, all quarters, TDC 405 and TD 413
    # TDC 463, all quarters, TDC 405 and TD 413
    # TDC 477, all quarters, TDC 463 or CSC 435
    # CNS 477, fall/winter, CNS 440 or IS 433
    # CNS 440, all quarters, none

    #Advanced Courses, take all 3 ACs
    #prereqs - must finish TDC 460, TD 463, and TDC 477
    AC = ['TDC 511', 'TDC 563', 'TDC 577']

    # complete 1 of the folowing
    take1 = ['TDC 468', 'TDC 562', 'TDC 567', 'TDC 560', 'TDC 568']

    #Major Elective Courses
    # Complete 1 CINS course 421+ OR 1 course from list
    ME = ['ACC 500', 'ACC 541', 'ACC 547', 'CSC 439', 'CSC 440', 'CSC 536',
         'CSC 557', 'ECT 582', 'IS 421', 'IS 444', 'IS 505', 'IS 506', 'SE 430',
         'SE 482', 'SE 525', 'SE 526', 'SE 529', 'TDC 468', 'TDC 511', 'TDC 560',
         'TDC 562', 'TDC 563', 'TDC 567', 'TDC 568', 'TDC 577']

    # 2 open electiveS in the range 421-699
    OE = [ 'CSC', 'CNS', 'TDC', 'SE', 'IS', 'ECT',
           'IT', 'PM', 'IPD', 'HIT', 'HCI', 'GAM']

    #capstone, 1 of the following
    # CNS 594, winter/spring, TDC 477 or CNS 533
    # CSC 695, winter/spring, all foundation courses
    # CSC 698, fall/spring, successful defense of a thesis
    CAP = ['CNS 594', 'CSC 695', 'CSC 698']

    #list of all elective courses required
    #OE - take 2 courses
    #ME, take1 - take 1
    #TOTAL 4 FAEs
    FAE = ['take1', 'ME', 'OE']

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['TDC 460', 'TDC 463', 'CNS 440']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['TDC 477', 'CNS 477', 'FAE']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['AC', 'FAE', 'FAE']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['AC', 'AC', 'FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['CAP']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'CAP' and course != 'FAE' and course != 'AC':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'CAP':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'AC':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    return str(courseTrack)


# Major: Digital Communication and Media Arts
def majorMediaArts():
    ''' defines Digital Communication and Media Arts major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #DC 414, fall, none
    #DMA 405, fall, none

    #foundation courses
    # CMNS 570, fall, none
    # DMA 527, winter, none
    # DMA 525, winter, none
    # MCS 575, spring, none

    #Advanced Courses - take both classes
    #DMA 555 must be taken twice, winter, none
    AC = ['DMA 555', 'DMA 555', 'DMA 535']

    #take 2 from the list
    take2 = ['DMA 410', 'DMA 415', 'DMA 425', 'DMA 475', 'DMA 480',
             'DMAN 490', 'EXP 440', 'EXP 441', 'HCD 401']

    #Major electives - take 4
    # 2 graduate level (400+) from College of Communication
    # 2 graduate level (400+) from College of Communication, CDM or another
    #college at DePaul
    # TL,DR: take 2 from each list
    NMS = ['NMS 502', 'NMS 504', 'NMS 508', 'NMS 509', 'NMS 520', 'NMS 521']
    ART = ['ART 405', 'ART 427', 'ART 460', 'ART 461', 'ART 489', 'ART 490']

    #NMS,ART,take2 - take 2 classes
    #total FAEs - 6
    FAE = ['take2', 'NMS', 'ART']

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['DC 414', 'DMA 405', 'FAE']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['DMA 527', 'DMA 525', 'AC']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['MCS 575', 'FAE', 'AC']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['CMNS 570', 'FAE', 'FAE']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['AC', 'FAE', 'FAE']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'FAE' and course != 'AC':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'AC':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'FAE':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    return str(courseTrack)


# Major: E-Commerce Technology
def majorECommerceTech():
    ''' defines E-Commerce Technology major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #Introductory courses (name, quarters offered, prereqs)
    #CSC 401, all quarters, none
    #CSC 402, all quarters, CSC 401
    #CSC 403, all quarters, CSC 402
    #ECT 410, fall/spring, CSC 401 or IT 411

    #foundation courses
    # ECT 424, all quarters, none
    # ECT 455, fall/spring, ECT 410 or HCI 430
    # CSC 453, all quarters, CSC 403
    # SE 430, all quarters, CSC 403

    #Advanced Courses - take ALL classes
    #ECT 480, spring, ECT 424
    #ECT 481, winter, ECT 410
    #ECT 582, fall, ECT 424
    AC = ['ECT 480', 'ECT 481', 'ECT 582']

    #Major Elective Courses
    # take 5, at least 2 must be 500+
    ME = ['ECT 436', 'ECT 556', 'ECT 565', 'ECT 583', 'ECT 584', 'ECT 586',
          'ECT 587', 'HCI 440', 'HCI 421', 'IS 430', 'IS 431', 'IS 485', 'IS 535',
          'IS 560', 'IS 570', 'CSC 452', 'CSC 454', 'CSC 495', 'CSC 543',
          'CSC 554', 'SE 452', 'SE 457', 'SE 511', 'SE 554', 'SE 560']

    #capstone, fall, completion of req. courses
    CAP = 'ECT 589'

    # dictionaries are class names to panda queries
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['ECT 424', 'ECT 455', 'ME']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 453', 'ME', 'AC']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2013-2014'
    springOne =  ['SE 430', 'ME', 'AC']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['ECT 589', 'AC']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['ME', 'ME']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'ME' and course != 'AC':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'AC':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'ME':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"

    # works
    return str(courseTrack)

#major: Human Computer Interaction
#author: Al Abdeladi 
def majorHumanComputerInteraction():
    ''' Human-Computer Interaction major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    #foundation courses
    # *HCI 440, all quarters, none
    # *HCI 441, no records, CSC 403
    # *NOTE: Students can take either 440 or 441
    # HCI 450, all quarters, IT 403
    # HCI 430, all quarters, IT 411 and enrolled/completed HCI 440/441

    #Advanced Courses
    # HCI 445, all quarters, IT 403 and HCI 440/441
    # HCI 454, all quarters, HCI 406 and HCI 440/441
    # HCI 460, all quarters, IT 403 and HCI 440/441
    # HCI 470, all quarters, HCI 402 and HCI 406
    # *HCI 511, fall, HCI 445
    # *HCI 514, winter, HCI 445 and HCI 460
    # *HCI 515, spring, HCI 445 and HCI 454 and HCI 430
    # *NOTE: students can take either of the three: 511, 514, or 515
    # Take all four from AC, and 1 of 3 from ACsub
    AC = ['HCI 445', 'HCI 454', 'HCI 460', 'HCI 470', 'ACsub']
    ACsub = ['HCI 511', 'HCI 514', 'HCI 515']

    #3 elective courses
    E = ['HCI 421', 'HCI 422', 'HCI 512', 'HCI 520', 'HCI 530', 'HCI 553',
         'HCI 580', 'HCI 590', 'CNS 440', 'CSC 423', 'CSC 424', 'CSC 451',
         'CSC 465', 'CSC 587', 'ECT 455', 'ECT 480', 'ECT 586', 'GAM 424',
         'IS 485', 'IS 511', 'IS 570', 'IT 432', 'IT 590', 'MKT 555', 'PM 430',
         'PM 440', 'PSY 404', 'PSY 473', 'PSY 680', 'SE 430', 'SE 482']

    # 1 Open Elective, range 421-699
    OE = ['CNS', 'CSC', 'ECT', 'GAM', 'GPH', 'HCI',
           'HIT', 'IPD', 'IS', 'IT', 'PM', 'SE', 'TDC']

    # capstone, all quarters, completion of the HCI core
    CAP = ['HCI 594']

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2013-2014'
    fallOne =  ['HCI 440', 'HCI 450', 'HCI 430']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    winterYearOne = 'Winter 2014-2015'
    winterOne =  ['AC', 'AC', 'AC']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    springYearOne = 'Spring 2014-2015'
    springOne =  ['E', 'OE', 'AC']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne
	
    fallYearTwo = 'Fall 2015-2016'
    fallTwo =  ['AC', 'E', 'E']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['HCI 594']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo



    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'OE' and course != 'AC':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'OE':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'AC':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    return str(courseTrack)


#major: Information Systems
#Concentration: Business Analysis/Systems Analysis
#Author: Al Abdeladi
def majorBusinessAnalysisSystemsAnalysis():
    ''' Information Systems Business Analysis/Systems Analysis Concentration major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # 2 Open Electives, range 421-699
    E = ['CNS', 'CSC', 'ECT', 'GAM', 'GPH', 'HCI',
           'HIT', 'IPD', 'IS', 'IT', 'PM', 'SE', 'TDC']
		   
    ME = ['CNS 440','IS 505','IS 536','CNS 487','IPD 451']

    # capstone, one of the three choices
    #IS - winter, PM - Spring, ECT - Fall
    CAP = ['IS 577']

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['IS 421', 'CSC 451', 'IS 435']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # animation focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['IS 430', 'IS 485', 'CNS 440']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # animation focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['IS 535', 'IS 560', 'IS 440']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne
	
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['IS 422', 'ME', 'E']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # animation focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['IS 577', 'ME']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo


    # query for course in season
    for season in list(courseTrack.keys()):
        print(season)
        for course in list(courseTrack[season].keys()):

            if course != 'E' and course != 'CAP' and course != 'ME':
                print(course)
                out = randomQuery(df, course, season)
                print(out)
                courseTrack[season][course] = out

            if course == 'E':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'ME':
                # TODO query for electives
                courseTrack[season][course] = "SEE ADVISOR"

            if course == 'CAP':
                # TODO queries for focus area electives
                courseTrack[season][course] = "SEE ADVISOR"


    # works
    print(courseTrack)


#major: Predictive Analytics
#Concentration: Hospitality
#author: Al Abdeladi
def majorPredictiveAnalyticsHospitality():
    ''' Predictive Analytics Hospitality major requirements'''

    df = returnDataFrame()
    # dict style is {season : {courseName: random panda query} }
    courseTrack = {}

    # 2 Open Electives, range 421-699
    E = ['CNS', 'CSC', 'ECT', 'GAM', 'GPH', 'HCI',
           'HIT', 'IPD', 'IS', 'IT', 'PM', 'SE', 'TDC']

    # capstone, one of the three choices
    #IS - winter, PM - Spring, ECT - Fall
    CAP = ['CSC 697', 'CSC 672', 'CSC 695', 'CSC 698']
	
    #Students must take 1 course in applied analytics chosen among:
    TAKE1 = ['CSC 465', 'CSC 495', 'ECT 584', 'CSC 575']
    TAKE2 = ['CSC 425', 'CSC 433', 'CSC 452', 'CSC 465', 'CSC 478',
          'CSC 481' ,'CSC 482','CSC 495','CSC 521','CSC 529',
          'CSC 543','CSC 555','CSC 575','CSC 576','CSC 578',
          'CSC 594','CSC 598','ECT 584','GEO 441','GEO 442',
          'GPH 565','HCI 512','IPD 451','IS 549','IS 574',
          'IS 578','MGT 559','MGT 798','MKT 555','MKT 530',
          'MKT 534','MKT 595','MKT 798']

    # dictionaries are class names to panda queries
    # first year maps to fall winter spring
    fallYearOne = 'Fall 2012-2013'
    fallOne =  ['IT 403', 'CSC 412', 'CSC 401']
    fallOne = toMap(fallOne)
    courseTrack[fallYearOne] = fallOne
    # works
    #print(fallOne)

    # animation focus area elective is FAE
    winterYearOne = 'Winter 2013-2014'
    winterOne =  ['CSC 455', 'CSC 423', 'CSC 424']
    winterOne = toMap(winterOne)
    courseTrack[winterYearOne] = winterOne

    # animation focus areaelective is FAE
    springYearOne = 'Spring 2013-2014'
    springOne =  ['CSC 697', 'CSC 465', 'TAKE2']
    springOne = toMap(springOne)
    courseTrack[springYearOne] = springOne

    # second year maps to fall winter with open electives later
    # animation elective is E
    fallYearTwo = 'Fall 2013-2014'
    fallTwo =  ['CSC 529', 'E' 'HSP 562']
    fallTwo = toMap(fallTwo)
    courseTrack[fallYearTwo] = fallTwo

    # works
    #print(fallTwo)

    # animation focus area elective is FAE
    winterYearTwo = 'Winter 2014-2015'
    winterTwo =  ['HSP 561', 'HSP 563', 'CAP']
    winterTwo = toMap(winterTwo)
    courseTrack[winterYearTwo] = winterTwo

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


##majorAnimator()
##majorTechnicalArtist()
##majorBusinessIT()
##majorProduction()
##majorPostProduction()
##majorSound()
##majorComputationalFinance()
##majorComputerGameDev()
##majorComputerScience()
##majorComputerSecurity()
##majorGovtRiskMgmtCompl()
##majorNetworkSecurity()
##majorMediaArts()
##majorECommerceTech()
##majorHumanComputerInteraction()
majorBusinessAnalysisSystemsAnalysis()
##majorPredictiveAnalyticsHospitality()
##majorSoftwareArchitecture()
##majorSoftwareDevelopment()
