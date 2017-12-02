# Interactive pyspark lecture

Interactive Spark lecture using RISE and PySpark.

## Prerequisites

* Python 3.5. 
* (Optional) Anaconda. I usually use Anaconda for managing my Python environments, which explains why the guide uses conda commands in the following.
* Spark 2.2.0 referenced inside a `SPARK_HOME` environment variable.

The following guide has Windows users in mind.

## Install development environment

We provide you with a `environment.yml` which Anaconda can use to create a Python environment named `pyspark-interactive-lecture`.

```
conda env create -f environment.yml
activate pyspark-interactive-lecture
```

After installation, you should get access to `invoke`, you should be able to see all defined tasks for the project with `invoke -l` 

## Run notebook for editing

`invoke notebook`

Inside the notebook, launch the slideshow with `Enter/Exit Live Reveal Slideshow` button.

## Export slidedeck

### nbconvert

`invoke nbconvert` will convert the notebook to a HTML file inside the `build/` directory.

`invoke nbconvert --serve` to launch With a local server for serving the slides as a Reveal.js slideshow.

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