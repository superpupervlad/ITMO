package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.logic.WritableDatabaseRecord;

import java.nio.charset.StandardCharsets;

/**
 * Запись в БД, означающая добавление значения по ключу
 */
public class SetDatabaseRecord implements WritableDatabaseRecord {
    byte[] objectKey;
    byte[] objectValue;

    public SetDatabaseRecord(String key, byte[] value){
        objectKey = key.getBytes(StandardCharsets.UTF_8);
        objectValue  = value;
    }

    public SetDatabaseRecord(byte[] key, byte[] value){
        objectKey = key;
        objectValue  = value;
    }

    @Override
    public byte[] getKey() {
        return objectKey;
    }

    @Override
    public byte[] getValue() {
        return objectValue;
    }

    @Override
    public long size() {
        return getKeySize() + getValueSize() + 8;
    }

    @Override
    public boolean isValuePresented() {
        if (objectValue == null) {
            return false;
        }
        return (objectValue.length > 0);
    }

    @Override
    public int getKeySize() {
        return objectKey.length;
    }

    @Override
    public int getValueSize() {
        if (objectValue == null) {
            return 0;
        }
        return objectValue.length;
    }
}
