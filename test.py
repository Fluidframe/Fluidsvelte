from src.compiler import FluidCompiler
from src.utils.file_utils import create_project, init_project

compiler = FluidCompiler(
    output_dir="dist",
    base_url="http://127.0.0.1:8000",
)

compiler.compile_directory("examples")
# compiler.compile_files([
#     "examples/counter.fluid", 
#     "examples/counter2.fluid",
# ])

compiler.build()

# init_project("test")
