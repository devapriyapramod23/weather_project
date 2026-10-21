import check_sensors as cs
import weekly_summary as ws
import classify_days as cds
import hot_coolcity as hct
import rainfall_byday as rbd
import rain_alert as rbc
import kochi_avg as ka

weather={
    "Kochi":{
        "temp":[31,32,30,29,31,33,32],
        "rain":[0,5,12,20,0,0,3]
    },
    "Munnar":{
        "temp":[18,19,17,16,18,20,19],
        "rain":[2,8,15,25,5,0,4]
    },
    "Palakkad":{
        "temp":[36,37,38,-999,37,39,38],
        "rain":[0,0,0,0,0,0,0]
    },
    "Kozhikode":{
        "temp":[30,31,30,29,30,32,31],
        "rain":[0,10,8,18,2,0,1]
    }
}

cs.sensor_check(weather)
ws.weekly_summary(weather)
cds.classify_days(weather, ws.clean)
hct.show_extremes(weather, ws.clean, ws.average)
rbd.rainfall_summary(weather, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
rbc.show_rain_alerts(weather, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
ka.show_moving_average(weather, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])    