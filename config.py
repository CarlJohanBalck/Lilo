IP_ADDRESS = "192.168.0.100"
PORT = 5001
PORT_BE = 5002
g = (0, 255, 0)

e = (0, 0, 0)
y = (0, 0, 0)

b = (0,0,255)

r = (255,0,0)

o = (255,165,0)

smiley_face = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, y, y, b, b, y, y, y,
   y, y, y, y, y, y, y, y
]

got_water = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y
]

needs_water = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, o, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y
]
gym = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, g, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y
]
swimming = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y
]

running = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, r, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y
]

g1 = [
	e, e, e, g, g, e, e, e,
	e, g, g, g, g, e, e, e,
	e, g, g, g, g, e, e, e,
	e, e, e, g, g, e, e, e,
	e, e, e, g, g, e, e, e,
	e, e, e, g, g, e, e, e,
	e, e, e, g, g, e, e, e,
	e, e, e, g, g, e, e, e
]
g2 = [
	e, g, g, g, g, g, e, e,
	e, g, g, g, g, g, e, e,
	e, e, e, g, g, g, e, e,
	e, e, e, g, g, g, e, e,
	e, g, g, g, g, e, e, e,
	e, g, g, e, e, e, e, e,
	e, g, g, g, g, g, e, e,
	e, g, g, g, g, g, e, e
]
g3 = [
	e, g, g, g, g, g, e, e,
	e, g, g, g, g, g, e, e,
	e, e, e, e, g, g, e, e,
	e, g, g, g, g, g, e, e,
	e, g, g, g, g, g, e, e,
	e, e, e, e, g, g, e, e,
	e, g, g, g, g, g, e, e,
	e, g, g, g, g, g, e, e
]
g4 = [
	e, g, g, e, e, g, g, e,
	e, g, g, e, e, g, g, e,
	e, g, g, g, g, g, g, e,
	e, g, g, g, g, g, g, e,
	e, e, e, e, e, g, g, e,
	e, e, e, e, e, g, g, e,
	e, e, e, e, e, g, g, e,
	e, e, e, e, e, g, g, e
]

r1 = [
	e, e, e, r, r, e, e, e,
	e, r, r, r, r, e, e, e,
	e, r, r, r, r, e, e, e,
	e, e, e, r, r, e, e, e,
	e, e, e, r, r, e, e, e,
	e, e, e, r, r, e, e, e,
	e, e, e, r, r, e, e, e,
	e, e, e, r, r, e, e, e
]
r2 = [
	e, r, r, r, r, r, e, e,
	e, r, r, r, r, r, e, e,
	e, e, e, r, r, r, e, e,
	e, e, e, r, r, r, e, e,
	e, r, r, r, r, e, e, e,
	e, r, r, e, e, e, e, e,
	e, r, r, r, r, r, e, e,
	e, r, r, r, r, r, e, e
]
r3 = [
	e, r, r, r, r, r, e, e,
	e, r, r, r, r, r, e, e,
	e, e, e, e, r, r, e, e,
	e, r, r, r, r, r, e, e,
	e, r, r, r, r, r, e, e,
	e, e, e, e, r, r, e, e,
	e, r, r, r, r, r, e, e,
	e, r, r, r, r, r, e, e
]
r4 = [
	e, r, r, e, e, r, r, e,
	e, r, r, e, e, r, r, e,
	e, r, r, r, r, r, r, e,
	e, r, r, r, r, r, r, e,
	e, e, e, e, e, r, r, e,
	e, e, e, e, e, r, r, e,
	e, e, e, e, e, r, r, e,
	e, e, e, e, e, r, r, e
]