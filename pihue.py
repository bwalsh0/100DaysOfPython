from phue import Bridge

b = Bridge('192.168.1.2')

b.connect()
b.get_api()
b.get_light(1, 'on')
b.set_light(1, 'bri', 254)
b.set_light(2, 'bri', 127)
b.set_light(2,'on', True)
b.set_light( [1,2], 'on', True)
b.get_light(1, 'name')
b.get_light('Kitchen')
b.set_light('Kitchen', 'bri', 254)
b.set_light(['Bathroom', 'Garage'], 'on', False)
command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
b.set_light(1, command)
