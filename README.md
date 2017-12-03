# Interactive pyspark lecture

Interactive Spark lecture using RISE and PySpark.

## Prerequisites

* Python 3.5+. 
* (Optional) Anaconda. I usually use Anaconda for managing my Python environments, which explains why the guide uses conda commands in the following.
* (Optional) Spark 2.2.0 referenced inside a `SPARK_HOME` environment variable.

The following guide has Windows users in mind.

## Install development environment

We provide you with a `environment.yml` which Anaconda can use to create a Python environment named `pyspark-interactive-lecture`.

```
conda env create -f environment.yml
activate pyspark-interactive-lecture
```

After installation, you should get access to `invoke` in a GNU terminal, and be able to see all defined tasks for the project with `invoke -l`.

Documentation on a task with `invoke <task> -h`.

## Download Spark

We try to use Spark inside `bin/spark` so we have provided with a task for downloading and extracting the archive : `invoke downloadSpark`.

Else you can just download and extract the archive by end.

## Run notebook for editing

Run a Jupyter Notebook session : `invoke notebook`.

If you need to pass a string of arguments : `invoke notebook -a "--port=9000"`

The invoke command will automatically send `bin/spark` as the `SPARK_HOME` environment variablen so you need to have downloaded Spark inside `bin/spark` before, which is normally easily done in the previous section. If you wish to change that use the `--spark_home` flag : `invoke notebook -s path/to/spark.`

## Export slidedeck

### nbconvert

`invoke nbconvert` will convert the notebook to a HTML file inside the `build/` directory.

`invoke nbconvert --serve` to launch the HTML file with a local server for serving the slides as a Reveal.js slideshow.

### decktape

[Node.js + npm](https://nodejs.org/) is required to export the RISE slides into a PDF.

Install decktape :

```
npm install
```

Then launch the Jupyter notebook and export script.

```
jupyter notebook --NotebookApp.token=''
npm run export
```

NB : [There is a fix to apply beforehand in RISE 5.1 + Decktape 2.6+](https://github.com/astefanutti/decktape/issues/110#issuecomment-345217070) :

```
Never mind!
I was just typing the incorrect URL as input to decktape rise.
So, the fix that I propose (i.e., replacing "start_livereveal" with "RISE" in the rise.js file) actually makes decktape 2.5.0 and RISE 5.1.0 work nicely.
Hope this helps!

Thanks,
Gabriele
```