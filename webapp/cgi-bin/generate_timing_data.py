import cgi
import athletemodel
import yate

import cgitb

cgitb.enable()

from_data = cgi.FieldStorage()
athlete_name = from_data['which_athlete'].value

athletes = athletemodel.get_from_store()

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Althlete:" + athlete_name + ",DOB:" +
                  athletes[athlete_name].dob + "."))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"Home:" : "/index.html",
                           "Select another athlete":"generate_list.py"}))
