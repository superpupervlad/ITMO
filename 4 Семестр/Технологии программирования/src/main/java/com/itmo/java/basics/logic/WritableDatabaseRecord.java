package com.itmo.java.basics.logic;

/**
 * Содержит информацию о параметрах {@link DatabaseRecord} для хранения в БД
 */
public interface WritableDatabaseRecord extends DatabaseRecord {

    /**
     * Возвращает размер ключа в байтах
     */
    int getKeySize();

    /**
     * Возвращает размер значения в байтах. -1, если значение отсутствует
     */
    int getValueSize();
}
