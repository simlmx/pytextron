import sys, subprocess, re, os
from os.path import join, exists, dirname

class LatexDocument(object):

    nb_compile_times = 1

    # Either set those while subclassing or pass them to __init__
    preambule = ''
    content = ''

    def __init__(self, preambule=None, content=None, nb_compile_times=1):
        if preambule is not None:
            self.preambule = preambule
        if content is not None:
            self.content = content
        self.nb_compile_times = nb_compile_times

    def make_tex(self, tex_file):

        if exists(tex_file):
            choice = ''
            while choice not in ['Y', 'N']:
                choice = raw_input("The file %s already exists. Overwrite? (Y/N) " % tex_file).upper()
            if choice == 'N':
                sys.exit()

        with open(tex_file, 'w') as f:
            f.write(unicode(self.preambule))
            f.write('\n\n')
            f.write(unicode(self.content))

    def make_pdf(self, tex_file):
        """
            Assumes the tex file has already been made.
            If not use `self.make`.
        """
        cwd = dirname(tex_file)
        if cwd == '' : cwd = '.'
        for i in range(self.nb_compile_times):
            subprocess.Popen([
                'pdflatex',
                '--file-line-error',
                '--shell-escape',
                '--synctex=1',
                os.path.basename(tex_file)], cwd=cwd).communicate()

        # cleaning
        for ext in 'sol qsl synctex.gz log aux'.split():
            path = '%s.%s' % (tex_file[:-4], ext)
            if exists(path):
                os.remove(path)
        for ext in r'func\d?.gnuplot func\d?.table'.split():
            regex = re.compile('^%s.%s$' % (tex_file[:-4], ext))
            for f in os.listdir(cwd):
                if regex.match(f):
                    os.remove(f)
    
    def make(self, output_dir, name):
        self.make_tex(join(output_dir, name + '.tex'))
        self.make_pdf(join(output_dir, name + '.tex')) 

    