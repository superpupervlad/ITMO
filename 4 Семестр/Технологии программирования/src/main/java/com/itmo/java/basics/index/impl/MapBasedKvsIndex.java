package com.itmo.java.basics.index.impl;

import com.itmo.java.basics.index.KvsIndex;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class MapBasedKvsIndex<K, V> implements KvsIndex<K, V> {
    private final Map<K, V> index = new HashMap<>(200);

    public void updateMultipleEntitiesWithOneValue(MapBasedKvsIndex<K, ?> keys, V value) {
        for (K curKey: keys.index.keySet()) {
            onIndexedEntityUpdated(curKey, value);
        }
    }

    @Override
    public void onIndexedEntityUpdated(K key, V value) {
        index.put(key, value);
    }

    @Override
    public Optional<V> searchForKey(K key) {
        return Optional.ofNullable(index.get(key));
    }
}
