{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.datasets import load_iris"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "iris = load_iris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "sklearn.datasets.base.Bunch"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(iris)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 5.1,  3.5,  1.4,  0.2],\n",
       "       [ 4.9,  3. ,  1.4,  0.2],\n",
       "       [ 4.7,  3.2,  1.3,  0.2],\n",
       "       [ 4.6,  3.1,  1.5,  0.2],\n",
       "       [ 5. ,  3.6,  1.4,  0.2],\n",
       "       [ 5.4,  3.9,  1.7,  0.4],\n",
       "       [ 4.6,  3.4,  1.4,  0.3],\n",
       "       [ 5. ,  3.4,  1.5,  0.2],\n",
       "       [ 4.4,  2.9,  1.4,  0.2],\n",
       "       [ 4.9,  3.1,  1.5,  0.1],\n",
       "       [ 5.4,  3.7,  1.5,  0.2],\n",
       "       [ 4.8,  3.4,  1.6,  0.2],\n",
       "       [ 4.8,  3. ,  1.4,  0.1],\n",
       "       [ 4.3,  3. ,  1.1,  0.1],\n",
       "       [ 5.8,  4. ,  1.2,  0.2],\n",
       "       [ 5.7,  4.4,  1.5,  0.4],\n",
       "       [ 5.4,  3.9,  1.3,  0.4],\n",
       "       [ 5.1,  3.5,  1.4,  0.3],\n",
       "       [ 5.7,  3.8,  1.7,  0.3],\n",
       "       [ 5.1,  3.8,  1.5,  0.3],\n",
       "       [ 5.4,  3.4,  1.7,  0.2],\n",
       "       [ 5.1,  3.7,  1.5,  0.4],\n",
       "       [ 4.6,  3.6,  1. ,  0.2],\n",
       "       [ 5.1,  3.3,  1.7,  0.5],\n",
       "       [ 4.8,  3.4,  1.9,  0.2],\n",
       "       [ 5. ,  3. ,  1.6,  0.2],\n",
       "       [ 5. ,  3.4,  1.6,  0.4],\n",
       "       [ 5.2,  3.5,  1.5,  0.2],\n",
       "       [ 5.2,  3.4,  1.4,  0.2],\n",
       "       [ 4.7,  3.2,  1.6,  0.2],\n",
       "       [ 4.8,  3.1,  1.6,  0.2],\n",
       "       [ 5.4,  3.4,  1.5,  0.4],\n",
       "       [ 5.2,  4.1,  1.5,  0.1],\n",
       "       [ 5.5,  4.2,  1.4,  0.2],\n",
       "       [ 4.9,  3.1,  1.5,  0.1],\n",
       "       [ 5. ,  3.2,  1.2,  0.2],\n",
       "       [ 5.5,  3.5,  1.3,  0.2],\n",
       "       [ 4.9,  3.1,  1.5,  0.1],\n",
       "       [ 4.4,  3. ,  1.3,  0.2],\n",
       "       [ 5.1,  3.4,  1.5,  0.2],\n",
       "       [ 5. ,  3.5,  1.3,  0.3],\n",
       "       [ 4.5,  2.3,  1.3,  0.3],\n",
       "       [ 4.4,  3.2,  1.3,  0.2],\n",
       "       [ 5. ,  3.5,  1.6,  0.6],\n",
       "       [ 5.1,  3.8,  1.9,  0.4],\n",
       "       [ 4.8,  3. ,  1.4,  0.3],\n",
       "       [ 5.1,  3.8,  1.6,  0.2],\n",
       "       [ 4.6,  3.2,  1.4,  0.2],\n",
       "       [ 5.3,  3.7,  1.5,  0.2],\n",
       "       [ 5. ,  3.3,  1.4,  0.2],\n",
       "       [ 7. ,  3.2,  4.7,  1.4],\n",
       "       [ 6.4,  3.2,  4.5,  1.5],\n",
       "       [ 6.9,  3.1,  4.9,  1.5],\n",
       "       [ 5.5,  2.3,  4. ,  1.3],\n",
       "       [ 6.5,  2.8,  4.6,  1.5],\n",
       "       [ 5.7,  2.8,  4.5,  1.3],\n",
       "       [ 6.3,  3.3,  4.7,  1.6],\n",
       "       [ 4.9,  2.4,  3.3,  1. ],\n",
       "       [ 6.6,  2.9,  4.6,  1.3],\n",
       "       [ 5.2,  2.7,  3.9,  1.4],\n",
       "       [ 5. ,  2. ,  3.5,  1. ],\n",
       "       [ 5.9,  3. ,  4.2,  1.5],\n",
       "       [ 6. ,  2.2,  4. ,  1. ],\n",
       "       [ 6.1,  2.9,  4.7,  1.4],\n",
       "       [ 5.6,  2.9,  3.6,  1.3],\n",
       "       [ 6.7,  3.1,  4.4,  1.4],\n",
       "       [ 5.6,  3. ,  4.5,  1.5],\n",
       "       [ 5.8,  2.7,  4.1,  1. ],\n",
       "       [ 6.2,  2.2,  4.5,  1.5],\n",
       "       [ 5.6,  2.5,  3.9,  1.1],\n",
       "       [ 5.9,  3.2,  4.8,  1.8],\n",
       "       [ 6.1,  2.8,  4. ,  1.3],\n",
       "       [ 6.3,  2.5,  4.9,  1.5],\n",
       "       [ 6.1,  2.8,  4.7,  1.2],\n",
       "       [ 6.4,  2.9,  4.3,  1.3],\n",
       "       [ 6.6,  3. ,  4.4,  1.4],\n",
       "       [ 6.8,  2.8,  4.8,  1.4],\n",
       "       [ 6.7,  3. ,  5. ,  1.7],\n",
       "       [ 6. ,  2.9,  4.5,  1.5],\n",
       "       [ 5.7,  2.6,  3.5,  1. ],\n",
       "       [ 5.5,  2.4,  3.8,  1.1],\n",
       "       [ 5.5,  2.4,  3.7,  1. ],\n",
       "       [ 5.8,  2.7,  3.9,  1.2],\n",
       "       [ 6. ,  2.7,  5.1,  1.6],\n",
       "       [ 5.4,  3. ,  4.5,  1.5],\n",
       "       [ 6. ,  3.4,  4.5,  1.6],\n",
       "       [ 6.7,  3.1,  4.7,  1.5],\n",
       "       [ 6.3,  2.3,  4.4,  1.3],\n",
       "       [ 5.6,  3. ,  4.1,  1.3],\n",
       "       [ 5.5,  2.5,  4. ,  1.3],\n",
       "       [ 5.5,  2.6,  4.4,  1.2],\n",
       "       [ 6.1,  3. ,  4.6,  1.4],\n",
       "       [ 5.8,  2.6,  4. ,  1.2],\n",
       "       [ 5. ,  2.3,  3.3,  1. ],\n",
       "       [ 5.6,  2.7,  4.2,  1.3],\n",
       "       [ 5.7,  3. ,  4.2,  1.2],\n",
       "       [ 5.7,  2.9,  4.2,  1.3],\n",
       "       [ 6.2,  2.9,  4.3,  1.3],\n",
       "       [ 5.1,  2.5,  3. ,  1.1],\n",
       "       [ 5.7,  2.8,  4.1,  1.3],\n",
       "       [ 6.3,  3.3,  6. ,  2.5],\n",
       "       [ 5.8,  2.7,  5.1,  1.9],\n",
       "       [ 7.1,  3. ,  5.9,  2.1],\n",
       "       [ 6.3,  2.9,  5.6,  1.8],\n",
       "       [ 6.5,  3. ,  5.8,  2.2],\n",
       "       [ 7.6,  3. ,  6.6,  2.1],\n",
       "       [ 4.9,  2.5,  4.5,  1.7],\n",
       "       [ 7.3,  2.9,  6.3,  1.8],\n",
       "       [ 6.7,  2.5,  5.8,  1.8],\n",
       "       [ 7.2,  3.6,  6.1,  2.5],\n",
       "       [ 6.5,  3.2,  5.1,  2. ],\n",
       "       [ 6.4,  2.7,  5.3,  1.9],\n",
       "       [ 6.8,  3. ,  5.5,  2.1],\n",
       "       [ 5.7,  2.5,  5. ,  2. ],\n",
       "       [ 5.8,  2.8,  5.1,  2.4],\n",
       "       [ 6.4,  3.2,  5.3,  2.3],\n",
       "       [ 6.5,  3. ,  5.5,  1.8],\n",
       "       [ 7.7,  3.8,  6.7,  2.2],\n",
       "       [ 7.7,  2.6,  6.9,  2.3],\n",
       "       [ 6. ,  2.2,  5. ,  1.5],\n",
       "       [ 6.9,  3.2,  5.7,  2.3],\n",
       "       [ 5.6,  2.8,  4.9,  2. ],\n",
       "       [ 7.7,  2.8,  6.7,  2. ],\n",
       "       [ 6.3,  2.7,  4.9,  1.8],\n",
       "       [ 6.7,  3.3,  5.7,  2.1],\n",
       "       [ 7.2,  3.2,  6. ,  1.8],\n",
       "       [ 6.2,  2.8,  4.8,  1.8],\n",
       "       [ 6.1,  3. ,  4.9,  1.8],\n",
       "       [ 6.4,  2.8,  5.6,  2.1],\n",
       "       [ 7.2,  3. ,  5.8,  1.6],\n",
       "       [ 7.4,  2.8,  6.1,  1.9],\n",
       "       [ 7.9,  3.8,  6.4,  2. ],\n",
       "       [ 6.4,  2.8,  5.6,  2.2],\n",
       "       [ 6.3,  2.8,  5.1,  1.5],\n",
       "       [ 6.1,  2.6,  5.6,  1.4],\n",
       "       [ 7.7,  3. ,  6.1,  2.3],\n",
       "       [ 6.3,  3.4,  5.6,  2.4],\n",
       "       [ 6.4,  3.1,  5.5,  1.8],\n",
       "       [ 6. ,  3. ,  4.8,  1.8],\n",
       "       [ 6.9,  3.1,  5.4,  2.1],\n",
       "       [ 6.7,  3.1,  5.6,  2.4],\n",
       "       [ 6.9,  3.1,  5.1,  2.3],\n",
       "       [ 5.8,  2.7,  5.1,  1.9],\n",
       "       [ 6.8,  3.2,  5.9,  2.3],\n",
       "       [ 6.7,  3.3,  5.7,  2.5],\n",
       "       [ 6.7,  3. ,  5.2,  2.3],\n",
       "       [ 6.3,  2.5,  5. ,  1.9],\n",
       "       [ 6.5,  3. ,  5.2,  2. ],\n",
       "       [ 6.2,  3.4,  5.4,  2.3],\n",
       "       [ 5.9,  3. ,  5.1,  1.8]])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris.data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']\n"
     ]
    }
   ],
   "source": [
    "print(iris.feature_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
      " 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
      " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n",
      " 2 2]\n"
     ]
    }
   ],
   "source": [
    "print(iris.target)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['setosa' 'versicolor' 'virginica']\n"
     ]
    }
   ],
   "source": [
    "print(iris.target_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\nRK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1b94db796d8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1b94e00a198>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(iris.data[:,1],iris.data[:,2],c=iris.target, cmap=plt.cm.Paired)\n",
    "plt.xlabel(iris.feature_names[1])\n",
    "plt.ylabel(iris.feature_names[2])\n",
    "plt.show()\n",
    "\n",
    "plt.scatter(iris.data[:,0],iris.data[:,3],c=iris.target, cmap=plt.cm.Paired)\n",
    "plt.xlabel(iris.feature_names[0])\n",
    "plt.ylabel(iris.feature_names[3])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p = iris.data\n",
    "q = iris.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(150, 4)\n",
      "(150,)\n"
     ]
    }
   ],
   "source": [
    "print(p.shape)\n",
    "print(q.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\bhatn\\Anaconda3\\lib\\site-packages\\sklearn\\cross_validation.py:44: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.\n",
      "  \"This module will be removed in 0.20.\", DeprecationWarning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.cross_validation import train_test_split\n",
    "p_train,p_test,q_train,q_test = train_test_split(p,q,test_size=0.2,random_state=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(120, 4)\n",
      "(30, 4)\n"
     ]
    }
   ],
   "source": [
    "print(p_train.shape)\n",
    "print(p_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(120,)\n",
      "(30,)\n"
     ]
    }
   ],
   "source": [
    "print(q_train.shape)\n",
    "print(q_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "\n",
    "from sklearn import metrics\n",
    "\n",
    "k_range = range(1,26)\n",
    "scores = {}\n",
    "scores_list = []\n",
    "for k in k_range:\n",
    "        knn = KNeighborsClassifier(n_neighbors=k)\n",
    "        knn.fit(p_train,q_train)\n",
    "        q_pred=knn.predict(p_test)\n",
    "        scores[k] = metrics.accuracy_score(q_test,q_pred)\n",
    "        scores_list.append(metrics.accuracy_score(q_test,q_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 0.93333333333333335,\n",
       " 2: 0.93333333333333335,\n",
       " 3: 0.96666666666666667,\n",
       " 4: 0.96666666666666667,\n",
       " 5: 0.96666666666666667,\n",
       " 6: 0.96666666666666667,\n",
       " 7: 0.96666666666666667,\n",
       " 8: 0.96666666666666667,\n",
       " 9: 0.96666666666666667,\n",
       " 10: 0.96666666666666667,\n",
       " 11: 0.96666666666666667,\n",
       " 12: 0.96666666666666667,\n",
       " 13: 0.96666666666666667,\n",
       " 14: 0.96666666666666667,\n",
       " 15: 0.96666666666666667,\n",
       " 16: 0.96666666666666667,\n",
       " 17: 0.96666666666666667,\n",
       " 18: 0.96666666666666667,\n",
       " 19: 0.96666666666666667,\n",
       " 20: 0.93333333333333335,\n",
       " 21: 0.96666666666666667,\n",
       " 22: 0.93333333333333335,\n",
       " 23: 0.96666666666666667,\n",
       " 24: 0.96666666666666667,\n",
       " 25: 0.96666666666666667}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.text.Text at 0x1b94e254630>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nSUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1b94e1a6b38>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the relationship between K and the testing accuracy\n",
    "plt.plot(k_range,scores_list)\n",
    "plt.xlabel('Value of K for KNN')\n",
    "plt.ylabel('Testing Accuracy')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
       "           metric_params=None, n_jobs=1, n_neighbors=5, p=2,\n",
       "           weights='uniform')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "knn = KNeighborsClassifier(n_neighbors=5)\n",
    "knn.fit(p,q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "versicolor\n",
      "setosa\n"
     ]
    }
   ],
   "source": [
    "#0 = setosa, 1=versicolor, 2=virginica\n",
    "classes = {0:'setosa',1:'versicolor',2:'virginica'}\n",
    "\n",
    "\n",
    "x_new = [[3,4,5,2],\n",
    "         [5,4,2,2]]\n",
    "y_predict = knn.predict(x_new)\n",
    "\n",
    "print(classes[y_predict[0]])\n",
    "print(classes[y_predict[1]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}