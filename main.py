import webbrowser
from datetime import datetime, timedelta
import calendar

FMT = '%H:%M:%S'
tempoadiantado = timedelta(minutes=5)

aula = [["Thursday", datetime.strptime('07:15:00', FMT)],
        ["Friday", datetime.strptime('20:40:00', FMT)]]

now = datetime.now()

for i in range(len(aula)):
    if aula[i][0] == calendar.day_name[now.weekday()]:
        quantofalta = aula[i][1] - now

        if quantofalta.seconds < tempoadiantado.seconds:
            webbrowser.open("http://youtube.com", new=1)
            now = datetime.now()