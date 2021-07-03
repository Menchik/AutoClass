from script import meet_Bot
from datetime import datetime, timedelta
import calendar

obj = meet_Bot()
obj.loginGmail("emial@ufms.br", "senha")

FMT = '%H:%M:%S'
tempoadiantado = timedelta(minutes=30)

aula = [["Thursday", datetime.strptime('07:15:00', FMT), "https://meet.google.com/qqd-rhrr-unh"],
        ["Saturday", datetime.strptime('12:00:00', FMT), "https://meet.google.com/qqd-rhrr-unh"]]

now = datetime.now()

for i in range(len(aula)):
    if aula[i][0] == calendar.day_name[now.weekday()]:
        quantofalta = aula[i][1] - now
        if quantofalta.seconds < tempoadiantado.seconds:
            obj.joinClassRoom(aula[i][2])