---
id: 8189a2c6-621e-41a9-93e3-fdaedc8b85a8
longname: Линейная регрессия
languages: [python]
tags: [numpy,ml,OOP]
checker: cmp_yesno
time_limit: 60
real_time_limit: 60
max_vm_size: 256M
---

Необходимо реализовать класс Линейной Регрессии. При создании объекта можно указать параметры запуска. Логистическую регрессию можно обучить и сделать предсказания. 


<code>
class LinearRegression:
    def __init__(self, alpha=1e-4: float, l0=0.: float, l1=0.: float, l2=0.: float, 
                 stop_iter=1e6: float, stop_delta=1e-6: float, verbose=False: bool, model=None: object):
        '''
        Linerar Regression object constructor
        
        :param alpha: alpha param for gradient descent
        :param l0: L0 regularization coefficient
        :param l1: L1 regularization coefficient
        :param l2: L2 regularization coefficient
        :param stop_iter: maximum iterations of traing
        :param stop_delta: stop iteration delta
        :param verbose: show verbose information
        :param model: get params from other model
        '''
        pass
    
    def train(self, X: np.array, y: np.array, warm_start=False: bool):
        '''
        Fit Linear Regression params
        
        :param X: training data
        :param y: training ansewers
        :param warm_start: must be set True to continue training, false to reset params
        '''
        pass
    
    def get_params(self): -> dict
        '''
        Return model params
        
        :return: dict of model params
        '''
        pass
    
    def predict(self, X: np.array): -> np.array
        '''
        Predit answers on given data
        
        :param X: data
        :return: predicted answers
        '''
        pass
    
    def test(self, X: np.array, y: np.array, metric=None): -> float
        '''
        Test the model
        
        :param X: test data
        :param y: test answers
        :param metric: must be a function of 2 numpy arrays. If None, MSE is used.
        :return: metric value
        '''
        pass
</code>