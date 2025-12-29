APPNAME = "LearnOpenGL"

top = "."
out = "build"

def options(opt):
	opt.load(["compiler_cxx", "compiler_c"])

def configure(conf):
	conf.load(["compiler_cxx", "compiler_c"])
	conf.check(lib="glfw")
	conf.recurse(["vendor/glad"])

def build(bld):
	bld.recurse(["vendor/glad"])
	bld.program(target=APPNAME, source="src/main.cpp", includes=["include", "vendor/glad/include"], use="glad", lib="glfw")

