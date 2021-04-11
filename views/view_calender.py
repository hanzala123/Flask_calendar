from core.security import session_required
from flask import (
  Blueprint, 
  request, 
  redirect,
  make_response,
  render_template,
  jsonify
)
from datetime import datetime

from core.redis import rds

classes = {'Normal':'event-info','Low': 'event-success','Medium':'event-warning','Important':'event-important', 'Special': 'event-special'}

def convertToMilis(time):
	dt_obj = datetime.strptime(time,'%Y-%m-%dT%H:%M')
	millisec = dt_obj.timestamp() * 1000

	return millisec

calender = Blueprint('calender', __name__,
                   template_folder='templates')

@calender.route('/calender')
@session_required
def home():
	return render_template('calender_only.html')

@calender.route('/calendar-events')
@session_required
def calendar_events():
	try:
		rows = rds.get_json('calenderEvents')
		if not rows:
			rows = []
		resp = jsonify({'success' : 1, 'result' : rows})
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@calender.route('/calender/addevent')
@session_required
def view_addevent():
	title = request.args.get('title')
	start = convertToMilis(request.args.get('start'))
	if request.args.get('end'):
		stop  = convertToMilis(request.args.get('end'))
	else:
		stop = start
	tmp = rds.get_json('calenderEvents')
	if tmp:
		id = tmp[0]['id']+1
	else:
		id = 1
	eventClass = classes[request.args.get('class')]
	data = {
		"id": id,
		"title": title,
		"url": request.args.get('url'),
		"class": eventClass,
		"start": int(start), #Milliseconds
		"end": int(stop) # Milliseconds
	}
	if tmp:
		tmp.insert(0,data)
	else:
		tmp = [data]
	rds.store_json('calenderEvents',tmp)

	return redirect('/calender')

@calender.route('/calender/removeevent')
@session_required
def view_removeevent():
	id = request.args.get('id')
	tmp = rds.get_json('calenderEvents')
	for i in range(len(tmp)):
		if tmp[i]['id'] == int(id):
			del tmp[i]
			break
	if tmp:
		rds.store_json('calenderEvents',tmp)
	else:
		rds.delete('calenderEvents')
	return redirect('/calender')

@calender.route('/calender/removeall')
@session_required
def view_removeall():
	rds.delete('calenderEvents')
	return redirect('/calender')
