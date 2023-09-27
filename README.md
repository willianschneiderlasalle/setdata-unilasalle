# setdata-unilasalle

Como foi conversado em aula, escolhi a HashTable por causa da sua melhor eficiência em comparação com outras estruturas de dados como Array, Array Ordenado ou até mesmo Árvore Binária.

Complexidade de Tempo das operações feitas em Hash Tables:

    No caso médio:

    _hashFunction:  O(1)
    _rehash:        O(1)
    _get:           O(1)
    _put:           O(1)
    _delete:        O(1)

    No pior caso:

    _hashFunction:  O(n)
    _rehash:        O(n)
    _get:           O(n)
    _put:           O(n)
    _delete:        O(n)

Complexidade de Espaço de Hash Tables: 
    O(n)