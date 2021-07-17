package com.itmo.java.basics.logic.impl;

import com.itmo.java.basics.logic.WritableDatabaseRecord;

import java.nio.charset.StandardCharsets;

/**
 * Запись в БД, означающая удаление значения по ключу
 */
public class RemoveDatabaseRecord implements WritableDatabaseRecord {
    byte[] objectKey;

    public RemoveDatabaseRecord(String key){
        objectKey = key.getBytes(StandardCharsets.UTF_8);
    }

    public RemoveDatabaseRecord(byte[] key){
        objectKey = key;
    }

    @Override
    public byte[] getKey() {
        return objectKey;
    }

    @Override
    public byte[] getValue() {
        return null;
    }

    @Override
    public long size() {
        return getKeySize() + 4;
    }

    @Override
    public boolean isValuePresented() {
        return false;
    }

    @Override
    public int getKeySize() {
        return objectKey.length;
    }

    @Override
    public int getValueSize() {
        return 0;
    }
}
