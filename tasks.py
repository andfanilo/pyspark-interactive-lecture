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
def notebook(ctx, notebook_dir='notebooks', spark_home=Path.getcwd() / 'bin/spark'):
    """Launch jupyter notebook to edit notebook files. Ideal for modifying pyspark.ipynb"""
    cmd = ['jupyter notebook']
    cmd.append('--notebook-dir={}'.format(notebook_dir))
    ctx.run(' '.join(cmd), env={'SPARK_HOME': spark_home})


@task(help={
    'serve': 'serve file through a local http server',
    'font_awesome_url': 'url to font-awesome',
    'reveal_url_prefix': 'url to reveal.js',
    'theme': 'reveal.js theme to use',
    'transition': 'reveal.js transition to use'
    })
def nbconvert(ctx, serve=False, font_awesome_url='https://use.fontawesome.com/releases/v5.0.0/css/all.css', reveal_url_prefix='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0', theme='simple', transition='fade'):
    """
    Convert your lecture notebook to a HTML file, stored in the static/ directory.
    """
    cmd = ['jupyter nbconvert'] 
    cmd.append('--to slides')
    cmd.append('--SlidesExporter.font_awesome_url={}'.format(font_awesome_url))
    cmd.append('--SlidesExporter.reveal_url_prefix={}'.format(reveal_url_prefix))
    cmd.append('--SlidesExporter.reveal_theme={}'.format(theme))
    cmd.append('--SlidesExporter.reveal_transition={}'.format(transition))
    cmd.append('--output-dir=static/')
    cmd.append('--output=index')
    cmd.append('--template=pyspark-interactive-lecture.tpl')
    cmd.append('notebooks/pyspark.ipynb')
    if serve:
        cmd.append('--post serve')
        cmd.append('--ServePostProcessor.reveal_cdn={}'.format(reveal_url_prefix))
    ctx.run(' '.join(cmd))


@task
def decktape(ctx):
    """Specialized export of RISE notebook to a PDF file under the build/ directory"""
    build_folder = Path('build/')
    build_folder.mkdir_p()

    jupyter_proc = psutil.Popen(['jupyter', 'notebook' , '--NotebookApp.token=""', '--notebook-dir="notebooks"', '--no-browser'])
    time.sleep(10)
    ctx.run('npm run export')
    
    for child in jupyter_proc.children(recursive=True):
        child.terminate()
    jupyter_proc.terminate()
    jupyter_proc.wait()