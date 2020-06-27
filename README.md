# covid_new_cases

To see how the US response to the coronavirus compares to countries with socialized medicine, I grabbed some data from Our World in Data, passed it into python and plotted the daily new cases reported by each country since April 01 of this year.  The countries with socialized medicine are:  

Australia, Austria, Bahrain, Belgium, Brunei, Canada, Cyprus, Denmark, Finland, France, Germany, Greece, Hong Kong, Iceland, Ireland, Israel, Italy, Japan, Kuwait, Luxembourg, the Netherlands, New Zealand, Norway, Portugal, Singapore, Slovenia, South Korea, Spain, Sweden, Switzerland, the United Arab Emirates, United Kingdom.  
This resulted in two datasets: the new cases per day in the US and the new cases in all the socialized medicine countries per day, summed together.  These datasets are then plotted in two ways.  Once on the same y-axis scale showing new cases per day in both the US and the countries with socialized medicine and then on two different y-axis scales, each relative to its respective dataset.  The latter helping to control for population in the two datasets.


The newest data file (`owid-covid-data.csv`) https://github.com/owid/covid-19-data/tree/master/public/data/

usage:

with `owid-covid-data.csv` in the same directory as `covid_new_cases.py`:

```
$ python ./covid_new_cases.py
```
