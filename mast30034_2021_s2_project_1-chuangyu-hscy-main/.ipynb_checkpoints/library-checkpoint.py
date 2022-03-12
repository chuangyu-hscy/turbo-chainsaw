import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark import StorageLevel, SparkConf, SparkContext
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

import folium
from folium.plugins import FastMarkerCluster
from folium.plugins import HeatMap

from bokeh.plotting import figure, show
from bokeh.tile_providers import get_provider, Vendors
from bokeh.io import save, reset_output,  output_notebook

from bokeh.models import ColorBar, LinearColorMapper
from bokeh.palettes import all_palettes

import json

from shapely.geometry import shape

import plotly.offline as py
import plotly.graph_objs as go

import datetime as dt

from pyspark.ml.feature import *
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
from pyspark.ml.regression import LinearRegression 