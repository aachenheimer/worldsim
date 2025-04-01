from pygame import *

def draw_text(text = "test", fontParam = font.get_default_font(), size = 12, color = Color(255, 255, 255), pos = (0,0)):
	if fontParam != font.get_default_font():
		fontParam = font.match_font(fontParam)
	newFont = font.Font(fontParam, size)
	SCREEN.blit(newFont.render(text, True, color), pos)

font.init()
display.init()

SCREEN = display.set_mode()

FONT = "bell"

draw_text("hello world!", "bell", 144, Color(255, 255, 255), (0,0))

display.update()

while True:
	pass




