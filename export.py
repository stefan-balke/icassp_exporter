import argparse
import ics
import sqlite3
from datetime import datetime, timedelta


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ICASSP schedule exporter.')
    parser.add_argument('-i', '--input', help='path to your ICASSP app export')
    parser.add_argument('-o', '--offset', default=0, help='Time zone offset in hours.')
    args = parser.parse_args()

    FILENAME = args.input

    # open sqlite database
    try:
        conn = sqlite3.connect(FILENAME)
    except sqlite3.Error as e:
        print(e)

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM userScheduleItems")

    # export to ics
    cal = ics.Calendar()

    for cur_sql_event in cur.fetchall():
        cur_event = ics.Event()
        cur_event.name = cur_sql_event[3]
        cur_event.location = cur_sql_event[10]
        cur_event.begin = datetime.fromtimestamp(cur_sql_event[9]) + timedelta(hours=int(args.offset))
        cur_event.end = cur_event.begin + timedelta(minutes=int(cur_sql_event[6]))
        cal.events.add(cur_event)
        print('Exporting {}...'.format(cur_event.name))

    # print(cal.events)

    # write to ics file
    with open('ICASSP19.ics', 'w') as fh:
        fh.writelines(cal)
