# ========================================
# OOP UNTUK MACHINE LEARNING
# Part 2: Model Classes & Training
# ========================================

# file ini menunjukkan bagaimana oop digunakan untuk :
# - membuat wrapper untuk berbagai ml models
#- unified interface untuk training dan evaluation
# model management dan comparsion

import numpy as np
from abc import ABC, abstractmethod  # Untuk abstract classes
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from typing import Dict, Any
import time
# ========================================
# BASE MODEL CLASS (Abstract)
# ========================================

class BaseModel(ABC):
    """
    abstract base class untuk ml models
    semua model harus inherit dari class ini
    provides unified interface untuk berbagai algoritma ml
    """
    def __init__(self,name,**kwargs):
        """"
        Constructor BaseModel
        Args:
            name : nama model ( untuk display )
            **kwargs: parameter konfigurasi model (key-calue pairs"""
        self.name = name        # nama model
        self.model = None       # object model sklearn
        self.is_trained = False #flag training status
        self.training_time = 0  # waktu training
        self.config = kwargs    # simpan configurasi

    @abstractmethod
    def build_models(self):
        """
        abstract method untuk build model
        child class wajib implement method ini
        setiap algoritma punya cara build berbeda
        """
        pass

    def train(self, X_train, y_train):
        """
        train model pada data
        method concrete yang bisa dipakai semua child class
        args :
            X_train : training features
            y_train : training target
            returns : self (untuk method chaining )
        :param X_train:
        :param y_train:
        :return:
        """

        #build model jika belum ada
        if self.model is None:
            self.build_models()

        print(f"\n Training {self.name}....")

        # record waktu training
        start_time = time.time()

        # training model (fit )
        self.model.fit(X_train, y_train)

        # hitung durasi training
        self.training_time = time.time() - start_time
        self.is_trained = True

        print(f" Training comepleted in {self.training_time:.2f}s")
        return self # return self untuk chaining

    def predict(self, X):
        """
        make prediction
        args :
        X : features untuk predict
        returns : array prediction
        """

        # validasi : pastikan model sudah di training
        if not self.is_trained:
            raise ValueError(f"{self.name} is not trained")

        return self.model.predict(X)

    def predict_proba(self, X):
        """
        predict probabilities ( untuk model yang support )
        args :
        X : features untuk predict
        returns : array probabilities
        """
        if not self.is_trained:
            raise ValueError(f"{self.name} is not trained")

        # cek apakah models support predict_proba
        if hasattr(self.model, "predict_proba"):
            return self.model.predict_proba(X)
        else:
            raise NotImplementedError(f"{self.name} is not support predict_proba")

    def get_params(self):
        """
        get model parameters
        :returns : dictionary parameters
        """
        if self.model is not None:
            return self.model.get_params()
        return None

    def __str__(self):
        """
        string representation untuk print
        :returns: string status model
        """
        status = "Trained" if self.is_trained else "Not trained"
        return f"{self.name} - {status}"

    # ========================================
    # CONCRETE MODEL IMPLEMENTATIONS
    # ========================================
    # Child classes yang implement BaseModel untuk berbagai algoritma

class LogisticRegressionModel(BaseModel):
    """
    Logistic Regression Model
    inherit dari basemodel, implement build_model()
    """

    def __init__(self,max_iter= 1000, random_state = 42, **kwargs):
        """
            Constructor LogisticRegressionModel
            Args:
                max_iter: maksimum iterasi untuk convergence
                random_state: seed untuk reproducibility
                **kwargs: parameter tambahan untuk LogisticRegression
        """
        # panggil constuctor parent dengan nama dan config
        super().__init__(
            name="Logistic Regression",
            max_iter = max_iter,
            random_state=random_state,
            **kwargs
        )

    def build_models(self):
        """
               Implementation build_model untuk Logistic Regression
               Buat instance LogisticRegression dari sklearn
        """
        self.model = LogisticRegression(
            max_iter= self.config.get('max_iter',1000),
            random_state=self.config.get('random_state',42),
        )

class DecisionTreeModel(BaseModel):
    """Decision Tree Model wrapper"""

    def __init__(self,max_dept=None,random_state = 42,**kwargs):
        """
        Constructor DecisionTreeModel
        Args:
            max_depth: kedalaman maksimum tree (None = unlimited)
            random_state: seed
        """
        super().__init__(
            name = "Decision Tree",
            max_dept= max_dept,
            random_state=random_state,
            **kwargs
        )

    def build_models(self):
        """Build Decision Tree classifier"""
        self.model = DecisionTreeClassifier(
            max_depth=self.config.get('max_depth'),
            random_state=self.config.get('random_state',42)
        )
class RandomForestModel(BaseModel):
    """
        Random Forest model wrapper
        Ensemble method - kombinasi banyak decision trees
    """
    def __init__(self, n_estimators=100, max_depth= None, random_state= 42, **kwargs):
        """
        Constructor RandomForestModel
        Args:
                n_estimators: jumlah trees dalam forest
                max_depth: kedalaman maksimum setiap tree
                random_state: seed
        """
        super().__init__(
            name="random forest",
            n_estimators=n_estimators,
            max_depth= max_depth,
            random_state=random_state,
            **kwargs
        )

    def build_models(self):
        """Build Random Forest classifier"""
        self.model = RandomForestClassifier(
            n_estimators=self.config.get('n_estimators',100),
            max_depth=self.config.get('max_depth'),
            random_state=self.config.get('random_state',42)
        )

class SVMModel(BaseModel):
    """Suport Vector Machine model wrapper"""
    def __init__(self, kernel='rbf', C=1.0, random_state= 42, **kwargs):
        """
               Constructor SVMModel
               Args:
                   kernel: kernel function ('linear', 'rbf', 'poly')
                   C: regularization parameter
                   random_state: seed
        """
        super().__init__(
            name="Support Vector Machine",
            kernel= kernel,
            C=C,
            random_state=random_state,
            **kwargs
        )

    def build_models(self):
        self.model = SVC(
            kernel=self.config.get('kernel','rbf'),
            C=self.cofig.get('C',1.0),
            random_state=self.config.get('random_state',42),
            probability=True        #enable predict_proba
        )

# ========================================
# MODEL EVALUATOR
# ========================================

class ModelEvaluator:
    """
    class untuk evalusasi dan comparsion model
    calculate metrics dan compare performance metrics
    """

    def __init__(self):
        """constructor - initialize result storage"""
        self.results = {} # dictionaey untuk simpan hasil evaluasi

    def evaluate(self,model : BaseModel, X_test, y_test, dataset_name: str = "Test"):
        """
        evaluate model performance
        :args:
        model = obejct basemodel yang ingin di evaluasi
        X_test: test features
        y_test: test target
        dataset_name: dataset name ( display)
        """
        print(f"\n Evaluating {model.name} on {dataset_name} set...")
        print("=" * 60)

        # make predic
        y_pred = model.predict(X_test)

        #calculate berbagai metrics
        metrics ={
        'model_name'    : model.name,
        'accuracy'      : accuracy_score(y_test,y_pred),
        'precision'     : precision_score(y_test,y_pred,average='weighted', zero_division=0),
        'recall'        : recall_score(y_test,y_pred, average='weighted', zero_division=0),
        'f1'            : f1_score(y_test,y_pred, average='weighted', zero_division=0),
        'training_time' : model.training_time
        }

        # store result untuk comparsion
        self.results[dataset_name] = metrics

        #output
        print(f"Accuracy:  {metrics['accuracy']:.4f}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall:    {metrics['recall']:.4f}")
        print(f"F1-Score:  {metrics['f1']:.4f}")
        print(f"Training time: {metrics['training_time']:.2f}s")

        return metrics

    def comapare_models(self):
        """
            Compare semua model yang sudah dievaluasi
            Print comparison table
        """
        if not self.results:
            print("no models to compare")
            return

        print("\n" + "=" * 80)
        print("MODEL COMPARSION")
        print("\n" + "=" * 80)

        # HEADER TABLE
        print(f"{'Model':<30} {'Acciracy':>10} {'F1-score':>10} {'Time (s)':>10}")

        # sort models by accuracy (ascending)
        sorted_models = sorted(
            self.results.items(),
            key=lambda x: x[1] ['accuracy'],
            reverse=True
        )