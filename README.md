# Linear Regression for Relationship Between Water Salinity and Water Temperature
Data is from [Kaggle (CalCOFI)](https://www.kaggle.com/sohier/calcofi)

The purpose of this python program is to test for a relationship between water salinity and water temperature off the coast of central California by using linear regression.

The jupyter notebook file contains two implementations of the program, one using seaborn (an advanced data visualization library) and one using sklearn and matplotlib.

## Running the program

If you wish to run this program and see the results for yourself, download the repository and open up the `kernel.ipynb` file in jupyter notebook, which can be [downloaded here](http://jupyter.org/). This can also be opened from Google Drive using [Google's Colaboratory environment](https://colab.research.google.com/). Note that these two programs allow you to download the notebook as a python file.

Since the datafile itself is too large for github to handle (~250 MB), only the 500 lines of the original file are included. Make sure to download the file from the kaggle website link if you want the full dataset.

If you wish to increase the amount of data trained and tested against to fit a more representative model, simply download the original file from the Kaggle challenge listed above and change the following line to a larger number (or eliminate the line altogether). 

```python
bottle = bottle[:][500]
```
