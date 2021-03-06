# Flamespeed

## What is Flamespeed?

Flamespeed is the measured rate of expansion of the flame front in a combustion reaction.

It is also an open-source Python library with object-orientated methods for chemical kinetics with the following core functionality:

* API to import a database of elementary reactions in XML-format
* Efficiently calculate reaction rates for systems of irreversible elementary chemical reactions
* Output provided in format suitable for further analysis

Potential **applications** for Flamespeed includes:

* Validation of chemical phase input files
* Input for solving ODEs for system of reactions
* Input for machine learning methods (e.g. neural networks) that predict reaction types

## Installation

There are two ways to install Flamespeed:

* **Install Flamespeed from PyPI (recommended)**

```bash
pip3 install flamespeed
```

* **Alternatively: Install Flamespeed form Github source**

First, clone Flamespeed using `git`:

```sh
git clone https://github.com/bkleyn/flamespeed.git
```
Then, `cd` to the root folder and run the install command:
```sh
python setup.py install
```

The package **test suite** can be run as follows:

First, `cd` to the flamespeed folder and then run pytest:
```sh
cd flamespeed
pytest
```

**Requirements:**
* Python (>= 3.3)
* NumPy (>= 1.8.2)
* SciPy (>= 0.13.3)


## Getting started

Import the `chemkin` module in flamespeed, which is the main module to evaluate chemical reaction rates.

```python
from flamespeed import chemkin
```
Instantiate the reaction rates class and import reaction database in XML format. Example reaction files can be found in the `./data` directory within `flamespeed`.

```python
a = chemkin.ReactionRate()
a.read_XML('./flamespeed/data/rxns_reversible.xml')
print(a)
```
Next, set the initial concentrations for each of the species included in the reaction and the temperature.

```python
a.set_temp(750)
x = [2.0, 1.0, 0.5, 1.0, 1.0, 1.5, 0.5, 1]
```
Now that all the input parameters have been specified the reaction rates for each of the species in the system can be determined as follows:

```python
r = a.get_reaction_rate(x)
print(r)
```

## Documentation

Technical detail regarding the chemical theory underlying the reaction rate calculations and detailed documentation of the relevant classes and methods included in the Flamespeed package can be found in the `docs` directory.