# template for "Stopwatch: The Game"
import simplegui

# define global variables
seconds = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    print t
    #print t/600
    #print ((t/10) % 60)/10
    #print ((t/10) %60)%10
    a = t/600
    b = ((t/10) %60)/10
    c = ((t/10) %60)%10
    d = t %10
    
    message = str(a) + ":" + str(b) + str(c) + "." +str(d)
    return message
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
def stop_handler():
    timer.stop()
def restart_handler():
    global seconds
    seconds = 0
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global seconds
    seconds += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(seconds), [250,250], 32, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 500, 500)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("start", start_handler)
frame.add_button("stop", stop_handler)
frame.add_button("restart", restart_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
