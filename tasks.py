from invoke import task


@task
def clean(ctx):
    """Clean build directory"""
    ctx.run('rm -rf build/')


@task
def notebook(ctx, args=None):
    """Launch jupyter notebook to edit notebook files. Add a string of arguments through the -a/--args flag"""
    cmd = ['jupyter notebook']
    if args:
        cmd.append(args)
    ctx.run(' '.join(cmd))


@task
def nbconvert(ctx, serve=False):
    """
    Convert your lecture notebook to a HTML file, stored in the build/ directory. With -s/--serve argument, the HTML file is served by a local server as a Reveal.js slideshow.
    """
    cmd = ['jupyter nbconvert --to slides lecture.ipynb --output-dir=build/']
    if serve:
        cmd.append('--post serve')
    ctx.run(' '.join(cmd))


@task
def decktape(ctx):
    """Specialized export of RISE notebook to a PDF file under the build/ directory"""
    pass
