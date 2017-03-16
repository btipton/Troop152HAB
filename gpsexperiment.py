import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        #print report
        print session.fix.latitude
        print session.fix.longitude
        print session.fix.altitude
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print report.time
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
        
