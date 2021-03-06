# g_shader.py

from OpenGL.GL import *

# Vertex shader
VertexShader = """
#version 130

in vec2 mesh; //xy
in vec2 position; //xy
in vec3 color;    //rgb

out vec3 colorVS;

uniform mat4 projection;
uniform mat4 view;

void main()
{
	vec2 vertex = mesh.xy + position.xy;
	gl_Position = projection * view * vec4(vertex, 0.0f, 1.0f);

	colorVS = color;
}
"""

# Fragment shader
FragmentShader = """
#version 130

in vec3 colorVS;

out vec3 colorFS;

void main()
{
	colorFS = colorVS;
}
"""

# Compile a vertex or fragment shader from source
def compile_shader(name):
	global VertexShader, FragmentShader
	if name == "VS":
		source = VertexShader
		shader_type = GL_VERTEX_SHADER
	elif name == "FS":
		source = FragmentShader
		shader_type = GL_FRAGMENT_SHADER        
	shader = glCreateShader(shader_type)
	glShaderSource(shader, source)
	glCompileShader(shader)
	# check compilation error
	result = glGetShaderiv(shader, GL_COMPILE_STATUS)
	if not(result):
		raise RuntimeError(glGetShaderInfoLog(shader))
	return shader

# Create a shader program with from compiled shaders
def link_shader_program(vertex_shader, fragment_shader):
	program = glCreateProgram()
	glAttachShader(program, vertex_shader)
	glAttachShader(program, fragment_shader)
	glLinkProgram(program)
	# check linking error
	result = glGetProgramiv(program, GL_LINK_STATUS)
	if not(result):
		raise RuntimeError(glGetProgramInfoLog(program))
	return program
