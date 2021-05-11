
## Naive Bayes

- This is a scratch program (Without ML libraries) to implement the naive bayes algorithm (m-estimate version) to classify categorical features.

- The program will take
one input: a dataset with multiple categorical features where the last column is the class
variable. The input to the program will be a training and a testing dataset. The output will be
overall accuracy which will be printed on the console.


Naive Bayes model is easy to build and particularly useful for very large data sets. Along with simplicity, Naive Bayes is known to outperform even highly sophisticated classification methods.

Bayes theorem provides a way of calculating posterior probability P(c|x) from P(c), P(x) and P(x|c).


Look at the equation below:

![Alt Image text](https://github.com/TP1232/Naive_Bayes/blob/1a19972aab4cb20ee314f0356467dd1d5ca4b16a/Bayes_rule-300x172.png?raw=true "Optional Title")

Above,

- P(c|x) is the posterior probability of class (c, target) given predictor (x, attributes).
- P(c) is the prior probability of class.
- P(x|c) is the likelihood which is the probability of predictor given class.
- P(x) is the prior probability of predictor.

# m-estimate of probability

### m−estimate=(n_c+mp)/(n+m)

### m = constant or weight 

###  p = prior 
  - #### assume uniform prior = 1/(number of possible values of the feature)
 ### m -> additional virtual samples 
  - #### One possible option = number of possible values of the feature

## Dataset

[Car_Dataset](https://github.com/TP1232/Naive_Bayes/blob/1a19972aab4cb20ee314f0356467dd1d5ca4b16a/car.data)

## Usage

```bash
python NB_m_estimate.py
```



