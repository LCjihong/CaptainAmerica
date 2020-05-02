import turtle as t

def fiveStar(color, length):
	t.begin_fill()
	t.color(color, color)
	for i in range(5):
		t.forward(length)
		t.right(144)
	t.end_fill()

def dot(color, r):
	t.pencolor(color)
	t.dot(r)

if __name__ == '__main__':
	t.screensize(500, 500, 'black')
	t.hideturtle()
	dot('red', 300)
	dot('white', 250)
	dot('red', 200)
	dot('blue', 150)
	t.penup()
	t.goto(-71, 23)
	t.pendown()

	fiveStar('white', 142)
	t.done()
