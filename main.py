from EmailParser import EmailParser
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

def crear_dataset(indice, num):
    email_parser = EmailParser()
    x, y = leer_correos(indice, num)
    X_proc = []
    for i, email in zip(range(len(x)), x):
        print('\rParsing email: {0}'.format(i+1), end='')
        X_proc.append(email_parser.parser(email))
    return X_proc, y

def leer_correos(indice, num_correos):
    X = []
    Y = []
    with open('C:/Users/Mikel IBK/curso_python_udemy/Sección 13/Deteccion de SPAM con Machine Learning/full/' + indice,'r') as index:
        etiquetas = index.read().splitlines()

    for c in etiquetas[:num_correos]:
        label, email_path = c.split(' ../')
        Y.append(label)
        with open('C:/Users/Mikel IBK/curso_python_udemy/Sección 13/Deteccion de SPAM con Machine Learning/'+email_path, errors='ignore') as texto:
            X.append(texto.read())
    return X, Y


x, y = crear_dataset('index', 5000)
x_train, y_train = x[:4000], y[:4000]
x_test, y_test = x[4000:], y[4000:]
vectorizer = CountVectorizer()
vectorizer.fit(x_train)
X_vect = vectorizer.transform(x_train)
clf = LogisticRegression()
clf.fit(X_vect, y_train)
x_test = vectorizer.transform(x_test)
y_pred = clf.predict(x_test)
print('Accuracy: {:.3f}'.format(accuracy_score(y_test, y_pred)))