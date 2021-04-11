from core.security import session_required
from flask import (
  Blueprint, 
  request, 
  redirect,
  make_response,
  render_template
)

index = Blueprint('index', __name__,
                   template_folder='templates')

@index.route('/')
@session_required
def view_index():
  return redirect('/calender')
