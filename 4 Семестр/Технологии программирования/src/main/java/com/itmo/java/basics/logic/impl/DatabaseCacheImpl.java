package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.logic.DatabaseCache;

import java.util.LinkedHashMap;
import java.util.Map;

public class DatabaseCacheImpl implements DatabaseCache {
    private static final int CAPACITY = 5_000;

    private final LinkedHashMap<String, byte[]> db =
            new LinkedHashMap<>(1000, 0.75F, true) {
                @Override
                protected boolean removeEldestEntry(Map.Entry eldest) {
                    return size() > CAPACITY;
                }
            };

    @Override
    public byte[] get(String key) {
        return db.get(key);
    }

    @Override
    public void set(String key, byte[] value) {
        db.put(key, value);
    }

    @Override
    public void delete(String key) {
        db.put(key, null);
    }

    public boolean contains(String key) {
        return db.containsKey(key);
    }
}
