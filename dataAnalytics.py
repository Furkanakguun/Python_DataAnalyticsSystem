import time
import random
import bisect
import sys


class Log:
    def __init__(self, arrivaltime, user, session, event, usrfield):
        self.arrivaltime = arrivaltime
        self.user = user
        self.session = session
        self.event = event
        self.usrfield = usrfield

    def getArrivaltime(self):
        return self.arrivaltime

    def getUser(self):
        return self.user

    def getSession(self):
        return self.session

    def getEvent(self):
        return self.event

    def getUsrfield(self):
        return self.usrfield

    def __str__(self):
        return "(arrivaltime:%s, user:%s, session:%d, event:%s, usrfield:%d)" % (time.ctime(self.arrivaltime),
                                                                                 self.user,
                                                                                 self.session,
                                                                                 self.event,
                                                                                 self.usrfield)

    def __repr__(self):
        return "(arrivaltime:%s, user:%s, session:%d, event:%s, usrfield:%d)" % (time.ctime(self.arrivaltime),
                                                                                 self.user,
                                                                                 self.session,
                                                                                 self.event,
                                                                                 self.usrfield)


def compareDates(trueDate, startDate, endDate):
    return trueDate > startDate and trueDate < endDate


def printListFurkan(list):
    for element in list:
        print(element)


def createDictionary(logs):
    bigDictionary = {}
    for log in logs:
        dictToAdd = log._dictionary_()

    return bigDictionary


def randomLogs(n):
    stringmaxlen = 3
    sessionmax = 1000
    events = ['eventA', 'eventB', 'eventC', 'eventD', 'eventE']
    arrivalmin = int(time.mktime(time.strptime('Mon Jan 1 12:00:00 2020')))
    arrivalmax = int(time.mktime(time.strptime('Mon Mar 1 12:00:00 2020')))
    usrfieldmax = 10000
    chars = 'abcdefghijklmnprstuvyz'
    logs = []

    for i in range(1, n + 1):
        arrival = random.randint(arrivalmin, arrivalmax)
        user = ''
        for x in range(0, stringmaxlen):
            user += random.choice(chars)
        session = random.randint(0, sessionmax)
        event = random.choice(events)
        usrfield = random.randint(0, usrfieldmax)
        log = Log(arrival, user, session, event, usrfield)
        logs.append(log)
    return logs


def registerEqualQuery(logs, field):
    def query(val1):
        res = []
        for (index, log) in enumerate(logs):
            if getattr(log, field)() == val1:
                res.append(log)
        return res

    if field not in ['getArrivaltime', 'getUser', 'getSession', 'getEvent', 'getUsrfield']:
        raise Exception('field name not found')
    return query


def registerRangeQuery(logs, field):
    def subProgram(p1, p2):
        res = []
        if field in ['getSession']:
            for (index, log) in enumerate(logs):
                if int(log.getSession()) >= (p1) and int(log.getSession()) <= int(p2):
                    res.append(log)
            return res
        else:
            for (index, log) in enumerate(logs):
                if log.getArrivaltime() >= p1 and log.getArrivaltime() <= p2:
                    res.append(log)
            return res

    if field not in ['getArrivaltime', 'getSession']:
        print('not a supported field for range query')
        sys.exit(0)
    return subProgram


def registerOptimizedRangeQuery(logs, field):
    dictionary = {}
    # First we sort the logs
    logs.sort(key=lambda x: getattr(x, field)())
    # Then we add empty list as a value for our logs in dictionary
    for log in logs:
        dictionary[getattr(log, field)()] = []

    for log in logs:
        dictionary[getattr(log, field)()].append(log)

    attList = []

    for log in logs:
        attList.append(getattr(log, field)())

    def SubProgram(p1, p2):
        start = bisect.bisect(attList, p1 - 1)
        end = bisect.bisect(attList, p2)
        return logs[start:end]

    if field not in ['getArrivaltime', 'getSession']:
        raise Exception('field name not found')
    return SubProgram


def registerOptimizedEqualQuery(logs, field):
    dictionary = {}
    for log in logs:
        dictionary[getattr(log, field)()] = []

    for log in logs:
        dictionary[getattr(log, field)()].append(log)

    def SubProgram(param):
        opList = []

        LogDic = {}

        return dictionary[param]

    if field not in ['getArrivaltime', 'getUser', 'getSession', 'getEvent', 'getUsrfield']:
        raise Exception('field name not found')
    return SubProgram


import test


def main():
    case = input("Enter test item: ")
    casefun = getattr(test, case)
    casefun()


if __name__ == '__main__':
    main()
