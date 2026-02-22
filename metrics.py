import numpy as np

# confusion matrix
cm = np.array([
    [5, 10, 5],
    [15, 20, 10],
    [0, 15, 10]
])

classes = ["Cat", "Dog", "Rabbit"]

# per-class metrics
precision = []
recall = []

for i in range(len(classes)):
    tp = cm[i, i]
    fp = cm[i].sum() - tp
    fn = cm[:, i].sum() - tp
    
    p = tp / (tp + fp)
    r = tp / (tp + fn)
    
    precision.append(p)
    recall.append(r)
    
    print(f"{classes[i]} -> Precision: {p:.2f}, Recall: {r:.2f}")

# macro
macro_p = sum(precision) / len(precision)
macro_r = sum(recall) / len(recall)

# micro
tp_total = np.trace(cm)
total = cm.sum()

micro_p = tp_total / total
micro_r = tp_total / total

print("\nMacro Precision:", round(macro_p, 2))
print("Macro Recall:", round(macro_r, 2))
print("Micro Precision:", round(micro_p, 2))
print("Micro Recall:", round(micro_r, 2))
