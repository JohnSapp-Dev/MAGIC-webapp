from django.shortcuts import render
from django.http import HttpResponse
from .models import WaitTimes
from .form import Attraction_select_form
import plotly.express as px
import plotly.graph_objects as go
from django.utils import timezone
import datetime


def index(request):

  if request.method == "POST":
    # getting the data from the section
    print("post method")

    form = Attraction_select_form(request.POST)
    """ wait_time_data = WaitTimes.objects.all() """

    if form.is_valid():
      print("form valid")
      theme_park = form.cleaned_data["theme_park"]
      attraction = form.cleaned_data["attraction"]
      start_date = form.cleaned_data["start_date"]
      end_date = form.cleaned_data["end_date"]

      print("start date:" + str(start_date))
      print("end date:" + str(end_date))

      add_hours = datetime.timedelta(hours=4)

      wait_time_data = WaitTimes.objects.filter(theme_park = theme_park)

      # sets the start date. returns any value greater than or equal to start date
      if start_date:
        wait_time_data = wait_time_data.filter(updated__gte=(start_date+add_hours))

      # set the end date. Returns any value less than or equal to the end date
      if end_date:
        add_day = datetime.timedelta(days=1)
        end_date = end_date + add_day

        wait_time_data = wait_time_data.filter(updated__lte=(end_date+add_hours))

      # Filters data to only include the attraction we are interested in. 
      attration_data = wait_time_data.filter(attraction=attraction)
      """ attration_data = wait_time_data """

      timezone_update = timezone.get_fixed_timezone((-4*60))

      # loops through the dataset and converts the database provided datetime to the local utc-4 datetime
      converted_WT_object = []
      max = 0
      for time in attration_data:

        converted_time = time.updated.astimezone(timezone_update)

        converted_WT_object.append({
            'attraction': time.attraction, 
            'is_open': time.is_open,
            'wait_time': time.wait_time,
            'updated_converted': converted_time, # The converted datetime
        })

        if max <= time.wait_time:
          max = time.wait_time
        
    else:
      print("not valid")
      print(form.errors)   
        

    # creating the line chart with selected data
  
    """ for attration in attration_data: """

    line = go.Scatter(
      x=[time['updated_converted'] for time in converted_WT_object],
      y=[waittime['wait_time'] for waittime in converted_WT_object],
      mode='lines',
      name="Wait Time",
    )

    bar = go.Bar(
      x=[time['updated_converted'] for time in converted_WT_object],
      y=[open['is_open']*max for open in converted_WT_object],
      marker_color=['green' if time['is_open'] == 0 else 'green' for time in converted_WT_object],
      marker=dict(color='green'),
      opacity= 0.6,
      name="Attraction is open",
      #showlegend=False,
      )
    
    fig = go.Figure(data=[line,bar])

    fig.update_layout(
      title_text=f"{attraction} Wait time and Open Status",
      yaxis=dict(title='Wait Time'),
      xaxis=dict(title='Time of Day'),
      yaxis2=dict(
        title='Attraction Open Status',
        overlaying='y',
        side='right',
        ),
      legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
      ),
    )

    chart = fig.to_html()

    form = Attraction_select_form()
    context = {
      "form": form,
      "chart": chart,
      }
    
  else:
    form = Attraction_select_form()
    context = {
      "form": form,
      }

  return render(request,'Magic_app/index.html',context)

def load_attraction(request):

  theme_park_passed = request.GET.get("theme_park")

  attraction_name = WaitTimes.objects.filter(
    theme_park=theme_park_passed
    ).values_list('attraction',flat=True).distinct().order_by('attraction')
  
  return render(request,'Magic_app/attraction_options.html',{'attraction': attraction_name})

def homepage(request):
  return render(request,'Magic_app/homepage.html')

def heatmap(request):
  return render(request,'Magic_app/heatmap.html')
                
def wait_time_view(request,wait_time_id):
  responce = f"You're looking at attraction id: {wait_time_id}"
  return HttpResponse(responce) 
