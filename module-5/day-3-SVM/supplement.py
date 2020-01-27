<img src="img/problems_of_maximal_margin.png" width=450, height=450>
<img src="img/non_separable_case.png" width=450, height=450>

# for more on possible values of scoring parameter
# https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
cv = cross_validate(svclassifier,
                    X_train,
                    y_train,
                    cv =5,
                    scoring= 'roc_auc',
                    return_estimator= True,
                    return_train_score= True,
                    n_jobs= -1)