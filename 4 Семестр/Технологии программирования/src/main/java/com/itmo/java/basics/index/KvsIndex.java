package com.itmo.java.basics.index;

import java.util.Optional;

public interface KvsIndex<K, V> {
    /**
     * Оповещает индекс об обновлении значения по определенному ключу.
     *
     * @param key ключ, который обновился
     * @param value новое значение
     */
    void onIndexedEntityUpdated(K key, V value);

    /**
     * Ищет значение в индексе по указанному ключу.
     *
     * @param key ключ, по которому нужно провести поиск значение
     * @return {@code Optional<V>}
     */
    Optional<V> searchForKey(K key);
}
