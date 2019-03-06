from conanos.builder.builder import Builder

def Main(name,pure_c=True):
    Builder(name, pure_c).run()