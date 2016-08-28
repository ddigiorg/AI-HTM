# g_input.py

from OpenGL.GL import *
from OpenGL.GLUT import *
from graphics.g_global import Flags, ViewParams, SceneParams

ESCAPE = '\x1b'

def mouseFunc( button, state, x, y ):
	if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
		selected = False
		for assembly in SceneParams.assemblies:
			for polygon in assembly.polygons:
				lower_x = polygon.position[0] + ViewParams.viewX
				upper_x = lower_x + polygon.size
				lower_y = polygon.position[1] + ViewParams.viewY
				upper_y = lower_y + polygon.size

				if lower_x <= x <= upper_x and lower_y <= y <= upper_y:
					SceneParams.selectedAssembly = assembly
					SceneParams.selectedPolygon = polygon
					selected = True

				if not selected:
					SceneParams.selectedAssembly = None
					SceneParams.selectedPolygon = None

def keyboardFunc( key, x, y ):
	if key == ESCAPE.encode(): Flags.cleanGraphics = True
	if key == 'a'.encode(): ViewParams.viewX += ViewParams.viewSpeed
	if key == 'd'.encode(): ViewParams.viewX -= ViewParams.viewSpeed
	if key == 'w'.encode(): ViewParams.viewY += ViewParams.viewSpeed
	if key == 's'.encode(): ViewParams.viewY -= ViewParams.viewSpeed
	if key == 'p'.encode(): print( "put continue flag here" )

	glutPostRedisplay()
