package com.itmo.java.basics.logic;

import com.itmo.java.basics.exceptions.DatabaseException;

import java.util.Optional;

public interface Database {
    /**
     * Возвращает имя базы данных.
     *
     * @return имя базы данных
     */
    String getName();

    /**
     * Создает таблицу с указанным именем, если это имя еще не занято.
     *
     * @param tableName имя таблицы
     * @throws DatabaseException если таблица с данным именем уже существует или если произошла ошибка ввода-вывода
     */
    void createTableIfNotExists(String tableName) throws DatabaseException;

    /**
     * Записывает значение в указанную таблицу по переданному ключу.
     *
     * @param tableName таблица, в которую нужно записать значение
     * @param objectKey ключ, по которому нужно записать значение
     * @param objectValue значение, которое нужно записать
     * @throws DatabaseException если указанная таблица не была найдена или если произошла ошибка ввода-вывода
     */
    void write(String tableName, String objectKey, byte[] objectValue) throws DatabaseException;

    /**
     * Считывает значение из указанной таблицы по заданному ключу.
     *
     * @param tableName таблица, из которой нужно считать значение
     * @param objectKey ключ, по которому нужно получить значение
     * @return значение, которое находится по ключу
     * @throws DatabaseException если не была найдена указанная таблица, или произошла ошибка ввода-вывода
     */
    Optional<byte[]> read(String tableName, String objectKey) throws DatabaseException;

    void delete(String tableName, String objectKey) throws DatabaseException;
}