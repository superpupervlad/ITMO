package com.itmo.java.basics.logic;

/**
 * Представляет собой единицу хранения в БД
 */
public interface DatabaseRecord {
    /**
     * Возвращает ключ
     */
    byte[] getKey();

    /**
     * Возвращает значение
     */
    byte[] getValue();

    /**
     * Возвращает размер хранимой записи в базе данных. Используется для определения offset (сдвига)
     */
    long size();

    /**
     * Индикатор, есть ли значение
     */
    boolean isValuePresented();
}

