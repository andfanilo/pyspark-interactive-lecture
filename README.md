# Pyspark lecture

Interactive Spark lecture using RISE and PySpark.

## Prerequisites

* Python 3.5+. 
* (Optional) Anaconda. I usually use Anaconda for managing my Python environments, which explains why the guide uses conda commands in the following.
* (Optional) Spark 2+ referenced inside a `SPARK_HOME` environment variable for Spark Streaming.

The following guide has Windows users in mind.

## Install development environment

### Python

We provide you with a `environment.yml` which Anaconda can use to create a Python environment named `pyspark-interactive-lecture`.

```
conda env create -f environment.yml
activate pyspark-interactive-lecture
```

After installation, you should get access to `invoke` in a GNU terminal, and be able to see all defined tasks for the project with `invoke -l`.

Documentation on a task with `invoke <task> -h`.

### Node

If you wish to use decktape for exporting your slides as a Reveal.js slidedeck with `decktape`, you need to prepare your environment. [Node.js + npm](https://nodejs.org/) is required for the following.

```
npm install
```

## Invoke task list

```
$ invoke -l
Available tasks:

  clean           Clean build directory
  decktape        Specialized export of RISE notebook to a PDF file under the build/ directory
  lab             Launch jupyter lab to edit notebook files. Add a string of arguments through the -a/--args flag and --spark_home for path to Spark
  nbconvert       Convert your lecture notebook to a HTML file, stored in the build/ directory. With -s/--serve argument, the HTML file is served by a local server as
                  a Reveal.js slideshow.
  notebook        Launch jupyter notebook to edit notebook files. Add a string of arguments through the -a/--args flag and --spark_home for path to Spark
```

## Download Spark

Download Spark and unzip it in `bin/spark`.

## Configure Spark

In `conf/log4j.properties`, set `log4j.rootCategory=WARN, console`.

In `conf/spark-defaults.conf`, set 

```
spark.sql.shuffle.partitions   4
```

## Run notebook for editing

Run a Jupyter Notebook session : `invoke notebook`.

If you need to pass a string of arguments : `invoke notebook -a "--port=9000"`

The invoke command will automatically send `bin/spark` as the `SPARK_HOME` environment variablen so you need to have downloaded Spark inside `bin/spark` before, which is normally easily done in the previous section. If you wish to change that use the `--spark_home` flag : `invoke notebook -s path/to/spark.`

## Export slidedeck

### nbconvert

We use a personalized nbconvert template to generate a correct Reveal.js HTML file from the notebook file.

```
$ invoke nbconvert -h
Usage: inv[oke] [--core-opts] nbconvert [--options] [other tasks here ...]

Docstring:
  Convert your lecture notebook to a HTML file, stored in the src/ directory. With -s/--serve argument, the HTML file is served by a local server as a Reveal.js slideshow.

Options:
  -a STRING, --transition=STRING
  -f STRING, --font-awesome-url=STRING
  -r STRING, --reveal-url-prefix=STRING
  -s, --serve
  -t STRING, --theme=STRING
```

`invoke nbconvert` will convert the notebook to a HTML file inside the `static/` directory. You can then visualize them by double-clicking on the file, or with `python -m http.server`.

`invoke nbconvert --serve` to launch the HTML file with a local server for serving the slides as a Reveal.js slideshow.

### decktape

Run the following command to run decktape on a background Jupyter notebook: `invoke decktape`

NB : [There is a fix to apply beforehand in RISE 5.1 + Decktape 2.6+](https://github.com/astefanutti/decktape/issues/110#issuecomment-345217070) :

```
Never mind!
I was just typing the incorrect URL as input to decktape rise.
So, the fix that I propose (i.e., replacing "start_livereveal" with "RISE" in the rise.js file) actually makes decktape 2.5.0 and RISE 5.1.0 work nicely.
Hope this helps!

Thanks,
Gabriele
```