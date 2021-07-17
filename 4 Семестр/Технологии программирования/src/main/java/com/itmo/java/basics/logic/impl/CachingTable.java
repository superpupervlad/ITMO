package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.exceptions.DatabaseException;
import com.itmo.java.basics.logic.Table;

import java.util.Optional;

/**
 * Декоратор для таблицы. Кэширует данные
 */
public class CachingTable implements Table {
    DatabaseCacheImpl storage = new DatabaseCacheImpl();
    public TableImpl realTable;

    public CachingTable(TableImpl realTable) {
        this.realTable = realTable;
    }

    @Override
    public String getName() {
        return realTable.getName();
    }

    @Override
    public void write(String objectKey, byte[] objectValue) throws DatabaseException {
        storage.set(objectKey, objectValue);
        realTable.write(objectKey, objectValue);
    }

    @Override
    public Optional<byte[]> read(String objectKey) throws DatabaseException {
        if (storage.contains(objectKey)) {
            return Optional.ofNullable(storage.get(objectKey));
        }
        Optional<byte[]> value = realTable.read(objectKey);
        storage.set(objectKey, value.orElse(null));

        return value;
    }

    @Override
    public void delete(String objectKey) throws DatabaseException {
        realTable.delete(objectKey);
        storage.set(objectKey, null);
    }
}
