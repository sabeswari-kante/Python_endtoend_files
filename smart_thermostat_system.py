# You're building a smart thermostat alert system:
# - if the device_status is 'active'
# -- and temperature>35-> warn :'High temperature alert'
# -- else: 'Temperature normal'
# -if the device is off-> "Device is offline"

device_status = input('the device status: active or off??: ').strip().lower()


if device_status == 'active':
    temperature = input('give temperature: ').strip()
    if int(temperature) >=35:
        print('High temperature alert')
    else:
        print('Normal temperature')
else:
    print('Device is offline!') 