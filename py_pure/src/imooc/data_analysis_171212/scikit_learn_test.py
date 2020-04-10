from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn import metrics


def main():
    iris = load_iris()
    print(iris)
    print(iris['data'])
    # 1. 数据域处理
    train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.2,
                                                                        random_state=1)
    # 2. 建模
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    clf.fit(train_data, train_target)
    y_pred = clf.predict(test_data)

    # 3. 验证
    print(metrics.accuracy_score(y_true=test_target, y_pred=y_pred))
    print(metrics.confusion_matrix(y_true=test_target, y_pred=y_pred))

    with open('data/tree.dot', 'w') as f:
        tree.export_graphviz(clf, out_file=f)


if __name__ == '__main__':
    main()
