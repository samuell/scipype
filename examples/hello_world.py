import scipype

workflow = scipype.Workflow()

foowrite = scipype.Process('echo "Foo" > {o:foo}')
footobar = scipype.Process('sed "s/foo/bar/g" | {i:foo} > {o:bar:{i:foo:.txt}.bar.txt}')

workflow.add_process('Foo writer', foowrite)
workflow.add_process('Foo to bar', footobar)

footobar.inp_foo = foowrite.outp_foo

workflow.run()
