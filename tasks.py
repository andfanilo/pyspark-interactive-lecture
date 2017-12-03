from invoke import task
import os
import patoolib
from path import Path
import psutil
import requests
import time


@task
def clean(ctx):
    """Clean build directory"""
    ctx.run('rm -rf build/')


@task
def downloadSpark(ctx):
    """Download Spark to bin/ directory"""
    bin_folder = Path('bin/')
    bin_folder.mkdir_p()

    spark_archive = bin_folder / 'spark.tgz'
    spark_folder = bin_folder / 'spark'

    if not (spark_archive.exists() | spark_folder.exists()):
        url = 'http://apache.mediamirrors.org/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz'
        r = requests.get(url)
        with open(spark_archive, 'wb') as f:
            f.write(r.content)

    if not spark_folder.exists():
        patoolib.extract_archive(spark_archive, outdir=spark_folder)
        spark_archive.rm_p()


@task
def notebook(ctx, args=None, spark_home=Path.getcwd() / 'bin/spark'):
    """Launch jupyter notebook to edit notebook files. Add a string of arguments through the -a/--args flag and --spark_home for path to Spark"""
    cmd = ['jupyter notebook']
    if args:
        cmd.append(args)
    ctx.run(' '.join(cmd), env={'SPARK_HOME': spark_home})


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
    build_folder = Path('build/')
    build_folder.mkdir_p()

    jupyter_proc = psutil.Popen(['jupyter', 'notebook' , '--NotebookApp.token=""', '--no-browser'])
    time.sleep(10)
    ctx.run('npm run export')
    
    for child in jupyter_proc.children(recursive=True):
        child.terminate()
    jupyter_proc.terminate()
    jupyter_proc.wait()