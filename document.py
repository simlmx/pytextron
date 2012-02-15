import sys, subprocess, re
from os.path import join, exists, dirname

class LatexDocument(object):

    nb_compile_times = 1

    def __init__(self, preambule, core):
        self.preambule = preambule
        self.core = core

    def make_tex(self, tex_file, ask_overwrite=True):

        if exists(tex_file):
            if ask_overwrite:
                choice = ''
                while choice not in ['Y', 'N']:
                    choice = raw_input("The file %s already exists. Overwrite? (Y/N) " % tex_file).upper()
                if choice == 'N':
                    sys.exit()

        with open(tex_file, 'w') as f:
            f.write(unicode(self.preambule))
            f.write('\n\n')
            f.write(unicode(self.core))

    def make_pdf(self, tex_file):

        cwd = dirname(tex_file)
        if cwd == '' : cwd = '.'
        for i in range(self.nb_compile_times):
            subprocess.Popen([
                'pdflatex',
                '--file-line-error',
                '--shell-escape',
                '--synctex=1',
                os.path.basename(path)], cwd=cwd).communicate()

        # cleaning
        for ext in 'sol qsl synctex.gz log aux'.split():
            os.remove('%s.%s' % (path[:-4],ext))
        for ext in r'func\d?.gnuplot func\d?.table'.split():
            regex = re.compile('^%s.%s$' % (path[:-4], ext))
            for f in os.listdir(cwd):
                if regex.match(f):
                    os.remove(f)
    
    def make(self, output_dir, name):
        self.make_tex(join(output_dir, name + '.tex'))
        self.make_pdf(join(output_dir, name + '.tex')) 

    
