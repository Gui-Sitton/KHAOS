# Conclusão do Projeto Titanic


* Categorias que indicavam sexo e classe socioeconômica tem a maior correlação com a sobrevivência. Indicando que era mais importante você ser rico para sobreviver do que criança por exemplo.

* Categorias que indicam companhia no navio não tem muita correlação com a sobrevivência, indicando que isso não era o mais importante para determinar se a pessoa iria se salvar ou não.

* O tipo de pessoa com a maior chance de sobreviver de acordo com as categorias mais influentes eram claramente **mulheres jovens ricas**, sendo mais importante ser **mulher** e **rica** do que jovem. 


## Qual o melhor modelo feito para a previsão?
* Foi um modelo esamble stacking combinando Random Forest, Catboost, Xgboost, Lightgbm, e uma Rede Neural como modelo meta. 


```python
estimators = [
    ('rf', rf_model),
    ('lgb', lgb_model),
    ('xgb', xgb_model),
    ('cat', cat_model)
]

# MLPClassifier como meta-modelo
mlp_model = MLPClassifier(hidden_layer_sizes=(1000,500), max_iter=200000, random_state=42,learning_rate_init=0.01, learning_rate='invscaling')

stacking_model1 = StackingClassifier(estimators=estimators, final_estimator=mlp_model)
```

### Resultados do modelo com a submissão no kaggle:
* Precisão de 77%, nos deixando no top 40% do kaggle.

---


# Titanic Project Conclusion

* Categories indicating gender and socioeconomic class have the highest correlation with survival. This suggests that being wealthy was more important for survival than, for example, being a child.

* Categories that indicate companionship on the ship do not have much correlation with survival, suggesting that this was not a key factor in determining if a person would be saved.

* The type of person with the highest chance of survival, according to the most influential categories, were clearly **young wealthy women**. Being **female** and **wealthy** was more important than being young.

## What is the best model created for prediction?
* A stacking ensemble model was used, combining Random Forest, CatBoost, XGBoost, LightGBM, and a Neural Network as the meta model.

```python
estimators = [
    ('rf', rf_model),
    ('lgb', lgb_model),
    ('xgb', xgb_model),
    ('cat', cat_model)
]

# MLPClassifier as the meta model
mlp_model = MLPClassifier(hidden_layer_sizes=(1000,500), max_iter=200000, random_state=42, learning_rate_init=0.01, learning_rate='invscaling')

stacking_model1 = StackingClassifier(estimators=estimators, final_estimator=mlp_model)
```

### Model Results with Kaggle Submission:
* Achieved an accuracy of 77%, placing us in the top 40% on Kaggle.